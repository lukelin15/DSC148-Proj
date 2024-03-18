import joblib
import streamlit as st

# load the model 
model = joblib.load('Final_Model.joblib')
st.write(f'Model accuracy: 0.75')

# Create sliders for the features
latitude = st.slider('Latitude', min_value=49.91443, max_value=60.757544, value=55.0, step=0.1)
light_conditions = st.slider('Light Conditions', min_value=0, max_value=4, value=2, step=1)
district_area = st.slider('District Area', min_value=0.0, max_value=421.0, value=210.0, step=1.0)
longitude = st.slider('Longitude', min_value=-7.516225, max_value=1.76201, value=-3.0, step=0.1)
num_casualties = st.slider('Number of Casualties', min_value=1, max_value=68, value=10, step=1)
num_vehicles = st.slider('Number of Vehicles', min_value=1, max_value=32, value=5, step=1)
road_surface_conditions = st.slider('Road Surface Conditions', min_value=0, max_value=4, value=2, step=1)
road_type = st.slider('Road Type', min_value=0, max_value=4, value=2, step=1)
urban_or_rural_area = st.slider('Urban or Rural Area', min_value=0, max_value=2, value=1, step=1)
weather_conditions = st.slider('Weather Conditions', min_value=0, max_value=7, value=3, step=1)
vehicle_type = st.slider('Vehicle Type', min_value=0, max_value=15, value=7, step=1)
month = st.slider('Month', min_value=1, max_value=12, value=6, step=1)
day = st.slider('Day', min_value=1, max_value=31, value=15, step=1)

# Predict button
if st.button('Predict'):
    result = model.predict([[latitude, light_conditions, district_area, longitude, num_casualties, num_vehicles, road_surface_conditions, road_type, urban_or_rural_area, weather_conditions, vehicle_type, month, day]])
    st.write(f'Predicted class: {result}')