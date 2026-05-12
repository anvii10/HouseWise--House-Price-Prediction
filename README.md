# HouseWise – House Price Prediction

HouseWise is a web-based application built using Python and Streamlit that helps users estimate house prices based on property details such as location, area, number of bedrooms, bathrooms, and amenities.

The project provides an interactive user interface with multiple pages including sign-up, home, prediction, and result pages.

## Features

- User-friendly multi-page interface
- Sign-up page for user onboarding
- House price prediction based on property details
- Selection of city/location
- Input for area, bedrooms, bathrooms
- Amenities selection
- Instant price estimation
- Interactive result display

## How It Works

1. User signs up on the platform
2. User navigates to the home page
3. User enters house details:
   - Location
   - Area
   - Bedrooms
   - Bathrooms
   - Amenities
4. Application processes the inputs
5. Predicted house price is displayed on the result page

## Tech Stack

### Frontend + Backend
- Python
- Streamlit

## Libraries Used

- Streamlit
- Python

## Project Structure

```text
HouseWise
│
├── app.py              # Main application file
├── home.py             # Home page
├── predict.py          # Prediction page
├── result.py           # Result page
└── README.md
```

## Core Functionality

- Multi-page navigation using session state
- User input collection
- Basic price prediction logic
- Dynamic result display
- Interactive property selection UI

## Prediction Parameters

The application predicts house prices based on:

- Location
- Area (sq ft)
- Number of bedrooms
- Number of bathrooms
- Amenities:
  - Parking
  - Lift
  - Gym
  - Swimming Pool
  - Garden
  - Security

## Future Improvements

- Integrate real machine learning model
- Train on actual housing datasets
- Add property image upload
- Add map-based location selection
- Deploy on Streamlit Cloud
- Improve prediction accuracy

## Learning Outcomes

This project helped in understanding:

- Streamlit application development
- Multi-page app navigation
- Session state management
- User interface design
- Python-based web app development
- Basic prediction system implementation
