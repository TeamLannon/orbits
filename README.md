# Orbital Simulation

This is an experiment in writing python-based orbit simulator

## Getting things set up

The steps below need to be executed to get things set up.

1. In the terminal, `cd` to the directory where you want to set up this code.
1. Setup an ssh key with Github following instructions at Github (if you haven't done this before).
1. Pull the code down from Github by cloning the repository:
   ```
   git@github.com:TeamLannon/orbits.git
   ```
1. Create the corresponding `mamba`/`conda` environment (requires that you've installed `mamba` or `conda`).  I'll give the `mamba` command, but to use `conda`, just replace `mamba` with `conda`.
   ```
   mamba env create -f environment.yml
   ```
1. Activate your environment
   ```
   mamba activate orbits
   ```
1. Install the orbits package in your environment
   ```
   pip install -e .
   ```

## What to do when you're using the code after first setting it up
1. In the terminal, navigate to the directory where you installed orbits (see above).
2. Activate the mamba environment with `mamba activate orbits`

## Useful references
* [Astroquery](https://astroquery.readthedocs.io/en/latest/): A tool for getting data about planetary locations
