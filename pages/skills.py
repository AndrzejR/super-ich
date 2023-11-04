import streamlit as st
import sqlite3

st.title("My Skills")

con = sqlite3.connect("skills.db")
cur = con.cursor()
cur.execute("CREATE TABLE skill(name, year, value)")

cur.execute("""
    INSERT INTO skill VALUES
        ('AWS', 2023, 120),
        ('AWS', 2022, 162),
        ('AWS', 2021, 51),
        ('Python', 2023, 32),
        ('Python', 2022, 5),
        ('German', 2023, 142)
""")
con.commit()

res = cur.execute("SELECT * FROM skill")
list_of_skills = res.fetchall()

col1, col2 = st.columns(2)

for skill in list_of_skills:
    with col1:
        st.text(f"{skill}")
    with col2:
        st.text(f"{str(value)}")
