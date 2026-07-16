
"""
Prediction Utilities
"""

import tempfile


def run_prediction(model, image):

    """
    Run YOLO inference on the uploaded image.
    """

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as temp:

        image.save(temp.name)

        results = model.predict(

            source=temp.name,

            conf=0.25,

            verbose=False

        )

    return results[0]
