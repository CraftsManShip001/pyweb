import streamlit as st
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
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
score = 0
st.write('')
st.write('')
st.write('')

age = st.slider("나의 키는?", 100, 200, 1)
if age == 175:
    score += 1
st.write('')
st.write('')

birth = st.date_input("나의 생일은?", datetime.date(2000, 1, 1))
if birth == datetime.date(2008,8,29):
    score += 1
st.write('')
st.write('')

lang = st.radio(
    "내가 가장 좋아하는 색은?",
    ["빨간색", "검은색", "파란색","하얀색"],
    captions = ["빨간색", "검은색", "파란색","하얀색"])
if lang == "하얀색":
    score += 1
st.write('')
st.write('')

number = st.number_input("내가 가장 좋아하는 숫자는?", min_value=0, max_value=10, step=1, placeholder="숫자를 입력하시오")
if number == 0:
    score += 1
st.write('')
st.write('')

lang = st.radio(
    "내가 의외로 한번정도는 배운적 있는 언어는?",
    ["C#", "아희", "JAVA","Ruby"],
    captions = ["C#", "아희", "JAVA","Ruby"])
if lang == "JAVA":
    score += 1
st.write('')
st.write('')
if st.button("Submit"):
    st.write(score)

