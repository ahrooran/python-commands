import matplotlib.pyplot as plt

year=[2010,2011,2012,2013,2014,2015]
rice=[10,30,50,30,40,200]


plt.xlabel('years')
plt.ylabel('rice prod')
plt.title('riceprod in ')

plt.plot(year,rice)
plt.show()