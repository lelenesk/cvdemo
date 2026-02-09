import requests
import streamlit as st


def log_visitors(visitor_name: str, page_name: str, hit_ts: str):
    webhook_url = st.secrets['discord']['webhook_bot_channel']
    # avoid not existing discord acc -> switch off logging in app.py
    if not webhook_url:
        return
    str_to_send = f"""visitor_name:{visitor_name}
    page_name: {page_name}
    hit_ts: {hit_ts}"""
    requests.post(webhook_url, data={'content': str_to_send})


def app_clear_cache():
    keys = list(st.session_state.keys())
    for key in keys:
        st.session_state.pop(key)


@st.dialog("Wait a moment❗", width='medium', dismissible=True, on_dismiss='ignore')
def app_alert_popup(message: str = "Page under construction"):
    st.subheader(f"{message}")
    # if st.button("Continue on this page ↩️", width='stretch'):
    # #     st.session_state.login_user_check = None
    #     st.rerun()
