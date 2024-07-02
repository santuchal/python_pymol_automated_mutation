import sys
import os
from pymol import cmd

def load_and_prepare_pdb(pdb_file):
    cmd.reinitialize()
    cmd.load(pdb_file)

def get_mutations_from_file(mutation_file):
    with open(mutation_file, 'r') as f:
        return [line.strip() for line in f]

def mutate_residue(molecule, chain, resi, target):
    cmd.wizard("mutagenesis")
    cmd.get_wizard().set_mode(target)
    selection = f"/{molecule}//{chain}/{resi}"
    cmd.get_wizard().do_select(selection)
    cmd.get_wizard().apply()
    cmd.set_wizard()

def create_output_folder(folder_name):
    """Create the output folder if it doesn't exist."""
    output_path = os.path.join('output', folder_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    return output_path

def main(pdb_file_to_load, mutation_file, chain_name):
    three_letter = {
        'V': 'VAL', 'I': 'ILE', 'L': 'LEU', 'E': 'GLU', 'Q': 'GLN', 'D': 'ASP', 'N': 'ASN', 'H': 'HIS', 'W': 'TRP', 'F': 'PHE', 'Y': 'TYR', 'R': 'ARG', 'K': 'LYS', 'S': 'SER', 'T': 'THR', 'M': 'MET', 'A': 'ALA', 'G': 'GLY', 'P': 'PRO', 'C': 'CYS'}

    mutations = get_mutations_from_file(mutation_file)

    for mutation in mutations:
        load_and_prepare_pdb(pdb_file_to_load)
        folder_name = str(mutation)
        output_path = create_output_folder(folder_name)
        residues = mutation.split(",")

        for res in residues:
            target_aa = three_letter[res[-1]]
            resi_number = int(res[1:-1])
            mutate_residue(pdb_file_to_load[:-4], chain_name, resi_number, target_aa)
        
        cmd.save(os.path.join(output_path, f'{mutation}_out.pdb'))

if __name__ == "__main__":
    pdb_file_to_load = sys.argv[1]
    mutation_file = sys.argv[2]
    chain_name = sys.argv[3]

    print("pdb_file_to_load:", pdb_file_to_load)
    print("mutation_file:", mutation_file)
    print("chain_name:", chain_name)

    main(pdb_file_to_load, mutation_file, chain_name)
