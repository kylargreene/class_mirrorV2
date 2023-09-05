from classy import Class
cosmo=Class()

params = {'tau_reio': 0.054308, 'varying_alpha': 1.01408,'varying_me': 0.9724,'omega_b': 0.02237, 'omega_cdm': 0.146216, 'h': 0.733, 'A_s': 2.10655188e-09, 'n_s': 0.9660499, 'T_cmb': 2.7255, 'recombination': 'HyRec', 'reio_parametrization': 'reio_half_tanh', 'YHe': 0.245373653547, 'varying_fundamental_constants': 'instantaneous',  'bbn_alpha_sensitivity': 1, 'varying_transition_redshift': 50, 'modes': 's', 'ic': 'ad', 'gauge': 'synchronous', 'l_max_scalars': 3000, 'lensing': 'yes', 'N_ur': 3.60453, 'dark_m_p': 0.65507 , 'dark_m_e': 0.55182, 'dark_fs': 1.08851, 'f_idm': 0.028217, 'xi_mirror': 0.65507, 'output': 'tCl lCl', 'alpha_idm_dr': '0.9 1.'}

cosmo.set(params)

cosmo.compute()

