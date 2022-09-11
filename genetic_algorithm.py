from re import I
from statistics import mean
import random


def log_generation_data(population: list[str], population_eval: list[int], generation_num: int):
    print(f'--- Generation #{generation_num} Statistics ---')
    print('\tBest individual: ', population[population_eval.index(max(population_eval))])
    print('\tBest individual aptitude: ', max(population_eval))
    print('\tAverage aptitude: ', mean(population_eval))
    print('\n\n')

def evaluate(population: list[str]) -> list[int]:
    max_aptitude = len(population[0])
    aptitudes = []
    for individual in population:
        aptitudes.append((individual.count('1') / max_aptitude))

    return aptitudes

def select(population: list[str], population_eval: list[int]):
    total = sum(population_eval)
    weights = [population_eval[i] / total for i in range(len(population))]
    
    return random.choices(population, weights, k=len(population))

def reproduce(population: list[str]):
    x = 0
    y = 1
    while y < len(population):
        ind1 = population[x]
        ind2 = population[y]

        cross = random.randint(1, len(ind1) - 1)

        offspring1 = ind1[:cross] + ind2[cross:]
        offspring2 = ind2[:cross] + ind1[cross:]

        population[x] = offspring1
        population[y] = offspring2

        x += 2
        y += 2

def mutate(population: list[str]):
    while random.randint(0, 1):
        individual_idx = random.randint(0, len(population) - 1)
        gen_idx = random.randint(0, len(population[individual_idx]) - 1)

        new_individual = list(population[individual_idx])
        new_individual[gen_idx] = '0' if new_individual[gen_idx] == '1' else '1'
        population[individual_idx] = ''.join(new_individual)

def is_convergent(population: list[str]):
    model = population[0]
    individual_idx = 1

    while individual_idx < len(population):
        for char_idx in range(len(model)):
            individual = population[individual_idx]
            if model[char_idx] != individual[char_idx]:
                return False
        
        individual_idx += 1

    return True

def genetic(N = 14, L = 10):
    generation_num = 1
    population = []

    for _ in range(N):
        population.append(f'{random.getrandbits(L):0{L}b}')
        
    population_eval = evaluate(population)

    log_generation_data(population, population_eval, generation_num)

    while not is_convergent(population):
        population = select(population, population_eval)
        reproduce(population)
        mutate(population)
        population_eval = evaluate(population)
        
        generation_num += 1
        log_generation_data(population, population_eval, generation_num)
        

    return population

    

if __name__ == '__main__':
    with_defaults = input('Run algorithm with defaults (N=14, L=10)? (Y/n) ')


    if with_defaults.casefold() == 'y':
        print(genetic())
    else:
        N = int(input('# of individuals: '))
        L = int(input('# of bits for each individual: '))
        print(genetic(N, L))