#put in the PDB code
cmd.fetch("7CHB")

altered_protein=[]
#note:[chain identifier, what to rename it as] add more as needed
altered_protein.append(["H", "vh"])
altered_protein.append(["L", "vl"])
altered_protein.append(["R", "wt_rbd"])


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

# for heavy chain subregion
region=[]
#note:[what to rename it to, residue location] add as needed
region.append(["vh_fr1", "1-25"])
region.append(["vh_cdr1", "26-33"])
region.append(["vh_fr2", "34-50"])
region.append(["vh_cdr2", "51-57"])
region.append(["vh_fr3", "58-95"])
region.append(["vh_constant", "96-97"])

#renames specific regions to names specified above
for i in range(len(region)):
    cmd.select(region[i][0], "chain vh and resi "+region[i][1])
# epitotes, heavy chain subregions
for i in range(len(region)):
    cmd.select("epi "+region[i][0], f"(chain wt_rbd) within 4.0 of (chain vh and resi {region[i][1]})")
# paratope, hc, subregion
for i in range(len(region)):
    cmd.select("para "+region[i][0], f"(chain vh and resi {region[i][1]}) within 4.0 of (chain wt_rbd)")
# h-bond, hc, subregion
for i in range(len(region)):
    cmd.distance("h_"+region[i][0], "epi_"+region[i][0], "para_"+region[i][0], 3.5, 2)

