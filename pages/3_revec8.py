import streamlit as st
from streamlit.elements import markdown
from funcs.revec8funcs import topog, γLS_CC, Sα475, Sβ475, Sα_ref, levels, fh, Sβ_ref, Sα_RP, Sβ_RP, FT, pga, ra, Fα1, Fα2, Fa_cho,rb , Fβ1, Fβ2, Fb_cho, Sα1, Sα2, Sa_cho, Sβ1, Sβ2, Sb_cho, TC, TB, TA, TD, h, Se
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


st.set_page_config(
    page_title="REVISED EC8",)

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
st.markdown(f'<font color="{custom_color}" size="6" class="centered"><h2><u>ΦΑΣΜΑΤΑ ΚΑΤΑ REVISED EC8</u></h2></font>', unsafe_allow_html=True)

text = """

- More information on streamlit [here](https://docs.streamlit.io/)

"""

#ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ
#ΤΥΠΟΣ ΕΔΑΦΟΥΣ
st.sidebar.markdown('#####  ΚΑΤΗΓΟΡΙΑ ΕΔΑΦΟΥΣ')
edafos = st.sidebar.selectbox(
     "Ποια είναι η κατηγορία εδάφους;",
     ("A", "B", "C", "D", "E", "F"),
     index=0,
     placeholder="Επέλεξε την κατηγορία εδάφους",)

ed_url = 'img/revec8_ed.jpg'

with st.sidebar.expander("Πίνακας 1 : Κατηγορίες εδάφους "):
        st.image(ed_url,use_container_width=True)
  

#ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ
st.sidebar.markdown('##### ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ')
zoni = st.sidebar.selectbox(
     "Ποια είναι η ζώνη επικινδυνότητας;",
     ("Z1", "Z2", "Z3", "Z4"),
     index=0,
     placeholder="Επέλεξε την ζώνη επικινδυνότητας",)

pga_url = 'img/revec8_pga.jpg' 

with st.sidebar.expander("Πίνακας 2 : Tιμές μέγιστης σεισμικής επιτάχυνσης εδάφους $PGA$, της μέγιστης φασματικής επιτάχυνσης $S_{α,475}$ και της φασματικής επιτάχυνσης $S_{β,475}$ στο 1 sec"):
         st.image(pga_url,use_container_width=True)

map_url = 'img/revec8_map.png'
with st.sidebar.expander("Σχήμα 1: Χάρτης Σεισμικής Επικινδυνότητας της Ελλάδος "):
   st.image(map_url, use_container_width=True)

lev_url = 'img/revec8_lev.jpg' 

with st.sidebar.expander("Πίνακας 3 : Εύρος τιμών της φασματικής επιτάχυνσης $S_{α,475}$, για τον καθορισμό των επιπέδων σεισμικότητας"):
            st.image(lev_url,use_container_width=True)
   
sa_url = 'img/revec8_mapsa.png'
with st.sidebar.expander("Σχήμα 2: Χωρική κατανομή της μέγιστης φασματικής επιτάχυνσης $S_{α,475}$, για εδαφικές συνθήκες βράχου και περίοδο επαναφοράς 475 έτη"):
   st.image(sa_url, use_container_width=True)


#ΠΕΡΙΓΡΑΦΗ ΤΟΠΟΓΡΑΦΙΑΣ
st.sidebar.markdown('##### ΠΕΡΙΓΡΑΦΗ ΤΟΠΟΓΡΑΦΙΑΣ')
topo = st.sidebar.selectbox("Επιλέξετε την τοπογραφία του εδάφους",
                            ("a", "b", "c", "d"),
                            index=0,)

ft_url = 'img/revec8_ft.jpg'

with st.sidebar.expander("Πίνακας 4 : Συντελεστές ενίσχυσης τοπογραφίας $F_T$ για τοπογραφικές ανωμαλίες "):
      st.image(ft_url,
               use_container_width=True)
   
fafb_url = 'img/revec8_fafb.jpg'

with st.sidebar.expander("Πίνακας 5 : Τιμές συντελεστών ενίσχυσης $F_α$ και $F_β$ "):
      st.image(fafb_url,use_container_width=True)

#ΚΑΤΗΓΟΡΙΑ ΣΥΝΕΠΕΙΑΣ
st.sidebar.markdown('##### ΚΑΤΗΓΟΡΙΑ ΣΥΝΕΠΕΙΑΣ')
con_class = st.sidebar.selectbox("Επιλέξετε την κατηγορία συνέπειας",
                                 ("CC1", "CC2", "CC3-a", "CC3-b"),
                                 index=0,)
with st.sidebar.expander("Πίνακας 6 :  "):
   st.write('')
#ΟΡΙΑΚΗ ΚΑΤΑΣΤΑΣΗ
st.sidebar.markdown('##### ΟΡΙΑΚΗ ΚΑΤΑΣΤΑΣΗ')
limit = st.sidebar.selectbox('Επιλέξετε την οριακή κατάσταση',
                            ("nc","sd", "dl"),
                            index=0,)    
with st.sidebar.expander("Πίνακας 7 : Κατηγορίες Οριακών Καταστάσεων"):
 st.write('')

g_url = 'img/revec8_g.jpg'

with st.sidebar.expander("Πίνακας 8 : Τιμές συντελεστή απόδοσης κτιρίων $γ_{LS,CC}$"):
      st.image(g_url,
               use_container_width=True)


#ΠΟΣΟΣΤΟ ΑΠΟΣΒΕΣΗΣ ζ
st.sidebar.markdown('##### ΤΙΜΗ ΠΟΣΟΣΤΟΥ ΑΠΟΣΒΕΣΗΣ $ζ$ %')
ζ = st.sidebar.number_input('Ποια είναι η τιμή του ποσοστού απόσβεσης $ζ$ %;', value=5, 
                            placeholder="Πληκτρολόγησε την τιμή...") 

#vs H για Fα ,Fβ
choice = st.sidebar.radio(label='Είναι διαθέσιμες η ταχύτητα διάδοσης των διατμητικών κυμάτων $v_{s,H}$ και το βάθος $H$ ;',
options=['Ναι', 'Όχι'],
index=1)
if choice == 'Ναι':
     vs = st.sidebar.number_input('Ποια είναι η τιμή της ταχύτητας διάδοσης των διατμητικών κυμάτων $v_{s,H}$;', value=30, 
  placeholder="Πληκτρολόγησε την τιμή...")
     H = st.sidebar.number_input('Ποια είναι η τιμή του βάθους $H$;', value=800, 
 placeholder="Πληκτρολόγησε την τιμή...")
elif choice == 'Όχι':
     vs = None
     H = None
  
xTB = st.sidebar.number_input('Πληκτρογήστε την τιμή της παραμέτρου $χ$, σύμφωνα με την οποία ορίζεται η τιμή της ιδιοπεριόδου $Τ_Β$', value=4.00, 
  placeholder="Πληκτρολόγησε την τιμή...")

#ΤΙΜΗ ΙΔΙΟΠΕΡΙΟΔΟΥ Τ
#st.success('###### ΤΙΜΗ ΙΔΙΟΠΕΡΙΟΔΟΥ Τ')
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
#ΧΑΡΑΚΤΗΡΙΣΤΙΚΟΙ ΠΕΡΙΟΔΟΙ
   st.write('Η τιμή του $T_A$ είναι : ',TA ,'sec')
   st.write(f'Η τιμή του $T_B$ είναι :', round(TB(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB),2), ' sec')
   st.write('Η τιμή του $T_C$ είναι : ', round(TC(choice,topo,zoni,limit,con_class,edafos,vs,H),2),'sec')
   st.write('Η τιμή του $T_D$ είναι : ',round(TD(limit, con_class, zoni),2) ,'sec')
   st.write('')
#ΤΟΠΟΓΡΑΦΙΑ ΕΔΑΦΟΥΣ
   st.write('Η τοπογραφία του εδάφους είναι :', topog(topo)) 
   st.write('Ο συντελεστής ενίσχυσης $F_T$, που σχετίζεται με την τοπογραφία του εδάφους, είναι :', FT(topo))
   st.write('Ο συντελεστής εδαφικής ενίσχυσης $F_α$, που αντιστοιχεί σε μικρές περιόδους, είναι :', round(Fa_cho(choice,edafos,vs,H,limit,con_class,zoni),2)) 
   st.write('Ο συντελεστής εδαφικής ενίσχυσης $F_β$, που αντιστοιχεί σε ενδιάμεσες περιόδους, είναι :', round(Fb_cho(choice,edafos,vs,H,limit,con_class,zoni),2))
   st.write('')
#ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ
   st.write('‣ Επέλεξες ζώνη επικινδυνότητας :', zoni)
   st.write('Η τιμή της μέγιστης σεισμικής επιτάχυνσης εδάφους $PGA$ είναι :', pga(zoni),'m/s²')
   st.write('To επίπεδο σεισμικότητας είναι : ', levels(zoni)) 
   st.write('Η τιμή της φασματικής επιτάχυνσης $S_{α,475}$ είναι', Sα475(zoni),'m/s². Η τιμή της φασματικής επιτάχυνσης $S_{β,475}$, για $Τ_β$ = 1 sec, είναι ', Sβ475(zoni),'m/s².')
   st.write('Η τιμή της φασματικής επιτάχυνσης $S_{α,ref}$ είναι', Sα_ref(zoni), 'm/s². Η τιμή της φασματικής επιτάχυνσης $S_{β,ref}$ είναι', round(Sβ_ref(zoni),2), 'm/s².')
   st.write('Η τιμή της φασματικής επιτάχυνσης $S_{α,RP}$ είναι',
            round(Sα_RP(limit,con_class,zoni),2),'m/s². Η τιμή της φασματικής επιτάχυνσης $S_{β,RP}$ είναι',
            round(Sβ_RP(limit,con_class,zoni),2), 'm/s².')
   st.write('')
   st.write('')
   st.write('Η τιμή της μέγιστης φασματικής επιτάχυνσης $S_α$, που αντιστοιχεί στον σταθερό κλάδο επιτάχυνσης, είναι :', round(Sa_cho(choice,topo,zoni,limit,con_class,edafos,vs,H),2), 'm/s²')
   st.write('Η τιμή της φασματικής επιτάχυνσης $S_β$, που αντιστοιχεί σε περίοδο ταλαντωσης $Τ_β$ = 1 sec, είναι :', round(Sb_cho(choice,topo,zoni,limit,con_class,edafos,vs,H),2),'m/s²')
   st.write('')
#ΣΥΝΤ. ΑΠΟΔΟΣΗΣ γ
   st.write('Η τιμη του συντελεστή απόδοσης κτιρίων $γ_{LS,CC}$ είναι :', γLS_CC(limit, con_class))
   st.write('')
#ΠΟΣΟΣΤΟ ΑΠΟΣΒΕΣΗΣ      
   st.write("Η τιμή του ποσοστού απόσβεσης $ζ$ είναι" , ζ,"%")
   st.write('Ο διορθωτικός συντελεστής για ποσοστό απόσβεσης', ζ,'% είναι', round(h(ζ,T,choice,topo,zoni,limit,con_class,edafos,vs,H,xTB),2))

st.write('')
st.write('')
#ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ ΚΑΤΑ EC8
st.success('###### Ελαστική επιτάχυνση $S_e$')
st.write('Η ελαστική επιτάχυνση $S_e$ για ιδιοπερίοδο $Τ$ =', (T),'sec, κατά τον αναθεωρημένο EC8, ισούται με', round(Se(T,choice,topo,zoni,limit,con_class,edafos,vs,H,ζ,xTB),2),' m/s².')

st.write('')
st.write('')
st.write('')

#ΔΙΑΓΡΑΜΜΑΤΑ

my_custom_color = "#6495ED"

text_in_frame = f'<font color="{my_custom_color}" size="5" class="centered">ΔΙΑΓΡΑΜΜΑΤΑ</font>'
st.markdown(f'<div style="border:1px solid #000000; padding: 10px">{text_in_frame}</div>', unsafe_allow_html=True)


#ΟΡΙΖΟΝΤΙΟ ΕΛΑΣΤΙΚΟ ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ 
Tβ=1.00
x = [0, TA] + [TB(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB),
               TC(choice,topo,zoni,limit,con_class,edafos,vs,H)] +list(np.linspace(TC(choice,topo,zoni,limit,con_class,edafos,vs,H), TD(limit,con_class,zoni))) + list(np.linspace(TD(limit,con_class,zoni), 3.0, 80))

y = [Se(T=period,choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB) for period in x]

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y, mode='lines', name='ΟΡΙΖ. ΕΛΑΣΤΙΚΟ ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ'))

fig1.update_xaxes(tickvals=[TB(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB), 
                            TC(choice,topo,zoni,limit,con_class,edafos,vs,H),
                           TD(limit,con_class,zoni),TA,T,Tβ] + list(np.arange(0, 4.1, 0.5)),ticktext=[f'<span style="color:black;">TB={TB(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB)}',
                            f'<span style="color:black;">TC={TC(choice,topo,zoni,limit,con_class,edafos,vs,H)}',
                                                                     f'<span style="color:black;">TD={TD(limit,con_class,zoni)}',
                                                                          f'<span style="color:black;">TA={TA}',f'<span style="color:red;">T={T}',f'Tβ={Tβ}'] + [f'{val:.1f}' for val in np.arange(0, 4.1, 0.5)],tickangle = 90)
y_max = max(y)
fig1.update_yaxes(tickvals=[Se(T=T,choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),Sa_cho(choice=choice,topo=topo,edafos=edafos,vs=vs,H=H,limit=limit,con_class=con_class,zoni=zoni),Sb_cho(choice=choice,topo=topo,edafos=edafos,vs=vs,H=H,limit=limit,con_class=con_class,zoni=zoni),Se(T=0,choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB)] + list(np.arange(0, y_max + 1, 0.1)),
                  ticktext=[f'<span style="color:red;">Se={Se(T=T,choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB):.2f}',f'<span style="color:green;">Sα', f'<span style="color:green;">Sβ',f'<span style="color:green;">Sα/Fα']  + [f'{val:.1f}' for val in np.arange(0, y_max + 1, 0.1)])

T_marked = T 
Se_marked = Se(T=T,choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB) 
fig1.add_trace(go.Scatter(x=[T_marked], y=[Se_marked], mode='markers', marker=dict(color='red'), name='Ελαστική επιτάχ. για Τ'))

Sa_marked = Sa_cho(choice=choice,topo=topo,edafos=edafos,vs=vs,H=H,limit=limit,con_class=con_class,zoni=zoni)
fig1.add_trace(go.Scatter(x=[TB(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB)],y=[Sa_marked], mode='markers', marker=dict(color='green'), name='Sα'))
Sb_marked = Sb_cho(choice=choice,topo=topo,edafos=edafos,vs=vs,H=H,limit=limit,con_class=con_class,zoni=zoni)
fig1.add_trace(go.Scatter(x=[Tβ],y=[Sb_marked], mode='markers', marker=dict(color='green'), name='Sβ'))


fig1.update_layout(title='ΟΡΙΖΟΝΤΙΟ ΕΛΑΣΤΙΚΟ ΦΑΣΜΑ ΚΑΤΑ REV EC8',
                   xaxis_title='Τ (sec)',
                   yaxis_title='Se(T)(m/s²)')

fig1.add_shape(type="line",
              x0=TA, y0=0,        x1=TA,y1=Se(T=TA,choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),
               line=dict(color="grey", width=2, dash="dash"))

fig1.add_shape(type="line",
  x0=TB(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB), y0=0,        x1=TB(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB),y1=Se(T=TB(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB),choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),
   line=dict(color="grey", width=2, dash="dash"))

fig1.add_shape(type="line",
  x0=TC(choice,topo,zoni,limit,con_class,edafos,vs,H), y0=0,        x1=TC(choice,topo,zoni,limit,con_class,edafos,vs,H),y1=Se(T=TC(choice,topo,zoni,limit,con_class,edafos,vs,H),choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),
   line=dict(color="grey", width=2, dash="dash"))

fig1.add_shape(type="line",
  x0=TD(limit,con_class,zoni), y0=0,        x1=TD(limit,con_class,zoni),y1=Se(T=TD(limit,con_class,zoni),choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),
   line=dict(color="grey", width=2, dash="dash"))


fig1.add_shape(type="line",
  x0=T, y0=0,        x1=T,y1=Se(T,choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),
   line=dict(color="pink", width=2, dash="dash"))
fig1.add_shape(type="line",
  x0=0, y0=Se(T,choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),        x1=T,y1=Se(T,choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),
   line=dict(color="pink", width=2, dash="dash"))



st.plotly_chart(fig1)
