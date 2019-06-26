import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_30_day_m1.json'

with open(filename) as f:
  json_data = json.load(f)
  all_eq_data = json_data['features']
  print(len(all_eq_data))

  mags, lons, lats, hover_texts = [], [], [], []
  for eq_data in all_eq_data:
    mag =  eq_data['properties']['mag']
    lon = eq_data['geometry']['coordinates'][0]
    lat = eq_data['geometry']['coordinates'][1]
    text = eq_data['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(text)


data = [{
  'type': 'scattergeo',
  'lon': lons,
  'lat': lats,
  'text': hover_texts,
  'marker': {
    'size': [5*mag for mag in mags],
    'color': mags,
    'colorscale': 'Viridis',
    'reversescale': True,
    'colorbar': {'title': 'Magnitude'}
  }
}]
# data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title='Global Earthquakes')

fig = {
  'data': data,
  'layout': my_layout
}
offline.plot(fig, filename='global_earthquakes_1.html')