import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from urllib.request import urlopen
import json
import plotly.express as px
import plotly.graph_objects as go

#This functions creates a choropleth map of the US states in relation to the amount of FUEL_TYPE
def create_country_map(data):
    fig = go.Figure(data=go.Choropleth(
        locations=df['code'],  # Spatial coordinates
        z=data,  # Data to be color-coded
        locationmode='USA-states',  # set of locations match entries in `locations`
        colorscale='reds',
        colorbar_title="amount of LPG fueling stations",
    ))

    fig.update_layout(
        title_text='Number of LPG fueling stations by state as of April 23, 2015.',
        geo_scope='usa',  # limite map scope to USA
    )

    fig.show()


#This function creates a bar graph showing each state and it's number of fuel stations
def create_barh_graph(y_data, x_data, ):

    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 9))

    # Horizontal Bar Plot

    ax.barh(y_data, x_data, color='maroon')

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=70)

    # Add x, y gridlines
    ax.grid(color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)

    # Show top values
    ax.invert_yaxis()

    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
                 str(round((i.get_width()), 2)),
                 fontsize=10, fontweight='bold',
                 color='grey')

    # Add Plot Title
    ax.set_title('The # of propane/liquefied petroleum gas (LPG) fueling stations in each State',
                 loc='left', )

    # Add Text watermark
    fig.text(0.9, 0.15, 'Reed Goldsworthy', fontsize=12,
             color='grey', ha='right', va='bottom',
             alpha=0.7)

    # Show Plot
    plt.show()


#import data from csv file
data = pd.read_csv('fuelStations.csv')


x = data['Fuel Type Code']
y = data['State']

stateCount = {}

# This for loop builds our count of fuel station types (ELEC, LPG, E85, etc...) in each state
for fuel_type , state in zip(x,y):

    if fuel_type == 'ELEC':
        if state in stateCount:
            stateCount[state][0] += 1
        else:
            stateCount[state] = [1,0,0,0,0,0,0]

    if fuel_type == 'LPG':
        if state in stateCount:
            stateCount[state][1] += 1
        else:
            stateCount[state] = [0,1,0,0,0,0,0]

    if fuel_type == 'E85':
        if state in stateCount:
            stateCount[state][2] += 1
        else:
            stateCount[state] = [0,0,1,0,0,0,0]

    if fuel_type == 'BD':
        if state in stateCount:
            stateCount[state][3] += 1
        else:
            stateCount[state] = [0,0,0,1,0,0,0]

    if fuel_type == 'CNG':
        if state in stateCount:
            stateCount[state][4] += 1
        else:
            stateCount[state] = [0,0,0,0,1,0,0]

    if fuel_type == 'HY':
        if state in stateCount:
            stateCount[state][5] += 1
        else:
            stateCount[state] = [0,0,0,0,0,1,0]

    if fuel_type == 'LNG':
        if state in stateCount:
            stateCount[state][6] += 1
        else:
            stateCount[state] = [0,0,0,0,0,0,1]



# We now have a map of each state to the count of each fuel station type in that particular state
# Lets separate these values into their own individual lists so that we can graph them
ELEC_list = []
LPG_list = []
E85_list = []
BD_list = []
CNG_list = []
HY_list = []
LNG_list = []

#this is the order of states that correspond to each lists values, i.e the first state corresponds to the first value in each list.
states = list(stateCount.keys())

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

#This puts the states in the same order as the dataset used to graph the map
newStateCount = {}

for state in df['code']:
    if state in stateCount:
        newStateCount[state] = stateCount[state]
    else:
        newStateCount[state] = [0,0,0,0,0,0,0]

for val in newStateCount.values():
    ELEC_list.append(val[0])
    LPG_list.append(val[1])
    E85_list.append(val[2])
    BD_list.append(val[3])
    CNG_list.append(val[4])
    HY_list.append(val[5])
    LNG_list.append(val[6])

#now we have each fuel type in its own list, where the order is the order of states from our dictionary
# To see the order of states, call print(states)

#This variable controls which fuel type is displayed
FUEL_TYPE = LPG_list


# These functions draw graphs of the processed data

# create_barh_graph(df['code'], FUEL_TYPE)

create_country_map(FUEL_TYPE)