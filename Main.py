import streamlit as st

st.title('나를 소개합니다, 서정현')
col1,col2,col3,col4 = st.columns(4)
with col1:
    st.page_link("Main.py", label="Home", icon="🗼")
with col2:
    st.page_link("pages/awards.py", label="My awards", icon="🏆")
with col3:
    st.page_link("pages/solved.py", label="My solved.ac", icon="🧩")
with col4:
    st.page_link("pages/quiz.py", label="Quiz", icon="🎢")
st.write('')
st.write('')
st.write('')
st.markdown(
    """
    <div style="text-align: center;">
        <h2 style="font-size: 20px;">저는 AI 개발자를 희망하는 부산 소프트웨어 마이스터고 1학년 서정현입니다.</h2>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://github.com/CraftsManShip001" target="_blank">
            <button style="padding: 10px 20px; font-size: 16px; background-color: purple; color: white; border: none; border-radius: 5px;">Visit GitHub</button>
        </a>
        <a href="https://www.notion.so/16b4cba41d854e328528ca44706e6489?pvs=4" target="_blank">
            <button style="padding: 10px 20px; font-size: 16px; background-color: red; color: white; border: none; border-radius: 5px; margin-left:30px;">Visit Notion</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('secret.json')
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://test2-40632-default-rtdb.firebaseio.com'
    })