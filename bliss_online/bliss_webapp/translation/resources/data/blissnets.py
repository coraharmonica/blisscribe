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
from .bci_blissnet import BCI_BLISSNET
from .all_blissymbols import ALL_BLISSYMBOLS
from .blissnet import BLISSNET
from .bci_blissnames import BCI_BLISSNAMES