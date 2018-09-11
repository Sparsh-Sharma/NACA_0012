from pysces import *
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from pylab import *

angle = 0
airfoil = naca_airfoil("0012", 200, zero_thick_te=True)  
airfoil = TransformedBody(airfoil, displacement=(2.5, 2.5))
airfoil = TransformedBody(airfoil, angle)
bound = BoundVortices(airfoil)

num_steps = 20000
Uinfty = (25.16,0)
dt = 0.000025
Vortices.core_radius = dt

#free vortices

v1	=	(	3.724339281	,	4.926183197	)
v2	=	(	4.461335941	,	2.79738703	)
v3	=	(	1.213016931	,	4.667959579	)
v4	=	(	0.647984879	,	3.60171603	)
v5	=	(	1.125339411	,	2.420192584	)
v6	=	(	1.750069595	,	3.195155463	)
v7	=	(	1.435423066	,	4.438184329	)
v8	=	(	4.637440036	,	0.99368375	)
v9	=	(	0.256568784	,	1.97683137	)
v10	=	(	2.963333776	,	4.960876512	)
v11	=	(	0.814494501	,	2.011758085	)
v12	=	(	4.192028848	,	3.294282405	)
v13	=	(	0.837804651	,	4.506740615	)
v14	=	(	2.511003077	,	4.976908883	)
v15	=	(	4.996647395	,	3.265816405	)
v16	=	(	1.777035756	,	0.542182139	)
v17	=	(	0.235388548	,	0.180570154	)
v18	=	(	1.068302926	,	3.090456195	)
v19	=	(	1.989195621	,	2.835721809	)
v20	=	(	1.668340902	,	4.809823289	)
v21	=	(	1.14801266	,	3.730527347	)
v22	=	(	4.680600888	,	3.312580492	)
v23	=	(	3.415943923	,	2.616566592	)
v24	=	(	4.810568979	,	1.299471407	)
v25	=	(	2.189865888	,	4.809968835	)
v26	=	(	4.701683272	,	2.701020188	)
v27	=	(	0.029171623	,	0.151350817	)
v28	=	(	3.05153515	,	3.481572317	)
v29	=	(	4.005378785	,	2.59858079	)
v30	=	(	1.164907667	,	0.295152778	)
v31	=	(	4.66234338	,	4.450181166	)
v32	=	(	3.816313877	,	1.651011213	)
v33	=	(	4.132247699	,	1.148505989	)
v34	=	(	2.867317943	,	0.56974321	)
v35	=	(	3.962908321	,	1.554613567	)
v36	=	(	1.645205979	,	1.142161611	)
v37	=	(	1.117309881	,	3.259985836	)
v38	=	(	1.56193171	,	0.330800623	)
v39	=	(	2.922617393	,	1.377156899	)
v40	=	(	4.149570705	,	1.409101188	)
v41	=	(	1.452312458	,	4.400331299	)
v42	=	(	2.01277196	,	2.221651793	)
v43	=	(	4.310286492	,	3.779570605	)
v44	=	(	3.073697751	,	3.016481879	)
v45	=	(	4.955938942	,	3.916329687	)
v46	=	(	1.018494376	,	0.569653193	)
v47	=	(	4.136045425	,	4.892819426	)
v48	=	(	3.379308095	,	4.242983377	)
v49	=	(	1.24474735	,	0.253232488	)
v50	=	(	2.378928133	,	2.331009169	)
v51	=	(	1.995376134	,	1.628266375	)
v52	=	(	2.997191245	,	3.151025625	)
v53	=	(	4.002613829	,	1.151495819	)
v54	=	(	0.525343856	,	2.899424866	)
v55	=	(	4.107210971	,	3.015781602	)
v56	=	(	4.20543165	,	2.999395479	)
v57	=	(	1.772531222	,	2.242139402	)
v58	=	(	2.150347313	,	0.177117303	)
v59	=	(	2.861196092	,	2.569074175	)
v60	=	(	3.504123654	,	2.038650809	)
v61	=	(	3.712348785	,	0.540230183	)
v62	=	(	3.789420753	,	2.299378145	)
v63	=	(	1.945643818	,	2.254413768	)
v64	=	(	2.146512425	,	2.755701679	)
v65	=	(	4.781723288	,	4.027021585	)
v66	=	(	2.864856836	,	3.504250364	)
v67	=	(	4.248610271	,	4.36117752	)
v68	=	(	1.381726581	,	0.260960762	)
v69	=	(	3.111618076	,	1.098406557	)
v70	=	(	2.941808423	,	2.298210051	)
v71	=	(	4.817342329	,	4.792667981	)
v72	=	(	0.429513475	,	3.950226785	)
v73	=	(	2.502494458	,	2.259373045	)
v74	=	(	2.607948382	,	1.667140932	)
v75	=	(	0.450830011	,	0.295476563	)
v76	=	(	4.523332398	,	3.704526514	)
v77	=	(	4.421944693	,	2.53397262	)
v78	=	(	2.194948334	,	0.999627066	)
v79	=	(	3.908613065	,	2.135967756	)
v80	=	(	0.742325115	,	0.843451394	)
v81	=	(	3.099079636	,	3.758472954	)
v82	=	(	1.303118397	,	1.841754208	)
v83	=	(	2.228281057	,	4.709088976	)
v84	=	(	4.219997557	,	0.085862705	)
v85	=	(	0.981024594	,	4.145279544	)
v86	=	(	1.519258114	,	3.132954875	)
v87	=	(	2.416472839	,	2.693732576	)
v88	=	(	1.689060219	,	3.252538177	)
v89	=	(	3.992429148	,	3.633147662	)
v90	=	(	4.937437876	,	0.47244282	)
v91	=	(	0.795237774	,	4.387869672	)
v92	=	(	1.184398916	,	0.07181072	)
v93	=	(	3.511183163	,	1.471513134	)
v94	=	(	1.877358313	,	0.899574393	)
v95	=	(	4.868524513	,	4.631471341	)
v96	=	(	4.861527778	,	0.340902184	)
v97	=	(	3.218490247	,	2.905466138	)
v98	=	(	4.300494384	,	3.185756113	)
v99	=	(	2.00941699	,	3.256346324	)
v100	=	(	3.15965399	,	4.323110063	)
s1	=	-0.00810137
s2	=	-0.002358173
s3	=	-0.005739786
s4	=	-0.00301405
s5	=	-0.005104372
s6	=	0.007146763
s7	=	-0.006217448
s8	=	0.003309552
s9	=	-0.009628271
s10	=	0.003148365
s11	=	0.001601919
s12	=	-0.000267816
s13	=	-0.004203056
s14	=	-0.007332782
s15	=	-0.007438438
s16	=	0.005952526
s17	=	-0.002406503
s18	=	-0.009211939
s19	=	-0.003261878
s20	=	-0.004885199
s21	=	-0.007855187
s22	=	-0.005157929
s23	=	0.001390677
s24	=	-0.009458933
s25	=	-0.008514089
s26	=	-0.007476089
s27	=	-0.009596561
s28	=	-0.00254231
s29	=	0.004407038
s30	=	-0.008525512
s31	=	-0.009407032
s32	=	-0.008240197
s33	=	-0.008299178
s34	=	-0.00134553
s35	=	-0.008120331
s36	=	-0.008863652
s37	=	-0.009670941
s38	=	0.00526943
s39	=	-0.004817803
s40	=	-0.000933753
s41	=	-0.00903471
s42	=	0.005010489
s43	=	0.003657597
s44	=	-0.00817259
s45	=	-0.009759993
s46	=	-0.00389436
s47	=	-0.00790767
s48	=	-0.00471163
s49	=	-0.005847883
s50	=	-0.008320943
s51	=	-0.008063403
s52	=	-0.008914486
s53	=	0.008245472
s54	=	-0.009561177
s55	=	-0.006836382
s56	=	-0.007735695
s57	=	0.000727321
s58	=	0.002482442
s59	=	-0.006056835
s60	=	-0.002724207
s61	=	-0.008023285
s62	=	-0.007642553
s63	=	-0.003042322
s64	=	-0.003108074
s65	=	-0.008703396
s66	=	-0.000556651
s67	=	0.008210182
s68	=	-0.007415711
s69	=	0.003421072
s70	=	-0.009945001
s71	=	-0.008586365
s72	=	0.007591843
s73	=	-0.005495165
s74	=	-0.006837172
s75	=	-0.006850401
s76	=	-0.001579866
s77	=	-0.005260703
s78	=	-0.00582793
s79	=	-0.000795596
s80	=	0.009450254
s81	=	-0.006623332
s82	=	0.006623376
s83	=	-0.006968241
s84	=	-0.002979532
s85	=	-0.00823507
s86	=	-0.009793557
s87	=	-0.004185213
s88	=	0.002325612
s89	=	-0.009226417
s90	=	-0.000673677
s91	=	0.00088115
s92	=	0.006958312
s93	=	0.001442221
s94	=	-0.007387849
s95	=	0.001112722
s96	=	0.00369892
s97	=	-0.00931818
s98	=	-0.009690903
s99	=	0.007405307
s100	=	-0.009010548

vort = Vortices([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32,v33,v34,v35,v36,v37,v38,v39,v40,v41,v42,v43,v44,v45,v46,v47,v48,v49,v50,v51,v52,v53,v54,v55,v56,v57,v58,v59,v60,v61,v62,v63,v64,v65,v66,v67,v68,v69,v70,v71,v72,v73,v74,v75,v76,v77,v78,v79,v80,v81,v82,v83,v84,v85,v86,v87,v88,v89,v90,v91,v92,v93,v94,v95,v96,v97,v98,v99,v100],[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s55,s56,s57,s58,s59,s60,s61,s62,s63,s64,s65,s66,s67,s68,s69,s70,s71,s72,s73,s74,s75,s76,s77,s78,s79,s80,s81,s82,s83,s84,s85,s86,s87,s88,s89,s90,s91,s92,s93,s94,s95,s96,s97,s98,s99,s100])

flow = ExplicitEuler(dt, Uinfty, bound, wake=vort, need_force='wake_impulse')

for i in range(1,num_steps):
    flow.advance()

#plot force
f = flow.force
steps = np.arange(0, num_steps*dt, dt)
expected_Cl = (np.pi * np.pi / 90) * angle
expected = np.array([expected_Cl, expected_Cl])
steps2 = np.array([0, num_steps*dt])

#saving data
data = (steps, 2*f[:,0])  
savetxt('Tu_038__GA_20000.csv',np.column_stack((steps, 2*f[:,1])), fmt='%5s', delimiter=',')

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(steps, 2*f[:,0], c='b', edgecolors='none', label='Cd')
ax1.scatter(steps, 2*f[:,1], c='r', edgecolors='none', label='Cl')
ax1.plot(steps2, expected, c='g', label='expected Cl')
plt.legend();
plt.xlabel('time')
#plt.grid(True)
plt.savefig('Tu_038_GA__20000.pdf')
plt.show()



average_thrust = np.average(flow.force[:,0])
#print average_thrust

average_lift = np.average(flow.force[:,1])
#print average_lift

def Curles_loadingNoise(y_int,c_sound,r_dist,L,dt,Velo):
	p_acoustic = ((y_int*L)/(4*np.pi*dt*c_sound*(r_dist**2)))*(0.5*1.225*pow(Velo,2))
	return p_acoustic

noise = Curles_loadingNoise(1, 343,1, 2*f[:,1],dt,25.16)
print noise

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

def L_p(x):
	return 20*np.log10(np.abs(x)/2.e-5)

blocksize=100
j=0

(werte,freq)=plt.psd(noise, NFFT=blocksize, Fs=10000, detrend=mlab.detrend_none,window=mlab.window_hanning, noverlap=04, pad_to=None,sides='default', scale_by_freq='True')
#xx=30


pegel=L_p(werte)
#freq=freq[xx:]
plt.plot()

	
#Sr=freq*durchmesser/U
#solldrucklist=[1000,1200,1500,1700]
alphalist=[0.25,0.5,0.75,1.0]
stylelist=['--','-.',':','-']

plt.figure(1,figsize=(8.4/2.54,4.0/2.54))
plt.semilogx(freq,pegel,linestyle=stylelist[j],linewidth=0.6,alpha=alphalist[j])
j+=1
plt.savefig('SPL_20000.pdf')
plt.show()
