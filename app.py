import streamlit as st
import numpy as np
import datetime
import random

today = datetime.date.today()
date_seed = int(str(today.month) + str(today.day) + str(today.year))
random.seed(date_seed)
bark_likelihood = random.random()

is_bark = np.random.uniform(0, 1) < bark_likelihood

if is_bark:
    text = "The Dog is Currently Barking"
else:
    text = "The Dog is Not Currently Barking"

st.text(text)