# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "mdtraj",
#   "numpy",
# ]
# ///

import mdtraj as md
import numpy as np

def analyze_complex(topology_pdb: str, trajectory_dcd: str):
    traj = md.load(trajectory_dcd, top=topology_pdb)
    
    # Select chain A (alpha-synuclein) and chain B (designed binder)
    asynuc = traj.topology.select('chainid 0')
    binder = traj.topology.select('chainid 1')
    
    # RMSD of binder relative to initial pose — did it stay bound?
    rmsd = md.rmsd(traj, traj, 0, atom_indices=binder)
    
    # Contacts between chains (proxy for binding)
    contacts, _ = md.compute_contacts(traj, scheme='closest-heavy')
    
    # Number of inter-chain contacts < 4.5 Å
    n_contacts = np.sum(contacts < 0.45, axis=1)
    
    print(f"Mean inter-chain contacts: {n_contacts.mean():.1f}")
    print(f"Binder RMSD range: {rmsd.min():.2f} – {rmsd.max():.2f} nm")
    
    return rmsd, n_contacts
