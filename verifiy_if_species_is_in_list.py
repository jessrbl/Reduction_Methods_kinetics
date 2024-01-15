import cantera as ct 

gas = ct.Solution('gri30.yaml')
gas.TPX = 1200, ct.one_atm, 'CH4:1,O2:2,N2:7.52'
reactions = gas.reactions()
species = gas.species()
species_list = ['O', 'O2', 'OH', 'H', 'H2']
leng_species_list = len(species_list)

# Extrair os nomes das espécies
species_names = [spec.name for spec in species]

# Imprimir a lista de nomes das espécies
print(species_names)

# Contar o número de nomes de espécies na lista
num_species = len(species_names)
print(f"Número de espécies: {num_species}")

# Verificar se cada espécie do mecanismo está na species_list
for spec_name in species_names:
    if spec_name in species_list:
        print(f"{spec_name} está na lista.")
    else:
        print(f"{spec_name} não está na lista.")
