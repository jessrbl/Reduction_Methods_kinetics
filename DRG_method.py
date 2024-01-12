import cantera as ct 
import numpy as np 
import matplotlib.pyplot as plt

g = ct.Solution('gri30.yaml')
species_names = g.species_names
all_reactions_of_the_mechanism = g.reaction_equations()
target_species = ['CH4']
threshold = 0.01
initial_state = 1200, 5 * ct.one_atm, 'CH4:0.35, O2:1.0, N2:3.76'

def calculate_direct_interaction_coefficient(g, target_species, species_names):
    length_number_of_species = len(species_names)
    interaction_coefficients = np.zeros(length_number_of_species)    #inicia zerado pois será calculado na sequência


    for j, species in enumerate(g.species()): 
        if species.name != target_species:
            denominator = 0  # Inicia o denominador para cada espécie

            for i, reaction in enumerate(g.reactions()):
                delta_Bi = 1 if (species in reaction.reactants) or (species in reaction.products) else 0


                stoichiometric_coefficient = reaction.product_stoich_coeffs[j] - reaction.reactant_stoich_coeffs[j]
                overall_rate = g.net_rates_of_progress[i] * stoichiometric_coefficient
                interaction_coefficients[j] += abs(overall_rate)*delta_Bi 

                 # Acumula o termo no denominador
                denominator += abs(overall_rate)

            # Aplica a fórmula completa para obter os coeficientes de interação
            if denominator > 0:
                interaction_coefficients[j] /= denominator

    return interaction_coefficients
