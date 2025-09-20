database(
    thermoLibraries = ['primaryThermoLibrary',
                        'SABIC_aromatics',], 
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)

# List of species
species(
        label='C6H14',
        reactive=True,
        structure=SMILES("CCCCCC")
        )

species(
        label='C2H2',
        reactive=True,
        structure=SMILES("C#C")
        )

species(
        label='C2H4',
        reactive=True,
        structure=SMILES("C=C")
        )

species(
        label='C2H6',
        reactive=True,
        structure=SMILES("CC")
        )

species(
        label='C3H8',
        reactive=True,
        structure=SMILES("CCC")
        )

species(
        label='C3H6',
        reactive=True,
        structure=SMILES("CC=C")
        )

species(
        label='CH4',
        reactive=True,
        structure=SMILES("C")
        )

species(
        label='CH3',
        reactive=True,
        structure=SMILES("[CH3]")
        )

species(
        label='CH2',
        reactive=True,
        structure=SMILES("[CH2]")
        )
        
species(
        label='C6H6',
        reactive=True,
        structure=SMILES("c1ccccc1")
        )

species(
        label='H2',
        reactive=True,
        structure=SMILES("[H][H]")
        )

species(
        label='H',
        reactive=True,
        structure=SMILES("[H]")
        )

species(
        label='Ar',
        reactive=False,
        structure=SMILES("[Ar]")
        )

# forbidden
forbidden(
        label='O2',
        structure=adjacencyList("""
            1 O u1 p2 {2,S}
            2 O u1 p2 {1,S}
            """),
)


# Reaction systems
simpleReactor(
    temperature=(1373,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "C6H14": 0.073,
        "Ar": 0.463,
        "H2": 0.463,
    },
    terminationConversion={
        'C6H14': 0.9,
    
    },
    terminationTime=(1e6,'s'),
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.1,
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=100000,
    filterReactions=True,
)

generatedSpeciesConstraints(
    maximumCarbonAtoms=7,
)


options(
    units='si',
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
    )
