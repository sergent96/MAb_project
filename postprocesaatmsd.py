import os
import pyrotein as pr


temp_pdb="6xc4.pdb"
temp_list=pr.atom.read(temp_pdb)
temp_dict=pr.atom.create_lookup_table(temp_list)

output=open("vh_7chb1process.csv", "w")


# for vl_7chb in os.listdir(pathway):
text_list=open(f"vh_7chb1.txt").read().split()
grouped_text_list=list(zip(*(iter(text_list),)*3))[1:] #group elements by 3
for ele1, ele2, ele3 in grouped_text_list: 
    if float(ele1)  <= 5.0:  #if less than 10, low region of read depth
        output.write(f"{ele1}|{ele2}|{ele3}\n")  