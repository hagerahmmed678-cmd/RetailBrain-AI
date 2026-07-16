import os
import joblib

RULES_PATH = os.path.join(
    "models",
    "rules.pkl"
)


def load_rules():

    if not os.path.exists(RULES_PATH):

        return None

    return joblib.load(RULES_PATH)


rules = load_rules()


def get_recommendations(products):

    if rules is None:

        return []

    recommendations = set()

    for product in products:

        rec = rules[
            rules["antecedents"].apply(
                lambda x: product in x
            )
        ]

        for _, row in rec.iterrows():

            for item in row["consequents"]:

                recommendations.add(item)

    recommendations = recommendations - set(products)

    return list(recommendations)
