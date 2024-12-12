import streamlit as st
import sidebar
import textPage
import home
import imdbReviewsPage
from pathlib import Path
import imagePage
import about
import contact
page = sidebar.show()
current_dir = Path(__file__).parent if "_file__" in locals() else Path.cwd()
css_file = current_dir/"style"/"main.css"
with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
if page == "Home":
    # st.title(f"You have selected {page}")
    home.renderPage()
if page=="Text":
    textPage.renderPage()
elif page=="IMDb movie reviews":
    imdbReviewsPage.renderPage()
elif page=="Image":
    imagePage.renderPage()
elif page =="About":
    # st.title(f"You have Selected{page}"
    about.renderApp()
elif page=="Contact":
    # st.title(f"you have selected{page}")
    contact.renderPage()

