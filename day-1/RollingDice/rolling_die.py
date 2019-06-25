from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die1 = Die(3)
die2 = Die(10)
die3 = Die(18)

results = [] 

for roll_num  in range(1000000):
  result = die1.roll() + die2.roll()
  results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(2, max_result + 1):
  frequency = results.count(value)
  frequencies.append(frequency)
print(frequencies)

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Result of rolling D3, D10 and D18 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d3_d10_d18.html')