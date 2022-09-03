"""

# Plotting the stable BH mass distribution for several SFRD Z-distribution variations

"""

import sys
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
# configure backend here
matplotlib.use('Agg')

import seaborn as sns
from scipy import stats

import h5py as h5 
from astropy.table import Table
import astropy.units as u
from astropy import constants as const

# Chosen cosmology 
from astropy.cosmology import WMAP9 as cosmo
from astropy.cosmology import z_at_value

import json
import argparse

# My own helper funcitons:
import importlib
import MassDistHelperFunctions as mfunc
importlib.reload(mfunc)

import gc
import paths
import init_values as In

import time

import Plot_Mass_distributions as pltmass


#################################################################################################
#                                                                                               #
#                                          Call plots                                           #
#                                                                                               #
#################################################################################################
if __name__ == "__main__": 

    # Initialize values
    In.init()
    
    only_stable = True
    only_CE     = False
    channel_string = 'stable'

    print('making Figure ', save_loc + '/Mass_distributions_'+ channel_string+'_SFRD_variations.pdf')

    fig = plt.figure( figsize = (24, 28))

    ####################################################
    # width of SFRD at z=0
    ####################################################
    #add first subplot in layout that has 3 rows and 2 columns
    subplot1 = fig.add_subplot(321)

    ax1 = pltmass.plot_mass_distribution(sim_dir = data_dir, rate_file='/RateData/'+str(In.rate_file_name), simulation_data = '/'+str(In.COMPASfilename),
                           x_key = 'M_moreMassive',  rate_keys  = ['Rates_mu00.025_muz-0.049_alpha-1.778_sigma0%s_sigmaz0.048_a0.017_b1.481_c4.452_d5.913'%(x) for x in [0.7, 1.129, 2.0]], channel_string = channel_string,
                           show_hist = False, show_KDE = True,  plot_LIGO = True, Color =  'navy',
                           only_CE = only_CE, only_stable = only_stable, 
                           bootstrap = False, bootstraps = 50, save_name = 'SFRD_width_variations.pdf', titletext = "Width of metallicity dist."+"\n"+r"$\omega_0$, (scale $z=0$)",
                           labels = [r'$\mathrm{Narrow: \ }  (\omega_0 = 0.70) \  \mathcal{R}_{0.2} = \ $',
                                     r'$\mathrm{Fiducial: \ } (\omega_0 = 1.13) \ \mathcal{R}_{0.2}= \ $', 
                                     r'$\mathrm{Wide: \ } \phantom{xx} (\omega_0 = 2.00) \  \mathcal{R}_{0.2} = \ $'],
                          multipanel = True, subplot = subplot1)

    # 'Rates_mu00.025_muz-0.049_alpha-3.5_sigma01.129_sigmaz0.048_a0.017_b1.481_c4.452_d5.913
    # Rates_mu00.025_muz-0.049_alpha-1.778_sigma01.129_sigmaz0.048_a0.017_b1.481_c4.452_d5.913

    ####################################################
    # Redshift evolution of the width
    ####################################################
    #add Second subplot in layout that has 3 rows and 2 columns
    subplot2 = fig.add_subplot(322)

    ax2 = pltmass.plot_mass_distribution(sim_dir = data_dir,rate_file='/RateData/'+str(In.rate_file_name) , simulation_data = '/'+str(In.COMPASfilename),
                           x_key = 'M_moreMassive',  rate_keys = ['Rates_mu00.025_muz-0.049_alpha-1.778_sigma01.129_sigmaz%s_a0.017_b1.481_c4.452_d5.913'%(x) for x in [0.0, 0.048, 0.1]],channel_string = channel_string,
                           show_hist = False, show_KDE = True,  plot_LIGO = True, Color = '#00a6a0', 
                           only_CE = only_CE, only_stable = only_stable,
                           bootstrap = False, bootstraps = 50, save_name = 'SFRD_zevol_width_variations.pdf',  titletext = "Redshift evol. width of metallicity dist." +"\n"+ r"$\omega_z$, (scale z evol.)",
                           labels = [r'$\mathrm{Flat \ width: \ } \phantom{i} (\omega_z = 0.00) \ \mathcal{R}_{0.2} = \ $',
                                     r'$\mathrm{Fiducial: \ } \phantom{xxi} (\omega_z = 0.05) \ \mathcal{R}_{0.2}= \ $', 
                                     r'$\mathrm{Steep \ width: \ } (\omega_z = 0.10) \ \mathcal{R}_{0.2} = \ $'],
                            multipanel = True, subplot = subplot2)


    ####################################################
    # Mean metallicity at z=0
    ####################################################
    #add third subplot in layout that has 3 rows and 2 columns
    subplot3 = fig.add_subplot(323)

    ax3 = pltmass.plot_mass_distribution(sim_dir = data_dir,rate_file='/RateData/'+str(In.rate_file_name) , simulation_data = '/'+str(In.COMPASfilename),
                           x_key = 'M_moreMassive',  rate_keys = ['Rates_mu0%s_muz-0.049_alpha-1.778_sigma01.129_sigmaz0.048_a0.017_b1.481_c4.452_d5.913'%(x) for x in [0.007, 0.025, 0.035]],channel_string = channel_string,
                           show_hist = False, show_KDE = True,  plot_LIGO = True, Color = '#e1131d', 
                           only_CE = only_CE, only_stable = only_stable,
                           bootstrap = False, bootstraps = 50, save_name = 'SFRD_meanZ_variations.pdf',  titletext = 'Mean metallicity'+"\n"+r"$\mu_0$",
                           labels = [r'$\mathrm{low \ <Z_0> : \ } \phantom{x} (\mu_0 = 0.007) \ \mathcal{R}_{0.2} = \ $',
                                     r'$\mathrm{Fiducial : \ } \phantom{xxxi} (\mu_0 = 0.025) \ \mathcal{R}_{0.2} = \ $',
                                     r'$\mathrm{high \ <Z_0> : \ } \phantom{i} (\mu_0 = 0.035) \ \mathcal{R}_{0.2} = \ $'],
                            multipanel = True, subplot = subplot3)

    ####################################################
    # Redshift evolution of mean metallicity
    ####################################################
    #add 4th subplot in layout that has 3 rows and 2 columns
    subplot4 = fig.add_subplot(324)

    ax4 = pltmass.plot_mass_distribution(sim_dir = data_dir,rate_file='/RateData/'+str(In.rate_file_name) , simulation_data = '/'+str(In.COMPASfilename),
                           x_key = 'M_moreMassive',  rate_keys = ['Rates_mu00.025_muz%s_alpha-1.778_sigma01.129_sigmaz0.048_a0.017_b1.481_c4.452_d5.913'%(x) for x in [0.0, -0.049, -0.5]],channel_string = channel_string,
                           show_hist = False, show_KDE = True,  plot_LIGO = True, Color = '#ff717b', 
                           only_CE = only_CE, only_stable = only_stable,
                           bootstrap = False, bootstraps = 50, save_name = 'SFRD_zevol_mean_variations.pdf', titletext = "Redshift evol. of mean metallicity" +"\n"+ r"$\mu_z$", 
                           labels = [r'$\mathrm{Flat: \ } \phantom{xxi} (\mu_z = 0.0) \ \mathcal{R}_{0.2} = \ $',
                                     r'$\mathrm{Fiducial: \ } (\mu_z = -0.05) \ \mathcal{R}_{0.2}= \ $', 
                                     r'$\mathrm{Steep: \ } \phantom{xx} (\mu_z = -0.5) \ \mathcal{R}_{0.2} = \ $'],
                            multipanel = True, subplot = subplot4)


    ####################################################
    # Skewness
    ####################################################
    #add 5th subplot in layout that has 3 rows and 2 columns
    subplot5 = fig.add_subplot(325)

    ax5 = pltmass.plot_mass_distribution(sim_dir = data_dir,rate_file='/RateData/'+str(In.rate_file_name) , simulation_data = '/'+str(In.COMPASfilename),
                           x_key = 'M_moreMassive',  rate_keys = ['Rates_mu00.025_muz-0.049_alpha%s_sigma01.129_sigmaz0.048_a0.017_b1.481_c4.452_d5.913'%(x) for x in [0.0, -1.778, -6.0]],channel_string = channel_string,
                           show_hist = False, show_KDE = True, plot_LIGO = True, Color = '#acbf00', 
                           only_CE = only_CE, only_stable = only_stable,
                           bootstrap = False, bootstraps = 50, save_name = 'SFRD_skewness_variations.pdf', titletext = "Skewness of metallicity dist." +"\n"+ r"$\alpha$, (shape)", 
                           labels = [r'$\mathrm{Symmetric: \ } (\alpha = 0.0)   \ \mathcal{R}_{0.2} = \ $',
                                     r'$\mathrm{Fiducial: \  } \phantom{xx} (\alpha = -1.77)  \ \mathcal{R}_{0.2}= \ $', 
                                     r'$\mathrm{Skewed: \    } \phantom{xxi} (\alpha = -6)  \ \mathcal{R}_{0.2} = \ $'],
                            multipanel = True, subplot = subplot5)


    ####################################################
    # Star formation norm
    ####################################################
    #add 6th subplot in layout that has 3 rows and 2 columns
    subplot6 = fig.add_subplot(326)


    ax6 = pltmass.plot_mass_distribution(sim_dir = data_dir, rate_file='/RateData/'+str(In.rate_file_name), simulation_data = '/'+str(In.COMPASfilename),
                           x_key = 'M_moreMassive',  
                           rate_keys = ['Rates_mu00.025_muz-0.049_alpha-1.778_sigma01.129_sigmaz0.048_a0.01_b2.6_c3.2_d6.2',
                                       'Rates_mu00.025_muz-0.049_alpha-1.778_sigma01.129_sigmaz0.048_a0.017_b1.481_c4.452_d5.913', 
                                       'Rates_mu00.025_muz-0.049_alpha-1.778_sigma01.129_sigmaz0.048_a0.03_b2.6_c3.3_d5.9'],
                                 channel_string = channel_string,
                           show_hist = False, show_KDE = True,  plot_LIGO = True, Color = '#ecb05b', 
                           only_CE = only_CE, only_stable = only_stable,
                           bootstrap = False, bootstraps = 50, save_name = 'SFRD_skewness_variations.pdf', titletext = "Overall SFR history"+"\n"+ r'$ \mathrm{SFRD(}z\rm{)} \ [a,b,c,d]$', 
                           labels = [r'$\mathrm{Madau \ \& \ Fragos \ 2017: } \phantom{xxxx} \ \mathcal{R}_{0.2}= \ $', 
                                     r'$\mathrm{Fiducial: \ } \phantom{xxxxx-xxxxx-} \ \mathcal{R}_{0.2}= \ $', 
                                     r'$\mathrm{Approx. \ to \ upper \ limit:}  \ \mathcal{R}_{0.2} = \ $'],
                            multipanel = True, subplot = subplot6)



    ####################################################
    # Final plot properties
    fig.savefig(save_loc + '/Mass_distributions_'+ channel_string+'_SFRD_variations.pdf' , bbox_inches='tight')
    # plt.show()




