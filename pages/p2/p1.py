import streamlit as st
from datetime import datetime as ddt
import datetime as dd
from src.temp_app_func import log_visitors


st.set_page_config(page_title="Project 2", page_icon="🤖", layout="wide")

if st.session_state.send_dc_alert == "ON":
    log_visitors(visitor_name=st.session_state.logged_visitor_name,
                 page_name="Project 2 - Page 1",
                 hit_ts=(ddt.now() + dd.timedelta(hours=2)).strftime("%B %d - %H:%M:%S"))

st.write("Hello Recruiters")
