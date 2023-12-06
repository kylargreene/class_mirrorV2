from classy import Class

params = {'varying_alpha': 1.012638,
          'varying_me': 0.9727925,
          'f_adm': 0.03056,
          'xi_mirror': 0.7184,
          'N_ur': 3.2299,
          'omega_b': 0.022372, 
          'omega_cdm': 0.14699, 
          'h': 0.73965, 
          'A_s': 2.043266e-09, 
          'n_s': 0.95889,
          'tau_reio': 0.0483597, 
          'T_cmb': 2.7255,
          'recombination': 'HyRec', 
          'reio_parametrization': 'reio_camb', 
          'YHe': 0.245373653547, 
          'varying_fundamental_constants': 'instantaneous', 
          'bbn_alpha_sensitivity': 1, 
          'varying_transition_redshift': 15,  
          'modes': 's', 
          'ic': 'ad', 
          'gauge': 'synchronous', 
          'Pk_ini_type': 'analytic_Pk', 
          'l_max_scalars': 3000, 
          'lensing': 'yes', 
          'output': 'tCl lCl mPk pCl'}

cosmo=Class()
cosmo.set(params)
cosmo.compute()
import numpy as np
cls = cosmo.lensed_cl(3000)

a_file=open('ell_ds.txt','w')
np.savetxt(a_file,cls['ell'])
a_file.close()

a_file=open('ee_ds.txt','w')
np.savetxt(a_file,cls['ee'])
a_file.close()

a_file=open('tt_ds.txt','w')
np.savetxt(a_file,cls['tt'])
a_file.close()

