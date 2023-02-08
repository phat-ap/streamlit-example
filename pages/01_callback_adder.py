# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:05:15 2023

@author: phata
"""

import streamlit as st

st.set_page_config(
    page_title="Callback: Adder"
)


st.title('Counter Example using Callbacks with kwargs')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter(increment_value=0):
    st.session_state.count += increment_value

def decrement_counter(decrement_value=0):
    st.session_state.count -= decrement_value

st.button('Increment', on_click=increment_counter,
    kwargs=dict(increment_value=5))

st.button('Decrement', on_click=decrement_counter,
    kwargs=dict(decrement_value=1))

st.write('Count = ', st.session_state.count)