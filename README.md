# vina-splitter.py
#By dropping this script into a folder containing PDBQT files and launching, 
it will separate all the PDBQT files into each pose it contains as individual PDBs.

It will produces the PDBQT files without MODEL and ENDML in new folder that you assigned.
It will replace Si atom with C atom to avoid vina reading inputs error.
