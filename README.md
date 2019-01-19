
# Nowan's Mafia Gametype prediction competition - Baseline model

This is the repository for the baseline solution to the stated Kaggle competition. 
It is hosted by Kaggle InClass and contains data from the Bay12 Games forums, 
where I have played a lot of mafia (werewolf) and variants.

The solution itself can be found in [this notebook](https://github.com/NowanIlfideme/kaggle_ni_mafia_gametype/blob/master/notebooks/1_initial_model.ipynb). 
It requires the libraries to be installed, though.

## Installing the library

In order to use this effectively, you need to install the library `bay12_solution_eposts` and its dependencies from the src directory. 
You may want to activate a new virtual environment before running (example with Conda, using the environment name from the file):

```{cmd}
conda env create -f environment.yaml
activate kaggle-mafia-gametype
```

Then you can install (better, "develop") from source:

```{cmd}
cd src
python setup.py develop
``` 

You may use `python setup.py install` instead, but it won't update with any changes 
you will make, so I suggest develop. 
Side note: The references to "eposts" are due to the initial name for the competition 
being "extended posts", which is how I called it during the internet scraping phase.

## Where to put the data

I set the data to be in the directories:

* Train: `data/train/...`
* Test: `data/test/...`
* Label map: `data/label_map.csv`.

In order for the loading funtions from `bay12_solution_eposts.prepare` to work, you should 
set them there. However, you can just set the `path_data` variable in the function call (if the path is 
somewhere else) or even change the `DEFAULT_PATH_DATA` variable.

## Running the notebooks

Use the `jupyter notebook` command from this directory, then navigate to the notebooks. 
If you want to do some of your own experiments, I suggest making a copy first. ;)
