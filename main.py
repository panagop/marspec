import streamlit as st



st.set_page_config(
    page_title="ΦΑΣΜΑΤΑ",
    page_icon="👷🏻‍♀️",
)



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
st.markdown('<style>h2{color: blue;}</style>', unsafe_allow_html=True)
st.markdown(f'<font color="{custom_color}" size="6" class="centered"><h2><u>ΦΑΣΜΑΤΑ</u></h2></font>', unsafe_allow_html=True)

st.success("Επιλέξτε ποιο κανονισμό θέλετε να εκτελέσετε από το μενού επιλογών.")
st.write('')
st.markdown('<div class="centered"><h6>Πληροφορίες για τους κανονισμούς</h6></div>', unsafe_allow_html=True)



with st.expander("Ελληνικός Αντισεισμικός Κανονισμός 2000"):
  st.write("")
  eak_url = 'img/eak.png'
  st.image(eak_url,caption = 'Σχήμα 1 : Διαγραμματική απεικόνιση του Ε.Α.Κ. 2000', use_container_width=True)
  
  eak = st.button(label="Τυπική μορφή Φάσματος Σχεδιασμού κατά τον Ε.Α.Κ. 2000")
  if eak:
   eakfd_url = 'img/eak_fd.png'
   st.image(eakfd_url, caption = 'Σχήμα 2 : Τυπική μορφή Φάσματος Σχεδιασμού', use_container_width=True)
  
  col1, col2 = st.columns(2)
  with col1:
    eak_syn1 = st.button(label="Εξισώσεις που ορίζουν το Φάσμα Σχεδιασμού κατά τον Ε.Α.Κ. 2000")
    if eak_syn1:        
        st.latex(r'0 \leq T < T_1\ : \ Φ_d(T) = A \cdot \gamma_1 \cdot \left[1 + \frac{T}{T_1} \left(\frac{\eta \cdot \theta \cdot \beta_0}{q} - 1\right)\right]')
        st.latex(r'T_1 \leq T \leq T_2 \ : \ Φ_d(T) = A \cdot \gamma_1 \cdot \frac{\eta \cdot \theta \cdot \beta_0}{q}')
        st.latex(r'T_2 < T \ : \ Φ_d(T) = A \cdot \gamma_1 \cdot \left[\frac{\eta \cdot \theta \cdot \beta_0}{q} \cdot \left(\frac{T_2}{T}\right)^{\frac{2}{3}} \right]')
  with col2:
      eak_syn2 = st.button(label="Εξισώσεις που ορίζουν το Ελαστικό Φάσμα Απόκρισης κατά τον Ε.Α.Κ. 2000")
      if eak_syn2:
         st.latex(r'0 \leq T < T_1\ : \ Φ_e(T) = A \cdot \gamma_1 \cdot \left[1 + (\eta \cdot \beta_0  - 1) \cdot \frac{T}{T_1}\right]')
         st.latex(r'T_1 \leq T \leq T_2 \ : \ Φ_e(T) = A \cdot \gamma_1 \cdot \eta \cdot \beta_0')
         st.latex(r'T_2 < T \ : \ Φ_e(T) = A \cdot \gamma_1 \cdot \eta \cdot \beta_0 \cdot \frac{T_2}{T}')


with st.expander("Ευρωκώδικας 8: Αντισεισμικός Σχεδιασμός Κατασκευών"):
  st.write("")

  ec8_url = 'img/ec8.png'
  st.image(ec8_url, caption = 'Σχήμα 3 : Διαγραμματική απεικόνιση του Ευρωκώδικα 8', use_container_width=True)

  ec8 = st.button(label="Τυπική μορφή ελαστικού φάσματος απόκρισης κατά τον Ευρωκώδικα 8")
  if ec8:
   eakse_url = 'img/ec8_se.png'
   st.image(eakse_url, caption = 'Σχήμα 4 : Τυπική μορφή Ελαστικού Φάσματος Απόκρισης', use_container_width=True)
    
  col1, col2 = st.columns(2)
  with col1:
    ec8_syn1 = st.button(label="Εξισώσεις που ορίζουν το Φάσμα Σχεδιασμού κατά τον Ευρωκώδικα 8")
    if ec8_syn1:
      st.latex(r'0 \leq T \leq T_B \ : \ S_d(T) = a_g \cdot \ S \cdot \left[\frac{2}{3} + \frac{T}{T_B} \cdot \left(\frac{2.50}{q} - \frac{2}{3}\right)\right]')
      st.latex(r'T_B \leq T \leq T_C \ : \ S_d(T) = a_g \cdot \ S \cdot \frac{2.50}{q}')
      st.latex(r'T_C \leq T \leq T_D \ : \ S_d(T) = a_g \cdot \ S \cdot \frac{2.50}{q} \cdot \frac{T_C}{T}')
      st.latex(r'T_D \leq T \leq 4 \ sec \ : \ S_d(T) = a_g \cdot \ S \cdot \frac{2.50}{q} \cdot \frac{T_C \cdot \ T_D}{T^2}')
  with col2:
      ec8_syn2 = st.button(label="Εξισώσεις που ορίζουν το Ελαστικό Φάσμα Απόκρισης κατά τον Ευρωκώδικα 8")
      if ec8_syn2:  
         st.latex(r'0 \leq T \leq T_B \ : \ S_e(T) = a_g \cdot \ S \cdot \left[1 + \frac{T}{T_B}\cdot \ (\eta \cdot 2.50 - 1)\right]')
         st.latex(r'T_B \leq T \leq T_C \ : \ S_e(T) = a_g \cdot \ S \cdot \eta \cdot 2.50')
         st.latex(r'T_C \leq T \leq T_D \ : \ S_e(T) = a_g \cdot \ S \cdot \eta \cdot 2.50 \cdot \frac{T_C}{T}')
         st.latex(r'T_D \leq T \leq 4 \ sec \ : \ S_e(T) = a_g \cdot \ S \cdot \eta \cdot 2.50 \cdot \frac{T_C \cdot \ T_D}{T^2}')


with st.expander("Αναθεωρημένος Ευρωκώδικας 8"):
  st.write("")
  
  revec8_url = 'img/revec8.png'
  st.image(revec8_url,  caption = 'Σχήμα 5 : Διαγραμματική απεικόνιση του αναθεωρημένου Ευρωκώδικα 8', use_container_width=True)
  
  revec8 = st.button(label="Τυπική μορφή ελαστικού φάσματος απόκρισης κατά τον αναθεωρημένο Ευρωκώδικα 8")
  if revec8:
   revec8se_url = 'img/revec8_se.png'
   st.image(revec8se_url, caption = 'Σχήμα 6 : Τυπική μορφή Φάσματος Σχεδιασμού', use_container_width=True)
    
  col1, col2 = st.columns(2)
  with col1:
    revec8_syn = st.button(label="Εξισώσεις που ορίζουν το Ελαστικό Φάσμα Απόκρισης κατά τον Αναθεωρημένο Ευρωκώδικα 8")
    if revec8_syn:
      st.latex(r'0 \leq T \leq T_A \ : \ S_e(T) = \frac{S_a}{F_A}')
      st.latex(r'T_A \leq T \leq T_B \ : \ S_e(T) = \frac{S_a}{T_B - T_A}  \cdot  \left[ \eta \cdot \ (T - T_A) + \frac{T_B - T}{F_A} \right]')
      st.latex(r'T_B \leq T \leq T_C \ : \ S_e(T) = \eta \cdot S_a')
      st.latex(r'T_C \leq T \leq T_D \ : \ S_e(T) = \eta \cdot  \frac{S_\beta \cdot \ T_\beta}{T} ')
      st.latex(r'T_D \leq T \ : \ S_e(T) = \eta \cdot T_D \cdot \frac{S_\beta \cdot T_\beta}{T^2} ')
