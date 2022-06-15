#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 18:58:47 2022

@author: mac
"""

import numpy as np
import pandas as pd 
import pickle
import streamlit as st
import base64
from PIL import Image
import re
import unicodedata
import string
import nltk
from gensim.parsing.preprocessing import remove_stopwords
from nltk.corpus import stopwords
stemmer = nltk.SnowballStemmer("english")
#df = pd.read_csv('/content/drive/My Drive/amazonreviews.tsv',sep='\t')
model=pickle.load(open('model.pkl','rb'))

st.set_page_config(page_title="Hate Speech Web App",page_icon="",layout="centered",initial_sidebar_state="expanded",)
st.title('Hate Speech Detection')
st.subheader('by Oluwaseun Alagbe')


#main_bg = "https://cdn.miscellaneoushi.com/1440x900/20121018/abstract%20technology%20hearts%201440x900%20wallpaper_www.miscellaneoushi.com_20.jpg"
#main_bg_ext = "jpg"

#st.markdown(
 #   f"""
  #  <style>
   # .reportview-container {{
    #    background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    #}}
    #</style>
    #""",
    #unsafe_allow_html=True
#)


st.markdown("""
<style>
body {
    color: #ff0000;
    background-color: #001f;
    etc. 
}
</style>
    """, unsafe_allow_html=True)




st.header("Hate Speech Detector")
st.subheader("Enter the statement that you want to Detect")
text = st.text_area("","Enter sentence", height=50)
def simplify(text):
    '''Function to handle the diacritics in the text'''
    try:
        text = unicode(text, 'utf-8')
    except NameError:
        pass
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    return str(text)
def filter_text(text):
    text = re.sub(r'@\w+', '',text)
    text = re.sub(r'http\S+', '', text)
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    # Remove stopwords
    text = remove_stopwords(text)
    return text
    
text = simplify(text)
text = filter_text(text)
	# Model Selection 
if st.button("Predict"):
    print("continue")
   
    
    # Make the prediction 
    if model.predict([text]):
        st.write("**Hate Speech Detected!!!**")
    else:
        st.write("This statement is **Not a Hate Speech**")

		

  #for index, item in enumerate(df['review']):
      #st.write(f'{item} : {q[0][index]*100}%')

st.sidebar.subheader("About App")

st.sidebar.info("This web app was created to Detect hate speeches from tweets")

st.sidebar.info("Click on the 'Predict' button to check whether the entered text is an 'Hate speech' or 'Non Hate Speech' ")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=10,step=1)

if feedback:
  st.header("Thank you for rating the app!")