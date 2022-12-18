#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
import sys
import isometabolabpy

def main():

    if not ((sys.version_info[0] != 3) or (sys.version_info[1] >= 6)):
        sys.exit("Python >=3.6 is required ")

    # read the contents of your README file
    with open('README.rst', encoding='utf-8') as f:
        long_description = f.read()

    setuptools.setup(name="qtmetabolabpy",
        version=qtmetabolabpy.__version__,
        description="Python package for calculation of isotopomer distribution of NMR and MS based metabolic tracing data",
        long_description=long_description,
        author="Christian Ludwig",
        author_email="C.Ludwig@bham.ac.uk ",
        url="https://github.com/ludwigc/isometabolabpy",
        license="GPLv3",
        platforms=['MacOS, Windows, UNIX'],
        keywords=['Metabolomics', 'Tracing', 'NMR', 'MS', '13C'],
        packages=setuptools.find_packages(),
        test_suite='tests.suite',
        install_requires=open('requirements.txt').read().splitlines(),
        include_package_data=True,
        classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.9",
          "Topic :: Scientific/Engineering :: Bio-Informatics",
          "Topic :: Scientific/Engineering :: Chemistry",
          "Topic :: Utilities",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent",
        ],
        entry_points={
         'console_scripts': [
             'isometabolabpy = isometabolabpy.__main__:main'
         ]
        }
    )


if __name__ == "__main__":
    main()
  
