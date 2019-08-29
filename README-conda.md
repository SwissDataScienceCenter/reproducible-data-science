
# Create Environment

0. If you do not yet have conda, you should first [install miniconda for your platform](https://conda.io/miniconda.html)
1. Download the [conda environment](https://raw.githubusercontent.com/SwissDataScienceCenter/reproducible-data-science/master/environment.yml)
2. In the directory where `environment.yml` is located, execute `conda env create -n r10eds -f environment.yml`


# Verify Environment

1. Activate the environment with `conda activate r10eds`
2. Run `git --version` -- the result should be "git version 2.21.0" (or newer)
3. Run `git lfs --version` -- the result should be "git-lfs/2.8.0" (or newer)
4. Run `renku --version` -- the result should be "0.5.2" (or newer)


# Clone Tutorial Repository

1. Activate the environment with `conda activate r10eds`
2. Clone the repository `git clone https://github.com/SwissDataScienceCenter/reproducible-data-science.git`

# Work Through Hands On

0. cd into the tutorial repository `cd reproducible-data-science`
1. Activate the environment with `conda activate r10eds`
2. Start jupyter lab `jupyter lab` (you can also use plan jupyter)

Enter the [notebooks/hands-on/local_notebook](notebooks/hands-on/local_notebook) directory, and start jupyter, and open the `index.ipynb` notebook to work through the hands-on.
