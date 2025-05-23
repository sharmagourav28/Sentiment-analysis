

<br>

# Sentiment Analysis App 😊😐😔😡

<br>

## About
**A sentiment analysis application built using Streamlit( An open source framework to build web applications in python )**

Sentiment Analysis is one of the most famous applications of Natural Language Processing. Wherever data is present, we can apply it. It applies to all types of data, from text to audio to video to image. Data in any form can be processed to get sentiments out of it. The objective of the project is to create a web application which will harbor all sorts of applications in the field of sentiment analysis from applying it on text to analyzing images.

<br>


## Project Specifications

**Below are the libraries and frameworks used to create the project**
- **Web Framework** :- Streamlit
- **Graphs and Images** :- PIL, plotly, cv2
- **Libraries for sentiment analysis** :- textblob, nltk(vader), flair, text2emotion, fer
- **Libraries for API requests** :- requests, json

<br>

## Project Components

**The project currently contains 3 applications :-**
1. **Text** - Applying sentiment analysis on text given by the user.
2. **IMDb movie reviews** - We get review data based on movie entered by user from the IMDb API and process the same to obtain emotions of people regarding the movie.
3. **Image** - Here we analyze sentiments out of image uploaded by the user. We detect faces and then analyze sentiments for each.  We also calculate the sentiment of image as a whole.

<br>



## Models used
There are multiple libraries available in python for sentiment analysis. Let's see them below 👇

- **TextBlob** - TextBlob is a Python library for processing textual data. It provides a simple API for diving into common (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
- **Flair** - A very simple framework for state-of-the-art NLP. It is a powerful NLP library which allows you to apply state-of-the-art natural language processing (NLP) models to your text, such as named entity recognition (NER), part-of-speech tagging (PoS), etc.
- **Vader** - VADER (Valence Aware Dictionary and Sentiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. 
- **text2emotion** - text2emotion is the python package which will help you to extract the emotions from the content. It processes any textual message and recognize the emotions embedded in it. It is compatible with 5 different emotion categories as Happy, Angry, Sad, Surprise and Fear.

<br>

*__Note :-__* 
1. textblob, flair and vader provide polarity score where text is declared in either of 3 states (POSITIVE🙂, NEGATIVE☹️, NEUTRAL😐)
2. text2emotion is the only library among the others mentioned above which can classify text in 5 emotion categories (HAPPY😊, ANGRY😡, SAD😔, SURPRISE😲, FEAR😨)

<br>

## Project development ideas

**Below mentioned applications can be implemented as a future scope -**
- Tweets analysis using Twitter API
- Sentiment analysis on Live video streaming
- Sentiment analysis of Audio data
- Sentiment analysis of data received from site given by user using web scraping in python.

<br>

## Thank You!
Thank you. **I hope you liked the project**. 

If you really did then don't forget to **give a star**⭐ to this repo. It would mean a lot.
