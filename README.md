# Python Pymol Script to automate the mutaion calling and automate the mutation in PDB
## _Python Pymol for automate mutagenesis_

PyMOL is a powerful molecular visualization tool used extensively in structural biology for visualizing macromolecular structures and conducting a variety of molecular modeling tasks, including mutagenesis. By leveraging PyMOL's scripting capabilities with Python, automate the process of introducing mutations into protein structures, streamlining tasks that would otherwise be labor-intensive.


## Features

- **Automated Structure Loading**: Loads a protein structure from a PDB file into PyMOL.
- **Residue Selection and Mutation**: Automatically selects specific residues and performs mutagenesis, changing them to specified new residues.
- **Batch Mutagenesis**: Processes a list of mutations, applying multiple changes in a single run.
- **Structure Saving**: Saves the modified protein structure to a new PDB file.
- **Command Line Execution**: Allows the script to be run from the command line, facilitating integration into larger workflows.
- **Visualization Setup**: Sets up the initial visualization style in PyMOL for better clarity of the protein structure.
- **Flexibility**: Easily customizable for different proteins, chains, residues and mutation types.
- **Non-interactive Mode**: Runs PyMOL in quiet mode without a GUI, suitable for automated pipelines and remote execution.
- **Error Handling**: Basic error handling can be added to manage issues like invalid residue selections or unsupported mutations.
- **Extensibility**: Can be extended with additional features such as automated energy minimization, validation of mutated structures and integration with external databases for mutation information.

## Installation

This script requires [PyMol](https://pymol.org/) and [Python](https://www.python.org/) to run.

Install the dependencies

Install [Python](https://www.python.org/)
Install [Anaconda](https://docs.anaconda.com/anaconda/install/)
Then install pymol. 
```sh
conda install -c conda-forge -c schrodinger pymol-bundle
```

## Run
First clone this repositary. 
To run the script you need an external csv file, where 
**For Single Mutation** 
Y150W
K67R
Seprated in new line.
**For Double Mutation**
Y150W,K67R
Y150W,K67H
Every mutation is defined by comma then seprated by new line. 
**For Multi Mutation**
Rule is same. Every mutation is defined by comma then separated by new line. 

Then run :

```sh
python python_pymol_mutation_updated.py <pdb_file_to_load> <mutation_file> <chain_name>
```
