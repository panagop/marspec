import streamlit as st
from streamlit.elements import markdown
from funcs.ec8funcs import TB, TC, TD, S, agR, γ1, h, Sd, Se, agR
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(
    page_title="EC8",)

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
st.markdown(f'<font color="{custom_color}" size="6" class="centered"><h2><u>ΦΑΣΜΑΤΑ ΚΑΤΑ EC8</u></h2></font>', unsafe_allow_html=True)

text = """

- More information on streamlit [here](https://docs.streamlit.io/)

"""
#ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ
#ΤΥΠΟΣ ΕΔΑΦΟΥΣ
st.sidebar.markdown('#####  ΚΑΤΗΓΟΡΙΑ ΕΔΑΦΟΥΣ')
edafos = st.sidebar.selectbox(
     "Ποια είναι η κατηγορία εδάφους;",
     ("A", "B", "C" , "D", "E"),
     index=0,
     placeholder="Επέλεξε την κατηγορία εδάφους",)

ed1_url = 'img/ec8_ed1.jpg'

with st.sidebar.expander("Πίνακας 1 : Τιμές χαρακτηριστικών περιόδων και συντελεστή εδάφους"):
       st.image(ed1_url,
                use_container_width=True)

ed_url = 'img/ec8_ed.png'

with st.sidebar.expander("Πίνακας 2 : Κατηγορίες εδάφους"):
       st.image(ed_url,
                use_container_width=True)
  
#ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ
st.sidebar.markdown('##### ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ')
zoni = st.sidebar.selectbox(
     "Ποια είναι η ζώνη επικινδυνότητας;",
     ("Z1", "Z2", "Z3" ),
     index=0,
     placeholder="Επέλεξε την ζώνη επικινδυνότητας",)

a_url = 'img/ec8_a.jpg'

with st.sidebar.expander("Πίνακας 3 : Τιμές $a_{gR}$ / $g$ "):
       st.image(a_url,
                use_container_width=True)
xart_url = 'img/ec8_xartis.png'
with st.sidebar.expander("Σχήμα 1 : Χάρτης Σεισμικής Επικινδυνότητας της Ελλάδος"):
           st.image(xart_url,
                    use_container_width=True)
   
#ΚΑΤΗΓΟΡΙΑ ΣΠΟΥΔΑΙΟΤΗΤΑΣ
st.sidebar.markdown('##### ΚΑΤΗΓΟΡΙΑ ΣΠΟΥΔΑΙΟΤΗΤΑΣ')
spoudaiothta = st.sidebar.selectbox(
       "Ποια είναι η κατηγορία σπουδαιότητας;",
       ("I", "II", "III" , "IV"),
       index=1,
       placeholder="Επέλεξε την κατηγορία σπουδαιότητας",)

g1_url = 'img/ec8_g1.png'

with st.sidebar.expander("Πίνακας 4 : Συντελεστές σπουδαιότητας $γ_1$"):
       st.image(g1_url,
                use_container_width=True)
  
#ΣΥΝΤ. ΣΥΜΠΕΡΙΦΟΡΑΣ q
st.sidebar.markdown('##### ΤΙΜΗ ΣΥΝΤΕΛΕΣΤΗ ΣΥΜΠΕΡΙΦΟΡΑΣ $q$')
q = st.sidebar.number_input('Ποια είναι η τιμή του συντελεστή συμπεριφοράς $q$;', value=3.9, placeholder="Πληκτρολόγησε την τιμή...") 

q_url = 'img/ec8_q.jpg'
aua1_url = 'img/ec8_aua1.jpg'

with st.sidebar.expander("Πίνακας 5 : Συντελεστές συμπεριφοράς $q$"):
 st.image(q_url,
           caption='με βάση το είδος του δομικού συστήματος και τις προσεγγιστικές τιμές γα το λόγο αu/α1',
           use_container_width=True)
with st.sidebar.expander("Πίνακας 6 : Τιμές λόγου $α_u$ / $α_1$"):
 st.image(aua1_url,
           use_container_width=True)
                         
#ΠΟΣΟΣΤΟ ΑΠΟΣΒΕΣΗΣ ζ 
st.sidebar.markdown('##### ΤΙΜΗ ΠΟΣΟΣΤΟΥ ΑΠΟΣΒΕΣΗΣ $ζ$%')
ζ = st.sidebar.number_input('Ποια είναι η τιμή του ποσοστού απόσβεσης $ζ$%;', value=5, placeholder="Πληκτρολόγησε την τιμή...")  

#ΤΙΜΗ ΙΔΙΟΠΕΡΙΟΔΟΥ Τ
#st.success('###### ΤΙΜΗ ΙΔΙΟΠΕΡΙΟΔΟΥ $Τ$')
T = st.number_input('Ποια είναι η τιμή της Ιδιοπεριόδου $Τ$ ; ', value=0.4, placeholder="Πληκτρολόγησε την τιμή...") 
st.write('Η τιμή της ιδιοπεριόδου $Τ$ είναι: ', T,'sec')

st.write('')
st.write('')

#ΠΡΟΒΟΛΗ ΔΕΔΟΜΕΝΩΝ
apotelesmata = st.button(label="ΥΠΟΛΟΓΙΣΜΟΣ ΠΑΡΑΜΕΤΡΩΝ")
if apotelesmata :
 with st.expander("###### Προβολή Δεδομένων και Υπολογισμός Παραμέτρων"):
    #ΕΔΑΦΟΣ
   st.write('‣ Επέλεξες κατηγορία εδάφους :', edafos)
   st.write('Η τιμή του $T_B$ είναι : ',TB(edafos),'sec')
   st.write('Η τιμή του $Τ_C$ είναι : ',TC(edafos), 'sec')
   st.write('Η τιμή του $Τ_D$ είναι : ',TD(edafos),'sec')
   st.write('Η τιμή του συντελεστή εδάφους $S$ είναι : ',S(edafos))
   st.write('')
   st.write('')
    #ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ
   st.write('‣ Επέλεξες ζώνη επικινδυνότητας :', zoni)
   st.write('Η τιμή της μέγιστης σεισμικής επιτάχυνσης εδάφους $α_{gR}$ είναι :', agR(zoni),'m/s²')
   st.write('')
   st.write('')
    #ΚΑΤΗΓΟΡΙΑ ΣΠΟΥΔΑΙΟΤΗΤΑΣ
   st.write('‣ Επέλεξες κατηγορία σπουδαιότητας :', spoudaiothta)
   st.write('Η τιμή του συντελεστή σπουδαιότητας $γ_1$ είναι :',γ1(spoudaiothta))
   st.write('')
   st.write('')
    #ΣΥΝΤΕΛΕΣΤΗΣ ΣΥΜΠΕΡΙΦΟΡΑΣ q
   st.write("Η τιμή του συντελεστή συμπεριφοράς $q$ είναι" , q)
   st.write('')
    #ΠΟΣΟΣΤΟ ΑΠΟΣΒΕΣΗΣ ζ
   st.write("Η τιμή του ποσοστού απόσβεσης $ζ$ είναι" , ζ,"%")
   st.write('Ο διορθωτικός συντελεστής για ποσοστό απόσβεσης', ζ,'% είναι', h(ζ))


st.write('')
st.write('')
col1, col2 = st.columns(2)
with col1:
#ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ ΚΑΤΑ EC8
 st.success('###### Ελαστική επιτάχυνση $S_e$')
 st.write('Η ελαστική επιτάχυνση $S_e$ για ιδιοπερίοδο $Τ$ =', T,'sec, κατά EC8, ισούται με', round(Se(T, edafos, spoudaiothta, zoni, ζ),2), 'm/s².')
with col2:
#ΦΑΣΜΑ ΣΧΕΔΙΑΣΜΟΥ ΚΑΤΑ EC8
 st.success('###### Φασματική επιτάχυνση σχεδιασμού $S_d$')
 st.write('Η φασματική επιτάχυνση $S_d$ για ιδιοπερίοδο $Τ$ =' ,T ,'sec, κατά EC8, ισούται με', round(Sd(T, edafos, spoudaiothta, zoni, q),2),' m/s².')


st.write('')
st.write('')
st.write('')


#ΔΙΑΓΡΑΜΜΑΤΑ

my_custom_color = "#6495ED"

text_in_frame = f'<font color="{my_custom_color}" size="5" class="centered">ΔΙΑΓΡΑΜΜΑΤΑ</font>'
st.markdown(f'<div style="border:1px solid #000000; padding: 10px">{text_in_frame}</div>', unsafe_allow_html=True)

#ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ
x = [0, TB(edafos)] + [TB(edafos), TC(edafos)] + list(np.linspace(TC(edafos), TD(edafos),200)) + list(np.linspace(TD(edafos), 4.00, 80))
y = [Se(T=period, edafos=edafos, ζ=ζ, spoudaiothta=spoudaiothta, zoni=zoni) for period in x]

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y, mode='lines', name='ΟΡΙΖ. ΕΛΑΣΤΙΚΟ ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ'))

fig1.update_xaxes(tickvals=[TB(edafos), TC(edafos), TD(edafos),T] + list(np.arange(0, 4.1, 0.5)), ticktext=[f'<span style="color:black;">TB={TB(edafos)}', f'<span style="color:black;">TC={TC(edafos)}', f'<span style="color:black;">TD={TD(edafos)}', f'<span style="color:red;">T={T}'] + [f'{val:.1f}' for val in np.arange(0, 4.1, 0.5)],tickangle=90)
y_max = max(y)
fig1.update_yaxes(tickvals=[Se(T=T,edafos=edafos, ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni)] + list(np.arange(0, y_max + 1, 0.1)), ticktext=[f'<span style="color:red;">Se={Se(T=T,edafos=edafos, ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni):.4f}'] + [f'{val:.1f}' for val in np.arange(0, y_max + 1, 0.1)])

T_marked = T 
Sd_marked = Se(T=T_marked,ζ=ζ, edafos=edafos, spoudaiothta=spoudaiothta, zoni=zoni) 
fig1.add_trace(go.Scatter(x=[T_marked], y=[Sd_marked], mode='markers', marker=dict(color='red'), name='Ελαστική επιτάχ. για Τ'))

fig1.update_layout(title='<span style="color:(light_blue);">ΟΡΙΖΟΝΤΙΟ ΕΛΑΣΤΙΚΟ ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ ΚΑΤΑ EC8', xaxis_title='Τ (sec)', yaxis_title='Se(T) (m/s²)')

fig1.add_shape(type="line",
  x0=TB(edafos), y0=0,
  x1=TB(edafos), y1=Se(T=TB(edafos),ζ=ζ, edafos=edafos, spoudaiothta=spoudaiothta, zoni=zoni),
  line=dict(color="grey", width=2, dash="dash"),)
fig1.add_shape(type="line",
  x0=TC(edafos), y0=0,
  x1=TC(edafos), y1=Se(T=TC(edafos),ζ=ζ, edafos=edafos, spoudaiothta=spoudaiothta, zoni=zoni),
  line=dict(color="grey", width=2, dash="dash"),)
fig1.add_shape(type="line",
  x0=TD(edafos), y0=0,
  x1=TD(edafos), y1=Se(T=TD(edafos),ζ=ζ, edafos=edafos, spoudaiothta=spoudaiothta, zoni=zoni),
  line=dict(color="grey", width=2, dash="dash"),)

fig1.add_shape(type="line",
  x0=T, y0=0,        x1=T,y1=Se(T=T,edafos=edafos, ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),
   line=dict(color="pink", width=2, dash="dash"))
fig1.add_shape(type="line",
  x0=0, y0=Se(T=T,edafos=edafos, ζ=ζ,spoudaiothta=spoudaiothta,zoni=zoni),        x1=T,y1=Se(T=T,edafos=edafos, ζ=ζ, spoudaiothta=spoudaiothta,zoni=zoni),
   line=dict(color="pink", width=2, dash="dash"))

st.plotly_chart(fig1)


#ΦΑΣΜΑ ΣΧΕΔΙΑΣΜΟΥ 
x = [0, TB(edafos)] + [TB(edafos), TC(edafos)] + list(np.linspace(TC(edafos), TD(edafos))) + list(np.linspace(TD(edafos), 4.00, 100))
y = [Sd(T=period, edafos=edafos,q=q, spoudaiothta=spoudaiothta, zoni=zoni) for period in x]

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x, y=y, mode='lines', name='ΦΑΣΜΑ ΣΧΕΔΙΑΣΜΟΥ'))
y_max = max(y)

fig2.update_xaxes(tickvals=[TB(edafos), TC(edafos), TD(edafos),T] + list(np.arange(0, 4.1, 0.5)), ticktext=[f'<span style="color:black;">TB={TB(edafos)}', f'<span style="color:black;">TC={TC(edafos)}', f'<span style="color:black;">TD={TD(edafos)}', f'<span style="color:red;">T={T}'] + [f'{val:.1f}' for val in np.arange(0, 4.1, 0.5)],tickangle=90)

fig2.update_yaxes(tickvals=[Sd(T=T,edafos=edafos,q=q,spoudaiothta=spoudaiothta,zoni=zoni)] + list(np.arange(0, y_max + 1, 0.1)), ticktext=[f'<span style="color:red;">Sd={Sd(T=T,edafos=edafos,q=q,spoudaiothta=spoudaiothta,zoni=zoni):.4f}'] + [f'{val:.1f}' for val in np.arange(0, y_max + 1, 0.1)])

T_marked = T 
Sd_marked = Sd(T=T_marked,q=q, edafos=edafos, spoudaiothta=spoudaiothta, zoni=zoni) 
fig2.add_trace(go.Scatter(x=[T_marked], y=[Sd_marked], mode='markers', marker=dict(color='red'), name='Επιτάχ. σχεδιασμού για Τ'))

fig2.update_layout(title='ΦΑΣΜΑ ΣΧΕΔΙΑΣΜΟΥ ΚΑΤΑ EC8',
                   xaxis_title='Τ (sec)',
                   yaxis_title='Sd(T) (m/s²)')

fig2.add_shape(type="line",
    x0=TB(edafos), y0=0,
    x1=TB(edafos), y1=Sd(T=TB(edafos),q=q, edafos=edafos, spoudaiothta=spoudaiothta, zoni=zoni),
    line=dict(color="grey", width=2, dash="dash"),)
fig2.add_shape(type="line",
  x0=TC(edafos), y0=0,
  x1=TC(edafos), y1=Sd(T=TC(edafos),q=q, edafos=edafos, spoudaiothta=spoudaiothta, zoni=zoni),
  line=dict(color="grey", width=2, dash="dash"),)
fig2.add_shape(type="line",
  x0=TD(edafos), y0=0,
  x1=TD(edafos), y1=Sd(T=TD(edafos),q=q, edafos=edafos, spoudaiothta=spoudaiothta, zoni=zoni),
  line=dict(color="grey", width=2, dash="dash"),)

fig2.add_shape(type="line",
  x0=T, y0=0,        x1=T,y1=Sd(T=T,edafos=edafos,q=q,spoudaiothta=spoudaiothta,zoni=zoni),
   line=dict(color="pink", width=2, dash="dash"))
fig2.add_shape(type="line",
  x0=0, y0=Sd(T=T,edafos=edafos,q=q,spoudaiothta=spoudaiothta,zoni=zoni),        x1=T,y1=Sd(T=T,edafos=edafos,q=q,spoudaiothta=spoudaiothta,zoni=zoni),
   line=dict(color="pink", width=2, dash="dash"))


st.plotly_chart(fig2)