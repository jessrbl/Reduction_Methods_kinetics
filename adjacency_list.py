import cantera as ct
import numpy as np

def obter_reactions_map():
    gas = ct.Solution('gri30.yaml')
    gas.TPX = 1200, ct.one_atm, 'CH4:1,O2:2,N2:7.52'
    reactions = gas.reactions()
    
    reaction_species_map = {}
    for i, reaction in enumerate(reactions):
        reactants = set(reaction.reactants.keys())
        products = set(reaction.products.keys())
        
        for species in reactants.union(products):
            if species not in reaction_species_map:
                reaction_species_map[species] = set()
            reaction_species_map[species].add(i)

    return reactions, reaction_species_map

reactions, reaction_species_map = obter_reactions_map()

# Imprimindo as informações
print("Reações:")
for i, reaction in enumerate(reactions):
    print(f"Reação {i + 1}: {reaction.equation}")

print("\nMapa de Espécies e Reações:")
for species, reactions_involved in reaction_species_map.items():
    print(f"Espécie: {species}, Reações Envolvidas: {reactions_involved}")

def criar_drg_adjacency_lists(reactions, reaction_species_map):
    drg_adjacency_lists = {i: set() for i in range(len(reactions))}
    
    for species, reactions_involved in reaction_species_map.items():
        for reaction in reactions_involved:
            drg_adjacency_lists[reaction].update(reactions_involved)

    return drg_adjacency_lists

def criar_adjacency_matrix(drg_adjacency_lists):
    num_reactions = len(drg_adjacency_lists)
    adjacency_matrix = np.zeros((num_reactions, num_reactions), dtype=int)

    for i, adjacent_reactions in drg_adjacency_lists.items():
        for j in adjacent_reactions:
            adjacency_matrix[i, j] = 1

    return adjacency_matrix

def criar_species_reaction_map(reaction_species_map):
    species_reaction_map = {species: set() for species in reaction_species_map.keys()}

    for species, reactions_involved in reaction_species_map.items():
        for reaction in reactions_involved:
            species_reaction_map[species].add(reaction)

    return species_reaction_map

reactions, reaction_species_map = obter_reactions_map()
drg_adjacency_lists = criar_drg_adjacency_lists(reactions, reaction_species_map)
adjacency_matrix = criar_adjacency_matrix(drg_adjacency_lists)
species_reaction_map = criar_species_reaction_map(reaction_species_map)

# Imprimindo a matriz de adjacência
print("\nMatriz de Adjacência para o Grafo de Reações (DRG):")
print(adjacency_matrix)

