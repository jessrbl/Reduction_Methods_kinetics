import cantera as ct 

gas = ct.Solution('gri30.yaml')
gas.TPX = 1200, ct.one_atm, 'CH4:1,O2:2,N2:7.52'
reactions = gas.reactions()
species = gas.species()

# Criar uma lista para armazenar as espécies de cada reação
species_in_reactions = []

# Iterar sobre as reações
for i, reaction in enumerate(reactions):
    # Criar uma lista para armazenar as espécies da reação atual
    species_in_current_reaction = []
    
    # Adicionar reagentes à lista
    species_in_current_reaction.extend(reaction.reactants)
    
    # Adicionar produtos à lista
    species_in_current_reaction.extend(reaction.products)
    
    # Adicionar a lista de espécies da reação atual à lista geral
    species_in_reactions.append(species_in_current_reaction)

# Imprimir a lista geral de espécies em cada reação
print("\nLista geral de espécies em cada reação:")
for i, species_list in enumerate(species_in_reactions):
    print(f"Reação {i + 1}: {species_list}")
