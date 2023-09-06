#%%
import folium
import re
import pandas as pd
import numpy as np
#%%

def function(input_df):


    m = folium.Map(location=[input_df.latitude.mean(), input_df.longitude.mean()], zoom_start=8)

    for i, row in input_df.iterrows():
        folium.Marker(
            location=[row.latitude, row.longitude],
            radius=20,
            fill = True,
            popup=pd.DataFrame(data=df_with_cities['value'].iloc[i], index=[f'{row.group_name}']).to_html(
                        classes="table table-striped table-hover table-condensed table-responsive"
                    ) ,
            color='#1787FE',
            fill_color='#1787FE').add_to(m)
    return m




# %%
# List the the lat and long of 10 mjor Dutch cities as a dataframe with columns Group name (as A, B, C, D, E, F, G, H, I, J), latitude, longitude,
# place_name, 'value' which is a dictionary with keys: 'value1', 'value2','value3' with some random values
df_with_cities = pd.DataFrame(index=range(10), data={'group_name': ['group A', 'group B', 'group C', 'group D', 'group E', 'group F', 'group G', 'group H', 'group I', 'group J' ],
                                                     'place_name': ['Amsterdam', 'Rotterdam', 'Utrecht', 'Den Haag', 'Eindhoven', 'Tilburg', 'Groningen', 'Almere', 'Breda', 'Nijmegen'],
                                                     'longitude': [4.895168, 4.47917, 5.12222, 4.3007, 5.469722, 5.091111, 6.566667, 5.216667, 4.777778, 5.866667],
                                                     'latitude': [52.370216, 51.9225, 52.09083, 52.0704978, 51.441944, 51.555, 53.219167, 52.350000, 51.586667, 51.833333],
                                                        'value': [{'value1': 1, 'value2': 2, 'value3': 3},
                                                                    {'value1': 1, 'value2': 2, 'value3': 3},
                                                                    {'value1': 1, 'value2': 2, 'value3': 3},
                                                                    {'value1': 1, 'value2': 2, 'value3': 3},
                                                                    {'value1': 1, 'value2': 2, 'value3': 3},
                                                                    {'value1': 1, 'value2': 2, 'value3': 3},
                                                                    {'value1': 1, 'value2': 2, 'value3': 3},
                                                                    {'value1': 1, 'value2': 2, 'value3': 3},
                                                                    {'value1': 1, 'value2': 2, 'value3': 3},
                                                                    {'value1': 1, 'value2': 2, 'value3': 3}]})



m = function(df_with_cities)

#%%
m.save("./index.html")

with open("./group_data_frame.json", "w") as f:
    f.write(df_with_cities.to_json())

# %%
