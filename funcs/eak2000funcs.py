#ΤΥΠΟΙ ΕΔΑΦΟΥΣ
def T1(edafos: str) -> float:
  if edafos == "A":
    T1 = 0.10
    return T1
  elif edafos == "B":
    T1 = 0.15
    return T1
  elif edafos == "C":
    T1 = 0.20
    return T1
  elif edafos == "D":
    T1 = 0.20
    return T1
 

def T2(edafos: str) -> float:
  if edafos == "A":
    T2 = 0.40
    return T2
  elif edafos == "B":
    T2 = 0.60
    return T2
  elif edafos == "C":
    T2 = 0.80
    return T2
  elif edafos == "D":
    T2 = 1.20
    return T2
  
#ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ
def A(zoni: str) -> float:
  g=9.80

  if zoni == "Z1":
    α = 0.12
    return α*g
  elif zoni == "Z2":
    α = 0.16
    return α*g
  elif zoni == "Z3":
    α = 0.24
    return α*g
  elif zoni == "Z4":
    α = 0.36
    return α*g


#ΚΑΤΗΓΟΡΙΑ ΣΠΟΥΔΑΙΟΤΗΤΑΣ
def γ1(spoudaiothta: str) -> float:
  if spoudaiothta == "I":
    γ1 = 0.85
    return γ1
  elif spoudaiothta == "II":
    γ1 = 1.00
    return γ1
  elif spoudaiothta == "III":
    γ1 = 1.15
    return γ1
  elif spoudaiothta == "IV":
    γ1 = 1.30
    return γ1
   
#ΔΙΟΡΘΩΤΙΚΟΣ ΣΥΝΤΕΛΕΣΤΗΣ ΓΙΑ ΠΟΣΟΣΤΟ ΑΠΟΣΒΕΣΗΣ
def h(ζ: float) -> float:

  _ζ = ζ
  h=(7/(2 + _ζ))**(1/2)
  return h

#ΦΑΣΜΑ ΣΧΕΔΙΑΣΜΟΥ ΚΑΤΑ ΕΑΚ 2000
def Fd(T: float,
       edafos: str,
       spoudaiothta: str,
       zoni: str ,
       q: float ,
       ζ: float,
       θ: float) -> float:

    _T1 = T1(edafos)
    _T2 = T2(edafos)
    _γ1= γ1(spoudaiothta)
    _A = A(zoni)
    _βο=2.50
    _q=q
    _θ=θ
    _η=h(ζ)
    _ζ=ζ


    if T >= 0 and T <= _T1:
        _Fd = _γ1 * _A * (1 + (T / _T1) * ((_η * _θ * _βο )/_q - 1))     
      
    elif T >= _T1 and T <= _T2:
        _Fd = _γ1 * _A * ((_η * _θ * _βο )/_q)        
      
    elif T > _T2:
        _Fd = _γ1 * _A *((_η * _θ * _βο )/_q) * (_T2/T)**(2/3)
        
    return _Fd

#ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ ΚΑΤΑ ΕΑΚ 2000
def Fe(T: float,
       edafos: str,
       spoudaiothta: str,
       zoni: str,
       ζ: float) -> float:

    _T1 = T1(edafos)
    _T2 = T2(edafos)
    _γ1 = γ1(spoudaiothta)
    _A = A(zoni)
    _η = h(ζ)
    _ζ = ζ
    _βο= 2.50

   
    if T >= 0 and T < _T1:
        _Fe = _A * _γ1 * (1 + (_η *_βο - 1)*(T / _T1))
       
    elif T >= _T1 and T <= _T2:
        _Fe = _A * _γ1 * _η *_βο
        
    elif T > _T2:
        _Fe = _A* _γ1 * _η *_βο* (_T2 / T)
        
    return _Fe  