# reproducible-data-science

This repository contains a tutorial on reproducible data science.

It includes a brief discussion of recent history and theory around reproduciblity, a cursory introduction to the technical building blocks for implementing reproducible data science, and a short survey of the current landscape of tools.

The core of the repository is a hands-on tutorial on doing reproducible data science using [RENKU](https://renkulab.io).

# Set-up

The tutorial comes in two variants, *hosted* and *local*. For the hosted version, no local setup is necessary. The only requirement is a reasonably current browser (Firefox, Chrome, and Safari have all been tested, Edge should work as well).

For the local version, follow these instructions.

## Step 1: Create Environment

To avoid conflicts in dependencies, we recommend creating a dedicated environment for this tutorial. You can do this using any tools you like, for example [pipenv](https://pipenv.readthedocs.io/en/latest/) or [conda](https://docs.conda.io/en/latest/miniconda.html). We provide instructions based on conda here.

```
conda create -n renku-tutorial python=3.7
conda activate renku-tutorial
```

## Step 2: Install renku and libraries used in the tutorial

```
pip install -r requirements.txt
```
