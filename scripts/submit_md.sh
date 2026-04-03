#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --gres=gpu:v100-sxm2:1
#SBATCH --ntasks=1
#SBATCH --mem=16GB
#SBATCH --time=24:00:00
#SBATCH --job-name=md-synuclein

DESIGN_PDB=$1          # e.g. boltzgen_out/design_001.pdb
NAME=$(basename $DESIGN_PDB .pdb)
SCRATCH=/scratch/$(whoami)/md-out/$NAME

mkdir -p $SCRATCH

# Prep
python scripts/prep_system.py $DESIGN_PDB $SCRATCH/prepped.pdb

# Run
python scripts/run_md.py $SCRATCH/prepped.pdb $SCRATCH/prod
