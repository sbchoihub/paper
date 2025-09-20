database(
    thermoLibraries = ['primaryThermoLibrary',], 
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
    temperature=(1273,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "C6H14": 0.004,
        "Ar": 0.996,
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
    maximumCarbonAtoms=6,
)


options(
    units='si',
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
    )
