import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = x
colors = ['green'] * (len(x) - 1)
colors.append('red')
plt.figure()
plt.scatter(x, y, s=100, c=colors)

zip_generator = zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
# print(list(zip_generator))

zip_generator = zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
x, y = zip(*zip_generator)

plt.figure()
plt.scatter(x[:2], y[:2], s=100, c='red', label='Tall students')
plt.scatter(x[2:], y[2:], s=100, c='blue', label='Short students')
plt.xlabel('The number of times the child kick the ball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')
plt.legend()
plt.legend(loc=4, frameon=False, title='Legend')

linear_data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
quadratic_data = linear_data ** 2
plt.figure()
plt.plot(linear_data, '-o', quadratic_data, '-o', [22, 44, 55], '--r')
plt.xlabel('Some data')
plt.ylabel('Some other data')
plt.title('A title')
plt.legend(['Baseline', 'Competition', 'Us'])
plt.gca().fill_between(range(len(linear_data)),
                       linear_data, quadratic_data,
                       facecolor='blue',
                       alpha=0.25)

plt.figure()
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates))
plt.plot(observation_dates, linear_data, '-o',
         observation_dates, quadratic_data, '-o')
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)
plt.subplots_adjust(bottom=0.25)
ax = plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title('Quadratic vs. Linear performance')

plt.show()
