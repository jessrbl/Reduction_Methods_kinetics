import cantera as ct
import numpy as np

target_species = 'CH4'


def get_reactions_map():
    gas = ct.Solution('gri30.yaml')
    gas.TPX = 1200, ct.one_atm, 'CH4:1,O2:2,N2:7.52'
    reactions = gas.reactions()
    
    reaction_species_map = {}
    for i, reaction in enumerate(reactions, start=1):  # Começando a indexação de 1
        reactants = set(reaction.reactants.keys())
        products = set(reaction.products.keys())
        
        for species in reactants.union(products):
            if species not in reaction_species_map:
                reaction_species_map[species] = set()
            reaction_species_map[species].add(i)  # Adicionando o índice da reação corretamente

    return reactions, reaction_species_map

# Chamando a função e capturando os valores retornados
reactions, reaction_species_map = get_reactions_map()

# Imprimindo as informações corrigidas
print("Reações:")
for i, reaction in enumerate(reactions, start=1):  # Começando a indexação de 1
    print(f"Reação {i}: {reaction.equation}")

print("\nMapa de Espécies e Reações:")
for species, reactions_involved in reaction_species_map.items():
    print(f"Espécie: {species}, Reações Envolvidas: {reactions_involved}")




