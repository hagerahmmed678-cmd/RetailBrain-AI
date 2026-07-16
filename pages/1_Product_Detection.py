import streamlit as st
from PIL import Image
import cv2

from utils.model import load_model
from utils.prediction import run_prediction
from utils.analytics import get_statistics, detection_table
from utils.visualization import draw_detection
from utils.download_models import download_fasterrcnn

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Product Detection",
    page_icon="📦",
    layout="wide"
)

# ==========================================
# Load YOLO Model
# ==========================================

model = load_model()

# ==========================================
# Header
# ==========================================

st.title("Product Detection")

st.markdown("""
Upload a retail shelf image and choose the AI model for product detection.
""")

st.divider()

# ==========================================
# Model Selection
# ==========================================

selected_model = st.selectbox(
    "Select Detection Model",
    [
        "YOLOv8",
        "Faster R-CNN"
    ]
)

# ==========================================
# Upload Image
# ==========================================

uploaded_file = st.file_uploader(
    "Upload Shelf Image",
    type=["jpg", "jpeg", "png"]
)

# ==========================================
# Display Uploaded Image
# ==========================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Original Image")

        st.image(
            image,
            use_container_width=True
        )

    with col2:

        st.subheader("Detection Result")

        st.info(
            "Click 'Run Detection' to start."
        )

    st.divider()

    # ==========================================
    # Run Detection
    # ==========================================

    if st.button(
        "Run Detection",
        use_container_width=True
    ):

        if selected_model == "YOLOv8":

            with st.spinner(
                "Running YOLOv8 Detection..."
            ):

                result, inference_time = run_prediction(
                    model,
                    image
                )

                detected_image = draw_detection(
                    result
                )

                statistics = get_statistics(
                    result
                )

                table = detection_table(
                    result
                )

                st.session_state.statistics = statistics

                detected_products = []

                for cls in result.boxes.cls.cpu().numpy():

                    detected_products.append(
                        model.names[int(cls)]
                    )

                st.session_state.detected_products = detected_products

            with col2:

                st.subheader(
                    "Detection Result"
                )

                st.image(
                    detected_image,
                    use_container_width=True
                )

            st.divider()

            st.subheader(
                "Detection Statistics"
            )

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(
                    "Total Products",
                    statistics["products"]
                )

            with c2:

                st.metric(
                    "Average Confidence",
                    f"{statistics['avg_confidence']:.2f}"
                )

            with c3:

                st.metric(
                    "Inference Time",
                    f"{inference_time:.3f} sec"
                )

            st.success(
                "YOLOv8 Detection Completed Successfully"
            )

            st.divider()

            st.subheader(
                "Detection Table"
            )

            st.dataframe(
                table,
                use_container_width=True,
                hide_index=True
            )

            st.divider()

            st.subheader(
                "Download Detection Result"
            )

            _, buffer = cv2.imencode(
                ".jpg",
                detected_image
            )

            st.download_button(
                label="Download Detection Image",
                data=buffer.tobytes(),
                file_name="RetailBrain_Detection.jpg",
                mime="image/jpeg",
                use_container_width=True
            )

        else:

            with st.spinner(
                "Loading Faster R-CNN Model..."
            ):

                download_fasterrcnn()

            st.success(
                "Faster R-CNN model downloaded successfully."
            )

            st.info(
                "Faster R-CNN inference will be enabled after integrating the prediction pipeline."
            )
