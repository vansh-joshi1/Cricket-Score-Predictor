import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import base64

# load the trained model from pickle
pipe = pickle.load(open('pipe.pkl', 'rb'))

# all the teams in the T20
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

# Function to set cricket-themed background
def set_cricket_background():
    # Use CSS to create a cricket-themed background
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                        url("https://images.unsplash.com/photo-1531415074968-036ba1b575da?q=80&w=2948&auto=format&fit=crop");
            background-size: cover;
            background-position: center;
        }
        .title {
            color: white !important;
            font-size: 3rem !important;
            font-weight: bold !important;
            text-align: center !important;
            text-shadow: 2px 2px 4px #000000 !important;
            padding: 20px 0 !important;
        }
        .stSelectbox label, .stNumberInput label {
            color: white !important;
            font-weight: bold !important;
            text-shadow: 1px 1px 2px #000000 !important;
        }
        /* Consistent styling for all input elements */
        div[data-baseweb="select"] {
            background-color: rgba(211, 211, 211, 0.8) !important;
            border-radius: 10px !important;
        }
        div[data-testid="stNumberInput"] input {
            background-color: rgba(211, 211, 211, 0.8) !important;
            border-radius: 10px !important;
        }
        /* Fix for dropdown menu corners */
        [data-baseweb="popover"] {
            border-radius: 10px !important;
        }
        [data-baseweb="select"] [data-baseweb="input"] {
            border-radius: 10px !important;
        }
        /* Style for number input fields */
        input[type="number"] {
            background-color: rgba(211, 211, 211, 0.8) !important;
            border-radius: 10px !important;
            border: none !important;
            padding: 10px !important;
        }
        /* Consistent styling for plus/minus buttons */
        .stNumberInput button {
            background-color: #2e3440 !important;
            color: white !important;
            border-radius: 10px !important;
        }
        .stButton button {
            background-color: #1e88e5 !important;
            color: white !important;
            font-weight: bold !important;
            border-radius: 10px !important;
            padding: 10px 20px !important;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.3) !important;
            width: 100% !important;
            margin-top: 20px !important;
        }
        .stHeader {
            color: #ffeb3b !important;
            background-color: rgba(0, 0, 0, 0.7) !important;
            padding: 10px !important;
            border-radius: 10px !important;
            text-align: center !important;
            font-weight: bold !important;
            text-shadow: 1px 1px 2px #000000 !important;
            margin: 20px 0 !important;
        }
        /* Fix for inconsistent appearance between browsers */
        input::-webkit-outer-spin-button,
        input::-webkit-inner-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply cricket-themed styling
set_cricket_background()

# Title with custom styling
st.markdown('<p class="title">T20 Cricket Score Predictor</p>', unsafe_allow_html=True)

# creates 2 columns for team selection in the app
col1, col2 = st.columns(2)

# select the batting team
with col1:
    battingTeam = st.selectbox('Select batting team', sorted(teams))

# select the bowling team
with col2:
    bowlingTeam = st.selectbox('Select bowling team', sorted(teams))

# select the city
city = st.selectbox('Select city', sorted(cities))

# create three columns for score, overs, and wickets input
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Current Score', min_value=0)

with col4:
    overs = st.number_input('Overs done (works for over>5)', min_value=5.0, max_value=20.0, step=0.1)

with col5:
    wickets = st.number_input('Wickets out', min_value=0, max_value=10)

Run_In_Last5 = st.number_input('Runs scored in last 5 overs', min_value=0)

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# button to predict score
if st.button('Predict Score'):
    try:
        # calculate deliveries left, wickets left, and current run rate
        delivery_left = 120 - (overs * 6)
        wicketsLeft = 10 - wickets
        CurrentRunRate = score / overs if overs > 0 else 0

        # create a DataFrame (df) for the model input
        input_df = pd.DataFrame(
            {'battingTeam': [battingTeam], 'bowlingTeam': [bowlingTeam], 'city': city, 'score': [score],
             'delivery_left': [delivery_left], 'wicketsLeft': [wicketsLeft], 'CurrentRunRate': [CurrentRunRate],
             'Run_In_Last5': [Run_In_Last5]})
        
        result = pipe.predict(input_df)
        st.markdown(f'<p class="stHeader">Predicted Final Score: {int(result[0])}</p>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.info("Please check your inputs and try again.")
