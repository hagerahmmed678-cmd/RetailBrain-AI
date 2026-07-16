import streamlit as st

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Recommendation System",
    page_icon="🧠",
    layout="wide"
)

# ==========================================
# Header
# ==========================================

st.title("Smart Retail Recommendation System")

st.markdown("""
AI-powered recommendations based on the object detection results.
""")

st.divider()

# ==========================================
# Check Detection Results
# ==========================================

if "statistics" not in st.session_state:

    st.warning("⚠ Please run Product Detection first.")

    st.stop()

statistics = st.session_state.statistics

products = statistics["products"]

confidence = statistics["avg_confidence"]

# ==========================================
# Shelf Status
# ==========================================

st.subheader("Shelf Status")

if products < 80:

    st.error("Shelf inventory is LOW.")

    st.write("Recommendation: Restock the shelf immediately.")

elif products < 150:

    st.warning("Shelf inventory is MODERATE.")

    st.write("Recommendation: Monitor inventory regularly.")

else:

    st.success("Shelf inventory is GOOD.")

    st.write("Recommendation: No action required.")

st.divider()

# ==========================================
# Confidence Status
# ==========================================

st.subheader("Detection Quality")

if confidence < 0.60:

    st.error("Low confidence detected.")

    st.write("Recommendation: Capture another image with better lighting.")

elif confidence < 0.85:

    st.warning("Medium confidence.")

    st.write("Recommendation: Review the prediction manually.")

else:

    st.success("High confidence.")

    st.write("Recommendation: Detection results are reliable.")

st.divider()

# ==========================================
# Final Recommendation
# ==========================================

st.subheader("Final Decision")

if products < 80:

    decision = "Restock Required"

elif confidence < 0.60:

    decision = "Retake Shelf Image"

else:

    decision = "Shelf Status is Healthy"

st.info(f"AI Decision: {decision}")
