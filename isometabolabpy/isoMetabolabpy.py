import numpy as np
import scipy as sp
import os
import math
import time
import metabolabpy.__init__ as ml_version


class IsoMetabolabpy:

    def __init__(self):
        self.fid = np.array([[]], dtype='complex')
        self.ver = ml_version.__version__
        # end __init__

    def __str__(self):  # pragma: no cover
        r_string = '______________________________________________________________________________________\n'
        r_string += '\nIsoMetaboLabPy Isotopomer Data (v. ' + self.ver + ')\n'
        r_string += '______________________________________________________________________________________\n\n'
        return r_string
        # end __str__

