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

# -- Project information -----------------------------------------------------

project = u'AMS-FPGA'
copyright = u'2021, M. Meiners'
author = u'A. Vasudevan, A. Venkatachalam, M. Meiners'

# The short X.Y version
version = u'0.1'
# The full version, including alpha/beta/rc tags
release = u'Summer 2021'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.todo',
    'sphinx.ext.mathjax', 'sphinx.ext.ifconfig', 'sphinx.ext.viewcode',
    'sphinx.ext.githubpages', 'sphinxcontrib.bibtex', 'recommonmark',
    'sphinx_markdown_tables'
]

bibtex_bibfiles = ['ams_fpga.bib']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = u'en'
locale_dirs = ['locale/']
gettext_compact = False

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'emacs'

# Configure math and equations
numfig = True
math_numfig = True
numfig_secnum_depth = 1
math_eqref_format = "Eq. {number}"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'nature'
# html_theme = 'bizstyle'
html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {

#    ‘logo_only’: True,
#    ‘display_version’: True,
#    ‘prev_next_buttons_location’: ‘bottom’,
#    ‘style_external_links’: True,
#
#    # Toc options
#    ‘collapse_navigation’: False,
#    ‘sticky_navigation’: False,
#    ‘navigation_depth’: 3,
#    ‘includehidden’: True,
#    ‘titles_only’: False
#}

# html_title = “AMS FPGA Design”
# html_logo = “fig/logo.png”
# html_favicon = “fig/favicon.ico”

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['themes']

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = ['themes']

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
# html_style = 'default.css'

# html_theme_options = {
#    # 'nosidebar': 'true',
#    'footerbgcolor': '#000000',
#    'relbarbgcolor': '#000000',
# }

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'AMS-FPGAdoc'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'AMS-FPGA.tex', u'AMS-FPGA Documentation',
     u'A. Vasudevan, A. Venkatachalam, M. Meiners', 'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'AMS-FPGA', u'AMS-FPGA Documentation', [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'AMS-FPGA', u'AMS-FPGA Documentation', author, 'AMS-FPGA',
     'One line description of project.', 'Miscellaneous'),
]
