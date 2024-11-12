import streamlit as st
import pandas as pd

logo_home = "assets/logo2.png"

st.set_page_config(page_title="GymTracker", page_icon=logo_home, layout="wide")

# Check if user is logged in
if "user" not in st.session_state:
    st.error("🚫 Please log in first.")
    st.stop()

# Load data
file_path = "assets/schema.xlsx"
data = pd.ExcelFile(file_path, engine="openpyxl")

workouts_df = data.parse("Workouts")
exercises_df = data.parse("Exercises")

# Sidebar for navigation
st.sidebar.title("🏋️ Workout Navigation")
workout_name = st.sidebar.selectbox("🏋️‍♂️ Select Workout", workouts_df["name"].tolist())

if workout_name:
    workout_id = workouts_df.loc[workouts_df["name"] == workout_name, "workout_id"].values[0]
    exercises = exercises_df.loc[exercises_df["workout_id"] == workout_id, "name"].tolist()
    exercise_name = st.sidebar.selectbox("💪 Select Exercise", exercises)

# Main body: Input weights
if workout_name and exercise_name:
    st.header(f"📝 Input Weights for {exercise_name}")
    st.subheader(f"**Workout:** {workout_name} 🏋️")
    st.markdown(f"#### Exercise: {exercise_name} 💪")

    # Input weights
    num_sets = st.number_input("🔢 Number of Sets", min_value=1, max_value=10, value=3, step=1)
    weights = []
    for i in range(1, num_sets + 1):
        weight = st.number_input(f"⚖️ Set {i} - Weight (kg):", min_value=0.0, step=0.1)
        weights.append(weight)

    if st.button("💾 Save Weights"):
        # Save weights (for demo purposes, just display them)
        st.success(f"✅ Weights saved for {exercise_name}: {weights} 🚀")
