import streamlit as st
from funcs.eak2000funcs import T1, T2, A, γ1, h, Fd, Fe
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


st.set_page_config(
    page_title="Ε.Α.Κ. 2000",
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
st.markdown(f'<font color="{custom_color}" size="6" class="centered"><h2><u>ΦΑΣΜΑΤΑ ΚΑΤΑ Ε.Α.Κ. 2000</u></h2></font>', unsafe_allow_html=True)
text = """

- More information on streamlit [here](https://docs.streamlit.io/)

"""

#ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ

#ΕΔΑΦΟΣ
st.sidebar.markdown('##### ΚΑΤΗΓΟΡΙΑ ΕΔΑΦΟΥΣ')
edafos = st.sidebar.selectbox(
    "Ποια είναι η κατηγορία εδάφους;",
    ("A", "B", "C", "D"),
    index=0,
    placeholder="Επέλεξε την κατηγορία εδάφους",)

ed1_url = 'img/eak_ed1.jpg'
ed2_url = 'img/eak_ed2.jpg'

with st.sidebar.expander("Πίνακας 1 : Τιμές των χαρακτηριστικών περιόδων $Τ_1$, $Τ_2$ (sec)"):
     st.image(ed1_url,
              use_container_width=True)
with st.sidebar.expander("Πίνακας 2 : Κατηγορίες εδάφους"):
     st.image(ed2_url,
              use_container_width=True)
    
#ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ
st.sidebar.markdown('##### ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ')
zoni = st.sidebar.selectbox(
    "Ποια είναι η ζώνη επικινδυνότητας;",
    ("Z1", "Z2", "Z3", "Z4"),
    index=0,
    placeholder="Επέλεξε την ζώνη επικινδυνότητας",)

a_url = 'img/eak_a.jpg'

with st.sidebar.expander("Πίνακας 3 : Σεισμική επιτάχυνση εδάφους $Α$ = $α$ ⋅ $g$"):
       st.image(a_url,
             caption='όπου g επιτάχυνση βαρύτητας',
             use_container_width=True)
xartis_url = 'img/eak_xartis.png'
with st.sidebar.expander("Σχήμα 1 : Χάρτης Σεισμικής Επικινδυνότητας της Ελλάδος (έως το 2003)"):
          st.image(xartis_url,
                   use_container_width=True)
#ΚΑΤΗΓΟΡΙΑ ΣΠΟΥΔΑΙΟΤΗΤΑΣ
st.sidebar.markdown('##### ΚΑΤΗΓΟΡΙΑ ΣΠΟΥΔΑΙΟΤΗΤΑΣ')
spoudaiothta = st.sidebar.selectbox(
    "Ποια είναι η κατηγορία σπουδαιότητας;",
    ("I", "II", "III", "IV"),
    index=1,
    placeholder="Επέλεξε την κατηγορία σπουδαιότητας",)

g1_url = 'img/eak_g1.jpg'
with st.sidebar.expander("Πίνακας 4 : Συντελεστές σπουδαιότητας $γ_1$"):
         st.image(g1_url,
                  use_container_width=True)
    
#ΤΙΜΗ ΣΥΝΤΕΛΕΣΤΗ ΣΥΜΠΕΡΙΦΟΡΑΣ q
st.sidebar.markdown('##### ΤΙΜΗ ΣΥΝΤΕΛΕΣΤΗ ΣΥΜΠΕΡΙΦΟΡΑΣ $q$')
q = st.sidebar.number_input('Ποια είναι η τιμή του συντελεστή συμπεριφοράς $q$;',
value=3.5,
placeholder="Πληκτρολόγησε την τιμή...")

q_url = 'img/eak_q.jpg'

with st.sidebar.expander("Πίνακας 5 : Μέγιστες τιμές συντελεστή συμπεριφοράς $q$ "):
     st.image(q_url,
              use_container_width=True)
    
#ΤΙΜΗ ΣΥΝΤΕΛΕΣΤΗ ΘΕΜΕΛΙΩΣΗΣ Θ
st.sidebar.markdown('##### ΤΙΜΗ ΣΥΝΤΕΛΕΣΤΗ ΘΕΜΕΛΙΩΣΗΣ $θ$')
θ = st.sidebar.slider('Ποια είναι η τιμή του συντελεστή θεμελίωσης $θ$;',
              min_value=0.80,
              max_value=1.00,
                      value=1.00,
              step=0.10)

th_url = 'img/eak_th.jpg'

with st.sidebar.expander("Πίνακας 6 : Συντελεστής θεμελίωσης $θ$"):
     st.image(th_url, use_container_width=True)
    
#ΤΙΜΗ ΠΟΣΟΣΤΟΥ ΑΠΟΣΒΕΣΗΣ ζ
st.sidebar.markdown('##### ΤΙΜΗ ΠΟΣΟΣΤΟΥ ΑΠΟΣΒΕΣΗΣ $ζ$ %')
ζ = st.sidebar.number_input('Ποια είναι η τιμή του ποσοστού απόσβεσης $ζ$ %;',
                      value=5.00,
                      placeholder="Πληκτρολόγησε την τιμή...")

z_url = 'img/eak_z.jpg'

with st.sidebar.expander("Πίνακας 7 : Τιμές ποσοστού απόσβεσης $ζ$ % "):
     st.image(z_url, use_container_width=True)


#ΤΙΜΗ ΙΔΙΟΠΕΡΙΟΔΟΥ Τ
#st.success('###### ΤΙΜΗ ΙΔΙΟΠΕΡΙΟΔΟΥ $Τ$')
T = st.number_input('Ποια είναι η τιμή της Ιδιοπεριόδου $Τ$;',
                    value=0.4,
                    placeholder="Πληκτρολόγησε την τιμή...")
st.write('Η τιμή της ιδιοπεριόδου $Τ$ είναι: ', T, 'sec')


st.write('')
st.write('')
#ΠΡΟΒΟΛΗ ΔΕΔΟΜΕΝΩΝ
apotelesmata = st.button(label="ΥΠΟΛΟΓΙΣΜΟΣ ΠΑΡΑΜΕΤΡΩΝ")
if apotelesmata :
 with st.expander("###### Προβολή Δεδομένων και Υπολογισμός Παραμέτρων"):
    #ΕΔΑΦΟΣ
   st.write('‣ Επέλεξες κατηγορία εδάφους :', edafos)
   st.write('Η τιμή του $Τ_1$ είναι : ', T1(edafos), 'sec')
   st.write('Η τιμή του $Τ_2$ είναι : ', T2(edafos), 'sec')
   st.write('')
   st.write('')
    #ΖΩΝΗ ΣΕΙΣΜ. ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ
   st.write('‣ Επέλεξες ζώνη επικινδυνότητας :', zoni)
   st.write('Η τιμή της μέγιστης οριζόντιας σεισμικής επιτάχυνσης εδάφους $Α$ είναι :', A(zoni),'m/s²')
   st.write('')
   st.write('')
    #ΚΑΤ. ΣΠΟΥΔΑΙΟΤΗΤΑΣ
   st.write('‣ Επέλεξες κατηγορία σπουδαιότητας :', spoudaiothta)
   st.write('Η τιμή του συντελεστή σπουδαιότητας $γ_1$ είναι :', γ1(spoudaiothta))
   st.write('')
   st.write('')
    #ΣΥΝΤ. ΣΥΜΠΕΡΙΦ. q
   st.write("Η τιμή του συντελεστή συμπεριφοράς $q$ είναι", q)
   st.write('')
    #ΣΥΝΤ. ΘΕΜ. θ
   st.write("Η τιμή του συντελεστή επιρροής της θεμελίωσης $θ$ είναι", θ)
   st.write('')
    #ΠΟΣΟΣΤ. ΑΠΟΣΒΕΣΗΣ ζ
   st.write("Η τιμή του ποσοστού απόσβεσης $ζ$ είναι", ζ,'%')
   st.write('Ο διορθωτικός συντελεστής για ποσοστό απόσβεσης', ζ, '% είναι', round(h(ζ),2))




st.write('')
st.write('')
col1, col2 = st.columns(2)
with col1:
#ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ ΚΑΤΑ ΕΑΚ 2000
 st.success('###### Ελαστική επιτάχυνση $Φ_e$')
 st.write('Η ελαστική επιτάχυνση $Φ_e$ για ιδιοπερίοδο $Τ$ =',T ,'sec, κατά τον Ε.Α.Κ. 2000, ισούται με', round(Fe(T, edafos, spoudaiothta, zoni, ζ),2),'m/s².')
with col2:
#ΦΑΣΜΑ ΣΧΕΔΙΑΣΜΟΥ ΚΑΤΑ ΕΑΚ 2000
 st.success('###### Φασματική επιτάχυνση σχεδιασμού $Φ_d$')
 st.write('Η φασματική επιτάχυνση σχεδιασμού $Φ_d$ για ιδιοπερίοδο $Τ$ =',T ,'sec, κατά τον Ε.Α.Κ. 2000, ισούται με', round(Fd(T,edafos,spoudaiothta,zoni,q,ζ,θ),2) ,' m/s².')


st.write('')
st.write('')
st.write('')

#ΔΙΑΓΡΑΜΜΑΤΑ

my_custom_color = "#6495ED"

text_in_frame = f'<font color="{my_custom_color}" size="5" class="centered">ΔΙΑΓΡΑΜΜΑΤΑ</font>'
st.markdown(f'<div style="border:1px solid #000000; padding: 10px">{text_in_frame}</div>', unsafe_allow_html=True)

#ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ
x = [0, T1(edafos)] + [T1(edafos), T2(edafos)] + list(np.linspace(T2(edafos), 4.00, 100))
y = [Fe(T=period, edafos=edafos, ζ=ζ, spoudaiothta=spoudaiothta, zoni=zoni)
    for period in x]

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y, mode='lines', name='ΟΡΙΖ. ΕΛΑΣΤΙΚΟ ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ'))

fig1.update_xaxes(
    tickvals=[T1(edafos), T2(edafos), T] + list(np.arange(0, 4.1, 0.5)), 
    ticktext=[
        f'<span style="color:black;">T1={T1(edafos)}', 
        f'<span style="color:black;">T2= {T2(edafos)}', 
        f'<span style="color:red;">T= {T}'
    ] + [f'{val:.1f}' for val in np.arange(0, 4.1, 0.5)],
    tickangle=90
)
y_max = max(y)
fig1.update_yaxes(tickvals=[Fe(T=T,edafos=edafos,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),] + list(np.arange(0, y_max + 1, 0.5)), ticktext=[f'<span style="color:red;">Φe={Fe(T=T,edafos=edafos,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni):.4f}'] + [f'{val:.1f}' for val in np.arange(0, y_max + 1, 0.5)])

T_marked = T 
Fe_marked = Fe(T=T_marked, edafos=edafos, ζ=ζ, spoudaiothta=spoudaiothta, zoni=zoni) 
fig1.add_trace(go.Scatter(x=[T_marked], y=[Fe_marked], mode='markers', marker=dict(color='red'), name='Ελαστική επιτάχ. για Τ'))

fig1.add_shape(type="line",
  x0=T1(edafos), y0=0,
  x1=T1(edafos), y1=Fe(T=T1(edafos),edafos=edafos,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),
  line=dict(color="grey", width=2, dash="dash"),)
fig1.add_shape(type="line",
  x0=T2(edafos), y0=0,
  x1=T2(edafos), y1=Fe(T=T2(edafos),edafos=edafos,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),
  line=dict(color="grey", width=2, dash="dash"),)


fig1.add_shape(type="line",
  x0=T, y0=0, 
   x1=T,y1=Fe(T=T,edafos=edafos,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),
   line=dict(color="pink", width=2, dash="dash"))
fig1.add_shape(type="line",
  x0=0, y0=Fe(T=T,edafos=edafos,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni), 
  x1=T,y1=Fe(T=T,edafos=edafos,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),
   line=dict(color="pink", width=2, dash="dash"))

fig1.update_layout(title='ΟΡΙΖΟΝΤΙΟ ΕΛΑΣΤΙΚΟ ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ ΚΑΤΑ ΤΟΝ Ε.Α.Κ. 2000',
                   xaxis_title='Τ (sec)',
                   yaxis_title='Φe(T) (m/s²)') 

st.plotly_chart(fig1)

#ΦΑΣΜΑ ΣΧΕΔΙΑΣΜΟΥ
x = [0, T1(edafos)] + [T1(edafos), T2(edafos)] + list(np.linspace(T2(edafos), 4.00, 100))
y = [Fd(T=period,
       edafos=edafos,
       q=q,
       θ=θ,
       ζ=ζ,
       spoudaiothta=spoudaiothta,
       zoni=zoni) for period in x]

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x, y=y, mode='lines', name='ΦΑΣΜΑ ΣΧΕΔΙΑΣΜΟΥ'))

fig2.update_xaxes(tickvals=[T1(edafos), T2(edafos), T]  + list(np.arange(0, 4.1, 0.5)),
                  ticktext=[f'<span style="color:black;">T1={T1(edafos)}',f'<span style="color:black;">T2= {T2(edafos)}',f'<span style="color:red;">T= {T}'] + [f'{val:.1f}' for val in np.arange(0, 4.1, 0.5)],
                  tickangle=90)
y_max = max(y)
fig2.update_yaxes(tickvals=[Fd(T=T,edafos=edafos,q=q,θ=θ,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni)]  + list(np.arange(0, y_max + 1, 0.5)), ticktext=[f'<span style="color:red;">Φd={Fd(T=T,edafos=edafos,q=q,θ=θ,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni):.4f}']  + [f'{val:.1f}' for val in np.arange(0, y_max + 1, 0.5)])

T_marked = T 
Fd_marked = Fd(T=T_marked, edafos=edafos, q=q, θ=θ, ζ=ζ, spoudaiothta=spoudaiothta, zoni=zoni) 
fig2.add_trace(go.Scatter(x=[T_marked], y=[Fd_marked], mode='markers', marker=dict(color='red'), name='Επιτάχ. σχεδιασμού για Τ'))
        

fig2.add_shape(type="line",
    x0=T1(edafos), y0=0,
    x1=T1(edafos), y1=Fd(T=T1(edafos),edafos=edafos,q=q,θ=θ,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),
    line=dict(color="grey", width=2, dash="dash"),)
fig2.add_shape(type="line",
  x0=T2(edafos), y0=0,
  x1=T2(edafos), y1=Fd(T=T2(edafos),edafos=edafos,q=q,θ=θ,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),
  line=dict(color="grey", width=2, dash="dash"),)


fig2.add_shape(type="line",
  x0=T, y0=0,        x1=T,y1=Fd(T=T,edafos=edafos,q=q,θ=θ,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),
   line=dict(color="pink", width=2, dash="dash"))
fig2.add_shape(type="line",
  x0=0, y0=Fd(T=T,edafos=edafos,q=q,θ=θ,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),        x1=T,y1=Fd(T=T,edafos=edafos,q=q,θ=θ,ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),
   line=dict(color="pink", width=2, dash="dash"))


fig2.update_layout(title='ΦΑΣΜΑ ΣΧΕΔΙΑΣΜΟΥ ΚΑΤΑ ΤΟΝ Ε.Α.Κ. 2000',
                   xaxis_title='Τ (sec)',
                   yaxis_title='Φd(T) (m/s²)')

st.plotly_chart(fig2)