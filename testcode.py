import numpy as np
import scipy as sc
import qutip as qt


def purity(rho):
    """
    Calculate the purity of a quantum state
    
    Parameters
    ---------
    rho : quti.Qobj
        Quantum density matrix
    
    Returns
    ---------
    purity_rho : float
        The purity of rho(=1 if pure, <1 if not pure)
    """

    purity_rho=(rho*rho).tr()
    return purity_rho
