import pandas as pd
from pandas.plotting import table
import matplotlib.pyplot as plt
import numpy as np

# import cleaned data
news = pd.read_csv("../data/clean_news.csv")

# generate unfiltered density plot
news["shares"].plot(kind='density')
plt.title("Density Plot of All Shares")
plt.savefig("../imgs/unfiltered_density.png", bbox_inches="tight")


# generate filtered density plot
pop_thresh = 2800
q = news["shares"].quantile(0.95)

pd.DataFrame(news["shares"][news["shares"] <= q]).plot(kind='density', legend=None)
plt.axvline(pop_thresh, color='orange')
plt.title("Density Plot of Shares (95% Quantile and Below)")
plt.savefig("../imgs/filtered_density.png", bbox_inches="tight")


# generate summary statistics
summary = pd.DataFrame(news["shares"].describe())
summary = np.round(summary, 2)
summary.index = ['Total Count', 'Mean', 'Standard Deviation', 'Minimum', '25%', '50%', '75%', 'Maximum']

# generate table and save it
fig, ax = plt.subplots(1, 1)

ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

summary_table = table(ax, summary, loc='center', colWidths=[1, 1])

summary_table.set_fontsize(12)
summary_table.scale(1, 1)

summary_table.figure.savefig("../imgs/summary_table.png", bbox_inches="tight")
