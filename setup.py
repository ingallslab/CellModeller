#!/usr/bin/env python

import os
#from distutils.core import setup
from setuptools import setup
import subprocess


# Fetch version from git tags, and write to version.py.
# Also, when git is not available (PyPi package), use stored version.py.
version_py = os.path.join(os.path.dirname(__file__), 'CellModeller/version.py')

try:
    version_git = subprocess.check_output(["git", "describe"]).rstrip()
except:
    with open(version_py, 'r') as fh:
        version_git = open(version_py).read().strip().split('=')[-1].replace('"','')

#version_msg = "# Do not edit this file, pipeline versioning is governed by git tags"
#with open(version_py, 'w') as fh:
#    fh.write(version_msg + os.linesep + "__version__='" + version_git + "'")


setup(name='CellModeller',
    install_requires=['numpy', 'scipy', 'pyopengl', 'mako', 'pyqt5', 'pyopencl', 'reportlab', 'matplotlib','vtk'],
    setup_requires=['numpy', 'scipy', 'pyopengl', 'mako', 'pyqt5', 'pyopencl', 'reportlab', 'matplotlib','vtk'],
    packages=['CellModeller',
                'CellModeller.Biophysics',
                'CellModeller.Biophysics.BacterialModels',
                'CellModeller.Biophysics.GeneralModels',
                'CellModeller.Integration',
                'CellModeller.Regulation',
                'CellModeller.Signalling',
                'CellModeller.GUI'],
     package_data={'':['*.cl','*.ui']},
     python_requires='>=3',
     version=str(version_git)
)
