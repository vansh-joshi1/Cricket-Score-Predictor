import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = ['Australia',
         'India',
         'Bangladesh',
         'New Zealand',
         'South Africa',
         'England',
         'West Indies',
         'Afghanistan',
         'Pakistan',
         'Sri Lanka']

cities = ['Colombo',
          'Mirpur',
          'Johannesburg',
          'Dubai',
          'Auckland',
          'Cape Town',
          'London',
          'Pallekele',
          'Barbados',
          'Sydney',
          'Melbourne',
          'Durban',
          'St Lucia',
          'Wellington',
          'Lauderhill',
          'Hamilton',
          'Centurion',
          'Manchester',
          'Abu Dhabi',
          'Mumbai',
          'Nottingham',
          'Southampton',
          'Mount Maunganui',
          'Chittagong',
          'Kolkata',
          'Lahore',
          'Delhi',
          'Nagpur',
          'Chandigarh',
          'Adelaide',
          'Bengaluru',
          'St Kitts',
          'Cardiff',
          'Christchurch',
          'Trinidad']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    battingTeam = st.selectbox('Select batting team', sorted(teams))
with col2:
    bowlingTeam = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works for over>5)')
with col5:
    wickets = st.number_input('Wickets out')

Run_In_Last5 = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    delivery_left = 120 - (overs * 6)
    wicketsLeft = 10 - wickets
    CurrentRunRate = score / overs

    input_df = pd.DataFrame(
        {'battingTeam': [battingTeam], 'bowlingTeam': [bowlingTeam], 'city': city, 'score': [score],
         'delivery_left': [delivery_left], 'wicketsLeft': [wicketsLeft], 'CurrentRunRate': [CurrentRunRate],
         'Run_In_Last5': [Run_In_Last5]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))
