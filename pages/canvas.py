import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import base64
import json
import os
import re
import time
import uuid
from io import BytesIO
from pathlib import Path
from PIL import Image
from streamlit_drawable_canvas import st_canvas
from svgpathtools import parse_path
import pytesseract
import platform
from code_editor import code_editor
from streamlit_server_state import server_state, server_state_lock,force_rerun_bound_sessions
from PIL import Image

with open( "styles.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

def get_image_download_link(img,filename,text):

  """
  The function `get_image_download_link` takes an image, filename, and text as input, converts the image to a base64
  encoded string, and returns an HTML link that allows the user to download the image with the specified filename and
  displays the specified text.

  :param img: The `img` parameter is the image object that you want to convert to a download link
  :param filename: The filename is the name that you want to give to the downloaded image file
  :param text: The text parameter is the text that will be displayed as the link for downloading the image
  :return: an HTML anchor tag (`<a>`) with a download link for an image. The link is encoded in base64 and includes the
  image data, filename, and text to display for the link.
  """
  buffered = BytesIO()
  img.save(buffered, format="JPEG")
  img_str = base64.b64encode(buffered.getvalue()).decode()
  href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
  return href




# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:",
    ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
)
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == "point":
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#ffffff")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component



canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image=Image.open(bg_image) if bg_image else None,
        update_streamlit=realtime_update,
        height=600,
        width=600,
        drawing_mode=drawing_mode,
        point_display_radius=point_display_radius if drawing_mode == "point" else 0,
        display_toolbar=st.sidebar.checkbox("Display toolbar", True),
        key="canvas",
      )
















# Do something interesting with the image data and paths
if canvas_result.image_data is not None:
    #update_canvas()
    st.write('## Texto:')
    r = pytesseract.image_to_string(canvas_result.image_data,lang="spa")

    st.write(r)
else :
  r = ''


if st.button('Descargar ') or canvas_result.image_data is not None:
    filename = st.text_input('Ingrese el nombre del archivo ','.jpg')
    result = Image.fromarray(canvas_result.image_data);
    st.markdown(get_image_download_link(result.convert('RGB'),filename,'Download '+filename))


code1 = r'''
'''
code1 = code1+r

st.session_state["edit"] = code1

bts = [
 {
   "name": "Copy",
   "feather": "Copy",
   "hasText": True,
   "alwaysOn": True,
   "commands": ["copyAll"],
   "style": {"top": "0.46rem", "right": "0.4rem"}
 },
 {
   "name": "Shortcuts",
   "feather": "Type",
   "class": "shortcuts-button",
   "hasText": True,
   "commands": ["toggleKeyboardShortcuts"],
   "style": {"bottom": "calc(50% + 1.75rem)", "right": "0.4rem"}
 },
 {
   "name": "Collapse",
   "feather": "Minimize2",
   "hasText": True,
   "commands": ["selectall",
                "toggleSplitSelectionIntoLines",
                "gotolinestart",
                "gotolinestart",
                "backspace"],
   "style": {"bottom": "calc(50% - 1.25rem)", "right": "0.4rem"}
 },
 {
   "name": "Guardar",
   "feather": "Save",
   "hasText": True,
   "commands": ["save-state", ["response","saved"]],
   "response": "saved",
   "style": {"bottom": "calc(50% - 4.25rem)", "right": "0.4rem"}
 },
 {
   "name": "Ejecutar",
   "feather": "Play",
   "primary": True,
   "hasText": True,
   "showWithIcon": True,
   "commands": ["submit"],
   "style": {"bottom": "0.44rem", "right": "0.4rem"}
 },
 {
   "name": "Comandos",
   "feather": "Terminal",
   "primary": True,
   "hasText": True,
   "commands": ["openCommandPallete"],
   "style": {"bottom": "3.5rem", "right": "0.4rem"}
 }
]

css_string = '''
background-color: #bee1e5;

body > #root .ace-streamlit-dark~& {
   background-color: #262830;
}

.ace-streamlit-dark~& span {
   color: #fff;
   opacity: 0.6;
}

span {
   color: #000;
   opacity: 0.5;
}

.code_editor-info.message {
   width: inherit;
   margin-right: 75px;
   order: 2;
   text-align: center;
   opacity: 0;
   transition: opacity 0.7s ease-out;
}

.code_editor-info.message.show {
   opacity: 0.6;
}

.ace-streamlit-dark~& .code_editor-info.message.show {
   opacity: 0.5;
}
'''
# create info bar dictionary
info_bar = {
  "name": "language info",
  "css": css_string,
  "style": {
            "order": "1",
            "display": "flex",
            "flexDirection": "row",
            "alignItems": "center",
            "width": "100%",
            "height": "2.5rem",
            "padding": "0rem 0.75rem",
            "borderRadius": "8px 8px 0px 0px",
            "zIndex": "9993"
           },
  "info": [{
            "name": "python",
            "style": {"width": "100px"}
           }]
}
# CSS string for Code Editor
css_string2 = '''
font-weight: 600;
&.streamlit_code-editor .ace-streamlit-dark.ace_editor {
  background-color: #111827;
  color: rgb(255, 255, 255);
}
&.streamlit_code-editor .ace-streamlit-light.ace_editor {
        background-color: #eeeeee;
        color: rgb(0, 0, 0);
}
'''
# style dict for Ace Editor
ace_style = {"borderRadius": "0px 0px 8px 8px"}

# style dict for Code Editor
code_style = {"width": "100%"}
editor0 = code_editor(st.session_state.edit,theme="contrast",buttons=bts,lang='python',height=[15, 30],focus=True,info=info_bar,props={"style": ace_style}, component_props={"style": code_style, "css": css_string2})

if st.session_state.edit != code1:
  st.session_state.edit = st.session_state.edit +code1




if editor0['type'] == "saved" and len(editor0['text']) != 0:
    filename = st.text_input('Ingrese el nombre del archivo ','example')
    st.download_button(
        label="Descargar",
        data=editor0['text'],
        file_name=filename,
        mime='text/python',)


st.subheader('Preview')

st.write(editor0['text'])


