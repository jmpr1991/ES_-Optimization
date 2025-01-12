import constants
import functions

import numpy as np

def survival_selection_function(mutated_vector, parent_vector):

    #initialize adaptation value
    adaptation_value = np.full(shape=(constants.POPULATION_SIZE + constants.OFFSPRING_SIZE, 2), fill_value=np.nan)

    #evaluate mutated vector
    for i in range(constants.OFFSPRING_SIZE):

        # save the index to support on the sort process
        adaptation_value[i, 1] = i

        if constants.FUNCTION == 'SPHERE':
            adaptation_value[i, 0] = functions.shifted_sph_fun(mutated_vector[0:constants.DIM, i])

        if constants.FUNCTION == 'SCHWEFEL':
            adaptation_value[i, 0] = functions.schwefel_fun(mutated_vector[0:constants.DIM, i])

    if constants.SELECTION_TYPE == 'NO_ELITISM':
        sorted_adaptation_value = adaptation_value[np.argsort(adaptation_value[:,0]), :]

        survival_population = mutated_vector[:, sorted_adaptation_value[0:constants.POPULATION_SIZE, 1].astype(int)]

        return survival_population, sorted_adaptation_value[0:constants.POPULATION_SIZE, 0]

    # evaluate parent vector
    counter = 0
    for i in range(constants.OFFSPRING_SIZE, constants.OFFSPRING_SIZE + constants.POPULATION_SIZE, 1):

        # save the index to support on the sort process
        adaptation_value[i, 1] = i

        if constants.FUNCTION == 'SPHERE':
            adaptation_value[i, 0] = functions.shifted_sph_fun(parent_vector[0:constants.DIM, counter])

        if constants.FUNCTION == 'SCHWEFEL':
            adaptation_value[i, 0] = functions.schwefel_fun(parent_vector[0:constants.DIM, i])

        counter = counter + 1

    if constants.SELECTION_TYPE == 'ELITISM':
        sorted_adaptation_value = adaptation_value[np.argsort(adaptation_value[:, 0]), :]

        #vector containing mutated vector and parent vector
        elitist_vector = np.concatenate((mutated_vector, parent_vector),axis=1)

        survival_population = elitist_vector[:, sorted_adaptation_value[0:constants.POPULATION_SIZE, 1].astype(int)]

        return survival_population, sorted_adaptation_value[0:constants.POPULATION_SIZE, 0]