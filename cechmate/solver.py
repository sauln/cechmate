import itertools
import time

import numpy as np
import phat


def phat_diagrams(simplices, hide_infs=True, verbose=True):
    """
    Do a custom filtration wrapping around phat

    Inputs
    -------
    simplices: A list of lists of simplices and their distances
        the kth element is itself a list of tuples ([idx1, ..., idxk], dist)
        where [idx1, ..., idxk] is a list of vertices involved in the simplex
        and "dist" is the distance at which the simplex is added
    hide_infs: Whether or not to return points that never die

    Returns
    --------
    dgms: A dictionary of persistence diagrams, where dgms[k] is 
        the persistence diagram for Hk 
    """

    ## Convert simplices representation to sparse pivot column
    ordered_simplices = sorted(simplices, key=lambda x: x[1])
    columns = simplices_to_sparse_pivot_column(ordered_simplices, verbose)
   
    ## Setup boundary matrix and reduce
    if verbose:
        print("Computing persistence pairs...")
        tic = time.time()

    boundary_matrix = phat.boundary_matrix(
        columns=columns, representation=phat.representations.sparse_pivot_column
    )
    pairs = boundary_matrix.compute_persistence_pairs()
    pairs.sort()

    if verbose:
        print(
            "Finished computing persistence pairs (Elapsed Time %.3g)"
            % (time.time() - tic)
        )

    ## Setup persistence diagrams by reading off distances
    dgms = process_distances(pairs, ordered_simplices)

    ## Add all unpaired simplices as infinite points
    if not hide_infs:
        dgms = add_unpaired(dgms, pairs, simplices)

    ## Convert to arrays:
    dgms = {i: np.array(dgm) for i, dgm in dgms.items()}

    return dgms


def simplices_to_sparse_pivot_column(ordered_simplices, verbose):
    """

    """

    idx = 0
    columns = []
    idxs2order = {}

    if verbose:
        print("Constructing boundary matrix...")
        tic = time.time()

    for idxs, dist in ordered_simplices:
        k = len(idxs)
        idxs = sorted(idxs)
        idxs2order[tuple(idxs)] = idx
        idxs = np.array(idxs)
        if len(idxs) == 1:
            columns.append((0, []))
        else:
            # Get all faces with k-1 vertices
            collist = []
            for fidxs in itertools.combinations(range(k), k - 1):
                fidxs = np.array(list(fidxs))
                fidxs = tuple(idxs[fidxs])
                if not fidxs in idxs2order:
                    print(
                        "Error: Not a proper filtration: %s added before %s"
                        % (idxs, fidxs)
                    )
                    return None
                collist.append(idxs2order[fidxs])
            collist = sorted(collist)
            columns.append((k - 1, collist))

        idx += 1

    if verbose:
        print(
            "Finished constructing boundary matrix (Elapsed Time %.3g)"
            % (time.time() - tic)
        )

    return columns

def process_distances(pairs, ordered_simplices):
    """ Setup persistence diagrams by reading off distances
    """
    
    dgms = {}
    posneg = np.zeros(len(ordered_simplices))
    
    for [bi, di] in pairs:
        bidxs, bd = ordered_simplices[bi]
        didxs, dd = ordered_simplices[di]

        assert posneg[bi] == 0 and posneg[di] == 0
        posneg[bi], posneg[di] = 1, -1

        assert dd >= bd
        assert len(bidxs) == len(didxs) - 1

        p = len(bidxs) - 1
        
        # Don't add zero persistence pairs
        if bd != dd:
            dgms.setdefault(p, []).append([bd, dd])

    return dgms


def add_unpaired(dgms, pairs, simplices):
    posneg = np.zeros(len(simplices))
    for [bi, di] in pairs:
        assert posneg[bi] == 0
        assert posneg[di] == 0
        posneg[bi] = 1
        posneg[di] = -1

    for i in range(len(posneg)):
        if posneg[i] == 0:
            (idxs, dist) = simplices[i]
            p = len(idxs) - 1
            if not p in dgms:
                dgms[p] = []
            dgms[p].append([dist, np.inf])

    return dgms

