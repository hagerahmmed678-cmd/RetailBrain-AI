import joblib
import os


RULES_PATH = os.path.join(
    "models",
    "rules.pkl"
)


def load_rules():

    if not os.path.exists(RULES_PATH):

        return None

    return joblib.load(RULES_PATH)


rules = load_rules()


def get_recommendations(detected_products):

    if rules is None:

        return []

    recommendations = []

    for product in detected_products:

        if product in rules:

            recommendations.extend(rules[product])

    recommendations = list(set(recommendations))

    recommendations = [

        item

        for item in recommendations

        if item not in detected_products

    ]

    return recommendations
