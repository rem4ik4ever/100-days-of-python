import matplotlib.pyplot as plt

plt.style.use('seaborn')

fig,ax = plt.subplots()

x_values = [i for i in range(1, 5001)]
y_values = [i ** 3 for i in range(1, 5001)]

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square Value', fontsize=14)

ax.tick_params(axis='both', labelsize =14)

ax.axis([0, 5100, 0, 5001 ** 3 + 1000])

plt.savefig('squares_plot.png', bbox_inches='tight')
# plt.show()

plt.cm.cmaps_listed.keys()