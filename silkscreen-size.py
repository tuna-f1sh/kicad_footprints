import sys
from pcbnew import *

"""
execfile ("c:/python_progs/test_pcb/set_text.py")
"""

def SetText(Filename = None):
    if Filename: 
        my_board = pcbnew.LoadBoard (Filename)
    else:
        my_board = pcbnew.GetBoard()

    for module in my_board.GetModules():
        print ("module ref %s %s" % ( module.GetReference(), my_board.GetLayerName(module.Reference().GetLayer())))

        # set size in mm
        module.Reference().SetSize (wxSize (FromMM(2),FromMM(2)))
        
        # set thickness in mm
        module.Reference().SetThickness (FromMM(0.3))

SetText(sys.argv[1])
