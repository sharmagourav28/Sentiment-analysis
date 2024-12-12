import streamlit as st
import streamlit.components.v1 as components
from textblob import TextBlob
from PIL import Image
import text2emotion as te
import plotly.graph_objects as go
import json
import requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from pathlib import Path
from PIL import Image

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# st.markdown(
#     """
#     <style>
#     .css-1y4p8pa{
#     background-color:red;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
def plotPie(labels, values):
    fig = go.Figure(
        go.Pie(
        labels = labels,
        values = values,
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    st.plotly_chart(fig)

    
def getPolarity(userText):
    tb = TextBlob(userText)
    polarity = round(tb.polarity, 2)
    subjectivity = round(tb.subjectivity, 2)
    if polarity>0:
        return polarity, subjectivity, "Positive"
    elif polarity==0:
        return polarity, subjectivity, "Neutral"
    else:
        return polarity, subjectivity, "Negative"

def getSentiments(userText, type):
    if(type == 'Positive/Negative/Neutral - TextBlob'):
        polarity, subjectivity, status = getPolarity(userText)
        if(status=="Positive"):
            image = Image.open('./images/positive.PNG')
        elif(status == "Negative"):
            image = Image.open('./images/negative.PNG')
        else:
            image = Image.open('./images/neutral.PNG')
        col1, col2, col3 = st.columns(3)
        col1.metric("Polarity", polarity, None)
        col2.metric("Subjectivity", subjectivity, None)
        col3.metric("Result", status, None)
        st.image(image, caption=status)
    elif(type == 'Happy/Sad/Angry/Fear/Surprise - text2emotion'):
        emotion = dict(te.get_emotion(userText))
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Happy 😊", emotion['Happy'], None)
        col2.metric("Sad 😔", emotion['Sad'], None)
        col3.metric("Angry 😠", emotion['Angry'], None)
        col4.metric("Fear 😨", emotion['Fear'], None)
        col5.metric("Surprise 😲", emotion['Surprise'], None)
        plotPie(list(emotion.keys()), list(emotion.values()))
        

def renderPage():
        st.markdown("""
                <h3 class="stTitle">Sentiment Web App</h3>
                    
                """
                , unsafe_allow_html=True)
        lottie_hello = load_lottieurl("https://lottie.host/c07b6c29-b864-4778-818e-31343fdfe521/XHvQsxmUDG.json")
        # st_lottie(lottie_hello,key="hello")
        # col6,col7 = st.columns(2,gap="small")
        # with col6:
        #     st_lottie(
        #     lottie_hello,
        #     height=250,
        #     width=300,
        #    ) 
        # with col7:
        #     st.markdown("""
        #         <h5 class="st3">Text To Sentiment</h5>
        #         """
        #         , unsafe_allow_html=True)
        
        # st_lottie(lottie_hello, key="hello")
        # components.html("""<hr style="height:3px;border:none;color:#333;background-color:#333; margin-bottom: 10px" /> """)
        # st.markdown("### User Input Text Analysis")
        st.subheader("User Input Text Analysis")
        st.text("Analyzing text data given by the user and find sentiments within it.")
        st.text("")
        userText = st.text_input('User Input', placeholder='Input text HERE')
        st.text("")
        type = st.selectbox(
        'Type of analysis',
        ('Positive/Negative/Neutral - TextBlob', 'Happy/Sad/Angry/Fear/Surprise - text2emotion'))
        st.text("")
        if st.button('Predict'):
          if(userText!="" and type!=None):
            st.text("")
            st.components.v1.html("""
                                <h3 style="color: #0284c7; font-family: Source Sans Pro, sans-serif; font-size: 28px; margin-bottom: 10px; margin-top: 50px;">Result</h3>
                                """, height=100)
            getSentiments(userText, type)