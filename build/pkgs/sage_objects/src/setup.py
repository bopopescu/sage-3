#!/usr/bin/env python

from distutils import log
from setuptools import setup

from sage_setup.command.sage_build_cython import sage_build_cython
from sage_setup.command.sage_build_ext import sage_build_ext

from sage_setup.find import find_python_sources, is_package_or_namespace_package_dir
python_packages, python_modules, cython_modules = find_python_sources(
    '.', ['sage'], distributions=None)   # for now, we do the filtering using MANIFEST

log.warn('python_packages = {0}'.format(python_packages))
log.warn('python_modules = {0}'.format(python_modules))
log.warn('cython_modules = {0}'.format(cython_modules))

import Cython.Build.Dependencies
import Cython.Build.Cythonize
import Cython.Utils
Cython.Utils.is_package_dir = Cython.Build.Cythonize.is_package_dir = Cython.Build.Dependencies.is_package_dir = is_package_or_namespace_package_dir

setup(
    cmdclass = dict(build_cython=sage_build_cython,
                    build_ext=sage_build_ext),
    packages = python_packages,
    py_modules  = python_modules,
    ext_modules = cython_modules
)
