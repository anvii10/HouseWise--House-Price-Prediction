import streamlit as st

# Page config
st.set_page_config(page_title="HouseWise", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f9f9f9, #e0eafc);
    }
    h1 {
        text-align: center;
        color: #d63031;
    }
    .slogan {
        text-align: center;
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Initialize session state ---
if "page" not in st.session_state:
    st.session_state.page = "signup"  # start at signup
if "prediction" not in st.session_state:
    st.session_state.prediction = None


# --- Functions to switch pages ---
def go_to(page):
    st.session_state.page = page


# --- 1. SIGN UP PAGE ---
if st.session_state.page == "signup":
    st.title("📝 Sign Up for HouseWise")
    st.markdown("<p class='slogan'>Confused about the right house? Let AI guide you to your dream home! 🏡</p>", unsafe_allow_html=True)

    username = st.text_input("👤 Username")
    email = st.text_input("📧 Email")
    password = st.text_input("🔒 Password", type="password")
    confirm = st.text_input("✅ Confirm Password", type="password")

    if st.button("Create Account"):
        if password != confirm:
            st.error("Passwords do not match.")
        elif not username or not email or not password:
            st.warning("Please fill all the fields.")
        else:
            st.success(f"🎉 Welcome {username}! Your account has been created successfully.")
            go_to("home")


# --- 2. HOME PAGE ---
elif st.session_state.page == "home":
    st.title("🏡 Welcome to HouseWise")
    st.markdown("<p class='slogan'>Find your perfect home with AI-powered price predictions</p>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1560185127-6ed189bf02f4", use_column_width=True)

    if st.button("Start Prediction"):
        go_to("predict")


# --- 3. PREDICTION PAGE ---
elif st.session_state.page == "predict":
    st.title("📊 House Price Prediction")

    location = st.selectbox("Select Location", ["Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Pune", "Kolkata"])
    area = st.number_input("Area (sqft)", min_value=100, max_value=10000, step=50)
    bedrooms = st.slider("Bedrooms", 1, 10, 3)
    bathrooms = st.slider("Bathrooms", 1, 10, 2)

    if st.button("Predict Price"):
        # Dummy ML prediction (replace later with your model)
        price = area * 50 + bedrooms * 100000 + bathrooms * 80000
        st.session_state.prediction = price
        go_to("result")


# --- 4. RESULT PAGE ---
elif st.session_state.page == "result":
    st.title("💰 Prediction Result")

    st.success(f"Estimated House Price: **₹ {st.session_state.prediction:,.0f}**")

    if st.button("🔄 Predict Again"):
        go_to("predict")
    if st.button("🏠 Back to Home"):
        go_to("home")






