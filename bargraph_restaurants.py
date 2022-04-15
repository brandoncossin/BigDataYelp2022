# Install dataset from https://www.yelp.com/dataset/download
# Extract wherever. Rename it yelp_dataset.tgz
# Re-extract. Now it has 5 files, place them in the root of this folder


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#Pandas can read many data types. CSV and JSON are most common
#Lines = True means the JSON is written in lines with \n
#df = pd.read_json(r'yelp_dataset.json', encoding = 'unicode_escape', lines=True)
df = pd.read_json(r'yelp_academic_dataset_business.json', lines=True)
#Allows us to view each column we have to work with
df = df.drop(columns=['business_id', 'city', 'categories', 'address', 'attributes', 'is_open'], axis=1)
df['Restaurants'] = df.groupby(['state'])['name'].transform('count')
df = df.groupby('state')
dfp = df.mean()
dfp = dfp.rename(columns={"review_count":"average_reviews"})
dfp = dfp.reset_index()
print(dfp)

fig = px.bar(dfp, 
	x='state', 
	y='stars',
	color='Restaurants',
	color_continuous_scale="Thermal", height=600)
fig.update_layout(xaxis={'categoryorder':'total descending'})

#fig.update_geos(fitbounds="locations")
fig.update_layout(title_text='YELP Restaurant Reviews by State', title_x=0.5)
#fig.update_layout(margin={"r":0,"t":100,"l":0,"b":0}, height=1000)
fig.show()
