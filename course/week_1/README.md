# Advanced Chemistry Practical - Computational
## University of Bath, Department of Chemistry
### Week 1

This week will involve a general introduction to molecular dynamics simulations, focusing on making use of the Python programming skills that you first met in years 1 and 2 of your chemistry degree. It may be the case that you cannot reckon particular aspects of Python, if this is the case you are advised to investigate the links within the Jupyter notebook or alternatively look back on the exercises from first and second year.

Before we can start, it is necessary to build the appropriate environment for to perform this exercise. To do this, first open the *Anaconda Prompt* (Start Menu -> Anaconda -> Anaconda 3), and type the following (each new line incidates that your should be pressing enter):

```
conda create -n adv_lab python
```

When asked if you would like to *proceed* with the installation of the sofwate press `y` and then enter.

You have just build a [conda environment](https://conda.io/docs/user-guide/tasks/manage-environments.html), to access your environment type:

```
activate adv_lab
```

You should now see the pharse `(adv_lab)` preceeding the line on which you are typing. Finally we must install two programs:

```
pip install pylj

conda install nb_conda
```

On the second installation you may be asked if you would like to *proceed*, once again press `y` and enter.

You can now launch the Jupyter notebook from this command line by typing

```
jupyter notebook
```

## Authors

- Andrew R. McCluskey
- Adam R. Symmington
