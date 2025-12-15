import streamlit as st
import pandas as pd
import os
import hashlib

st.set_page_config(page_title="Radar EW System - Login", layout="centered")

st.title("Radar PDW De-Interleaving System")
st.subheader("Secure Offline Login")

USER_DB = "users.csv"

# -------------------------------
# CREATE USER DATABASE IF NOT EXISTS
# -------------------------------
if not os.path.exists(USER_DB):
    df = pd.DataFrame(columns=["username", "password"])
    df.to_csv(USER_DB, index=False)

# -------------------------------
# SESSION STATE
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = ""

# -------------------------------
# PASSWORD HASH FUNCTION
# -------------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# -------------------------------
# SIGNUP FUNCTION
# -------------------------------
def signup(username, password):
    df = pd.read_csv(USER_DB)

    if username in df["username"].values:
        return False, "Username already exists"

    hashed_pwd = hash_password(password)
    new_user = pd.DataFrame([[username, hashed_pwd]], columns=["username", "password"])
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(USER_DB, index=False)

    return True, "Signup successful"

# -------------------------------
# LOGIN FUNCTION
# -------------------------------
def login(username, password):
    df = pd.read_csv(USER_DB)
    hashed_pwd = hash_password(password)

    user = df[
        (df["username"] == username) &
        (df["password"] == hashed_pwd)
    ]

    return not user.empty

# -------------------------------
# UI TABS
# -------------------------------
tab1, tab2 = st.tabs(["Login", "Signup"])

with tab1:
    st.subheader("Login")

    login_user = st.text_input("Username")
    login_pass = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(login_user, login_pass):
            st.session_state.logged_in = True
            st.session_state.user = login_user
            st.success("Login successful")
        else:
            st.error("Invalid username or password")

with tab2:
    st.subheader("Signup")

    signup_user = st.text_input("Create Username")
    signup_pass = st.text_input("Create Password", type="password")

    if st.button("Signup"):
        success, msg = signup(signup_user, signup_pass)
        if success:
            st.success(msg)
        else:
            st.error(msg)

# -------------------------------
# AFTER LOGIN
# -------------------------------
if st.session_state.logged_in:
    st.success(f"Welcome {st.session_state.user}")
    st.info("Password is securely stored using SHA-256 hashing (offline)")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.experimental_rerun()
