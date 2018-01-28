## Predicting the Popularity of Mashable Articles

This project analyzes the data set found [here](http://archive.ics.uci.edu/ml/datasets/Online+News+Popularity), which contains info on articles posted on Mashable, as well as the number of shares they received on social media. The goal of the project is to predict whether or not a Mashable article will be popular (where popular is defined as being above 2800 shares), as well identifying the most relevant features to an articles popularity.

A logistic regression model with L2-regularization was fit using recursive feature elimination in `sklearn`.

A write-up of the final analysis can be read [here](https://github.com/conleyst/predicting-social-media-shares/blob/master/analysis.md).

#### Requirements

The entire analysis is done in `Python 3.6.3`, using the following packages:
- `pandas, v0.20.3`
- `numpy, v1.13.3`
- `sklearn, v0.19.1`

#### Running the Analysis

The entire analysis can be run locally, after cloning, from within the `src` directory of the project.

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
