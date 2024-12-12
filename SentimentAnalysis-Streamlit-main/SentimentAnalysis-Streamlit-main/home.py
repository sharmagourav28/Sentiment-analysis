import streamlit as st
import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from pathlib import Path
from PIL import Image

# def load_lottiefile(filepath: str):
#     with open(filepath, "r") as f:
#         return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def renderPage():
    # st.title("Home Page")
    st.markdown("""<h3 class="stTitle">Sentiment Web App</h3>
                <br><br>
                <h5 class="st2">Play Around With Our Sentiment Analyzer</h5>
                """
                , unsafe_allow_html=True)
    
    col3,col4 = st.columns(2,gap="small")
    
       
    with col3:
        lottie_say=load_lottieurl("https://lottie.host/d97db881-9731-442e-9fec-620abbd932ea/X3yhgxSbU8.json")
        st_lottie(lottie_say,key="say")

    with col4:
         lottie_hello = load_lottieurl("https://lottie.host/3437beb5-edd4-4800-8d48-a21629ecc64a/g5WD3Cy1LU.json")
         st_lottie(lottie_hello,key="hello")
    
       
        # 