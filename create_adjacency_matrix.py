import cantera as ct
import numpy as np

def create_adjacency_matrix(state, solution):
   temp, pressure, mole_fractions = state
   solution.TPX = temp, pressure, mole_fractions


   product_stoich_coeffs = solution.product_stoich_coeffs  #no cantera 3.0, não precisa dos parênteses
   reactant_stoich_coeffs = solution.product_stoich_coeffs
   net_stoich_coeffs = product_stoich_coeffs - reactant_stoich_coeffs 

    #verificar quais espécies participam as reações. se participam, atribui 1, se não, atribui 0. 
   delta_Bi = np.where(((product_stoich_coeffs != 0) | (reactant_stoich_coeffs != 0)), 1, 0) 

   valid_reactions = np.where(solution.net_rates_of_progress != 0)[0]
   if valid_reactions.size:
    net_production_rate = np.abs(net_stoich_coeffs[:, valid_reactions] * solution.net_rates_of_progress[valid_reactions])
    denominator = np.sum(net_production_rate, axis=1)[:, np.newaxis]
    numerator = np.zeros((solution.n_species, solution.n_species))
    for species_B in range(solution.n_species):
          numerator[:, species_B] += np.sum(net_production_rate[:, np.where(delta_Bi[species_B, valid_reactions])[0]], axis=1)
          with np.errstate(divide='ignore', invalid='ignore'):
              adjacency_matrix = np.where(denominator != 0, numerator / denominator, 0)

    else: 
        adjacency_matrix = np.zeros((solution.n_species, solution.n_species))    

    # set diagonals to zero, to avoid self-directing graph edges
    np.fill_diagonal(adjacency_matrix, 0.0)

    return adjacency_matrix

#------------------------------------------------------------------------
print("Script executado com sucesso!")

