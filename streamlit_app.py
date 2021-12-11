from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import time
import os

import random

"""
# Welcome to Random Pick!
"""

def pick_random(data, n=1):
    a = [data]
    if '\n' in data:
        a = data.strip().split('\n')
    elif ',' in data:
        a = data.strip().split(',')

    if len(a) >= n:
        for i in range(n):
            x = random.choice(a)
            if x != "":
                st.write(' Number {}: {}'.format(i+1, x))
            time.sleep(1)
            a.remove(x)
    else:
        st.error('Number of options is not enough to pick from.')




with st.form('random-key'):
    data = ""
    data = st.text_area("Please add a list of items to pick from:")
    n = int(st.text_input("Number to pick:", value=1))
    st.form_submit_button("Random")



with st.spinner(text='In progess ...'):
    pick_random("")
    time.sleep(1)
    pick_random(data, n)
