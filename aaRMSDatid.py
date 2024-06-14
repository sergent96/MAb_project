# import pyrotein as pr
# import os

# #put in the PDB code
# temp_pdb="6xc4.pdb"
# temp_list=pr.atom.read(temp_pdb)
# temp_dict=pr.atom.create_lookup_table(temp_list)

from biopandas.pdb import PandasPdb

ppdb = PandasPdb().fetch_pdb("7chb")
ppdb.df["ATOM"].head()




# pm=pymolPy3.pymolPy3(0)
# pm(f"fetch 6xc4")
# altered_protein=[]
