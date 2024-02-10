# Data Visualization of Fueling Station Locations in the United States

A python program that uses pandas, matplotlib, numpy and geopandas in order to visualize a dataset from the NREL which contains alternative fueling station information for compressed natural gas (CNG), E85 (85% ethanol, 15% gasoline), propane/liquefied petroleum gas (LPG), biodiesel, electricity, hydrogen, and liquefied natural gas (LNG), as of April 23, 2015.

the dataset containing all this information can be found [here](https://catalog.data.gov/dataset/alternative-fueling-station-locations-422f2)

## Dependencies

This project uses five external python libraries: pandas, numpy, matplotlib.pyplot, geopandas, and plotly.
These can be downloaded by using "pip install" followed by the external library name

## Usage

1). Change the FUEL_TYPE variable in main.py to be one of the several fuel types in the format fuelType_list (i.e LPG_list)

2). Use either the create_barh_graph or create_country_map function to create graphs of the data

3). while in the project directory, run the program from the command line, as follows:

<pre>python main.py 
</pre>

# Result 

## Graphs on the amount of electric fueling stations in each state


![electric_fueling_stations_amount_per_state](https://github.com/ReedGoldsworthy/AlternativeFuelingLocationsDataVisualization/assets/59662986/44bfd780-a7df-462e-a9d7-35c1d60b21e5)

![electric_fueling_stations_map_graph](https://github.com/ReedGoldsworthy/AlternativeFuelingLocationsDataVisualization/assets/59662986/af782427-9c32-4b06-a348-3f67b034e9e4)


## Graphs on the amount of propane/liquefied petroleum gas (LPG) fueling stations in each state

![LPG_fueling_stations_amount_per_state](https://github.com/ReedGoldsworthy/AlternativeFuelingLocationsDataVisualization/assets/59662986/31cee14f-c70d-4ecf-ab8c-76d86360472c)


![LPG_fueling_stations_map_graph](https://github.com/ReedGoldsworthy/AlternativeFuelingLocationsDataVisualization/assets/59662986/b9130167-fdd5-4f19-8f84-84d4e5d19601)


### Note these graphs are interactive while ran through python, and hovering over a state will display its count


