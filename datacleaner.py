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
fig = px.choropleth(dfp,
                locations = 'state',
                color='Restaurants',
                #color='stars',
                #hover_data=['Restaurants'],
                hover_data=['stars'],
                color_continuous_scale="RdYlGn",
                locationmode='USA-states',
                scope="usa",
                #range_color=(0, 34000),
                range_color=(0, 5),
                title='YELP restaurant state scale',
                height=600)
fig.add_trace(go.Scattergeo(
            locationmode = 'USA-states',
            lon = dfp['longitude'],
            lat = dfp['latitude'],
            hoverinfo = 'text',
            mode = 'markers',
            #text = dfp['Restaurants'],
            text = dfp[['state', 'Restaurants']],
            name = "Star Count",
            marker = dict(
                size = ((dfp['Restaurants'] / 34039) * 100),
                #size = (dfp['stars'] * 15),
                color = 'rgb(102,102,102)',
                line = dict(
                width = 30,
                color = 'rgba(68, 68, 68, 0)'
                )          
            )))
fig.update_geos(fitbounds="locations")
fig.update_layout(title_text='YELP Restaurant Reviews by State', title_x=0.5)
fig.update_layout(margin={"r":0,"t":100,"l":0,"b":0}, height=1000)
fig.show()
