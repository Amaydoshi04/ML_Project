import streamlit as st

st.title("Take the Sleep Savvy Quiz")
st.markdown(
    "### Answer the following questions to get a better understanding of your sleep health."
)

with st.form("Sleep Health"):
    name = st.text_input("Enter your name")

    age = st.text_input("Enter your age")

    gender = st.radio("Select your Gender", ["Male", "Female"])

    occupation = st.selectbox(
        "What is your occupation?",
        [
            "Software Engineer",
            "Doctor",
            "Sales Representative",
            "Teacher",
            "Nurse",
            "Engineer",
            "Accountant",
            "Scientist",
            "Lawyer",
            "Salesperson",
            "Manager",
        ],
    )

    sleep_duration = st.slider("How many hours do you sleep per night?", 1, 12, 6)

    sleep_quality = st.slider("Rate your sleep quality", 1, 10, 7)

    activity_level = st.slider("How active are you during the day?", 1, 10, 2, 1)

    steps_per_day = st.slider("How many steps do you take per day?", 100, 30000, 5000)

    bmi_category = st.selectbox(
        "What is your BMI category?", ["Normal", "Overweight", "Obese"]
    )

    systolic_bp = st.slider("Enter your Systolic Blood Pressure", 80, 300, 120)

    diastolic_bp = st.slider("Enter your Diastolic Blood Pressure", 50, 200, 80)

    tnc = st.checkbox("I agree to the Terms and Conditions")

    submit = st.form_submit_button("Submit")
