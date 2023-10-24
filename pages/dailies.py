import streamlit as st
import backend
import time

# print(f"{time.strftime('%H:%M:%S')}")

st.title("Dailies - WIP")


def add_daily():
    new_daily = {}
    new_daily['name'] = st.session_state['new_daily']
    new_daily['done_today'] = False
    dailies.append(new_daily)
    backend.write_dailies(dailies)
    st.session_state['new_daily'] = ""


dailies = backend.get_dailies()

for i, d in enumerate(dailies):
    st.checkbox(d['name'], value=d['done_today'], key=d['name'])
    if st.session_state[d['name']]:
        dailies[i]['done_today'] = True
        backend.write_dailies(dailies)
    else:
        dailies[i]['done_today'] = False
        backend.write_dailies(dailies)

st.text_input(label="Enter a to-do:", placeholder="Add a daily...",
              on_change=add_daily, key='new_daily')

st.session_state
