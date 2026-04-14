#!/bin/bash
#SBATCH --partition=gpu-interactive
#SBATCH --nodes=1
#SBATCH --gres=gpu:v100-sxm2:1
#SBATCH --ntasks=1
#SBATCH --mem=16GB
#SBATCH --time=02:00:00
rm -r /scratch/$(whoami)/bg-cache/
mkdir -p /scratch/$(whoami)/bg-cache/
/home/$(whoami)/.local/bin/boltzgen run /home/$(whoami)/bg-a-synuclein/$CONFIG --cache=/scratch/$(whoami)/bg-cache/ --output=/scratch/$(whoami)/bg-out/ --protocol=protein-anything --num_designs=$NUM_DESIGNS --budget=2
