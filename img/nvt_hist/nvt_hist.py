#!/usr/bin/python


from pylab import *


################################################################################
################################################################################
def hist_f(data):
    hist = {}
    norm0 = 0.0
    for E in data:
        ibin = int(E)
        if (ibin in hist):
            hist[ibin] += 1.0
        else:
            hist[ibin] = 1.0
    
    norm0 = sum(hist.values())
    for E in hist:
        hist[E] /= norm0

    return hist
    
################################################################################
################################################################################
# Defining function to read data from file
def read_file(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    
    E_data = []
    V_data = []
    for line in lines:
        data = line.split()
        E_data.append( float(data[1]) )
        V_data.append( float(data[2]) )

    hist_E = hist_f(E_data)
    hist_V = hist_f(V_data)

    return E_data, V_data, hist_E, hist_V

################################################################################
################################################################################

T0=2.0
beta0 = 1.0/T0
E0_data, V0_data, hist_E0, hist_V0 = read_file('nvt_out_T_'+str(T0)+'.dat')

#T_data=[1.5, 1.8, 1.85, 1.9, 1.95, 2.0, 2.05, 2.1, 2.15, 2.2, 2.5]
#T_data=[1.5, 1.8, 2.0, 2.2, 2.5]
#T_data=[1.0, 1.8, 2.0, 2.2, 3.0]
T_data=[1.2, 1.8, 2.0, 2.2, 4.0]
colors = ['g', 'r', 'black', 'blue', 'orange']
#dict_colors = {1.5: 'g', 1.8: 'red', 2.0: 'blue', 2.2: 'magenta', 2.5: 'orange'}


# Extrapolated histograms

# ENERGY
figure(facecolor='white')

i=0
for T in T_data:
    beta = 1.0/T
    norm = 0.0
    hist_ext = {}
    for E in hist_E0:
#        if (hist[E] > 5.0):
        hist_ext[E] = hist_E0[E] * exp(-(beta-beta0)*float(E))
        norm += hist_ext[E]
        
    for E in hist_ext:
        hist_ext[E] /= norm
            
    x_data = [x for x in hist_ext.keys()]
    y_data = [hist_ext[x] for x in hist_ext.keys()]
    plot(x_data, y_data, lw=1, ls='dashed', color=colors[i])

    i += 1

# Simulation data
i=0
for T in T_data:
    E_data, V_data, hist_E, hist_V = read_file('nvt_out_T_'+str(T)+'.dat')
    x_data = [x for x in hist_E.keys()]
    y_data = [hist_E[x] for x in hist_E.keys()]
    plot(x_data, y_data, lw=2.0, color=colors[i], label="$k_B\,T="+str(T)+"\varepsilon$")

    i += 1

xlabel('U', fontsize=16)
ylabel('H (U)', fontsize=16)
xlim([-800.0, -400.0])
ylim([0.0, 0.04])
legend()
savefig('../energy_ext_hist.png', dpi=600)
show()


## VIRIAL
#figure(facecolor='white')
#
#i=0
#for T in T_data:
#    beta = 1.0/T
#    norm = 0.0
#    hist_ext = {}
#    for V in hist_V0:
##        if (hist[V] > 5.0):
#        hist_ext[V] = hist_V0[V] * exp(-(beta-beta0)*float(V))
#        norm += hist_ext[V]
#        
#    for V in hist_ext:
#        hist_ext[V] /= norm
#            
#    x_data = [x for x in hist_ext.keys()]
#    y_data = [hist_ext[x] for x in hist_ext.keys()]
#    plot(x_data, y_data, lw=2, color=colors[i])
#
#    i += 1
#
## Simulation data
#i=0
#for T in T_data:
#    E_data, V_data, hist_E, hist_V = read_file('nvt_out_T_'+str(T)+'.dat')
#    x_data = [x for x in hist_V.keys()]
#    y_data = [hist_V[x] for x in hist_V.keys()]
#    plot(x_data, y_data, lw=1.0, color=colors[i])
#
#    i += 1
#
#xlabel('V', fontsize=16)
#ylabel('H (V)', fontsize=16)
#savefig('virial_ext_hist.png', dpi=600)
#
#show()
    
    
