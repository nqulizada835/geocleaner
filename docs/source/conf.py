# docs/source/conf.py

project = 'geocleaner'
author = 'Nelofar Qulizada'
copyright = '2025, Nelofar Qulizada'

extensions = ["sphinx_rtd_theme"]
html_theme = "sphinx_rtd_theme"

# If you want to use autodoc, add this:
import os
import sys
sys.path.insert(0, os.path.abspath('C:\Users\nquli\Documents\GitHub\geocleaner'))  # Adjust path to your package root

# Optional: Add static and template paths if needed
# html_static_path = ['_static']
# templates_path = ['_templates']
