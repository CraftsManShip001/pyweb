import streamlit as st
import pandas as pd
import numpy as np

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
st.write('개인 대회')
solo_data = {
    '대회' : ['KOI 2022 1차','KOI 2023 1차','KOI 2023 2차','KOI 2024 1차'],
    '수상' : ['장려상(25%)','동상(15%)','미수상','미수상']
}
df_solo = pd.DataFrame(solo_data)
st.table(df_solo)

st.write('팀 대회')
multi_data = {
    '대회' : ['2030 과학 아이디어 해커톤','부산시 SW 해커톤 2022 중등부', '제 1회 동래 메이커톤'],
    '수상' : ['미수상','미수상','우수상']
}
df_multi = pd.DataFrame(multi_data)
st.table(df_multi)