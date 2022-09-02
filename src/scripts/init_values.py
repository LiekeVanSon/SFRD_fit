"""
Initialize global variables/names shared across the files
"""
import numpy as np
import paths

#################################################################
## 
##   Should be Changed by user ##
##
#################################################################
def init():
    # define initial settings
    global data_dir, script_dir, COMPASfilename, rate_file_name, user_email, fid_dpdZ_parameters, fid_sfr_parameters, SlurmJobString
    global mu0_best, muz_best, sigma0_best, sigmaz_best, alpha0_best,sf_a_best, sf_b_best, sf_c_best, sf_d_best
    global fit_param_filename
    # there is an extra /src in the paths. due to the import location (remove it)
    data_dir   = str(paths.data)[0:-8] + 'data/'
    script_dir = str(paths.scripts)[0:-11] + 'scripts/'

    COMPASfilename  = 'COMPAS_Output_wWeights.h5'#'small_COMPAS_Output_wWeights.h5'#
    rate_file_name  = 'Rate_info.h5'#'small_Rate_info.h5'#'Rate_info.h5'
    user_email      = "aac.van.son@gmail.com"


    # Name of the txt file for best fit parameters
    fit_param_filename  = 'test_best_fit_parameters.txt'
    try:
        mu0_best, muz_best, sigma0_best, sigmaz_best, alpha0_best,sf_a_best, sf_b_best, sf_c_best, sf_d_best = np.loadtxt(data_dir+'/'+fit_param_filename,unpack=True)
        fid_dpdZ_parameters = [mu0_best, muz_best, sigma0_best, sigmaz_best, alpha0_best]
        fid_sfr_parameters  = [sf_a_best, sf_b_best, sf_c_best, sf_d_best]
    except:
        print('Couldnt open', data_dir+'/'+fit_param_filename)






#################################################################
if __name__ == "__main__": 
    
    init()