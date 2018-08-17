"""
BLISSNETS:

    Stores different types of blissnets for easy access.
    ~
    Includes blissnets for:
     - BCI-AV# to synset
     - blissname to synset
"""
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from .all_blissymbols import ALL_BLISSYMBOLS
from .bci_blissnames import BCI_BLISSNAMES
from .bci_blissnet import BCI_BLISSNET
from .bliss_derivations import DERIVATIONS
from .bliss_unicode import BLISS_UNICODE
from .blissnet import BLISSNET
