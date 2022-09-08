from statistics import mean
import random


def evaluate_population(population: list[str]) -> list[int]:
    max_aptitude = len(population[0])
    aptitudes = []
    for individual in population:
        aptitudes.append((individual.count('1') / max_aptitude))

    return aptitudes

def select(population: list[str], population_eval: list[int]):
    new_population = []
    for _ in range(len(population)):
        new_population.append()

def genetic(N = 14, L = 10):
    population = []

    for _ in range(N):
        population.append(f'{random.getrandbits(L):0{L}b}')
    population_eval = evaluate_population(population)

    while mean(population_eval) < 1:
        selection = select(population, population_eval)
        

    return population

    

if __name__ == '__main__':
    with_defaults = input('Run algorithm with defaults (N=14, L=10)? (Y/n) ')


    if with_defaults.casefold() == 'y':
        print(genetic())
    else:
        N = int(input('# of individuals: '))
        L = int(input('# of bits for each individual: '))
        print(genetic(N, L))