# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pdbfixer",
#   "openmm",
# ]
# ///

from openmm import *
from openmm.app import *
from openmm.unit import *
from pdbfixer import PDBFixer


def prep_complex(input_pdb: str, output_pdb: str):
    fixer = PDBFixer(filename=input_pdb)
    fixer.findMissingResidues()
    fixer.findNonstandardResidues()
    fixer.replaceNonstandardResidues()
    fixer.removeHeterogens(True)
    fixer.findMissingAtoms()
    fixer.addMissingAtoms()
    fixer.addMissingHydrogens(7.0)  # pH 7

    # Solvate in a 10 Å padding water box
    fixer.addSolvent(padding=10 * angstroms, ionicStrength=0.15 * molar)

    with open(output_pdb, "w") as f:
        PDBFile.writeFile(fixer.topology, fixer.positions, f)

    return fixer.topology, fixer.positions


if __name__ == "__main__":
    import sys

    prep_complex(sys.argv[1], sys.argv[2])
