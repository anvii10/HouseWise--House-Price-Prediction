import streamlit as st

st.title("🔮 Predict House Price")

st.write("Fill in the details below to get an AI-powered house price prediction:")

location = st.selectbox(
    "📍 Select Location",
    ["Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Pune", "Kolkata"]
)

area = st.number_input("📏 Enter Area (sq ft)", min_value=100, max_value=10000, step=50)
bedrooms = st.slider("🛏️ Bedrooms", 1, 10, 3)
bathrooms = st.slider("🚿 Bathrooms", 1, 10, 2)

amenities = st.multiselect(
    "🏢 Amenities",
    ["Parking", "Lift", "Gym", "Swimming Pool", "Garden", "Security"]
)

if st.button("🚀 Predict Price"):
    # Placeholder for ML model
    predicted_price = 75_00_000  # dummy value
    st.session_state["predicted_price"] = predicted_price
    st.success("✅ Prediction ready! Go to the **Result Page** to see details.")
