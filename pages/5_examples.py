import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

from funcs.eak2000funcs import A, Fd, Fe, T1, T2, γ1, h
from funcs.ec8funcs import S, Sd, Se, TB, TC, TD, agR, γ1, h
from funcs.examplesfuncs import (
    show,
    show_L,
    show_T,
    show_fourier_spectra_stable_against_aliasing,
    show_response_spectra_at_high_frequencies,
    show_response_spectra_at_high_frequencies_L,
    show_response_spectra_at_high_frequencies_T,
    show_test_motion,
    show_test_motion_L,
    show_test_motion_T,
)

from funcs.test_motion import TestMotion


st.set_page_config(page_title="Παραδείγματα", )
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



st.markdown(
    f'<font color="{custom_color}" size="6" class="centered">Παραδείγματα</font>',
    unsafe_allow_html=True)


motion_step = st.sidebar.number_input(
    'Ορίστε το βήμα κίνησης',
    value=0.005,
    format="%.3f")


choice = st.sidebar.radio(
    label='#### Επιταχυνσιογραφήματα',
    options=[
        'Μεταφορτώστε αρχείο',
        'Εκτελέστε ένα από τα διαθέσιμα επιταχυνσιογραφήματα'
    ],
    index=1
)


pathfilename = None

if choice == 'Μεταφορτώστε αρχείο':
    with st.sidebar.expander('Προσοχή! Τα αρχεία που μεταφορτώνετε, θα πρέπει να έχουν την παρακάτω δομή. Οι τιμές που χρησιμοποιούνται είναι ενδεικτικές.'):
        st.image('img/sample.png', caption='Αρχείο με κατάληξη .asc',
                 use_container_width=True)
        st.image('img/sample2.png', caption='Αρχείο με κατάληξη .txt',
                 use_container_width=True)
    uploaded_file = st.sidebar.file_uploader(
        "Επιλέξτε ένα αρχείο", type=['txt', 'asc'])
    if uploaded_file is not None:
        file_extension = os.path.splitext(uploaded_file.name)[1]
        if file_extension == '.txt':
            pathfilename = uploaded_file
        elif file_extension == '.asc':
            pathfilename = uploaded_file
        else:
            st.sidebar.error(
                "Ελέξτε την ορθότητα του αρχείου, ως προς την σύνταξη του.")
    else:
        st.sidebar.error("Δεν επιλέξατε κάποιο αρχείο.")

elif choice == 'Εκτελέστε ένα από τα διαθέσιμα επιταχυνσιογραφήματα':
    epitax = st.sidebar.selectbox(
        "Επιταχυνσιογραφήματα πραγματικών σεισμών",
        ("Αθήνα, Ελλάδα (1999) - ATH39901", "Θεσσαλονίκη, Ελλάδα (1978) - THEA7802",
         "Καλαμάτα, Ελλάδα (1986) - KAL18601", "Κοζάνη, Ελλάδα (1995) - KRR19501"),
        index=0,
    )

    motion_files = {
        "Αθήνα, Ελλάδα (1999) - ATH39901": 'motions/ATH39901.dat.smc.cor_0p20.a.asc',
        "Θεσσαλονίκη, Ελλάδα (1978) - THEA7802": 'motions/THEA7802.dat.smc.cor_0p20.a.asc',
        "Καλαμάτα, Ελλάδα (1986) - KAL18601": 'motions/KAL18601.dat.smc.cor_0p10.a.asc',
        "Κοζάνη, Ελλάδα (1995) - KRR19501": 'motions/KRR19501.dat.smc.cor_0p15.a.asc'
    }
    pathfilename = motion_files[epitax]


if pathfilename is not None:
    if choice == 'Μεταφορτώστε αρχείο':
        if uploaded_file is not None:
            file_extension = os.path.splitext(uploaded_file.name)[1]
            if file_extension == '.txt':
                fig1 = show_test_motion(pathfilename, motion_step)
                fig2 = show_response_spectra_at_high_frequencies(
                    pathfilename, motion_step)
                st.pyplot(fig1)
                st.pyplot(fig2)
            elif file_extension == '.asc':
                fig1 = show_test_motion_L(pathfilename, motion_step)
                fig2 = show_test_motion_T(pathfilename, motion_step)
                fig3 = show_response_spectra_at_high_frequencies_L(
                    pathfilename, motion_step)
                fig4 = show_response_spectra_at_high_frequencies_T(
                    pathfilename, motion_step)
                col1, col2 = st.columns(2)
                with col1:
                    st.pyplot(fig1)
                    st.pyplot(fig3)
                with col2:
                    st.pyplot(fig2)
                    st.pyplot(fig4)
            else:
                st.sidebar.error(
                    "Ελέξτε την ορθότητα του αρχείου, ως προς την σύνταξη του.")
    elif choice == 'Εκτελέστε ένα από τα διαθέσιμα επιταχυνσιογραφήματα':
        fig1 = show_test_motion_L(pathfilename, motion_step)
        fig2 = show_test_motion_T(pathfilename, motion_step)
        fig3 = show_response_spectra_at_high_frequencies_L(
            pathfilename, motion_step)
        fig4 = show_response_spectra_at_high_frequencies_T(
            pathfilename, motion_step)
        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(fig1)
            st.pyplot(fig3)
        with col2:
            st.pyplot(fig2)
            st.pyplot(fig4)
else:
    st.sidebar.error("Παρακαλώ επιλέξτε ή ανεβάστε ένα αρχείο.")


if choice == 'Εκτελέστε ένα από τα διαθέσιμα επιταχυνσιογραφήματα' and epitax == "Αθήνα, Ελλάδα (1999) - ATH39901":
    st.write('Σύγκριση των Ελαστικών Φασμάτων Απόκρισης του σεισμού με τα αντίστοιχα Ελαστικά Φάσματα Απόκρισης των κανονισμών')
    x1 = [0, T1('B')] + [T1('B'), T2('B')] + \
        list(np.linspace(T2('B'), 4.00, 100))
    y1 = [Fe(T=period, edafos='B', ζ=5, spoudaiothta='II', zoni='Z2')
          for period in x1]

    x2 = [0, TB('B')] + [TB('B'), TC('B')] + list(np.linspace(TC('B'),
                                                              TD('B'), 200)) + list(np.linspace(TD('B'), 4.00, 80))
    y2 = [Se(T=period, edafos='B', ζ=5, spoudaiothta='II', zoni='Z2')
          for period in x2]

    fig = go.Figure()
    fig2 = show_L(pathfilename, motion_step)
    for line in fig2.axes[0].lines:
        fig.add_trace(go.Scatter(x=line.get_xdata(),
                      y=line.get_ydata(), mode='lines', name='ΑΘΗΝΑ'))
    fig.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='Ε.Α.Κ. 2000'))
    fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='EC8'))
    fig.update_layout(xaxis_title='Ιδιοπερίοδος T (sec)',
                      yaxis_title='Επιταχύνσεις (m/s²)')
    st.plotly_chart(fig)
    max_show_L = max(fig2.axes[0].lines[0].get_ydata())
    st.caption(
        f'Οριζόντιο ελαστικό φάσμα απόκρισης για το σεισμό της Αθήνας (ATH39901) με μέγιστη φασματική επιτάχυνση {max_show_L:.2f} m/s², σύμφωνα με την συνιστώσα L, και σύγκρισή του με τα φάσματα απόκρισης του Ε.Α.Κ.2000 και του EC8')

    fig3 = go.Figure()
    fig4 = show_T(pathfilename, motion_step)
    for line in fig4.axes[0].lines:
        fig3.add_trace(go.Scatter(x=line.get_xdata(),
                       y=line.get_ydata(), mode='lines', name='ΑΘΗΝΑ'))
    fig3.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='Ε.Α.Κ. 2000'))
    fig3.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='EC8'))
    fig3.update_layout(xaxis_title='Ιδιοπερίοδος T (sec)',
                       yaxis_title='Επιταχύνσεις (m/s²)')
    st.plotly_chart(fig3)
    max_show_T = max(fig4.axes[0].lines[0].get_ydata())
    st.caption(
        f'Οριζόντιο ελαστικό φάσμα απόκρισης για το σεισμό της Αθήνας (ATH39901) με μέγιστη φασματική επιτάχυνση {max_show_T:.2f} m/s², σύμφωνα με την συνιστώσα T, και σύγκρισή του με τα φάσματα απόκρισης του Ε.Α.Κ.2000 και του EC8')


elif choice == 'Εκτελέστε ένα από τα διαθέσιμα επιταχυνσιογραφήματα' and epitax == "Θεσσαλονίκη, Ελλάδα (1978) - THEA7802":
    st.write('Σύγκριση των Ελαστικών Φασμάτων Απόκρισης του σεισμού με τα αντίστοιχα Ελαστικά Φάσματα Απόκρισης των κανονισμών')
    x1 = [0, T1('C')] + [T1('C'), T2('C')] + \
        list(np.linspace(T2('C'), 4.00, 100))
    y1 = [Fe(T=period, edafos='C', ζ=5, spoudaiothta='II', zoni='Z2')
          for period in x1]

    x2 = [0, TB('C')] + [TB('C'), TC('C')] + list(np.linspace(TC('C'),
                                                              TD('C'), 200)) + list(np.linspace(TD('C'), 4.00, 80))
    y2 = [Se(T=period, edafos='C', ζ=5, spoudaiothta='II', zoni='Z2')
          for period in x2]

    fig = go.Figure()
    fig2 = show_L(pathfilename, motion_step)
    for line in fig2.axes[0].lines:
        fig.add_trace(go.Scatter(x=line.get_xdata(),
                      y=line.get_ydata(), mode='lines', name='ΘΕΣΣΑΛΟΝΙΚΗ'))
    fig.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='Ε.Α.Κ. 2000'))
    fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='EC8'))
    fig.update_layout(xaxis_title='Ιδιοπερίοδος T (sec)',
                      yaxis_title='Επιταχύνσεις (m/s²)')
    st.plotly_chart(fig)
    max_show_L = max(fig2.axes[0].lines[0].get_ydata())
    st.caption(
        f'Οριζόντιο ελαστικό φάσμα απόκρισης για το σεισμό της Θεσσαλονίκης (THEA7802) με μέγιστη φασματική επιτάχυνση {max_show_L:.2f} m/s², σύμφωνα με την συνιστώσα L, και σύγκρισή του με τα φάσματα απόκρισης του Ε.Α.Κ.2000 και του EC8')

    fig3 = go.Figure()
    fig4 = show_T(pathfilename, motion_step)
    for line in fig4.axes[0].lines:
        fig3.add_trace(go.Scatter(x=line.get_xdata(),
                       y=line.get_ydata(), mode='lines', name='ΚΟΖΑΝΗ'))
    fig3.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='Ε.Α.Κ. 2000'))
    fig3.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='EC8'))
    fig3.update_layout(xaxis_title='Ιδιοπερίοδος T (sec)',
                       yaxis_title='Επιταχύνσεις (m/s²)')
    st.plotly_chart(fig3)
    max_show_T = max(fig4.axes[0].lines[0].get_ydata())
    st.caption(
        f'Οριζόντιο ελαστικό φάσμα απόκρισης για το σεισμό της Θεσσαλονίκης (THEA7802) με μέγιστη φασματική επιτάχυνση {max_show_T:.2f} m/s², σύμφωνα με την συνιστώσα T, και σύγκρισή του με τα φάσματα απόκρισης του Ε.Α.Κ.2000 και του EC8')

elif choice == 'Εκτελέστε ένα από τα διαθέσιμα επιταχυνσιογραφήματα' and epitax == "Καλαμάτα, Ελλάδα (1986) - KAL18601":
    st.write('Σύγκριση των Ελαστικών Φασμάτων Απόκρισης του σεισμού με τα αντίστοιχα Ελαστικά Φάσματα Απόκρισης των κανονισμών')
    x1 = [0, T1('B')] + [T1('B'), T2('B')] + \
        list(np.linspace(T2('B'), 4.00, 100))
    y1 = [Fe(T=period, edafos='B', ζ=5, spoudaiothta='II', zoni='Z3')
          for period in x1]

    x2 = [0, TB('B')] + [TB('B'), TC('B')] + list(np.linspace(TC('B'),
                                                              TD('B'), 200)) + list(np.linspace(TD('B'), 4.00, 80))
    y2 = [Se(T=period, edafos='B', ζ=5, spoudaiothta='II', zoni='Z2')
          for period in x2]

    fig = go.Figure()
    fig2 = show_L(pathfilename, motion_step)
    for line in fig2.axes[0].lines:
        fig.add_trace(go.Scatter(x=line.get_xdata(),
                      y=line.get_ydata(), mode='lines', name='ΚΑΛΑΜΑΤΑ'))
    fig.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='Ε.Α.Κ. 2000'))
    fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='EC8'))
    fig.update_layout(xaxis_title='Ιδιοπερίοδος T (sec)',
                      yaxis_title='Επιταχύνσεις (m/s²)')
    st.plotly_chart(fig)
    max_show_L = max(fig2.axes[0].lines[0].get_ydata())
    st.caption(
        f'Οριζόντιο ελαστικό φάσμα απόκρισης για το σεισμό της Καλαμάτας (KAL18601) με μέγιστη φασματική επιτάχυνση {max_show_L:.2f} m/s², σύμφωνα με την συνιστώσα L, και σύγκρισή του με τα φάσματα απόκρισης του Ε.Α.Κ.2000 και του EC8')

    fig3 = go.Figure()
    fig4 = show_T(pathfilename, motion_step)
    for line in fig4.axes[0].lines:
        fig3.add_trace(go.Scatter(x=line.get_xdata(),
                       y=line.get_ydata(), mode='lines', name='ΚΟΖΑΝΗ'))
    fig3.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='Ε.Α.Κ. 2000'))
    fig3.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='EC8'))
    fig3.update_layout(xaxis_title='Ιδιοπερίοδος T (sec)',
                       yaxis_title='Επιταχύνσεις (m/s²)')
    st.plotly_chart(fig3)
    max_show_T = max(fig4.axes[0].lines[0].get_ydata())
    st.caption(
        f'Οριζόντιο ελαστικό φάσμα απόκρισης για το σεισμό της Καλαμάτας (KAL18601) με μέγιστη φασματική επιτάχυνση {max_show_T:.2f} m/s², σύμφωνα με την συνιστώσα T, και σύγκρισή του με τα φάσματα απόκρισης του Ε.Α.Κ.2000 και του EC8')

elif choice == 'Εκτελέστε ένα από τα διαθέσιμα επιταχυνσιογραφήματα' and epitax == "Κοζάνη, Ελλάδα (1995) - KRR19501":
    st.write('Σύγκριση των Ελαστικών Φασμάτων Απόκρισης του σεισμού με τα αντίστοιχα Ελαστικά Φάσματα Απόκρισης των κανονισμών')
    x1 = [0, T1('B')] + [T1('B'), T2('B')] + \
        list(np.linspace(T2('B'), 4.00, 100))
    y1 = [Fe(T=period, edafos='B', ζ=5, spoudaiothta='II', zoni='Z2')
          for period in x1]

    x2 = [0, TB('B')] + [TB('B'), TC('B')] + list(np.linspace(TC('B'),
                                                              TD('B'), 200)) + list(np.linspace(TD('B'), 4.00, 80))
    y2 = [Se(T=period, edafos='B', ζ=5, spoudaiothta='I', zoni='Z2')
          for period in x2]

    fig = go.Figure()
    fig2 = show_L(pathfilename, motion_step)
    for line in fig2.axes[0].lines:
        fig.add_trace(go.Scatter(x=line.get_xdata(),
                      y=line.get_ydata(), mode='lines', name='ΚΟΖΑΝΗ'))
    fig.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='Ε.Α.Κ. 2000'))
    fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='EC8'))
    fig.update_layout(xaxis_title='Ιδιοπερίοδος T (sec)',
                      yaxis_title='Επιταχύνσεις (m/s²)')
    st.plotly_chart(fig)
    max_show_L = max(fig2.axes[0].lines[0].get_ydata())
    st.caption(
        f'Οριζόντιο ελαστικό φάσμα απόκρισης για το σεισμό της Κοζάνης (KRR19501) με μέγιστη φασματική επιτάχυνση {max_show_L:.2f} m/s², σύμφωνα με την συνιστώσα L, και σύγκρισή του με τα φάσματα απόκρισης του Ε.Α.Κ.2000 και του EC8')

    fig3 = go.Figure()
    fig4 = show_T(pathfilename, motion_step)
    for line in fig4.axes[0].lines:
        fig3.add_trace(go.Scatter(x=line.get_xdata(),
                       y=line.get_ydata(), mode='lines', name='ΚΟΖΑΝΗ'))
    fig3.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='Ε.Α.Κ. 2000'))
    fig3.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='EC8'))
    fig3.update_layout(xaxis_title='Ιδιοπερίοδος T (sec)',
                       yaxis_title='Επιταχύνσεις (m/s²)')
    st.plotly_chart(fig3)
    max_show_T = max(fig4.axes[0].lines[0].get_ydata())
    st.caption(
        f'Οριζόντιο ελαστικό φάσμα απόκρισης για το σεισμό της Κοζάνης (KRR19501) με μέγιστη φασματική επιτάχυνση {max_show_T:.2f} m/s², σύμφωνα με την συνιστώσα T, και σύγκρισή του με τα φάσματα απόκρισης του Ε.Α.Κ.2000 και του EC8')
