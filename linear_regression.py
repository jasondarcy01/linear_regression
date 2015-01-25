import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# print loansData['Interest.Rate']
# print loansData['FICO.Range'][0:5]
# print loansData['Amount.Requested'][0:5]
# print loansData['Loan.Length'][0:5]

# g = lambda x: x**2
# print g(5)

# items = [1, 2, 3, 4, 5]
# print list(map((lambda x: x**2), items))

ir = loansData['Interest.Rate']
loansData['Interest'] = list(map((lambda x: x[:-1]), ir))


tm = loansData['Loan.Length']
term = list(map((lambda x: x[:-6]), tm))
# print term

fr = loansData['FICO.Range']
fr_min = map(lambda x: x.split('-'), fr)
loansData['FICO.Score'] = map(lambda x: min(x), fr_min)
# print loansData['FICO.Score'].dtypes
loansData['FICO.Score'] = loansData['FICO.Score'].astype(int)

# print loansData['FICO.Score']

import matplotlib.pyplot as plt

# plt.figure()
# loansData['FICO.Score'].hist()
# plt.show()

# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
# plt.show()

# print loansData

import numpy as np
import statsmodels.api as sm

intrate = loansData['Interest'].astype(float)
loanamt = loansData['Amount.Requested'].astype(float)
fico = loansData['FICO.Score']


y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

# print f.params
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared




