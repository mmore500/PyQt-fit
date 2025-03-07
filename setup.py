#!/usr/bin/env python

from setuptools import setup

#from path import path

#with (path(__file__).dirname() / 'pyqt_fit' / 'version.txt').open() as f:
    #__version__ = f.read().strip()

import os.path

version_filename = os.path.join(os.path.dirname(__file__), 'pyqt_fit', 'version.txt')
with open(version_filename, "r") as f:
    __version__ = f.read().strip()

with open("README.md", "r") as fh:
    long_description = fh.read()

extra = {}


setup(name='PyQt-Fit',
      version=__version__,
      description='Parametric and non-parametric regression, with plotting and testing methods.',
      author='Pierre Barbier de Reuille',
      author_email='pierre.barbierdereuille@gmail.com',
      url='https://github.com/PierreBdR/PyQt-fit',
      download_url='https://github.com/PierreBdR/PyQt-fit/archive/v_1_4_0.tar.gz',
      packages=['pyqt_fit', 'pyqt_fit.functions', 'pyqt_fit.residuals', 'pyqt_fit.test'],
      package_data={'pyqt_fit': ['qt_fit.ui',
                                 'version.txt',
                                 'cy_local_linear.pyx',
                                 '_kernels.pyx',
                                 '_kde.pyx',
                                 'cy_binning.pyx',
                                 'math.pxd'
                                 ]
                    },
      scripts=['bin/pyqt_fit1d.py'],
      install_requires=[
                        'numpy >=1.5.0',
                        'scipy >=0.10.0',
                        'matplotlib',
                        'path >=13.0',
                        'qtpy >=1.7.1',
                        ],
      extras_require={'Cython': ["Cython >=0.17"]
                      },
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='LICENSE.txt',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: X11 Applications :: Qt',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                   'Natural Language :: English',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Scientific/Engineering :: Mathematics',
                   'Topic :: Scientific/Engineering :: Visualization',
                   ],
      test_suite='nose.collector',
      platforms=['Linux', 'Windows', 'MacOS'],
      **extra
      )
