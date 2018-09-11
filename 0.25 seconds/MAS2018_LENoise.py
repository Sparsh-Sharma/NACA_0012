#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from pylab import *
from numpy import *

# Beschriftungseigenschaften
ts=8
rc('font', family='sans-serif',size=ts)
rc('axes', labelsize=ts)
rc('xtick',labelsize=ts)
rc('ytick',labelsize=ts)
rc('legend',fontsize=ts,handlelength=1.6,labelspacing=0.3,handletextpad=0.5,borderpad=0.3)
width=8.
height=6.
ymin,ymax=-20,120

collist=['b','g','r','c','m']



###################
##     Berechnung LEN
###################

# Amiet
def calcAmiet(bx,Rx,Ux,ux,Lambdax,tfreqx,cx):
	Mx=Ux/cx
	erg_ami=zeros(len(tfreqx))
	zaehler=0
	for fx in tfreqx:
		Kx=8.*pi*fx*Lambdax/(3.*Ux)
		erg_ami[zaehler]=10.*log10((bx*Lambdax*Mx**5.*ux**2.*Kx**3.)/(Rx**2.*Ux**2.*(1+Kx**2.)**(7./3.)))+181.3
		zaehler=zaehler+1
	return(erg_ami)

# Amiet + Gershfeld
def calcAmietGershfeld(bx,dx,Rx,Ux,ux,Lambdax,tfreqx,cx):
	Mx=Ux/cx
	erg_ami=zeros(len(tfreqx))
	zaehler=0
	for fx in tfreqx:
		Kx=8.*pi*fx*Lambdax/(3.*Ux)
		erg_ami[zaehler]=10.*log10(exp(-2.*pi*fx*dx/(2.*Ux))*(bx*Lambdax*Mx**5.*ux**2.*Kx**3.)/(Rx**2.*Ux**2.*(1+Kx**2.)**(7./3.)))+181.3
		zaehler=zaehler+1
	return (erg_ami)


#####################
##        Tu
#####################
chord=1
span=2
U=25.16
Lambda=0.0058
freq=array((10,12.5,16,20,25,31.5,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,3150,4000,5000,6300,8000,10000,12500,16000,20000))

Tulist=[3.8]

labellist=[r'$Tu$ = 3.8%']


figure(2,figsize=(width/2.54,height/2.54))
for Tu in Tulist:
	j=Tulist.index(Tu)
	
	b=span/2.
	d=0.12*chord
	pegelamiet=calcAmietGershfeld(b,d,1.0,U,Tu*U,Lambda,freq,343.)
	pegelamiet2=calcAmiet(b,1.0,U,Tu*U,Lambda,freq,343.)
	
	print max(pegelamiet), Tu

	semilogx(freq,pegelamiet,'-',linewidth=1.0,color=collist[j],label=labellist[j])
	semilogx(freq,pegelamiet2,'--',linewidth=1.0,color=collist[j])

grid(color='0.5',linestyle=':',linewidth=0.2)
xticks((20,50,100,200,500,1000,2000,5000,10000,20000),('0,02','0,05','0,1','0,2','0,5','1','2','5','10','20'))
xlim(20,20000)
ylim(ymin,ymax)
legend(loc='lower left')
xlabel('$f_m$ in kHz',labelpad=1.0)
ylabel(r'$L_{p}$ in dB',labelpad=1.0)
gca().set_position([0.135,0.13,0.81,0.84] )
savefig('Flatplate_LE_Tu038.pdf',dpi=600)


#####################
##        Einfluss der Machzahl
#####################
chord=0.2
span=0.4
Tu=0.1
Lambda=0.01
freq=array((10,12.5,16,20,25,31.5,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,3150,4000,5000,6300,8000,10000,12500,16000,20000))

Ulist=[17.15,34.3,68.6,102.9,137.2]

labellist=[r'$M$ = 0,05',r'$M$ = 0,1',r'$M$ = 0,2',r'$M$ = 0,3',r'$M$ = 0,4']


figure(1,figsize=(width/2.54,height/2.54))
for U in Ulist:
	j=Ulist.index(U)
	
	b=span/2.
	d=0.12*chord
	pegelamiet=calcAmietGershfeld(b,d,1.0,U,Tu*U,Lambda,freq,343.)
	pegelamiet2=calcAmiet(b,1.0,U,Tu*U,Lambda,freq,343.)

	semilogx(freq,pegelamiet,'-',linewidth=1.0,color=collist[j],label=labellist[j])
	semilogx(freq,pegelamiet2,'--',linewidth=1.0,color=collist[j])

grid(color='0.5',linestyle=':',linewidth=0.2)
xticks((20,50,100,200,500,1000,2000,5000,10000,20000),('0,02','0,05','0,1','0,2','0,5','1','2','5','10','20'))
xlim(20,20000)
ylim(ymin,ymax)
legend(loc='lower left')
xlabel('$f_m$ in kHz',labelpad=1.0)
ylabel(r'$L_{p}$ in dB',labelpad=1.0)
gca().set_position([0.135,0.13,0.81,0.84] )
savefig('MAS2018_LE_M.png',dpi=600)


#####################
##        Einfluss des Turbulenzgrads
#####################
chord=0.2
span=0.4
U=68.6
Lambda=0.01
freq=array((10,12.5,16,20,25,31.5,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,3150,4000,5000,6300,8000,10000,12500,16000,20000))

Tulist=[0.01,0.02,0.05,0.1,0.2]

labellist=[r'$Tu$ = 0,01',r'$Tu$ = 0,02',r'$Tu$ = 0,05',r'$Tu$ = 0,1',r'$Tu$ = 0,2']


figure(2,figsize=(width/2.54,height/2.54))
for Tu in Tulist:
	j=Tulist.index(Tu)
	
	b=span/2.
	d=0.12*chord
	pegelamiet=calcAmietGershfeld(b,d,1.0,U,Tu*U,Lambda,freq,343.)
	pegelamiet2=calcAmiet(b,1.0,U,Tu*U,Lambda,freq,343.)
	
	print max(pegelamiet), Tu

	semilogx(freq,pegelamiet,'-',linewidth=1.0,color=collist[j],label=labellist[j])
	semilogx(freq,pegelamiet2,'--',linewidth=1.0,color=collist[j])

grid(color='0.5',linestyle=':',linewidth=0.2)
xticks((20,50,100,200,500,1000,2000,5000,10000,20000),('0,02','0,05','0,1','0,2','0,5','1','2','5','10','20'))
xlim(20,20000)
ylim(ymin,ymax)
legend(loc='lower left')
xlabel('$f_m$ in kHz',labelpad=1.0)
ylabel(r'$L_{p}$ in dB',labelpad=1.0)
gca().set_position([0.135,0.13,0.81,0.84] )
savefig('MAS2018_LE_Tu.png',dpi=600)

#####################
##        Einfluss der Laengenskala
#####################
chord=0.2
span=0.4
U=68.6
Tu=0.1
freq=array((10,12.5,16,20,25,31.5,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,3150,4000,5000,6300,8000,10000,12500,16000,20000))

Lambdalist=[0.005,0.01,0.02,0.05,0.1]

labellist=[r'$\Lambda$ = 0,005',r'$\Lambda$ = 0,01',r'$\Lambda$ = 0,02',r'$\Lambda$ = 0,05',r'$\Lambda$ = 0,1']


figure(3,figsize=(width/2.54,height/2.54))
for Lambda in Lambdalist:
	j=Lambdalist.index(Lambda)
	
	b=span/2.
	d=0.12*chord
	pegelamiet=calcAmietGershfeld(b,d,1.0,U,Tu*U,Lambda,freq,343.)
	pegelamiet2=calcAmiet(b,1.0,U,Tu*U,Lambda,freq,343.)

	semilogx(freq,pegelamiet,'-',linewidth=1.0,color=collist[j],label=labellist[j])
	semilogx(freq,pegelamiet2,'--',linewidth=1.0,color=collist[j])

grid(color='0.5',linestyle=':',linewidth=0.2)
xticks((20,50,100,200,500,1000,2000,5000,10000,20000),('0,02','0,05','0,1','0,2','0,5','1','2','5','10','20'))
xlim(20,20000)
ylim(ymin,ymax)
legend(loc='lower left')
xlabel('$f_m$ in kHz',labelpad=1.0)
ylabel(r'$L_{p}$ in dB',labelpad=1.0)
gca().set_position([0.135,0.13,0.81,0.84] )
savefig('MAS2018_LE_Lambda.png',dpi=600)

#####################
##        Einfluss des Profils
#####################
chord=0.2
span=0.4
U=68.6
Tu=0.1
Lambda=0.01
freq=array((10,12.5,16,20,25,31.5,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,3150,4000,5000,6300,8000,10000,12500,16000,20000))

dlist=[0.06,0.1,0.12,0.18,0.24]

labellist=[r'NACA 0006',r'NACA 0010',r'NACA 0012',r'NACA 0018',r'NACA 0024']

figure(4,figsize=(width/2.54,height/2.54))
for dx in dlist:
	j=dlist.index(dx)
	
	b=span/2.
	d=dx*chord
	pegelamiet=calcAmietGershfeld(b,d,1.0,U,Tu*U,Lambda,freq,343.)
	pegelamiet2=calcAmiet(b,1.0,U,Tu*U,Lambda,freq,343.)

	semilogx(freq,pegelamiet,'-',linewidth=1.0,color=collist[j],label=labellist[j])
	#~ semilogx(freq,pegelamiet2+j*1,'--',linewidth=1.0,color=collist[j])

grid(color='0.5',linestyle=':',linewidth=0.2)
xticks((20,50,100,200,500,1000,2000,5000,10000,20000),('0,02','0,05','0,1','0,2','0,5','1','2','5','10','20'))
xlim(20,20000)
ylim(ymin,ymax)
legend(loc='lower left')
xlabel('$f_m$ in kHz',labelpad=1.0)
ylabel(r'$L_{p}$ in dB',labelpad=1.0)
gca().set_position([0.135,0.13,0.81,0.84] )
savefig('MAS2018_LE_Profil.png',dpi=600)