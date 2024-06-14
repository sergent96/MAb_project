# import pyrotein as pr
# import os
# import pymolPy3
import pymol
from pymol import cmd

#put in the PDB code
# temp_pdb="6xc4.pdb"
# temp_list=pr.atom.read(temp_pdb)
# temp_dict=pr.atom.create_lookup_table(temp_list)


# print (temp_dict)

# pm=pymolPy3.pymolPy3(0)
# pm(f"fetch 6xc4")
# altered_protein=[]


#put in the PDB code
cmd.fetch("7CHB")

cov=[]
altered_protein=[]
#note:[chain identifier, what to rename it as] add more as needed
altered_protein.append(["H", "vh"])
altered_protein.append(["L", "vl"])
altered_protein.append(["R", "wt_rbd"])
cov.append(["wt_rbd"])

#colors the image based on chain
cmd.util.cbc()


#NOTE: not sure if this is particularly useful 
currProtein=[]
#this gets list of every chain
for ch in cmd.get_chains():
    currProtein.append(ch)
#makes the transparency of the item not in altered protein seq lower (in theory. doesn't seem to work tho :<)
for i in currProtein:
    if i not in altered_protein:
        cmd.set('transparency', 0.3)
#renames the chain
for i in range(len(altered_protein)):
    cmd.alter(f'chain {altered_protein[i][0]}', f'chain="{altered_protein[i][1]}"')

#select
for i in range(len(altered_protein)):
    cmd.select(f"{altered_protein[i][1]}", f"chain {altered_protein[i][1]}")
# epitotes
for i in range(len(altered_protein)):
    if altered_protein[i][1] !="wt_rbd":
        cmd.select("epi "+altered_protein[i][1], f"chain wt_rbd within 4.0 of chain {altered_protein[i][1]}")
# paratope
for i in range(len(altered_protein)):
    if altered_protein[i][1] != "wt_rbd":
        cmd.select("para "+altered_protein[i][1], f"chain {altered_protein[i][1]} within 4.0 of chain wt_rbd")


epi_vh_p=cmd.index("epi_vh")
epi_vl_p=cmd.index("epi_vl")
para_vh_p=cmd.index("para_vh")
para_vl_p=cmd.index("para_vl")


# g=open("vl_7chb1.txt", "w")
# for i in range(len(epi_vl_p)):
#     for j in range(len(para_vl_p)):
#         x=cmd.get_distance(f"id {epi_vl_p[i][1]}", f"id {para_vl_p[j][1]}")
#         g.write(f"{x} {para_vl_p[j][1]} {epi_vl_p[i][1]} \n" )

print(len(epi_vh_p))
print(len(para_vh_p))
f=open("vh_7chb1.txt", "w")
for i in range(len(epi_vh_p)):
    for j in range(len(para_vh_p)):
        x=cmd.get_distance(f"id {epi_vh_p[i][1]}", f"id {para_vh_p[j][1]}")
        f.write(f"{x} {para_vh_p[j][1]} {epi_vh_p[i][1]} \n" )

# # paratope
# for i in range(len(altered_protein)):
#     if altered_protein[i][1] != "wt_rbd":
#         cmd.select(f"wt+{altered_protein[i][1]}", f"chain {altered_protein[i][1]}+wt_rbd")
# for i in range(len(altered_protein)):
#     if altered_protein[i][1] != "wt_rbd":
#         x=cmd.util.interchain_distances(f"wt+{altered_protein[i][1]}_interchain_any", f"wt+{altered_protein[i][1]}", cutoff=5.0)
#         # f.write(x)