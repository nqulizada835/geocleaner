Geocleaner
==========

A small Python package to clean and standardize location strings.

.. image:: https://img.shields.io/pypi/v/geocleaner.svg
   :target: https://pypi.org/project/geocleaner/

Features
--------

- Cleans and standardizes messy location strings
- Handles abbreviations, typos, accented characters, and punctuation
- Designed for easy integration

Installation
------------

.. code-block:: bash

   pip install geocleaner

Quickstart
----------

.. code-block:: python

   from geocleaner.core import clean_location
   print(clean_location("123 main st, ny"))  # 123 Main Street, New York

Links
-----

- `Source code <https://github.com/nqulizada835/geocleaner>`_
- `PyPI <https://pypi.org/project/geocleaner/>`_

.. toctree::
   :maxdepth: 2

   geocleaner.core
