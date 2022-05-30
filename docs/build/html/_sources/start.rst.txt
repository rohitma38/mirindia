Getting Started
===============

Installation
************
If you are new to python, we recommend first installing miniconda from - https://conda.io/projects/conda/en/latest/user-guide/install/index.html.

From Source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Download the library from github as a `zip file <https://github.com/rohitma38/mirindia/>`_ and extract to a location of your choice, or clone the library with::

    git clone https://github.com/rohitma38/mirindia

Next, set up a new virtual environment with the environment file provided in the library to create a new environment with the dependencies installed::

    conda env create –f environment.yml 
    conda activate mirindia

**OR**

With pip/conda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Install with pip/conda to a new or existing environment (TODO: upload library to pypi/conda-forge)::

    pip/conda install mirindia 

New environment can be created with conda using::

    conda create -n <name-of-environment>

Other optional setup 
^^^^^^^^^^^^^^^^^^^^
- Pytorch
- Spleeter (source separation) 


Usage
*****
Once installed you can start using the library in one of the following ways. See our tutorials for more comprehensive examples. 

1. Open anaconda prompt on Windows, or the regular terminal on Mac and Linux 

2. Start the virtual environment if you created one::

    conda activate mirindia

3. Start a python shell and import the library::

    python3 
    import mirindia

4. Or start jupyter notebook, open a new/existing notebook in the web browser interface and import the library (see one of the tutorial notebooks for an example)::

    jupyter-notebook 
    import mirindia


Tutorials 
*********
See below example jupyter notebook files to help you get started:

1. Load audio, compute pitch track, compute spectrogram, plot all (`Notebook 1 <https://github.com/rohitma38/rtd-test-code-2/blob/main/example%20notebooks/example-1.ipynb>`_)
2. Load audio, compute onsets, compute tempogram, plot all (`Notebook 2 <https://github.com/rohitma38/rtd-test-code-2/blob/main/example%20notebooks/example-tempogram.ipynb>`_)
