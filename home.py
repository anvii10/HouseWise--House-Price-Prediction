import streamlit as st

st.title("🏡 Welcome to HouseWise")
st.markdown("Find your perfect home with AI-powered price predictions 🏠✨")

st.image("https://images.unsplash.com/photo-1560185127-6ed189bf02f4", use_column_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1580587771525-78b9dba3b914", use_column_width=True)
    st.subheader("Owner Properties")
    st.write("Explore homes listed directly by owners — no extra brokerage.")

with col2:
    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c", use_column_width=True)
    st.subheader("New Projects")
    st.write("Browse brand-new projects from trusted builders in your city.")

with col3:
    st.image("https://images.unsplash.com/photo-1586105251261-72a756497a12", use_column_width=True)
    st.subheader("Budget Homes")
    st.write("Affordable homes tailored to every family’s budget.")

st.markdown("### 🔍 Ready to see your dream home's price?")
st.write("👉 Go to the **Predict** page from the sidebar to start prediction!")
