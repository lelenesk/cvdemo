import streamlit as st
import nest_asyncio
import random
import string


# **********************************************************************************************************************
#                             FIX INTERNAL EVENT LOOP AND HIDE LINKS ON ALL PAGE
# **********************************************************************************************************************

nest_asyncio.apply()
st.html("""<style> .stPageLink {position: fixed; right: 1rem; bottom: 0.2rem;} </style>""")

# **********************************************************************************************************************
#                                            HOUSEKEEPING
# **********************************************************************************************************************

if "send_dc_alert" not in st.session_state:
    st.session_state.send_dc_alert = "O...F....F"  # switch off dc messages (can be anything else but ON)
    if st.session_state.send_dc_alert == "ON":
        st.session_state.logged_visitor_name = "".join(random.choices(list(string.ascii_letters), k=10))


st.set_page_config(page_title="Demo", page_icon="🔥", layout="centered", initial_sidebar_state='expanded')
# st.logo("src/images/gts_new_square.png")
# st.markdown('<style>' + open('css/markdown_colors.css').read() + '</style>', unsafe_allow_html=True)

# **********************************************************************************************************************
#                                          RENDER SELECTED PAGE
# **********************************************************************************************************************

# Health app
welcome_page = st.Page("pages/health_app/welcome_page.py", title="Welcome", icon="🏠") # ":material/chat_info:")
plot_page = st.Page("pages/health_app/dashboard.py", title="Dashboard", icon="👋")
# Project 2
p2_page1 = st.Page("pages/p2/p1.py", title="temp", icon="🎫")

selected_page = st.navigation(# position="top",
    {"Health App": [welcome_page, plot_page
            ],
    "Other project": [
         p2_page1,
    ]}, position="sidebar", expanded=True)

selected_page.run()
