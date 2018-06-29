#!/usr/bin/python3
import Bio.PDB
import numpy as np
import matplotlib.pyplot as plt

phi_psi = ([0, 0])
phi_psi = np.array(phi_psi)
pdb1 = '1yjp.pdb'

for model in Bio.PDB.PDBParser().get_structure('1YJP', pdb1):
    for chain in model:
        polypeptides = Bio.PDB.PPBuilder().build_peptides(chain)
        for poly_index, poly in enumerate(polypeptides):
            print("Model %s Chain %s" % (str(model.id), str(chain.id))),
            print("(part %i of %i)" % (poly_index+1, len(polypeptides))),
            print("length %i" % (len(poly))),
            print("from %s%i" % (poly[0].resname, poly[0].id[1])),
            print("to %s%i" % (poly[-1].resname, poly[-1].id[1]))
            phi_psi = poly.get_phi_psi_list()
            for res_index, residue in enumerate(poly):
                # res_name = "%s%i" % (residue.resname, residue.id[1])
                # print res_name, phi_psi[res_index]
                phi_psi = np.vstack([phi_psi, np.asarray(phi_psi[res_index])]).astype(np.float)
                # np.float - conversion to float array from object

phi, psi = np.transpose(phi_psi)

phi = np.degrees(phi)
psi = np.degrees(psi)

phi = phi[~np.isnan(phi)]  # avoiding nan
psi = psi[~np.isnan(psi)]

plt.xticks(np.arange(-180, 180, 60))
plt.yticks(np.arange(-180, 180, 60))

# plt.title('Ramachandran Plot for 1YJP')
plt.xlabel('$\phi^o$', size=40, fontsize=30)
plt.ylabel('$\psi^o$ ', size=40, fontsize=30)
plt.xlim(-180, 180)
plt.ylim(-180, 180)
plt.grid(True, linewidth=1.5)
plt.axes().set_aspect(1)

plt.scatter(phi, psi)

# h = ax.hexbin(phi, psi, gridsize=25, extent=[-180, 180, -180, 180], cmap=(plt.cm.get_cmap('Blues')), linewidth=5.0)
# ax.tick_params(axis='both', which='major', labelsize=18)
# ax.grid(color='black', linestyle='solid', linewidth=10)

# h = ax.hexbin(phi, psi, gridsize=35,  extent=[-180,180,-180,180], cmap=plt.cm.Blues)

# f.colorbar(h)
plt.show()
