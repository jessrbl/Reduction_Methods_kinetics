import cantera as ct

target_species = 'CH4'

def get_reactions_map():
    gas = ct.Solution('gri30.yaml')
    gas.TPX = 1200, ct.one_atm, 'CH4:1,O2:2,N2:7.52'
    reactions = gas.reactions()
    
    reaction_species_map = {}
    for i, reaction in enumerate(reactions, start=1):  
        reactants = set(reaction.reactants.keys())
        products = set(reaction.products.keys())
        
        for species in reactants.union(products):
            if species not in reaction_species_map:
                reaction_species_map[species] = set()
            reaction_species_map[species].add(i)  

    return reactions, reaction_species_map

def find_species_with_shared_reactions(target_species, reactions, reaction_species_map):
    target_reactions = reaction_species_map.get(target_species, set())
    shared_species = set()

    for species, reactions_involved in reaction_species_map.items():
        if target_species != species and target_reactions.intersection(reactions_involved):
            shared_species.add(species)

    return shared_species

reactions, reaction_species_map = get_reactions_map()

print("\nMapa de Espécies e Reações:")
for species, reactions_involved in reaction_species_map.items():
    print(f"Espécie: {species}, Reações Envolvidas: {reactions_involved}")

shared_species = find_species_with_shared_reactions(target_species, reactions, reaction_species_map)

print(f"\nEspécies que compartilham pelo menos uma reação com {target_species}: {shared_species}")
