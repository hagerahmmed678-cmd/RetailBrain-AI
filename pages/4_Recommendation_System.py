import streamlit as st
from utils.report import generate_report
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

st.title("Recommendation System")

st.write(
    "AI-powered recommendations based on retail shelf analysis."
)

st.divider()

# ==========================================
# Check Session
# ==========================================

if "statistics" not in st.session_state:

    st.warning("Please run Product Detection first.")

    st.stop()

statistics = st.session_state.statistics

products = statistics["products"]

confidence = statistics["avg_confidence"]

# ==========================================
# KPI Cards
# ==========================================

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Detected Products",
        products
    )

with col2:

    st.metric(
        "Average Confidence",
        f"{confidence:.2f}"
    )

st.divider()

# ==========================================
# Inventory Status
# ==========================================

st.subheader("Inventory Status")

if products < 80:

    inventory = "Low"

    priority = "High"

    recommendation = (
        "Restock the shelf immediately."
    )

elif products < 150:

    inventory = "Medium"

    priority = "Medium"

    recommendation = (
        "Monitor shelf inventory regularly."
    )

else:

    inventory = "High"

    priority = "Low"

    recommendation = (
        "Inventory level is healthy."
    )

st.write(f"**Inventory Level:** {inventory}")

st.write(f"**Priority:** {priority}")

st.info(recommendation)

st.divider()

# ==========================================
# Detection Quality
# ==========================================

st.subheader("Detection Quality")

if confidence >= 0.90:

    quality = "Excellent"

elif confidence >= 0.80:

    quality = "Good"

elif confidence >= 0.60:

    quality = "Acceptable"

else:

    quality = "Poor"

st.write(f"**Quality:** {quality}")

if quality == "Poor":

    st.error(
        "Capture another image with better lighting."
    )

elif quality == "Acceptable":

    st.warning(
        "Review the detection results manually."
    )

else:

    st.success(
        "Detection quality is reliable."
    )

st.divider()

# ==========================================
# Final Decision
# ==========================================

st.subheader("Final AI Decision")

if inventory == "Low":

    decision = "Restock Required"

elif quality == "Poor":

    decision = "Capture New Shelf Image"

else:

    decision = "Shelf Status is Healthy"

st.success(decision)

st.divider()

# ==========================================
# Summary
# ==========================================

st.subheader("Summary")

st.write(f"- Inventory Status: {inventory}")

st.write(f"- Detection Quality: {quality}")

st.write(f"- Priority Level: {priority}")

st.write(f"- Final Decision: {decision}")
st.divider()

if st.button("Generate PDF Report"):

    generate_report(

        "Retail_Report.pdf",

        products,

        confidence,

        inventory,

        quality,

        decision

    )

    with open(
        "Retail_Report.pdf",
        "rb"
    ) as pdf:

        st.download_button(

            label="Download PDF",

            data=pdf,

            file_name="Retail_Report.pdf",

            mime="application/pdf"

        )
