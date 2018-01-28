import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import table
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

news = pd.read_csv("../data/clean_news.csv")

# create training and test set
print("Creating training and test set")
X, Xtest, y, ytest = train_test_split(news.iloc[:, :-2], news.iloc[:,-1:], test_size=0.2)
y = y.as_matrix().reshape(len(y),)
ytest = ytest.as_matrix().reshape(len(ytest),)
X = X.as_matrix()
Xtest = Xtest.as_matrix()


# run CV to find regularizer constant
C_range = [10**i for i in range(-5,6)]
rfe_cv = {}

for c in C_range:
    print("Running cross-validation with C = {}".format(c))
    lr_rfe = RFE(LogisticRegression(penalty='l2', C=c))
    rfe_cv[c] = cross_val_score(lr_rfe, X, y, scoring='accuracy')

mean_cv = []
for i in rfe_cv:
    mean_cv.append(np.mean(rfe_cv[i]))

plt.plot(C_range, mean_cv)
plt.xscale('log')
plt.savefig("../imgs/cv_accuracy.png")


# train best model and extract coefficients and weights
print("Fitting best model")
lr_mod = RFE(LogisticRegression(penalty='l2', C=10**-5))
lr_mod.fit(X, y)

coefs_taken = news.columns[:-2][lr_mod.support_]
mod_coefs = {}
for i in range(len(lr_mod.estimator_.coef_[0])):
    mod_coefs[coefs_taken[i]] = lr_mod.estimator_.coef_[0][i]

df_coefs = pd.DataFrame([mod_coefs], columns=mod_coefs.keys()).transpose()
df_coefs.columns = ['Coefficient Value']

# generate table and save it
fig, ax = plt.subplots(1, 1)

ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

coef_table = table(ax, df_coefs, loc='center', colWidths=[1, 1])

coef_table.set_fontsize(12)
coef_table.scale(1, 1)

coef_table.figure.savefig("../imgs/coefficients.png", bbox_inches="tight")


# find test accuracy
test_acc = lr_mod.score(Xtest, ytest)
print("Test accuracy of best model is {}".format(test_acc))
