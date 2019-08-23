#!/usr/bin/env python
"""Remove all artifacts of running"""
import subprocess
import glob


def strip_notebook_output_cells(notebook):
    subprocess.run(['jupyter',  'nbconvert', '--inplace', '--ClearOutputPreprocessor.enabled=True', notebook])

def strip_output_cells():
    """Strip output cells from the notebooks"""
    templates = glob.glob("templates/*.ipynb")
    for t in templates:
        strip_notebook_output_cells(t)
    metanbs = glob.glob("./*.ipynb")
    for t in metanbs:
        strip_notebook_output_cells(t)


def warn_tutorial_artifacts():
    """Check and warn if tutorial execution artifacts are found."""
    paths = glob.glob("renku-tutorial-*")
    if len(paths) < 1:
        print("No artifacts found.")
        return

    print("Found {} execution folder(s).".format(len(paths)))
    for path in paths:
        print("Found {}. May want to clean with 'rm -rf {}'".format(path, path))


print("Stripping output cells from notebooks...")
strip_output_cells()

print("\nChecking for tutorial execution artifacts...")
warn_tutorial_artifacts()

print("Done.")
