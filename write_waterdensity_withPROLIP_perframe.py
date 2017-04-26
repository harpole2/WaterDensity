import MDAnalysis as mda
from MDAnalysis.analysis.density import density_from_Universe
u = mda.Universe('../../step7_1.gro', '../../all_c_long.xtc')

sto=len(u.trajectory)
for i in range(0,sto):
	x=i+1
	D=density_from_Universe(u, delta=1.0,start=i,stop=x,step=1, atomselection="name OH2",padding=0)
	P=density_from_Universe(u, delta=1.0,start=i,stop=x,step=1, atomselection="protein",padding=0)
	L=density_from_Universe(u, delta=1.0,start=i,stop=x,step=1, atomselection="resname POPC",padding=0)
	D.convert_density('TIP3P') #assuming TIP3P
	D.export('water_density_convert_'+str(i)+'.dx')
	P.export('protein_density_notconvert_'+str(i)+'.dx')
	L.export('lipid_density_notconvert_'+str(i)+'.dx')


	

