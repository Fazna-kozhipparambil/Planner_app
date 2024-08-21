# -*- coding: utf-8 -*-
"""Project _1.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LqahZuArvut5BrnzG3AJE8ZswK5APjf7

Install required library
"""

pip install streamlit pandas google-auth google-auth-oauthlib

"""**Design the Planner App**

1.Import Libraries:
"""

import streamlit as st
import pandas as pd
from datetime import datetime, time
import streamlit as st

st.title('Simple Test App')
st.write('This is a test.')

"""2.Create User Login and Role Management:"""

users = {"parent1": "password1", "parent2": "password2", "child1": "password3"}
roles = {"parent1": "admin", "parent2": "admin", "child1": "user"}

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if username in users and users[username] == password:
    st.success(f"Welcome {username}")
    role = roles[username]
else:
    st.error("Invalid credentials")
    st.stop()

"""3.Design the Layout:"""

st.title(f"Family Planner - {username.capitalize()}")

# Daily Tasks
st.header("Daily Tasks")
tasks = st.text_area("Enter today's tasks (comma-separated)").split(',')

# Reminders
st.header("Reminders")
reminders = st.text_area("Enter reminders (comma-separated)").split(',')

# Household Chores
st.header("Household Chores")
chores = st.text_area("Enter household chores (comma-separated)").split(',')

# Daily Food Menu
st.header("Daily Food Menu")
breakfast = st.text_input("Breakfast")
lunch = st.text_input("Lunch")
dinner = st.text_input("Dinner")

# Sleep Routine
st.header("Sleep Routine")
sleep_time = st.time_input("Sleep Time", time(22, 0))
wake_time = st.time_input("Wake Time", time(6, 0))

"""4.Task Assignment:"""

st.header("Task Assignment")
for task in tasks:
    assignee = st.selectbox(f"Assign {task.strip()} to:", options=users.keys())
    st.write(f"{task.strip()} assigned to {assignee}")



"""5.Save and View Data:"""

data = {
    "Tasks": tasks,
    "Reminders": reminders,
    "Health Metrics": [health_metrics],
    "Chores": chores,
    "Food Menu": {"Breakfast": breakfast, "Lunch": lunch, "Dinner": dinner},
    "Sleep Routine": {"Sleep Time": sleep_time, "Wake Time": wake_time}
}

df = pd.DataFrame(data)
st.write(df)

