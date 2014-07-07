import os
from setuptools import setup, find_packages

setup(name='morepath_static',
      version = '0.1dev',
      description="Morepath more.static demo app",
      author="Martijn Faassen",
      author_email="faassen@startifact.com",
      license="BSD",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'morepath',
          'more.static',
        ],
      entry_points= {
        'console_scripts': [
            'morepath_static = morepath_static.main:main',
            ]
        },
      )
