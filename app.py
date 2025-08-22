import streamlit as st
import datetime
import requests
import pandas as pd


st.markdown('''
### 🐤 DuckDuck TaxiDrive
''')


st.markdown('''
## *Ride NY with us!*
''')


#Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions



pickup_datetime = st.date_input("Pickup date", datetime.date(2025,8,22))
st.write('Date de pickup:', pickup_datetime)

pickup_hour = st.time_input('Pickup time', datetime.time(8, 45))
st.write('Heure de pickup', pickup_hour)

pickup_longitude = st.number_input('Pickup longitude', value=-74.0060)
st.write('Longitude du pickup', pickup_longitude)

pickup_latitude = st.number_input('Pickup latitude', value=40.7128)
st.write('Latitude du pickup', pickup_latitude)

dropoff_longitude = st.number_input('Dropoff longitude', value =-73.1350)
st.write('Longitude du dropoff', dropoff_longitude)

dropoff_latitude = st.number_input('Dropoff latitude', value =40.7891)
st.write('Latitude du dropoff', dropoff_latitude)


passenger_count = st.number_input('Passenger count', value =2)
st.write('Passenger count', passenger_count)

# passenger_count = st.slider(
#     label="Passenger count",
#     min_value=1,
#     max_value=6,
#     value=3,   # default position
#     step=1     # integer step
# )
st.write('Nombre de passagers', passenger_count)


def get_map_data():

    return pd.DataFrame({
        "lat" : [pickup_latitude, dropoff_latitude],
        "lon" : [pickup_longitude, dropoff_longitude]})

df = get_map_data()

st.map(df)





url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

pickup_datetime_str = f"{pickup_datetime} {pickup_hour}"

params = {
        'pickup_datetime': pickup_datetime_str,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude' : dropoff_longitude,
        'dropoff_latitude' : dropoff_latitude,
        'passenger_count': passenger_count,
        }


response = requests.get(url, params=params)


if response.ok:
    data = response.json()
    fare = round(data.get("fare"),1)
    st.write("Predicted fare:", fare, "USD")
else:
    st.error(f"API returned {response.status_code}")
    st.write("Response:", response.text)


# st.write("Status code:", response.status_code)
# st.write("Content-Type:", response.headers.get("Content-Type"))
# st.write("Raw response (first 300 chars):", response.text[:300])


# data = response.json()
# fare = data.get("fare")

# st.write(response.status_code)
# st.write(response.text)
# st.write("Predicted fare:", fare)
