#ΤΥΠΟΙ ΕΔΑΦΟΥΣ 
def TB(edafos: str) -> float:
  if edafos == "A":
    TB = 0.15
    return TB
  elif edafos == "B":
    TB = 0.15
    return TB
  elif edafos == "C":
    TB = 0.20
    return TB
  elif edafos == "D":
    TB = 0.20
    return TB
  elif edafos == "E":
    TB = 0.15
    return TB

def TC(edafos: str) -> float:
  if edafos == "A":
    TC = 0.40
    return TC
  elif edafos == "B":
    TC = 0.50
    return TC
  elif edafos == "C":
    TC = 0.60
    return TC
  elif edafos == "D":
    TC = 0.80
    return TC
  elif edafos == "E":
    TC = 0.50
    return TC
  
def TD(edafos: str) -> float:
  if edafos == "A":
    TD = 2.50
    return TD
  elif edafos == "B":
    TD = 2.50
    return TD
  elif edafos == "C":
    TD = 2.50
    return TD
  elif edafos == "D":
    TD = 2.50
    return TD
  elif edafos == "E":
    TD = 2.50
    return TD
  
def S(edafos: str) -> float:
  if edafos == "A":
    S = 1
    return S
  elif edafos == "B":
    S = 1.20
    return S
  elif edafos == "C":
    S = 1.15
    return S
  elif edafos == "D":
    S = 1.35
    return S
  elif edafos == "E":
    S = 1.40
    return S

#ΖΩΝΗ ΣΕΙΣΜΙΚΗΣ ΕΠΙΚΙΝΔΥΝΟΤΗΤΑΣ 
def agR(zoni: str) -> float:
  if zoni == "Z1":
    agR = 0.16
    return agR
  elif zoni == "Z2":
    agR = 0.24
    return agR
  elif zoni == "Z3":
    agR = 0.36
    return agR
      
#ΚΑΤΗΓΟΡΙΑ ΣΠΟΥΔΑΙΟΤΗΤΑΣ
def γ1(spoudaiothta: str) -> float:
  if spoudaiothta == "I":
    γ1 = 0.80
    return γ1
  elif spoudaiothta == "II":
    γ1 = 1.00
    return γ1
  elif spoudaiothta == "III":
    γ1 = 1.20
    return γ1
  elif spoudaiothta == "IV":
    γ1 = 1.40
    return γ1

def ag(γ1: float, agR: float) -> float:
  return γ1*agR

#ΔΙΟΡΘΩΤΙΚΟΣ ΣΥΝΤΕΛΕΣΤΗΣ ΓΙΑ ΠΟΣΟΣΤΟ ΑΠΟΣΒΕΣΗΣ
def h(ζ: float) -> float:

  _ζ = ζ
  return (10/(5 + _ζ))**(1/2)

#ΦΑΣΜΑ ΣΧΕΔΙΑΣΜΟΥ ΚΑΤΑ EC8
def Sd(T: float,
   edafos: str,
   spoudaiothta: str,
   zoni: str,
   q: float) -> float:

  _S = S(edafos)
  _TB = TB(edafos)
  _TC = TC(edafos)
  _TD = TD(edafos)

  _ag = ag(γ1(spoudaiothta), agR(zoni))
  _q = q
  _β = 0.2

  if T >= 0 and T <= _TB:
   _sd = _ag * _S * ((2 / 3) + ( T / _TB) * ((2.5 / _q) - (2 / 3)))
  elif T >= _TB and T <= _TC:
   _sd = _ag * _S * (2.50 / _q)
  elif T >= _TC and T <= _TD:
   _sd = _ag * _S * (2.50 / _q) * (_TC / T)
  elif  T >= _TD:
   _sd = _ag * _S * (2.50 / _q) * ((_TC * _TD) / T**2)
  return _sd

#ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ ΚΑΤΑ EC8
def Se(T: float,
   edafos: str,
   spoudaiothta: str,
   zoni: str,
   ζ : str) -> float:

  _S = S(edafos)
  _TB = TB(edafos)
  _TC = TC(edafos)
  _TD = TD(edafos)
  η = h(ζ)
  _ag = ag(γ1(spoudaiothta), agR(zoni))

  if T >= 0 and T <= _TB:
    _se = _ag * _S * (1 + (T / _TB) * (η * 2.50 - 1))
  elif T >= _TB and T <= _TC:
    _se = _ag * _S * η * 2.50
  elif T >= _TC and T <= _TD:
    _se = _ag * _S * η * 2.50 * (_TC / T)
  elif T >= _TD and T <= 4:
    _se = _ag * _S * η * 2.50 * ((_TC * _TD) / T**2)
  return _se