# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "openmm",
# ]
# ///

import sys

from openmm import *
from openmm.app import *
from openmm.unit import *


def run_md(
    prepped_pdb: str, output_prefix: str, n_steps: int = 50_000_000
):  # 100 ns at 2 fs timestep

    pdb = PDBFile(prepped_pdb)

    # CHARMM36m — best for IDPs like alpha-synuclein
    forcefield = ForceField("charmm36m.xml", "charmm36/water_tip3p-pme.xml")

    system = forcefield.createSystem(
        pdb.topology,
        nonbondedMethod=PME,
        nonbondedCutoff=1.2 * nanometer,
        constraints=HBonds,
        hydrogenMass=1.5 * amu,  # allows 4 fs timestep
    )

    # Langevin integrator (NVT)
    integrator = LangevinMiddleIntegrator(
        300 * kelvin, 1 / picosecond, 2 * femtoseconds
    )

    # Barostat for NPT production
    system.addForce(MonteCarloBarostat(1 * bar, 300 * kelvin))

    platform = Platform.getPlatformByName("CUDA")
    properties = {"CudaPrecision": "mixed"}

    simulation = Simulation(pdb.topology, system, integrator, platform, properties)
    simulation.context.setPositions(pdb.positions)

    # Minimize
    print("Minimizing...")
    simulation.minimizeEnergy(maxIterations=1000)

    # Reporters
    simulation.reporters.append(DCDReporter(f"{output_prefix}.dcd", 5000))
    simulation.reporters.append(
        StateDataReporter(
            f"{output_prefix}.csv",
            5000,
            step=True,
            time=True,
            potentialEnergy=True,
            temperature=True,
            density=True,
            progress=True,
            totalSteps=n_steps,
        )
    )
    simulation.reporters.append(CheckpointReporter(f"{output_prefix}.chk", 50000))

    print(f"Running {n_steps} steps...")
    simulation.step(n_steps)


if __name__ == "__main__":
    run_md(sys.argv[1], sys.argv[2])
