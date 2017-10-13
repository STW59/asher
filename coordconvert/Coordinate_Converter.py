#!/usr/local/bin/python

import numpy as np

"""
Program reads a text file in PDB format and outputs two tables: 
Table 1 - Atom numbers with bond lengths and bond angle.
Table 2 - Residue number with phi, psi, and omega dihedral angles. 
"""

INPUT_FILENAME = "1qcq.pdb"
TABLE1_OUTPUT = "1qcq_t1.txt"
TABLE2_OUTPUT = "1qcq_t2.txt"


def calc_bond_length(r0, r1):
    """
    Calculates bond lengths given two position vectors
    :param r0: position of first atom
    :param r1: position of second atom
    :return: returns bond length
    """
    return np.sqrt((r0[0] - r1[0])**2 + (r0[1] - r1[1])**2 + (r0[2] - r1[2])**2)


def calc_bond_angle(r1, r2, r3):
    """
    Calculates the bond angle (theta) given three position vectors
    :param r1: position of first atom
    :param r2: position of second atom
    :param r3: position of third atom
    :return: returns angle theta
    """
    return 180 - np.degrees(np.arccos(np.dot(r3-r2, r2-r1)/(calc_bond_length(r3, r2) * calc_bond_length(r2, r1))))


def calc_dihedral(r1, r2, r3, r4):
    """
    Calculates the dihedral angle between four position vectors
    :param r1: position of first atom
    :param r2: position of second atom
    :param r3: position of third atom
    :param r4: position of fourth atom
    :return: returns dihedral angle
    """
    l1 = r2 - r1
    l2 = r3 - r2
    l3 = r4 - r3
    l1xl2 = np.cross(l1, l2)
    l2xl3 = np.cross(l2, l3)

    if np.dot(l1xl2, l3) < 0:
        sign = -1
    else:
        sign = 1

    return sign * np.degrees(np.arccos(np.dot(l1xl2, l2xl3) /
                                       (np.sqrt(l1xl2[0]**2 + l1xl2[1]**2 + l1xl2[2]**2) *
                                        np.sqrt(l2xl3[0]**2 + l2xl3[1]**2 + l2xl3[2]**2))))


def main():
    # Gather data on all backbone atoms from input file
    all_atoms = []

    input_file = open(INPUT_FILENAME, 'r')
    for line in input_file:
        if line[0:4] == "ATOM" and line[13:15] in ("N ", "CA", "C "):  # Filter based on PDB file structure and atom type
            index = int(line[6:11])  # Atom number
            atom = str(line[13:15])  # Atom type: Amine nitrogen (N), Alpha carbon (CA), or carbonyl carbon (C)
            if ' ' in atom:
                atom = atom.replace(' ', '')  # Remove spaces in atom name
            residue = str(line[17:20])  # Amino acid label
            atom_loc = np.array([float(line[30:38]),
                                 float(line[38:46]),
                                 float(line[46:54])])  # x, y, and z coordinates of atom

            atom_data = [index, atom, residue, atom_loc]
            all_atoms.append(atom_data)
    input_file.close()

    # Build Table 1
    bonds_angles = []

    for n in range(0, len(all_atoms)):
        try:
            atom0 = all_atoms[n - 1]
            atom1 = all_atoms[n]
            atom2 = all_atoms[n + 1]
        except IndexError:
            pass

        if n == 0:  # First atom does not have a bond length or angle
            bonds_angles.append([1, 'N/A', 'N/A'])
        elif n == len(all_atoms) - 1:  # Last backbone atom doesn't have a bond angle
            bond_length = calc_bond_length(atom0[3], atom1[3])
            bonds_angles.append([atom1[0], round(bond_length, 3), 'N/A'])
        else:
            bond_length = calc_bond_length(atom0[3], atom1[3])
            theta = calc_bond_angle(atom0[3], atom1[3], atom2[3])
            bonds_angles.append([atom1[0], round(bond_length, 3), np.around(theta, 3)])

    t1 = open(TABLE1_OUTPUT, 'w')
    t1.write('Table 1: Bond Length and Supplemental Bond Angle Theta\n')
    t1.write('Index  Atom  Bond Length  Theta\n')
    for n in range(0, len(bonds_angles)):
        col_index = str(bonds_angles[n][0]) + '{}'.format(' ' * (7 - len(str(bonds_angles[n][0]))))
        col_atom = str(all_atoms[n][1]) + '{}'.format(' ' * (6 - len(str(all_atoms[n][1]))))
        col_bond_length = str(bonds_angles[n][1]) + '{}'.format(' ' * (13 - len(str(bonds_angles[n][1]))))
        col_theta = str(bonds_angles[n][2])
        t1.write(str(col_index) + str(col_atom) + str(col_bond_length) + str(col_theta) + '\n')
    t1.close()

    # Build Table 2
    dihedrals = []

    # Calc Phi, Psi, Omega
    # Calculates all three angles for a residue and moves to the next amino acid
    index = 1
    for n in range(1, len(all_atoms), 3):
        try:
            atom0 = all_atoms[n - 2]
            atom1 = all_atoms[n - 1]
            atom2 = all_atoms[n]
            atom3 = all_atoms[n + 1]
            atom4 = all_atoms[n + 2]
            atom5 = all_atoms[n + 3]
        except IndexError:
            pass

        if n == 1:  # First residue does not have a phi angle
            phi = 'N/A'
            psi = np.around(calc_dihedral(atom1[3], atom2[3], atom3[3], atom4[3]), 3)
            omega = np.around(calc_dihedral(atom2[3], atom3[3], atom4[3], atom5[3]), 3)
        elif n == len(all_atoms) - 2:  # Last residue does not have psi or omega angles
            phi = np.around(calc_dihedral(atom0[3], atom1[3], atom2[3], atom3[3]), 3)
            psi = 'N/A'
            omega = 'N/A'
        else:
            phi = np.around(calc_dihedral(atom0[3], atom1[3], atom2[3], atom3[3]), 3)
            psi = np.around(calc_dihedral(atom1[3], atom2[3], atom3[3], atom4[3]), 3)
            omega = np.around(calc_dihedral(atom2[3], atom3[3], atom4[3], atom5[3]), 3)

        dihedrals.append([index, atom2[2], phi, psi, omega])
        index += 1

    # Table 2: Index, Residue, Phi, Psi, Omega
    t2 = open(TABLE2_OUTPUT, 'w')
    t2.write('Table 2: The Three Dihedrals\n')
    t2.write('Index  Residue  Phi       Psi       Omega\n')
    for residue in dihedrals:
        col_index = str(residue[0]) + '{}'.format(' ' * (7 - len(str(residue[0]))))
        col_residue = str(residue[1]) + '{}'.format(' ' * (9 - len(str(residue[1]))))
        col_phi = str(residue[2]) + '{}'.format(' ' * (10 - len(str(residue[2]))))
        col_psi = str(residue[3]) + '{}'.format(' ' * (10 - len(str(residue[3]))))
        col_omega = str(residue[4])
        t2.write(col_index + col_residue + col_phi + col_psi + col_omega + '\n')
    t2.close()


main()
