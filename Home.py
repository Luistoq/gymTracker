import streamlit as st
from dotenv import load_dotenv
import os
import bcrypt

# Basic Page Config
st.set_page_config(page_title="GymTracker", page_icon="💪")

# Load environment variables
load_dotenv()

# Fetch valid users and password from .env
VALID_USERS = os.getenv("USERS").split(",")
HASHED_PASSWORD = os.getenv("PASSWORD")  # Ensure the password is hashed in .env

# Display Logo
logo_path = "assets/logo.png"
logo_home = "assets/logo2.png"

col1, col2 = st.columns([3, 1])
with col1:
    st.title("🔒 Login to Gym Tracker")
with col2:
    st.image(logo_home, width=100)

# Login Form
email = st.text_input("📧 Email Address")
user_password = st.text_input("🔑 Password", type="password")


if st.button("Login"):
    # Validate email
    if email not in VALID_USERS:
        st.error("❌ Invalid email. Please try again.")
    else:
        # Validate hashed password
        if bcrypt.checkpw(user_password.encode('utf-8'), HASHED_PASSWORD.encode('utf-8')):
            st.success(f"✅ Welcome, {email}!")
            st.session_state["user"] = email  # Store logged-in user in session
            st.rerun()  # Refresh the app to update the session state
        else:
            st.error("❌ Incorrect password. Please try again.")

# Redirect User if Logged In
if "user" in st.session_state:
    st.info("✅ You are logged in! Navigate to the GymTracker from the left-hand menu.")
