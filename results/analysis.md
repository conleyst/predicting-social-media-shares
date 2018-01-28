### Overview

The data set [here](http://archive.ics.uci.edu/ml/datasets/Online+News+Popularity) contains information on articles posted on Mashable as well as the number of shares they received via social media. There are 61 features in the data set -- this includes the response `shares` as well the URL to the article and the time between the article's posting and when the data was found, both of which are metadata for the study the data was used in and are irrelevant to the response. After cleaning then, there are 58 predictors and one response. A full list of the predictors and what they measure can be found on the website the data was taken from. There are 39644 observations in the data set. The goal of the analysis is to predict whether or not an article will be popular and which features are most relevant to an article's popularity.

The first issue is of course what it means for an article to be popular. The distribution of the shares is incredibly right-skewed. We can see it from the below image,

![](../imgs/unfiltered_density.png)

It's even more evident from the summary statistics,

![](../imgs/summary_table.png)

where we can see the effect that a handful of outlier articles are having on the mean. With this in mind, the mean isn't a good benchmark to compare against to classify popularity. Instead, we can define popularity relative to quantiles -- we'll consider any article in the 75th-percentile (i.e. with shares above 2800) as being popular. Filtering out articles in the 95th percentile of shares, we can see where this benchmark lies,

![](../imgs/filtered_density.png)

### Analysis

Our analysis has two goals:

1. To be able to accurately predict the popularity of an article.
2. To identify the features most relevant to the popularity of an article.

 We're trying to predict the likelihood that a given article will surpass the 2800 article threshold. To classify new articles using the model, we'll predict that any article with a probability of at least 0.5 will be popular.

First, the data was randomnly split into a training and test set. The test set contained 20% of the observations. I wanted to encourae sparsity in the actual weights for the features to better identify the features that are potentially more relevant to an article's popularity. With this in mind, the model I fit used L2-regularized logistic regression along with recursive feature elimination for the actual feature selection.

To choose the penalty weight `C` used in the model, I used cross-validated and scored on accuracy. Powers of 10 were tested, ranging from 10^-5 to 10^5. In the end though, in turns out that accuracy varied very little between the tested values,

![](../imgs/cv_accuracy.png)

Note here that C is inversely proportional to the actual magnitude of the constant, so using a larger penalty actually scored a higher accuracy. In the interest of encouraging sparsity, I did take 10^-5 as the value for `C`.

Fitting the model with this value for C, only 29 features are actually used in the logistic regression -- half the number of features that we started with. The ones found are in the table below,

![](../imgs/coefficients.png)

A full description of these features can be found where the data was taken from, but there are a few interesting patterns that we can note. For one, no feature actually has that strong of a predictive power. However, of the coefficients used, four are an order of magnitude larger than the others:

- `n_tokens_title`: The number of words in the title.
- `num_self_hrefs`: The number of links in the article to other Mashable content.
- `average_token_length`: The average length of the words in the content.
- `num_keywords`: Number of keywords the article is tagged with.

All of these were negatively associated with a high probability of being popular, according to our model. We can hypothesize a few things from this. For one, it seems that shorter is better. According to the model, a long title and longer words are going to decrease the probability that an article becomes popular. Secondly, linking to other Mashable articles could decrease the probability of popularity. Perhaps people tend to link the last article they read -- if you link to other Mashable articles then yours won't be the last in the chain that people read. Finally, tagging your article with a lot of keywords also decreases the chance the article will be popular.

From the other coefficients, we can discern more patterns. For example, articles posted on weekends are more likely to be popular, and the most popular articles seem to be those posted in the Social Media channel on Mashable.

How confident should we be that the model is actually identifying important predictors for popularity? Well, in terms of the model performance on the test set, running the model on the test set gives an accuracy of approximately 74.56%. Considerably better than chance, though not perfect. It seems that the model might be identifying real trends in the data, but it's not capturing everything.
