import streamlit as st
import backend

st.title("Dailies - WIP")


def add_daily():
    new_daily = {}
    new_daily['name'] = st.session_state['new_daily']
    new_daily['done_today'] = False
    dailies.append(new_daily)
    backend.write_dailies(dailies)
    st.session_state['new_daily'] = ""


dailies = backend.get_dailies()

for d in dailies:
    st.checkbox(d['name'], value=d['done_today'])

st.text_input(label="Enter a todo:", placeholder="Add a daily...",
              on_change=add_daily, key='new_daily')

st.session_state
