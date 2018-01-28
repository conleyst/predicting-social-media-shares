## Predicting the Popularity of Mashable Articles

This project analyzes the data set found [here](http://archive.ics.uci.edu/ml/datasets/Online+News+Popularity), which contains info on articles posted on Mashable, as well as the number of shares they received on social media. The goal of the project is to predict whether or not a Mashable article will be popular (where popular is defined as being above 2800 shares), as well identifying the most relevant features to an articles popularity.

A logistic regression model with L2-regularization was fit using recursive feature elimination in `sklearn`.

A write-up of the final analysis can be read [here](https://github.com/conleyst/predicting-social-media-shares/blob/master/analysis.md).

#### Required Packages

The entire analysis is done in Python, using the following packages:
- `pandas`
- `numpy`
- `sklearn`

#### Running the Analysis

The entire analysis can be run locally from within the `src` directory of the project.

Cleaning the data:

```
python clean_data.py
```

Generating figures:

```
python gen_figs.py
```

Running the analysis:

```
python analysis.py
```
