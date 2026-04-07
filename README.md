# Alpha-synuclein inhibitor design via BoltzGen

1. Install uv: https://docs.astral.sh/uv/getting-started/installation/
2. Install boltzgen: `uv tool install boltzgen`
3. Run boltzgen: `NUM_DESIGNS=10 ./run.sh`

## Config explanation

* PDB 6CU7 was used as described here: https://www.nature.com/articles/s41589-024-01580-x
    * Residue 1: His50−Lys58, config/01-50-58.yaml
    * Residue 2: Thr72−Val77, config/02-72-77.yaml
* We want a protein to bind to this, so we use `--protocol=protein-anything` - TODO: try other methods
* For testing, we use `--num-design=10`. For the actual run, we'll use `--num-design=10,000` as a minimum. Maybe increase by orders of magnitude for fun
* For the designed proteins, we'll make them somewhat small (less than 200 residues), since those generally work better


## In-Silico Validation

1. Install tools
  1. `uv tool install openmm`
  2. `uv tool install pdbfixer`
  3. `uv tool install mdtraj`
2. 
