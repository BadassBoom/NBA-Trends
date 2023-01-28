import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import chi2_contingency, pearsonr

np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('nba_games.csv')

nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knicks_pts = nba_2010.pts[nba.fran_id =='Knicks']
nets_pts = nba_2010.pts[nba.fran_id =='Nets']
knicks_mean_score = np.mean(knicks_pts)
nets_mean_score = np.mean(knicks_mean_score)
diff_means_2010 = knicks_mean_score - nets_mean_score

print(diff_means_2010)

plt.hist(knicks_pts, alpha=0.8, label='knicks')
plt.hist(nets_pts, alpha=0.8, label='nets')

plt.legend()
plt.show()

knicks_pts_2014 = nba_2014.pts[nba.fran_id =='Knicks']
nets_pts_2014 = nba_2014.pts[nba.fran_id =='Nets']
knicks_mean_score_2014 = np.mean(knicks_pts_2014)
nets_mean_score_2014 = np.mean(knicks_mean_score_2014)
diff_means_2014 = knicks_mean_score_2014 - nets_mean_score_2014

print(diff_means_2014)

plt.hist(knicks_pts_2014, alpha=0.8, label='knicks_2014')
plt.hist(nets_pts_2014, alpha=0.8, label='nets_2014')
plt.legend()
plt.show()
plt.clf()

sns.boxplot(data = nba_2010, x = 'fran_id', y = 'pts' )
plt.show()

location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)

print(location_result_freq)

chi2, pval, dof, expected = chi2_contingency(location_result_freq)

print(expected)
print(chi2)

coraviance = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(coraviance)

corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(corr)

plt.clf()
plt.scatter('forecast', 'point_diff', data=nba_2010)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()