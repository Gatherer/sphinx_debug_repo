#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# This file is execfile()d with the current directory set to its
# containing dir.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# set submodule path
import os
import sys
sys.path.insert(0, 'sphinx_base_repo.git/')

from conf import *

# -- Project information -----------------------------------------------------
# Partner (usually customer, like in cgit). Empty for internal projects.
partner = ''
# Project name (short form).
project = 'Sphinx Template'
# Long project name to be used in the title only. Optional.
project_long = 'Just a design'
# Copyright notice. Usually just the date has to be adapted.
copyright = '2024, Thomas Inc'
# Author. Only to be changed if third party is involved.
author = 'gatherer'
legal = 'Company Confidential'

# By default, the different dates are set to something unusual
# variable used by latex_documents[]
version = "99.99.99"
# The full version, including alpha/beta/rc tags.
release = "99.99.99r18"

# configure bibtex
# bibtex_bibfiles = ['refs.bib']

# latex_elements = {
#     # The paper size ('letterpaper' or 'a4paper').
#     #
#     'papersize': 'a4paper',

#     # Additional stuff for the LaTeX preamble.
#     #
#     'preamble':
#         r'\usepackage{mle}' + '\n'
#         r'\setpartner{' + partner + ' }\n'
#         r'\setproject{' + project + '}\n'
#         r'\setprojectlong{' + project_long + '}\n'
#         r'\setlegal{' + legal + '}',

#     # add fancy chapter package
#     #
#     'fncychap': '',
# }

latex_documents = [
    (
        'index',
        'sphinx-test-guide_{}.tex'.format(version),
        'User Guide',
        'Gatherer',
        'manual'
    ),
]
