"""import streamlit as st
st.title("FITTRACK")
st.write("welcome to FITTRACK,your personal fitness tracking app")
#streamlit run app.py

if st.button("Register User"):
    st.write("user registration functionality coming soon!")"""

# run this command
#         if st.button("register user"):
#              git add app.py fittrak.db
#              git commit -m "Initial commit for FITTRACK .app"
#              git push origin main

import streamlit as st
import sqlite3
import datetime
import pandas as pd

# Database initialization function
@st.cache_data
def init_db():
    conn = sqlite3.connect('FitTRACK.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        age INTEGER, 
        gender TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS Workouts (
        wid INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER, 
        date TEXT, 
        exercise TEXT, 
        duration INTEGER, 
        calories_burned INTEGER,
        FOREIGN KEY(userid) REFERENCES users(id)
    )''')
    conn.commit()
    conn.close()

# Initialize DB on app start
init_db()

# Session state for current user
if 'current_user_id' not in st.session_state:
    st.session_state.current_user_id = None

st.title("FITTRACK")
st.write("Welcome to FITTRACK, your personal fitness tracking app!")

# Sidebar navigation
st.sidebar.title("Main Menu")
menu_options = ["Register User", "Log Exercise", "View Users", "View Progress", "Exit"]
choice = st.sidebar.selectbox("Select an option:", menu_options)

if choice == "Register User":
    st.header("Register User")
    with st.form("register_form"):
        name = st.text_input("Enter name:")
        age = st.number_input("Enter age:", min_value=1)
        gender = st.selectbox("Enter gender:", ["Male", "Female", "Other"])
        submitted = st.form_submit_button("Register")
        if submitted:
            conn = sqlite3.connect('FitTRACK.db')
            c = conn.cursor()
            c.execute('INSERT INTO users(name, age, gender) VALUES (?, ?, ?)', (name, age, gender))
            user_id = c.lastrowid
            conn.commit()
            conn.close()
            st.success(f"User {name} registered successfully with ID: {user_id}!")
            st.session_state.current_user_id = user_id

elif choice == "Log Exercise":
    st.header("Log Exercise")
    if st.session_state.current_user_id:
        conn = sqlite3.connect('FitTRACK.db')
        c = conn.cursor()
        c.execute('SELECT name FROM users WHERE id=?', (st.session_state.current_user_id,))
        user_name = c.fetchone()[0]
        conn.close()
        st.info(f"Logged in as: {user_name}")
        
        with st.form("log_exercise"):
            date = st.date_input("Date:", value=datetime.date.today())
            exercise = st.text_input("Enter exercise name:")
            duration = st.number_input("Duration (minutes):", min_value=0)
            calories = st.number_input("Calories burned:", min_value=0)
            submitted = st.form_submit_button("Log Exercise")
            if submitted:
                conn = sqlite3.connect('FitTRACK.db')
                c = conn.cursor()
                c.execute('''INSERT INTO Workouts(userid, date, exercise, duration, calories_burned) 
                           VALUES (?, ?, ?, ?, ?)''', 
                         (st.session_state.current_user_id, date.strftime('%Y-%m-%d'), exercise, duration, calories))
                conn.commit()
                conn.close()
                st.success("Exercise logged successfully!")
    else:
        st.warning("Please register a user first or select a user ID.")
        uid = st.number_input("Enter user ID:", min_value=1)
        if st.button("Set Current User"):
            # Verify user exists
            conn = sqlite3.connect('FitTRACK.db')
            c = conn.cursor()
            c.execute('SELECT id FROM users WHERE id=?', (uid,))
            if c.fetchone():
                st.session_state.current_user_id = uid
                st.success(f"Current user set to ID: {uid}")
            else:
                st.error("User ID not found!")
            conn.close()

elif choice == "View Users":
    st.header("View All Users")
    conn = sqlite3.connect('FitTRACK.db')
    df = pd.read_sql_query("SELECT * FROM users", conn)
    conn.close()
    st.dataframe(df)

elif choice == "View Progress":
    st.header("View Workout Progress")
    if st.session_state.current_user_id:
        conn = sqlite3.connect('FitTRACK.db')
        df = pd.read_sql_query("""
            SELECT w.date, w.exercise, w.duration, w.calories_burned 
            FROM Workouts w 
            WHERE w.userid = ? 
            ORDER BY w.date DESC
        """, conn, params=(st.session_state.current_user_id,))
        conn.close()
        if not df.empty:
            st.dataframe(df)
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Workouts", len(df))
            with col2:
                st.metric("Total Calories Burned", df['calories_burned'].sum())
        else:
            st.info("No workouts logged yet.")
    else:
        st.warning("Please set current user first.")

elif choice == "Exit":
    st.session_state.current_user_id = None
    st.stop()
