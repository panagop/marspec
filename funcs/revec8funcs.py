def topog(topo):
  if topo == "a":
   return '''Επίπεδη επιφάνεια εδάφους, πλαγιές και απομονωμένες κορυφογραμμές με
μέση γωνία κλίσης i < 15° ή ύψος < 30 m'''
  elif topo == "b":
   return '''Κλίση με μέση γωνία κλίσης i > 15°'''
  elif topo == "c":
   return '''Κορυφογραμμές με πλάτος στην κορυφή πολύ μικρότερο από το
η βάση και η μέση γωνία κλίσης 15° < i < 30°'''
  elif topo == "d":
   return '''Κορυφογραμμές με πλάτος στην κορυφή πολύ μικρότερο από το
η βάση και η μέση γωνία κλίσης i > 30°'''

#γLS,CC
def γLS_CC(limit: str, con_class: str) -> float:
 if limit == "nc" and con_class == "CC1":
   γLS_CC = 1.00
 elif limit == "nc" and con_class == "CC2":
   γLS_CC = 1.40
 elif limit == "nc" and con_class == "CC3-a":
   γLS_CC = 1.70
 elif limit == "nc" and con_class == "CC3-b":
   γLS_CC = 2.20
 elif limit == "sd" and con_class == "CC1":
   γLS_CC = 0.85
 elif limit == "sd" and con_class == "CC2":
   γLS_CC = 1.00
 elif limit == "sd" and con_class == "CC3-a":
   γLS_CC = 1.15
 elif limit == "sd" and con_class == "CC3-b":
   γLS_CC = 1.30
 elif limit == "dl" and con_class == "CC1":
  γLS_CC = 0.60
 elif limit == "dl" and con_class == "CC2":
  γLS_CC = 0.60
 elif limit == "dl" and con_class == "CC3-a":
  γLS_CC = 0.65
 elif limit == "dl" and con_class == "CC3-b":
  γLS_CC = 0.65
 return γLS_CC

#Sα,475
def Sα475(zoni: str) -> float:
 if zoni == "Z1": 
  Sα_475 = 0.31
 elif zoni == "Z2":
  Sα_475 = 0.50
 elif zoni == "Z3":
  Sα_475 = 0.71
 elif zoni == "Z4":
  Sα_475 = 0.92
 return Sα_475

#Sβ,475
def Sβ475(zoni: str) -> float:
 if zoni == "Z1": 
  Sβ_475 = 0.13
 elif zoni == "Z2":
  Sβ_475 = 0.16 
 elif zoni == "Z3":
  Sβ_475 = 0.24   
 elif zoni == "Z4":
  Sβ_475 = 0.34 
 return Sβ_475

#Sα,ref για Tref=475
def Sα_ref(zoni: str) -> float:
 Sα_ref = Sα475(zoni)
 return Sα_ref

#levels
def levels(zoni: str) -> float:
  sa475 = Sα475(zoni)
  
  if sa475 < 1:
    level = 'Πολύ χαμηλό'
    
  elif sa475 >= 1 and sa475 < 2.5:
    level = 'Χαμηλό'
    
  elif sa475 >= 2.5 and sa475 < 5:
    level = 'Μέτριο'
    
  elif sa475 >= 5:
    level = 'Υψηλό'
  return level

#fh
def fh(zoni: str) -> float:
    level = levels(zoni)
    if level == "Πολύ χαμηλό" or level == "Χαμηλό": 
        fh_ = 0.20
    elif level == "Μέτριο":
        fh_ = 0.30
    elif level == "Υψηλό":
        fh_ = 0.40
    return fh_

#Sβ,ref
def Sβ_ref(zoni: str) -> float:
 Sαref = Sα_ref(zoni)
 _fh = fh(zoni)
  
 Sbref = Sαref * _fh 
 return Sbref

#Sα,RP
def Sα_RP(limit: str, con_class: str, zoni: str) -> float:
 _γ = γLS_CC(limit, con_class)
 _S = Sα_ref(zoni)

 Sα_RP = _γ * _S 
 return Sα_RP

#Sβ,RP
def Sβ_RP(limit: str,
 con_class: str,
 zoni: str) -> float:

 _γ = γLS_CC(limit, con_class)
 _S = Sβ_ref(zoni)

 Sβ_RP = _γ * _S 
 return Sβ_RP

#FT
def FT(topo: str) -> float:
 if topo == "a":
  FT = 1.00
 elif topo == "b":
  FT = 1.20
 elif topo == "c":
  FT = 1.20
 elif topo == "d":
  FT = 1.40
 return FT

#pga
def pga(zoni: str) -> float:
 if zoni == "Z1": 
  _pga = 0.12
 elif zoni == "Z2":
  _pga = 0.20
 elif zoni == "Z3":
  _pga = 0.28
 elif zoni == "Z4":
  _pga = 0.37
 return _pga

#Fα
def ra(vs: float,
limit: str,
con_class: str,
zoni: str) -> float:

 _Sα_RP = Sα_RP(limit,con_class,zoni)
 _vs = vs
 g = 9.81

 ra = 1 - ((_Sα_RP / g) / (_vs / 150))
 return ra

def Fα1(edafos: str,
 vs: float,
 H: float,
 limit: str,
 con_class: str, 
 zoni: str) -> float:

 _ra = ra(vs,limit,con_class,zoni)
 _vs = vs
 _H = H
 g = 9.81

 if edafos == "A":
  Fα = 1.00
 elif edafos == "B":
  Fα = (_vs / 800) ** (-0.40 * _ra)
 elif edafos == "C":
  Fα = (_vs / 800) ** (-0.40 * _ra)
 elif edafos == "D":
  Fα = (_vs / 800) ** (-0.40 * _ra)
 elif edafos == "E":
  Fα = (_vs / 800) ** (-0.40 * _ra*(_H /30)*(4-(_H /10)))
 elif edafos == "F":
  Fα = 0.90 * (_vs / 800) ** (-0.40 * _ra)
 return Fα

def Fα2(edafos: str,
limit: str,
con_class: str,
zoni: str) -> float: 

 _Sα_RP = Sα_RP(limit,con_class,zoni)
 g = 9.81

 if edafos == "A":
  Fα = 1.00
 elif edafos == "B":
  Fα = 1.30 * (1 - 0.10 * _Sα_RP / g)
 elif edafos == "C":
  Fα = 1.60 * (1 - 0.20 * _Sα_RP / g)
 elif edafos == "D":
  Fα = 1.80 * (1 - 0.30 * _Sα_RP / g)
 elif edafos == "E":
  Fα = 2.20 * (1 - 0.50 * _Sα_RP / g)
 elif edafos == "F":
  Fα = 1.70 * (1 - 0.30 * _Sα_RP / g)
 return Fα

def Fa_cho(choice: str,
   edafos: str,
   vs: float,
   H: float,
   limit: str,
   con_class: str,
   zoni: str) -> float:

 if choice == 'Ναι':
  Fa = Fα1(edafos,vs,H,limit,con_class,zoni)  
  return Fa
 elif choice == 'Όχι':
  Fa = Fα2(edafos, limit, con_class, zoni)  
  return Fa

#Fβ
def rb(vs: float,
limit: str,
con_class: str,
zoni: str) -> float:

 _Sβ_RP = Sβ_RP(limit,con_class,zoni)
 _vs = vs
 g = 9.81

 rb = 1 - ((_Sβ_RP / g) / (_vs / 150))
 return rb

def Fβ1(edafos: str,
vs: float,
H: float,
limit: str,
con_class: str,
zoni: str) -> float:

 _rb = rb(vs,limit,con_class,zoni)
 _vs = vs
 _H = H
 g = 9.81

 if edafos == "A":
  Fβ = 1.00
 elif edafos == "B":
  Fβ = (_vs / 800) ** (-0.70 * _rb)
 elif edafos == "C":
  Fβ = (_vs / 800) ** (-0.70 * _rb)
 elif edafos == "D":
  Fβ = (_vs / 800) ** (-0.70 * _rb)
 elif edafos == "E":
  Fβ = (_vs / 800) ** (-0.70 * _rb*(_H /30))
 elif edafos == "F":
  Fβ = 1.25 * (_vs / 800) ** (-0.70 * _rb)
 return Fβ


def Fβ2(edafos: str,
limit: str,
con_class: str,
zoni: str) -> float: 

 g = 9.81
 _Sβ_RP = Sβ_RP(limit,con_class,zoni)

 if edafos == "A":
  Fβ = 1.00
 elif edafos == "B":
  Fβ = 1.60 * (1 - 0.20 * _Sβ_RP / g)
 elif edafos == "C":
  Fβ = 2.30 * (1 - 0.30 * _Sβ_RP / g)
 elif edafos == "D":
  Fβ = 3.20 * (1 - _Sβ_RP / g)
 elif edafos == "E":
  Fβ = 3.20 * (1 - _Sβ_RP / g)
 elif edafos == "F":
  Fβ = 4.00 * (1 - _Sβ_RP / g)
 return Fβ

def Fb_cho(choice: str,
edafos: str,
vs: float,
H: float,
limit: str,
con_class: str,
zoni: str) -> float:
 if choice == 'Ναι':
  Fb = Fβ1(edafos,vs,H,limit,con_class,zoni)  
  return Fb
 elif choice == 'Όχι':
  Fb = Fβ2(edafos, limit, con_class, zoni)  
  return Fb

#Sα

def Sα1(topo: str,
zoni: str,
limit: str,
con_class: str,
edafos: str,
vs: float,
H: float) -> float:

 _FT = FT(topo)
 _Fα = Fα1(edafos,vs,H,limit,con_class,zoni)
 _Sα_RP = Sα_RP(limit, con_class, zoni)

 Sa1 = _FT * _Fα * _Sα_RP 
 return Sa1


def Sα2(topo: str,
zoni: str,
limit: str,
con_class: str,  
edafos: str) -> float:

 _FT = FT(topo)
 _Fα = Fα2(edafos,limit,con_class,zoni)
 _Sα_RP = Sα_RP(limit, con_class, zoni)

 Sa2 = _FT * _Fα * _Sα_RP 
 return Sa2

def Sa_cho(choice: str,
topo: str,
zoni: str,
limit: str,
con_class: str,
edafos: str,
vs: float,
H: float) -> float:
 if choice == 'Ναι':
  Sa = Sα1(topo,zoni,limit,con_class,edafos,vs,H)  
  return Sa
 elif choice == 'Όχι':
  Sa = Sα2(topo,zoni,limit,con_class,edafos)  
  return Sa



#Sβ
def Sβ1(topo: str,
zoni: str,
limit: str,
con_class: str,
edafos: str,
vs: float,
H: float) -> float:

 _FT = FT(topo)
 _Fβ = Fβ1(edafos,vs,H,limit,con_class,zoni)
 _Sβ_RP = Sβ_RP(limit, con_class, zoni)

 Sb = _FT * _Fβ * _Sβ_RP 
 return Sb

def Sβ2(topo: str,
zoni: str,
limit: str,
con_class: str,  
edafos: str) -> float:

 _FT = FT(topo)
 _Fβ = Fβ2(edafos,limit,con_class,zoni)
 _Sβ_RP = Sβ_RP(limit, con_class, zoni)

 Sb = _FT * _Fβ * _Sβ_RP 
 return Sb

def Sb_cho(choice: str,
topo: str,
zoni: str,
limit: str,
con_class: str,         
edafos: str,
vs: float,
H: float) -> float:
 if choice == 'Ναι':
  Sb = Sβ1(topo,zoni,limit,con_class,edafos,vs,H)  
  return Sb
 elif choice == 'Όχι':
  Sb = Sβ2(topo,zoni,limit,con_class,edafos)  
  return Sb
   
#TA
TA = 0.02
Tβ = 1.00

#TC
def TC(choice: str,
topo: str,
zoni: str,
limit: str,
con_class: str,
edafos: str,
vs: float,
H: float)  -> float:

 _Sa = Sa_cho(choice,topo,zoni,limit,con_class,edafos,vs,H)
 _Sβ = Sb_cho(choice,topo,zoni,limit,con_class,edafos,vs,H)
 _Tβ = 1.00

 _TC = (_Sβ * _Tβ) / _Sa 
 return _TC

#TB
def TB(choice: str,
topo: str,
zoni: str,
limit: str,
con_class: str,
edafos: str,
vs: float,
H: float,
xTB: float) -> float:

 _TC = TC(choice, topo, zoni, limit, con_class, edafos, vs, H)
 x = xTB

 if (_TC / x) >= 0.05 and (_TC / x) <= 0.10:
  _TB = (_TC / x) 
  return _TB
 elif (_TC / x) <= 0.05:
  _TB = 0.05
  return _TB
 elif (_TC / x) >= 0.10:
  _TB = 0.10
  return _TB

def TD(limit: str,
con_class: str,
zoni: str) -> float:

 _Sβ = Sβ_RP(limit, con_class, zoni)

 if _Sβ <= 1:
  _TD = 2.00
 elif _Sβ > 1:
  _TD = 1 + _Sβ
 return _TD

def h(ζ: float,
T: float,
choice: str,
topo: str,
zoni: str,
limit: str,
con_class: str,
edafos: str,
vs: float,
H: float,
xTB: float) -> float:

 _ζ = ζ
 _TA = 0.02
 _TB = TB(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB)
 _TC = TC(choice,topo,zoni,limit,con_class,edafos,vs,H)

 if T <= _TA:
  η = 1.00
 elif T > _TA and T < _TB:
  η = ((10 + ((_TB - T) / (_TB - _TA))**3 * (_ζ - 5)) / ( 5 + _ζ))**(1 / 2)
 elif T >= _TB:
  η = (10 / (5 + _ζ))**(1 / 2)
 return η

#ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ ΚΑΤΑ rev EC8
def Se(T: float,
choice: str,
topo: str,
zoni: str,
limit: str,
con_class: str,
edafos: str,
vs: float,
H: float,
ζ: float,
xTB: float) -> float:

 _FA = 2.50
 _TA = 0.02
 _TB = TB(choice,topo,zoni,limit,con_class,edafos,vs,H,xTB)
 _TC = TC(choice,topo,zoni,limit,con_class,edafos,vs,H,)
 _TD = TD(limit,con_class,zoni)
 _Sa = Sa_cho(choice,topo,zoni,limit,con_class,edafos,vs,H)
 _Sβ = Sb_cho(choice,topo,zoni,limit,con_class,edafos,vs,H)
 _Tβ = 1.00
 η = h(ζ,T,choice,topo,zoni,limit,con_class,edafos,vs,H,xTB)


 if T >= 0 and T <= _TA:
  _se = _Sa / _FA
  
 elif T >= _TA and T <= _TB:
  _se = ( _Sa / ( _TB - _TA )) * ( η * (T - _TA) + (_TB - T) /_FA )
  
 elif T >= _TB and T <= _TC:
  _se = η * _Sa
  
 elif T >= _TC and T <= _TD:
  _se = η * ((_Sβ * _Tβ) / T)
  
 elif T >= _TD:
  _se = η * _TD * ((_Sβ * _Tβ) / T**2)
  
 return _se