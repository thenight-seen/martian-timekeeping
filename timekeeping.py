#!/usr/bin/env python3
from datetime import timedelta, datetime
from time import sleep
import math

epoch = datetime(1953,5,24)

mmonthname = ["Alfa","Beta","Gamma","Delta","Epsilon","Zeta",
              "Eta","Theta","Iota","Kappa","Lambda","Mu",
              "Nu","Ksi","Omicron","Pi","Rho","Sigma",
              "Tau","Upsilon","Phi","Chi","Psi","Omega"]
#mmonthname = ["Fehu","Uruz","Thurisaz","Ansuz","Raido","Kaunan",
#		"Gebo","Wunjo","Hagalaz","Naudiz","Isaz","Jera",
#		"Eihwaz","Perth","Algiz","Sowilo","Tiwaz","Berkanan",
#		"Ehwaz","Mannaz","Laguz","Ingwaz","Othala","Dagaz"]
#mweekdayname = ["Sunday","Monday","Tuesday","Wednesday",
#                "Thursday","Friday","Saturday"]
mweekdayname = ["\033[45mViolet\033[0m","\033[101mRed\033[0m",
                "\033[43mOrange\033[0m","\033[103mYellow\033[0m",
                "\033[102mGreen\033[0m","\033[106mBlue\033[0m",
                "\033[104mIndigo\033[0m"]
sekwmrok = 59390475
sekwmsol = 88775

while True:

    teraz1 = datetime.today()
    roznica = teraz1 - epoch
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
    print('czas lokalny:',teraz1)
    #print(roznica)
    print('data marsjańska:',mweekdayname[mtygd],msol,mmonthname[mmsc],mrok)
    print(f'data marsjańska: {msol}.{mmsc:02d}.{mrok} | {mtygd}-{mtyg}')
    print(f'czas marsjański: {mgodz:02d}:{mmin:02d}:{msek:02d}')
    print('========================================')
    teraz2 = datetime.now()
    dt = teraz2 - teraz1
    print(dt.total_seconds()*1000000,"us")
    sleep(60-dt.total_seconds()*2)
