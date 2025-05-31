# .readthedocs.yaml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
  extra_requirements:
    - docs  # Installs from docs/requirements.txt

sphinx:
  configuration: docs/source/conf.py

extensions = ["sphinx_rtd_theme"]
html_theme = "sphinx_rtd_theme"
