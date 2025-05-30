# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys

# Add your package to the Python path to enable autodoc
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------
project = 'GeoAddressCleaner'
copyright = '2025, Nelofar Qulizada'
author = 'Nelofar Qulizada'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',      # Automatically document your code
    'sphinx.ext.viewcode',     # Add links to source code
    'sphinx.ext.napoleon',     # Support for Google and NumPy docstrings
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'  # ReadTheDocs theme
# html_theme = 'alabaster'       # Uncomment to use the Alabaster theme

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files.
html_static_path = ['_static']
