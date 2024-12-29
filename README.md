Science Plots
=============

<p align="left">
    <table>
        <tr>
            <td style="text-align: center;">PyPI version</td>
            <td style="text-align: center;">
                <a href="https://badge.fury.io/py/SciencePlots">
                    <img src="https://badge.fury.io/py/SciencePlots.svg" alt="PyPI version" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">conda-forge version</td>
            <td style="text-align: center;">
                <a href="https://anaconda.org/conda-forge/scienceplots">
                    <img src="https://anaconda.org/conda-forge/scienceplots/badges/version.svg" alt="conda-forge version" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">DOI</td>
            <td style="text-align: center;">
                <a href="https://zenodo.org/badge/latestdoi/144605189">
                    <img src="https://zenodo.org/badge/144605189.svg" alt="DOI" height="18"/>
                </a>
            </td>
        </tr>
    </table>
</p>

> **Warning**
> : The `pubpy` needs LaTeX for math formatting: `sudo apt install texlive texlive-latex-extra texlive-fonts-recommended cm-super dvipng`
> : As of version 1.0.0, you need to add `import pubpy` before setting the style (`theme_publication('publication')`).

*Matplotlib styles for scientific figures*

This repo has Matplotlib styles to format your figures for scientific papers, presentations and theses.

<p align="center">
<img src="https://github.com/haihuilab/pubpy/examples/plots/fig01a.jpg" width="500">
</p>

You can find [the full tutorials of pubpy here](https://github.com/haihuilab/pubpy/wiki/Gallery).

Getting Started
---------------

The easiest way to install pubpy is by using `pip`:

```bash
# to install the latest release (from PyPI)
pip install pubpy

# to install the latest release (using Conda)
conda install -c conda-forge pubpy

# to install the latest commit (from GitHub)
pip install git+https://github.com/haihuilab/pubpy

# to clone and install from a local copy
git clone https://github.com/haihuilab/pubpy.git
cd pubpy
pip install -e .
```

From version `v1.0.0` on, `import pubpy` is needed on top of your scripts so Matplotlib can make use of the styles.

**Notes:** 
- pubpy-theme_publication requires matplotlib or seaborn

Using the Styles
----------------

``"publication"`` is the primary style in this repo. Whenever you want to use it, simply add the following to the top of your python script:

```python
import matplotlib.pyplot as plt
import pubpy

theme_publication('publication')
```


Examples
--------

The basic ``publication`` style is shown below:

<img src="https://github.com/haihuilab/pubpy/examples/plots/fig01a.jpg" width="500">



If you use ``pubpy`` in your paper/thesis, feel free to add it to the list!

Citing pubpy:
-------------------

    @article{pubpy,
      author       = {Haihui Zhang et al},
      title        = {haihuilab/pubpy},
      month        = Jan,
      year         = 2025,
      publisher    = {github},
      version      = {1.0.0},
      doi          = {......},
      url          = {https://github.com/haihuilab/pubpy}
    }
