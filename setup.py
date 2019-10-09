import os
import shutil
import sys
import glob
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = 'x.y.z'
if os.path.exists('VERSION'):
  version = open('VERSION').read().strip()

setup(
    name='scagaire',
    version=version,
    description='scagaire: filter anti-biotic genes by species',
	long_description=read('README.md'),
    packages = find_packages(),
    author='Andrew J. Page',
    author_email='andrew.page@quadram.ac.uk',
    url='https://github.com/quadram-institute-bioscience/scagaire',
    scripts=glob.glob('scripts/*'),
    test_suite='nose.collector',
    tests_require=['nose >= 1.3'],
    install_requires=[
           'biopython >= 1.68'
       ],
    package_data={'scagaire': ['data/*', 'data/*/*']},
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
		'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
)
