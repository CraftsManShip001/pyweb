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
        <a href="https://solved.ac/profile/august080829" target="_blank">
            <button style="padding: 10px 20px; font-size: 16px; background-color: gold; color: black; border: none; border-radius: 5px;">Visit Solved.ac</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)