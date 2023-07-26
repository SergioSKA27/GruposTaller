import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import os
import base64

#os.system("apt-get install tesseract-ocr tesseract-ocr-spa")

st.title('Teoria de Grupos')
with open( "styles.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)




file0_ = open("galois.gif", "rb")



contents0 = file0_.read()
data_url0 = base64.b64encode(contents0).decode("utf-8")
file0_.close()

st.markdown(
    f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url0}" alt="galois"></div>',
    unsafe_allow_html=True,
)
