import streamlit as st

st.title("📊 Prediction Result")

if "predicted_price" in st.session_state:
    price = st.session_state["predicted_price"]

    st.markdown(f"""
    <div style="background-color:#f0f8ff; padding:20px; border-radius:12px; text-align:center;">
        <h2>🏠 Estimated House Price</h2>
        <h1 style="color:#ff4b4b;">₹ {price:,.0f}</h1>
        <p>Based on your inputs and selected amenities ✨</p>
    </div>
    """, unsafe_allow_html=True)

    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c", use_column_width=True)

else:
    st.warning("⚠️ No prediction available. Please go to the **Prediction Page** first.")
