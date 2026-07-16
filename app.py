import streamlit as st

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="RetailBrainAI",
    page_icon="🛒",
    layout="wide"
)

# ==========================================
# Header
# ==========================================

st.title("RetailBrainAI")

st.subheader("AI-Powered Retail Shelf Monitoring System")

st.markdown("""
Welcome to **RetailBrainAI**, an intelligent computer vision platform designed for retail shelf monitoring.

The system uses **YOLOv8** and Artificial Intelligence to automatically detect products, analyze shelf inventory, compare object detection models, and generate intelligent retail recommendations.
""")

st.divider()

# ==========================================
# Features
# ==========================================

st.header("System Features")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### Product Detection

Detect products on retail shelves using the YOLOv8 object detection model.
""")

    st.info("""
### Retail Analytics

Generate real-time analytics and inventory statistics.
""")

with col2:

    st.info("""
### Model Comparison

Compare the performance of YOLOv8 Nano, YOLOv8 Small, and Faster R-CNN.
""")

    st.info("""
### Recommendation System

Generate intelligent inventory recommendations based on AI analysis.
""")

st.divider()

# ==========================================
# System Overview
# ==========================================

st.header("System Overview")

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric(
        "AI Models",
        "3"
    )

with metric2:
    st.metric(
        "Dataset",
        "SKU-110K"
    )

with metric3:
    st.metric(
        "Framework",
        "YOLOv8"
    )

st.divider()

# ==========================================
# Workflow
# ==========================================

st.header("Project Workflow")

st.markdown("""
1. Upload a retail shelf image.

2. Detect products using the YOLOv8 model.

3. Generate inventory analytics.

4. Produce intelligent recommendations.

5. Compare AI model performance.
""")

st.divider()

# ==========================================
# Navigation
# ==========================================

st.success(
    "Use the navigation menu on the left to access all project modules."
)

# ==========================================
# Footer
# ==========================================

st.divider()

st.caption(
    "RetailBrainAI | AI-Based Retail Shelf Monitoring System"
)
