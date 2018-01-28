import pandas as pd

# import raw data
news = pd.read_csv("../data/OnlineNewsPopularity/OnlineNewsPopularity.csv")

# remove whitespace and first two irrelevant features
news = news.rename(columns=lambda x: x.strip())
news = news.iloc[:, 2:]

# classify articles as popular or not
pop_thresh = 2800


def is_pop(x):
    if x >= pop_thresh:
        return 1
    else:
        return 0


news["is_pop"] = news["shares"].apply(lambda x: is_pop(x))

# save data frame
news.to_csv("../data/clean_news.csv")
