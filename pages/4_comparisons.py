import streamlit as st
from funcs.eak2000funcs import T1, T2, A, γ1, h, Fd, Fe
from funcs.ec8funcs import TB, TC, TD, S, agR, γ1, h, Sd, Se, agR
from funcs.revec8funcs import topog, γLS_CC, Sα475, Sβ475, Sα_ref, levels, fh, Sβ_ref, Sα_RP, Sβ_RP, FT, pga, ra, Fα1, Fα2, Fa_cho,rb , Fβ1, Fβ2, Fb_cho, Sα1, Sα2, Sa_cho, Sβ1, Sβ2, Sb_cho, TA, h
from funcs.revec8funcs import TB as TB_rev
from funcs.revec8funcs import TC as TC_rev
from funcs.revec8funcs import TD as TD_rev
from funcs.revec8funcs import Se as Se_rev
from plotly.subplots import make_subplots
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go




st.set_page_config(
    page_title="COMPARISONS",)

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
st.markdown(f'<font color="{custom_color}" size="6" class="centered"><h2><u>ΣΥΓΚΡΙΣΗ ΕΛΑΣΤΙΚΩΝ ΦΑΣΜΑΤΩΝ ΑΠΟΚΡΙΣΗΣ</u></h2></font>', unsafe_allow_html=True)

#TΙΜΗ ΙΔΙΟΠΕΡΙΟΔΟΥ Τ
with st.expander("Τιμή της Ιδιοπεριόδου $Τ$"):
 T = st.number_input('Ποια είναι η τιμή της Ιδιοπεριόδου $Τ$;',
                    value=0.4,
                    placeholder="Πληκτρολόγησε την τιμή...")
 st.write('Η τιμή της ιδιοπεριόδου $Τ$ είναι: ', T, 'sec')

st.write('')
st.markdown('<div class="centered"><h6>Εισαγωγή δεδομένων</h6></div>', unsafe_allow_html=True)


with st.expander("➤ Ελληνικός Αντισεισμικός Κανονισμός 2000"):
      #ΕΔΑΦΟΣ
    st.markdown('ΚΑΤΗΓΟΡΙΑ ΕΔΑΦΟΥΣ')
    edafos_eak_selectbox = st.selectbox(
         "Ποια είναι η κατηγορία εδάφους;",
         ("A", "B", "C", "D"),
         index=0,
         placeholder="Επέλεξε την κατηγορία εδάφους",
    key='selectbox1')
    edafos_eak = edafos_eak_selectbox

      #ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ
    st.markdown('ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ')
    zoni_eak_selectbox = st.selectbox(
         "Ποια είναι η ζώνη επικινδυνότητας;",
         ("Z1", "Z2", "Z3", "Z4"),
         index=0,
         placeholder="Επέλεξε την ζώνη επικινδυνότητας",
    key='selectbox2')
    zoni_eak = zoni_eak_selectbox
    

      #ΚΑΤΗΓΟΡΙΑ ΣΠΟΥΔΑΙΟΤΗΤΑΣ
    st.markdown('ΚΑΤΗΓΟΡΙΑ ΣΠΟΥΔΑΙΟΤΗΤΑΣ')
    spoudaiothta_eak_selectbox = st.selectbox(
        "Ποια είναι η κατηγορία σπουδαιότητας;",
        ("I", "II", "III", "IV"),
        index=1,
        placeholder="Επέλεξε την κατηγορία σπουδαιότητας",
    key='selectbox3')
    spoudaiothta_eak = spoudaiothta_eak_selectbox
    
      #ΤΙΜΗ ΣΥΝΤΕΛΕΣΤΗ ΣΥΜΠΕΡΙΦΟΡΑΣ q
    st.markdown('ΤΙΜΗ ΣΥΝΤΕΛΕΣΤΗ ΣΥΜΠΕΡΙΦΟΡΑΣ $q$')
    q_eak_numinput = st.number_input('Ποια είναι η τιμή του συντελεστή συμπεριφοράς $q$;',
     value=3.50,
     placeholder="Πληκτρολόγησε την τιμή...",
                                    key='input1')
    q_eak = q_eak_numinput
 
      #ΤΙΜΗ ΣΥΝΤΕΛΕΣΤΗ ΘΕΜΕΛΙΩΣΗΣ Θ
    st.markdown('ΤΙΜΗ ΣΥΝΤΕΛΕΣΤΗ ΘΕΜΕΛΙΩΣΗΣ $θ$')
    θ_eak_slider = st.slider('Ποια είναι η τιμή του συντελεστή θεμελίωσης $θ$;',
           min_value=0.80,
           max_value=1.00,
                   value=1.00,
           step=0.10,
                        key='slider1')
    θ_eak = θ_eak_slider

      #ΤΙΜΗ ΠΟΣΟΣΤΟΥ ΑΠΟΣΒΕΣΗΣ ζ
    st.markdown('ΤΙΜΗ ΠΟΣΟΣΤΟΥ ΑΠΟΣΒΕΣΗΣ $ζ$ %')
    ζ_eak_numinput = st.number_input('Ποια είναι η τιμή του ποσοστού απόσβεσης $ζ$ %;',
           value=5.00,
           placeholder="Πληκτρολόγησε την τιμή...",
                    key='input2')
    ζ_eak = ζ_eak_numinput

    



with st.expander("➤ Ευρωκώδικας 8: Αντισεισμικός Σχεδιασμός Κατασκευών"):
    #ΤΥΠΟΣ ΕΔΑΦΟΥΣ
    st.markdown('ΚΑΤΗΓΟΡΙΑ ΕΔΑΦΟΥΣ')
    edafos_ec8_selectbox = st.selectbox(
             "Ποια είναι η κατηγορία εδάφους;",
             ("A", "B", "C" , "D", "E"),
             index=0,
             placeholder="Επέλεξε την κατηγορία εδάφους",
    key='selectbox4')
    edafos_ec8 = edafos_ec8_selectbox
  
    #ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ
    st.markdown('ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ')
    zoni_ec8_selectbox = st.selectbox(
             "Ποια είναι η ζώνη επικινδυνότητας;",
             ("Z1", "Z2", "Z3" ),
             index=0,
             placeholder="Επέλεξε την ζώνη επικινδυνότητας",
    key='selectbox5')
    zoni_ec8 = zoni_ec8_selectbox

    #ΚΑΤΗΓΟΡΙΑ ΣΠΟΥΔΑΙΟΤΗΤΑΣ
    st.markdown('ΚΑΤΗΓΟΡΙΑ ΣΠΟΥΔΑΙΟΤΗΤΑΣ')
    spoudaiothta_ec8_selectbox = st.selectbox(
        "Ποια είναι η κατηγορία σπουδαιότητας;",
        ("I", "II", "III" , "IV"),
        index=1,
        placeholder="Επέλεξε την κατηγορία σπουδαιότητας",
    key='selectbox6')
    spoudaiothta_ec8 = spoudaiothta_ec8_selectbox

        #ΣΥΝΤ. ΣΥΜΠΕΡΙΦΟΡΑΣ q
    st.markdown('ΤΙΜΗ ΣΥΝΤΕΛΕΣΤΗ ΣΥΜΠΕΡΙΦΟΡΑΣ $q$')
    q_ec8_numinput = st.number_input('Ποια είναι η τιμή του συντελεστή συμπεριφοράς $q$;', value=3.90, placeholder="Πληκτρολόγησε την τιμή...",
        key='input3')
    q_ec8 = q_ec8_numinput
    
    #ΠΟΣΟΣΤΟ ΑΠΟΣΒΕΣΗΣ ζ 
    st.markdown('ΤΙΜΗ ΠΟΣΟΣΤΟΥ ΑΠΟΣΒΕΣΗΣ $ζ$%')
    ζ_ec8_numinput = st.number_input('Ποια είναι η τιμή του ποσοστού απόσβεσης $ζ$%;', value=5.00, placeholder="Πληκτρολόγησε την τιμή...",
                                     key='input4')  
    ζ_ec8 = ζ_ec8_numinput

   


with st.expander("➤ Αναθεωρημένος Ευρωκώδικας 8"):
    #ΤΥΠΟΣ ΕΔΑΦΟΥΣ
    st.markdown('ΚΑΤΗΓΟΡΙΑ ΕΔΑΦΟΥΣ')
    edafos = st.selectbox(
         "Ποια είναι η κατηγορία εδάφους;",
         ("A", "B", "C", "D", "E", "F"),
         index=0,
         placeholder="Επέλεξε την κατηγορία εδάφους",
    key='selectbox7')

    #ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ
    st.markdown('ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ')
    zoni = st.selectbox(
         "Ποια είναι η ζώνη επικινδυνότητας;",
         ("Z1", "Z2", "Z3", "Z4"),
         index=0,
         placeholder="Επέλεξε την ζώνη επικινδυνότητας",
    key='selectbox8')

    #ΠΕΡΙΓΡΑΦΗ ΤΟΠΟΓΡΑΦΙΑΣ
    st.markdown('ΠΕΡΙΓΡΑΦΗ ΤΟΠΟΓΡΑΦΙΑΣ')
    topo = st.selectbox("Επιλέξετε την τοπογραφία του εδάφους",
                                ("a", "b", "c", "d"),
                                index=0,
                       key='selectbox9')

    #ΚΑΤΗΓΟΡΙΑ ΣΥΝΕΠΕΙΑΣ
    st.markdown('ΚΑΤΗΓΟΡΙΑ ΣΥΝΕΠΕΙΑΣ')
    con_class = st.selectbox("Επιλέξετε την κατηγορία συνέπειας",
                                     ("CC1", "CC2", "CC3-a", "CC3-b"),
                                     index=0,
                            key='selectbox10')
    #ΟΡΙΑΚΗ ΚΑΤΑΣΤΑΣΗ
    st.markdown('ΟΡΙΑΚΗ ΚΑΤΑΣΤΑΣΗ')
    limit = st.selectbox('Επιλέξετε την οριακή κατάσταση',
                                ("nc","sd", "dl"),
                                index=0,
                        key='selectbox11')                                 
    #ΠΟΣΟΣΤΟ ΑΠΟΣΒΕΣΗΣ ζ
    st.markdown('ΤΙΜΗ ΠΟΣΟΣΤΟΥ ΑΠΟΣΒΕΣΗΣ $ζ$ %')
    ζ = st.number_input('Ποια είναι η τιμή του ποσοστού απόσβεσης $ζ$ %;', value=5, 
                                placeholder="Πληκτρολόγησε την τιμή...",
                       key='input5') 

    #vs H για Fα ,Fβ
    choice = st.radio(label='Είναι διαθέσιμες η ταχύτητα διάδοσης των διατμητικών κυμάτων $v_{s,H}$ και το βάθος $H$ ;',
    options=['Ναι', 'Όχι'],
    index=1)
    if choice == 'Ναι':
         vs = st.number_input('Ποια είναι η τιμή της ταχύτητας διάδοσης των διατμητικών κυμάτων $v_{s,H}$;', value=30, 
      placeholder="Πληκτρολόγησε την τιμή...",
                             key='input6')
         H = st.number_input('Ποια είναι η τιμή του βάθους $H$;', value=800, 
     placeholder="Πληκτρολόγησε την τιμή...",
                            key='input7')
    elif choice == 'Όχι':
         vs = None
         H = None

    xTB = st.number_input('Πληκτρογήστε την τιμή της παραμέτρου $χ$, σύμφωνα με την οποία ορίζεται η τιμή της ιδιοπεριόδου $Τ_Β$', value=4.00, 
      placeholder="Πληκτρολόγησε την τιμή...",
                         key='input7')

    







#ΔΙΑΓΡΑΜΜΑ

#EAK2000
x1 = [0, T1(edafos_eak)] + [T1(edafos_eak), T2(edafos_eak)] + list(np.linspace(T2(edafos_eak), 4.00, 100))
y1 = [Fe(T=period, edafos=edafos_eak, ζ=ζ_eak, spoudaiothta=spoudaiothta_eak, zoni=zoni_eak) for period in x1]

#EC8
x2 = [0, TB(edafos_ec8)] + [TB(edafos_ec8), TC(edafos_ec8)] + list(np.linspace(TC(edafos_ec8), TD(edafos_ec8),200)) + list(np.linspace(TD(edafos_ec8), 4.00, 100))
y2 = [Se(T=period, edafos=edafos_ec8, ζ=ζ_ec8, spoudaiothta=spoudaiothta_ec8, zoni=zoni_ec8) for period in x2]

#REV EC8
Tβ=1.00

x3 = [0, TA] + [TB_rev(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB),                 TC_rev(choice,topo,zoni,limit,con_class,edafos,vs,H)] +list(np.linspace(TC_rev(choice,topo,zoni,limit,con_class,edafos,vs,H), TD_rev(limit,con_class,zoni))) + list(np.linspace(TD_rev(limit,con_class,zoni), 4.0, 100))

y3 = [Se_rev(T=period,choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB) for period in x3]


fig = go.Figure()
fig.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='Ε.Α.Κ.2000', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines' ,name='EC8',line=dict(color='red')))
fig.add_trace(go.Scatter(x=x3, y=y3, mode='lines', name='rev EC8',line=dict(color='green')))

fig.update_layout(title='ΟΡΙΖΟΝΤΙΟ ΕΛΑΣΤΙΚΟ ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ', xaxis_title='Ιδιοπερίοδος T (sec)', yaxis_title='Επιταχύνσεις Φe(T), Se(T), Se(T) (m/s²)', 
                  legend_title='Αντισεισμικοί Κανονισμοί')

# fig.add_shape(type="line",
#               x0=T1(edafos_eak), y0=0,  x1=T1(edafos_eak),y1=Fe(T=T1(edafos_eak),edafos=edafos_eak,ζ=ζ_eak,spoudaiothta=spoudaiothta_eak,zoni=zoni_eak), line=dict(color="grey", width=2, dash="dash"),)
# fig.add_shape(type="line",
#   x0=T2(edafos_eak), y0=0,
#   x1=T2(edafos_eak), y1=Fe(T=T2(edafos_eak),edafos=edafos_eak,ζ=ζ_eak,spoudaiothta=spoudaiothta_eak,zoni=zoni_eak),
#   line=dict(color="grey", width=2, dash="dash"),)



# fig.add_shape(type="line",
#   x0=TB(edafos_ec8), y0=0,
#   x1=TB(edafos_ec8), y1=Se(T=TB(edafos_ec8),ζ=ζ_ec8, edafos=edafos_ec8, spoudaiothta=spoudaiothta_ec8, zoni=zoni_ec8),
#   line=dict(color="grey", width=2, dash="dash"),)
# fig.add_shape(type="line",
#   x0=TC(edafos_ec8), y0=0,
#   x1=TC(edafos_ec8), y1=Se(T=TC(edafos_ec8),ζ=ζ_ec8, edafos=edafos_ec8, spoudaiothta=spoudaiothta_ec8, zoni=zoni_ec8),
#   line=dict(color="grey", width=2, dash="dash"),)
# fig.add_shape(type="line",
#   x0=TD(edafos_ec8), y0=0,
#   x1=TD(edafos_ec8), y1=Se(T=TD(edafos_ec8),ζ=ζ_ec8, edafos=edafos_ec8, spoudaiothta=spoudaiothta_ec8, zoni=zoni_ec8),
#   line=dict(color="grey", width=2, dash="dash"),)


# fig.add_shape(type="line",
#       x0=TA, y0=0,        x1=TA,y1=Se_rev(T=TA,choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),
#        line=dict(color="grey", width=2, dash="dash"))

# fig.add_shape(type="line",
# x0=TB_rev(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB), y0=0,        x1=TB_rev(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB),y1=Se_rev(T=TB_rev(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB),choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),
# line=dict(color="grey", width=2, dash="dash"))

# fig.add_shape(type="line",
# x0=TC_rev(choice,topo,zoni,limit,con_class,edafos,vs,H), y0=0,        x1=TC_rev(choice,topo,zoni,limit,con_class,edafos,vs,H),y1=Se_rev(T=TC_rev(choice,topo,zoni,limit,con_class,edafos,vs,H),choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),
# line=dict(color="grey", width=2, dash="dash"))

# fig.add_shape(type="line",
# x0=TD_rev(limit,con_class,zoni), y0=0,        x1=TD_rev(limit,con_class,zoni),y1=Se_rev(T=TD_rev(limit,con_class,zoni),choice=choice,topo=topo,zoni=zoni,limit=limit,con_class=con_class,edafos=edafos,vs=vs,H=H,ζ=ζ,xTB=xTB),
#  line=dict(color="grey", width=2, dash="dash"))



# fig.update_xaxes(tickvals=[T1(edafos_eak), T2(edafos_eak), TB(edafos_ec8), TC(edafos_ec8), TD(edafos_ec8), TB_rev(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB),
#                            TC_rev(choice,topo,zoni,limit,con_class,edafos,vs,H),
#                            TD_rev(limit,con_class,zoni),TA] + list(np.arange(0, 4.1, 0.5)),
#                  ticktext=[f'T1={T1(edafos_eak)}',
#                            f'T2= {T2(edafos_eak)}',f'TB={TB(edafos_ec8)}', f'TC={TC(edafos_ec8)}', f'TD={TD(edafos_ec8)}'f'TB={TB_rev(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB)}',
#                            f'TC={TC_rev(choice,topo,zoni,limit,con_class,edafos,vs,H)}',                                             f'TD={TD_rev(limit,con_class,zoni)}',                                                  f'TA={TA}'] + [f'{val:.2f}' for val in np.arange(0, 4.1, 0.5)],
#                  tickangle=90)

fig.update_xaxes(tickvals=list(np.arange(0, 4.1, 0.5)),
                 ticktext=[f'{val:.2f}' for val in np.arange(0, 4.1, 0.5)],
                 tickangle=90)


st.plotly_chart(fig)


st.write(f'<span style="color:blue; font-size: smaller">Οριζόντιο ελαστικό φάσμα απόκρισης για κατηγορία εδάφους {edafos_eak}, ζώνη {zoni_eak} και κατηγορία σπουδαιότητας {spoudaiothta_eak}.</span>', unsafe_allow_html=True)

st.write(f'<span style="color:red; font-size: smaller">Οριζόντιο ελαστικό φάσμα απόκρισης για κατηγορία εδάφους {edafos_ec8}, ζώνη {zoni_ec8} και κατηγορία σπουδαιότητας {spoudaiothta_ec8}.</span>', unsafe_allow_html=True)

st.write(f'<span style="color:green; font-size: smaller">Οριζόντιο ελαστικό φάσμα απόκρισης για κατηγορία εδάφους {edafos}, ζώνη {zoni} και κατηγορία σπουδαιότητας {con_class}.</span>', unsafe_allow_html=True)
