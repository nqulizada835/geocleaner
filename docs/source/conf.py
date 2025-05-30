# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # Adjust path to find geocleaner

project = 'geocleaner'
copyright = '2025, Nelofar Qulizada'
author = 'Nelofar Qulizada'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']