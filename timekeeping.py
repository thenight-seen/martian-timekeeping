#!/usr/bin/env python3
from datetime import timedelta, datetime
from time import sleep
import math

epoch = datetime(1953,5,24)

urodziny = datetime(1990,5,13,5,40)

#mmonthname = ["Alfa","Beta","Gamma","Delta","Epsilon","Zeta",
#              "Eta","Theta","Iota","Kappa","Lambda","Mu",
#              "Nu","Ksi","Omicron","Pi","Rho","Sigma",
#              "Tau","Upsilon","Phi","Chi","Psi","Omega"]
mmonthname = ["Fehu","Uruz","Thurisaz","Ansuz","Raido","Kaunan",
		"Gebo","Wunjo","Hagalaz","Naudiz","Isaz","Jera",
		"Eihwaz","Perth","Algiz","Sowilo","Tiwaz","Berkanan",
		"Ehwaz","Mannaz","Laguz","Ingwaz","Othala","Dagaz"]
mweekdayname = ["Sunday","Monday","Tuesday","Wednesday",
                "Thursday","Friday","Saturday"]
sekwmrok = 59390475
sekwmsol = 88775

while True:

    teraz = datetime.today()
    roznica = teraz - epoch
    roznisek = roznica.days * 86400 + roznica.seconds
    roznimlat = roznisek // sekwmrok
    roznimsol = (roznisek % sekwmrok) // sekwmsol
    rozniresztsek = roznisek % sekwmsol

    mrok = 1 + roznimlat
    mmsc = roznimsol // 28
    mtyg = 1 + roznimsol // 7
    mtygd = roznimsol % 7
    msol = 1 + roznimsol % 28 - ((roznimsol // 28) // 8)
    if msol<1 :
        msol = 29 - ((roznimsol // 28) // 8) + roznimsol // 28
        mmsc -= 1
    mgodz = rozniresztsek // 3600
    mmin = (rozniresztsek % 3600) // 60
    msek = (rozniresztsek % 3600) % 60
    print('czas lokalny:',teraz)
    #print(roznica)

    print('data marsjańska:',msol,mmonthname[mmsc],mrok,mweekdayname[mtygd],mtyg)
    print('czas marsjański:',mgodz,':',mmin,':',msek)
    print('========================================')
    sleep(600)

