import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# =========================================================
# LOAD TRAINED MODEL
# =========================================================

try:
    model = joblib.load("rf_fraud_detection_model.pkl")
except Exception as e:
    st.error("❌ Unable to load the fraud detection model.")
    st.code(str(e))
    st.stop()


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 15px;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">💳 Credit Card Fraud Detection</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered system for detecting potentially fraudulent credit card transactions'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# MODEL STATUS
# =========================================================

st.success("✅ Random Forest fraud detection model loaded successfully.")


# =========================================================
# TRANSACTION INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">💰 Transaction Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    time = st.number_input(
        "Transaction Time",
        min_value=0.0,
        value=0.0,
        step=1.0,
        help="Seconds elapsed since the first transaction in the dataset."
    )

with col2:
    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=0.0,
        step=0.01
    )


# =========================================================
# V1 - V28 FEATURES
# =========================================================

st.markdown(
    '<div class="section-title">🧠 Transaction Features</div>',
    unsafe_allow_html=True
)

st.info(
    "V1–V28 are anonymized numerical features from the dataset. "
    "They are used by the trained machine learning model for prediction."
)

features = {}

# Create four columns
columns = st.columns(4)

for i in range(1, 29):

    column_index = (i - 1) % 4

    with columns[column_index]:

        features[f"V{i}"] = st.number_input(
            f"V{i}",
            value=0.0,
            format="%.6f",
            key=f"V{i}"
        )


# =========================================================
# CREATE TRANSACTION DATAFRAME
# =========================================================

transaction = pd.DataFrame([{
    "Time": time,
    **features,
    "Amount": amount
}])


# =========================================================
# DETECTION BUTTON
# =========================================================

st.divider()

button_col1, button_col2, button_col3 = st.columns([1, 2, 1])

with button_col2:

    detect_button = st.button(
        "🔍 DETECT FRAUD",
        use_container_width=True
    )


# =========================================================
# PREDICTION
# =========================================================

if detect_button:

    try:

        # Prediction
        prediction = model.predict(transaction)[0]

        # Fraud probability
        probability = model.predict_proba(transaction)[0][1]

        probability_percent = probability * 100

        st.divider()

        st.markdown(
            '<div class="section-title">📊 Prediction Result</div>',
            unsafe_allow_html=True
        )

        # Display probability
        st.metric(
            "Fraud Probability",
            f"{probability_percent:.2f}%"
        )

        # Progress bar
        st.progress(float(probability))

        # Fraud result
        if prediction == 1:

            st.error(
                "🚨 FRAUDULENT TRANSACTION DETECTED!"
            )

            st.warning(
                "The machine learning model predicts that this transaction "
                "has characteristics associated with fraudulent transactions."
            )

        else:

            st.success(
                "✅ GENUINE TRANSACTION"
            )

            st.info(
                "The machine learning model predicts that this transaction "
                "is likely to be genuine."
            )

        # =================================================
        # TRANSACTION SUMMARY
        # =================================================

        st.markdown(
            '<div class="section-title">📋 Transaction Summary</div>',
            unsafe_allow_html=True
        )

        summary_col1, summary_col2, summary_col3 = st.columns(3)

        with summary_col1:
            st.metric(
                "Transaction Amount",
                f"{amount:.2f}"
            )

        with summary_col2:
            st.metric(
                "Prediction",
                "Fraud" if prediction == 1 else "Genuine"
            )

        with summary_col3:
            st.metric(
                "Fraud Probability",
                f"{probability_percent:.2f}%"
            )

    except Exception as e:

        st.error("❌ Prediction failed.")

        st.code(str(e))


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Credit Card Fraud Detection using Machine Learning | "
    "Random Forest Classifier"
)