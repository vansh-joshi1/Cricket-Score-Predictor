# T20 Cricket Score Predictor

A machine learning-based web application that predicts the final score of a T20 cricket match based on current match statistics.

## Overview

This project consists of two main components:
1. A machine learning model trained on historical T20 International cricket data
2. A Streamlit web application that provides an intuitive interface for users to input match details and get score predictions

<img width="1470" alt="Screenshot 2025-04-24 at 1 18 24 PM" src="https://github.com/user-attachments/assets/4b7d4859-387e-406b-a73b-b83fa39dd141" />


## Features

- Predict final scores for T20 cricket matches
- User-friendly interface with cricket-themed design
- Support for 10 international cricket teams
- Multiple cricket venues (35 cities) included
- Real-time prediction based on current match statistics

## Model Development

The prediction model was built using the following steps:

1. **Data Collection**: Used T20 International Dataset.csv containing historical T20 match data
2. **Data Preprocessing**:
   - Selected relevant features (batting team, bowling team, city, current score, deliveries left, etc.)
   - Filtered data to include only cities with sufficient match history (>600 matches)
   - Shuffled data to ensure unbiased model training
3. **Feature Engineering**:
   - Transformed categorical variables (teams, cities) using One-Hot Encoding
   - Standardized numerical features
4. **Model Training**:
   - Split data into training (80%) and testing (20%) sets
   - Used XGBoost Regressor with optimized hyperparameters
   - Achieved high accuracy with low mean absolute error
5. **Model Evaluation**:
   - Evaluated using R-squared score and Mean Absolute Error
   - Validated model performance on unseen data

## Technical Details

### Model Information
- **Algorithm**: XGBoost Regressor
- **Hyperparameters**:
  - n_estimators: 1000
  - learning_rate: 0.2
  - max_depth: 12
- **Feature Transformation**: One-Hot Encoding for categorical variables
- **Scaling**: StandardScaler for numerical features

### Web Application
- **Framework**: Streamlit
- **UI Features**:
  - Cricket-themed background
  - Responsive design
  - Input validation
  - Interactive elements

## Installation and Usage

### Prerequisites
- Python 3.7+
- pip package manager

### Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/your-username/t20-cricket-score-predictor.git
   cd t20-cricket-score-predictor
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the web application:
   ```
   streamlit run app.py
   ```

5. Open your web browser and navigate to `http://localhost:8501`

### How to Use

1. Select the batting team from the dropdown
2. Select the bowling team from the dropdown
3. Choose the city/venue where the match is being played
4. Enter the current score
5. Enter the number of overs completed (must be greater than 5)
6. Enter the number of wickets lost
7. Enter the runs scored in the last 5 overs
8. Click the "Predict Score" button to get the final score prediction
