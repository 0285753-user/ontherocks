import streamlit as st

def show_header(text_title: str):
  #Layout: logo + title side by side
  col1, col2 = st.columns([1, 6])

  with col1:
    st.image("image_bi/on_the_rocks_f.jpg", width = 200)

  with col2:
    st.title(text_title)
    st.caption(" Developed for show pourposes")
    st.caption("On The Rocks Copyleft")
