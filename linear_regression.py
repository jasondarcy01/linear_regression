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

# ir = loansData['Interest.Rate']
# interest_rate = list(map((lambda x: x[:-1]), ir))
# print interest_rate

fc = loansData['FICO.Range']
fico = list(map((lambda x: x.split('-')), fc))
for item in fico:
  print min(item)


# tm = loansData['Loan.Length']
# term = list(map((lambda x: x[:-6]), tm))
# print term

# import matplotlib.pyplot as plt
# plt.figure()
# loansData['fico'].hist()
# plt.show()