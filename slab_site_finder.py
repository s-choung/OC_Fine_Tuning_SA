import copy
import itertools
import json
import logging
import math
import os
import warnings
from functools import reduce
from math import gcd

import numpy as np
from monty.fractions import lcm
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import squareform

from pymatgen.analysis.structure_matcher import StructureMatcher
from pymatgen.core.lattice import Lattice
from pymatgen.core.periodic_table import get_el_sp
from pymatgen.core.sites import PeriodicSite
from pymatgen.core.structure import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.util.coord import in_coord_list
from pymatgen.analysis.local_env import VoronoiNN
from pymatgen.io.ase import AseAtomsAdaptor  # Import the ASE to Pymatgen converter

def get_surface_sites(adslab):

    pymatgen_structure = AseAtomsAdaptor.get_structure(adslab)
    a = SpacegroupAnalyzer(pymatgen_structure)
    ucell = a.get_symmetrized_structure()
    cn_dict = {}
    v = VoronoiNN()
    unique_indices = [equ[0] for equ in ucell.equivalent_indices]
    for i in unique_indices:
        el = ucell[i].species_string
        if el not in cn_dict.keys():
            cn_dict[el] = []
        cn = v.get_cn(ucell, i, use_weights=True)
        cn = float("%.5f" % (round(cn, 5)))
        if cn not in cn_dict[el]:
            cn_dict[el].append(cn)
    v = VoronoiNN()
    surf_sites_dict, properties = {"top": []}, []
    z_median = np.median([site.frac_coords[2] for site in pymatgen_structure])

    for i, site in enumerate(pymatgen_structure):
        if site.frac_coords[2] > z_median:  # Consider only top surface sites
            cutoff = 1
            try:
                cn = float("%.5f" % (round(v.get_cn(pymatgen_structure, i, use_weights=True), 5)))
                if cn < min(cn_dict[site.specie.symbol]) + cutoff:
                    properties.append(True)
                    surf_sites_dict["top"].append([site, i])
                else:
                    properties.append(False)
            except RuntimeError:
                properties.append(True)
                surf_sites_dict["top"].append([site, i])
    return surf_sites_dict, properties

adslab = contcar_ase_dict['1_111'][0].copy()
surf_sites,properties = get_surface_sites(adslab)
top_surface_sites = surf_sites["top"]
print(len(top_surface_sites))
print(top_surface_sites)
## taken from DFT_preoptimizing/DFT_MKM/2_CO_vib_detection.ipynb
