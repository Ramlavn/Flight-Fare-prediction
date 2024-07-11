import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('flight_reg_xgbr.pkl', 'rb'))

# Create the Streamlit app
st.title('Flight Price Prediction using ML')

# Create input fields
st.header('Enter Flight Details')

# Airline
airline = st.selectbox('Airline', ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet', 'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia'])

# Source
source = st.selectbox('From', ['Delhi', 'Kolkata', 'Mumbai', 'Chennai', 'Bangalore'])

# Destination
destination = st.selectbox('To', ['Cochin', 'Bangalore', 'Delhi', 'New Delhi', 'Hyderabad', 'Kolkata'])

# Total Stops
total_stops = st.selectbox('Total Stops', [0, 1, 2, 3, 4])

# Journey Date
journey_date = st.date_input('Journey Date')

# Departure Time
dep_time = st.time_input('Departure Time')

# Prediction button
if st.button('Predict Price'):
    # Prepare the input data
    journey_day = journey_date.day
    journey_month = journey_date.month
    
    dep_hour = dep_time.hour
    dep_min = dep_time.minute

    # Create a dataframe with the input
    input_df = pd.DataFrame({
        'Total_Stops': [total_stops],
        'Journey_date': [journey_day],
        'Journey_month': [journey_month],
        'Dep_hour': [dep_hour],
        'Dep_min': [dep_min]
    })

    # Add airline columns (one-hot encoded)
    airlines = ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business',
       'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet',
       'Trujet', 'Vistara', 'Vistara Premium economy']
    for a in airlines:
        input_df[a] = 1 if airline == a else 0
    
    # Add source columns (one-hot encoded)
    sources = ['Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai']
    for s in sources:
        input_df[s] = 1 if source == s else 0
    
    # Add destination columns (one-hot encoded)
    destinations = ['Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad', 'Destination_Kolkata', 'Destination_New Delhi']
    for d in destinations:
        input_df[d] = 1 if destination == d else 0 

    # Make prediction
    prediction = model.predict(input_df)

    # Display prediction result
    st.success(f'Your Journey price is ₹{prediction[0]:.2f}')

# Additional developer details
st.write('**Built by: Ramlavan Arumugasamyi**')
st.write('**Twitter** [iramlavan](https://twitter.com/iramlavan/)')
st.write('**GitHub:** [Ramlavn](https://github.com/Ramlavn/)')
s