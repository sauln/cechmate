# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from cechmate import __version__

# -- Project information -----------------------------------------------------

project = u'Cechmate'
copyright = u'2019, Chris Tralie and Nathaniel Saul'
author = u'Chris Tralie and Nathaniel Saul'

# The short X.Y version
version = __version__
# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

html_context = {'google_code': 'UA-124965309-3'}

# nbsphinx_kernel_name = 'python3'
nbsphinx_allow_errors = True
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'nbsphinx',
    "sphinx.ext.napoleon",
    'IPython.sphinxext.ipython_console_highlighting',
    'sphinxcontrib.fulltoc'
]

autodoc_default_options = {
    'autoclass_content': "both"
}
autodoc_default_flags = [
    "members",
    "inherited-members"
]
autosummary_generate = False
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = False

html_logo = "logo.png"
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

templates_path = ['_templates']


from better import better_theme_path
html_theme_path = [better_theme_path]
html_theme = 'better'
html_sidebars = {
    '**': [
        'localtoc.html', 
        'sourcelink.html', 
        'searchbox.html'
    ],
}
html_static_path = ['_static']
html_short_title = project
html_theme_options = {
#   'cssfiles': 'custom_style.css',
 
  
  # show sidebar on the right instead of on the left
  'rightsidebar': False,

  # inline CSS to insert into the page if you're too lazy to make a
  # separate file
#   'inlinecss': '',

  # CSS files to include after all other CSS files
  # (refer to by relative path from conf.py directory, or link to a
  # remote file)
  'cssfiles': ['_static/custom_style.css'],  # default is empty list

  # show a big text header with the value of html_title
  'showheader': True,

  # show the breadcrumbs and index|next|previous links at the top of
  # the page
  'showrelbartop': True,
  # same for bottom of the page
  'showrelbarbottom': True,



  # show the self-serving link in the footer
  'linktotheme': True,

  # width of the sidebar. page width is determined by a CSS rule.
  # I prefer to define things in rem because it scales with the
  # global font size rather than pixels or the local font size.
  'sidebarwidth': '15rem',

  # color of all body text
  'textcolor': '#000000',

  # color of all headings (<h1> tags); defaults to the value of
  # textcolor, which is why it's defined here at all.
  'headtextcolor': '',

  # color of text in the footer, including links; defaults to the
  # value of textcolor
  'footertextcolor': '',

  # Google Analytics info
  'ga_ua': 'UA-124965309-3',
  'ga_domain': '',
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'cechmatedoc'


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {'https://docs.python.org/': None}
