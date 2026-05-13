import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

from funcs.eak2000funcs import A, Fd, Fe, T1, T2, γ1, h
from funcs.ec8funcs import S, Sd, Se, TB, TC, TD, agR, γ1, h

from funcs.test_motion import TestMotion

st.set_page_config(page_title="test_panagop", )
centered_style = """
  <style>
  .centered {
      display: flex;
      justify-content: center;
      align-items: center;
      height: auto;
  }
  </style>
"""
st.markdown(centered_style, unsafe_allow_html=True)

custom_color = "#00008B"


radio_select_motion = st.sidebar.radio(
    "Επιλογή διέγερσης", ["from acc file", "from list"])

if radio_select_motion == "from acc file":
    uploaded_file = st.sidebar.file_uploader(
        "Επιλέξτε ένα αρχείο", type=['txt', 'asc'])
    if uploaded_file is not None:
        tm = TestMotion.from_acc_file(
            pathfilename=uploaded_file,
            motion_step=0.01,
            scale_factor=0.01,
            accel_column=1,
            skiprows=1)

elif radio_select_motion == "from list":
    motion_files = {
        "Αθήνα, Ελλάδα (1999) - ATH39901": 'motions/ATH39901.dat.smc.cor_0p20.a.asc',
        "Θεσσαλονίκη, Ελλάδα (1978) - THEA7802": 'motions/THEA7802.dat.smc.cor_0p20.a.asc',
        "Καλαμάτα, Ελλάδα (1986) - KAL18601": 'motions/KAL18601.dat.smc.cor_0p10.a.asc',
        "Κοζάνη, Ελλάδα (1995) - KRR19501": 'motions/KRR19501.dat.smc.cor_0p15.a.asc'
    }
    selected_motion = st.sidebar.selectbox(
        "Επιλέξτε μια διέγερση", list(motion_files.keys()))
    motion_file = motion_files[selected_motion]

    tm = TestMotion.from_acc_file(
        pathfilename=motion_file,
        motion_step=0.01,
        scale_factor=0.01,
        accel_column=1,
        skiprows=1)


st.pyplot(tm.fig_time_histories())
st.pyplot(tm.fig_sa())


# uploaded_file = st.sidebar.file_uploader(
#     "Επιλέξτε ένα αρχείο", type=['txt', 'asc'])
# if uploaded_file is not None:
