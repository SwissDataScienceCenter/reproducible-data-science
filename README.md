# Reproducible Data Science in Python using Renku


# Description

The expectation of reproducibility in scientific work has been long established, and, increasingly, communities and funding sources are actually demanding it. Within the Python ecosystem, there are a variety of tools available to support reproducible data science, but choosing and using one is not always straightforward. In this tutorial, we will take a closer look at the concept of _reproducibility_, and, we will examine the technologies that provide building blocks and survey the landscape of tools. We spend the majority of the time looking at one solution in particular, [Renku](https://renkulab.io) and work through an end-to-end scenario with it.

# Set Up

There are several easy ways to set up an environment for working through the tutorial. The easiest is to use a hosted environment.

## Hosted

* Renkulab is a Renku environment hosted by SDSC. [Follow these instructions to use Renkulab](README-renkulab.md).

* Alternatively, you can use a [MyBinder Environment](https://mybinder.org/v2/gh/SwissDataScienceCenter/reproducible-data-science/master).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SwissDataScienceCenter/reproducible-data-science/master)

## Local

If you wish to run the tutorial on your own computer, you can create an environment with conda or docker.

* [Set up an environment using conda](README-conda.md)
* [Set up an environment using docker](README-docker.md)

 If you prefer to use something else (e.g., [pipenv](https://pipenv.readthedocs.io/en/latest/)), you will need to ensure that `git`, `git-lfs`, `curl`, and `node` are installed in your environment, but you should be able to pip install the requirements.txt file for the rest.

**Note for Windows users**
If you are on Windows, we recommend using one of the hosted environments, either renkulab or binder.

# Schedule

<table style="font-size: 14px; margin: 10px;">
    <tbody>
        <tr>
            <th>Introduction (1h)</th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th>15 min</th>
            <td>Background &amp; Theory</td>
            <td style="text-align: left">Terminology, history, and philosophy of reproducibility</td>
        </tr>
        <tr>
            <th>30 min</th>
            <td>Building Blocks</td>
            <td style="text-align: left">Building blocks for achieving reproducibility</td>
        </tr>
        <tr>
            <th>15 min</th>
            <td>Tools</td>
            <td style="text-align: left">Survey of the current tool landscape</td>
        </tr>
        <tr>
            <th></th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th>Break (10 min)</th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th></th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th>Hands-on with Renku (1h 30m)</th>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th>30 min</th>
            <td>Starting</td>
            <td style="text-align: left">Starting a project, importing data, building a workflow</td>
        </tr>
        <tr>
            <th>30 min</th>
            <td>Iterating</td>
            <td style="text-align: left">Updating code and data to improve analysis</td>
        </tr>
        <tr>
            <th>30 min</th>
            <td>Details and Reflection</td>
            <td style="text-align: left">What is the benefit? How much effort was it? How do we view, share, and reuse artifacts? How do things work under the covers?</td>
        </tr>
     </tbody>
</table>

# Acknowledgements

Many thanks to Erica Moreira, Laura Levin-Gleba, and Maja Garbulinksa from the Harvard School of Public Health for their helpful comments and suggestions!

The icons used are from [Icons8](https://icons8.com/).
