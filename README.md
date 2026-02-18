# Alpha-synuclein inhibitor design via BoltzGen

1. Install uv: https://docs.astral.sh/uv/getting-started/installation/
2. Install boltzgen: `uv tool install boltzgen`
3. Run boltzgen: `boltzgen run config/ --cache=/scratch/birt.k/bg-cache/ --output=<output-path> --protocol=protein-anything --num-design=10 --budget=2`

## Config explanation

* PDB 6CU7 was used as described here: https://www.nature.com/articles/s41589-024-01580-x
    * Residue 1: His50−Lys58, config/01-50-58.yaml
    * Residue 2: Thr72−Val77, config/02-72-77.yaml
* We want a protein to bind to this, so we use `--protocol=protein-anything` - TODO: try other methods
* For testing, we use `--num-design=10`. For the actual run, we'll use `--num-design=10,000` as a minimum. Maybe increase by orders of magnitude for fun
* For the designed proteins, we'll make them somewhat small (less than 200 residues), since those generally work better

