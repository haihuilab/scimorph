"""Install pubpy.

This script (setup.py) will install the pubpy package.
In order to expose .mplstyle files to matplotlib, "import pubpy"
must be called before theme_publication(...).
"""

import os
from setuptools import setup

# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pubpy',
    version='1.0.0',
    author="Haihui Zhang",
    author_email="hanfei19@gmail.com",
    maintainer="Haihui Zhang",
    maintainer_email="hanfei19@gmail.com",
    description="Scientific theme of Matplotlib for publication ",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="BSD 3-Clause License",
    url="https://github.com/haihuilab/pubpy/",

    install_requires=['matplotlib'],
    packages=["pubpy"],
    package_data={
      'pubpy': ['styles/**/*.mplstyle'],
    },

    classifiers=[
        'Framework :: Matplotlib', 
        'License :: OSI Approved :: BSD 3-Clause License',
        'Programming Language :: Python :: 3'
    ],
    keywords=[
        "matplotlib-style-sheets",
        "matplotlib-figures",
        "scientific-papers",
        "thesis-template",
        "matplotlib-styles",
        "python"
    ],
)
