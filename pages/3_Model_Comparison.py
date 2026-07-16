import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Model Comparison",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# Header
# ==========================================

st.title("AI Model Comparison")

st.markdown("""
Compare the performance of different object detection models.
""")

st.divider()

# ==========================================
# Model Results
# ==========================================

comparison = pd.DataFrame({

    "Model":[
        "YOLOv8 Nano",
        "YOLOv8 Small",
        "Faster R-CNN"
    ],

    "mAP50":[
        0.78,
        0.84,
        0.81
    ],

    "Inference Time (sec)":[
        0.021,
        0.038,
        0.120
    ],

    "Parameters (M)":[
        3.2,
        11.2,
        41.8
    ]

})

st.subheader("Performance Comparison")

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================
# Accuracy Chart
# ==========================================

st.subheader("mAP50 Comparison")

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(
    comparison["Model"],
    comparison["mAP50"]
)

ax.set_ylabel("mAP50")

st.pyplot(fig)

st.divider()

# ==========================================
# Speed Chart
# ==========================================

st.subheader("Inference Time")

fig2, ax2 = plt.subplots(figsize=(7,4))

ax2.bar(
    comparison["Model"],
    comparison["Inference Time (sec)"]
)

ax2.set_ylabel("Seconds")

st.pyplot(fig2)

st.divider()

# ==========================================
# Best Model
# ==========================================

best = comparison.loc[
    comparison["mAP50"].idxmax()
]

st.success(
    f" Best Model: {best['Model']} "
    f"(mAP50 = {best['mAP50']})"
)
