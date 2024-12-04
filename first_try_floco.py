from itertools import product, combinations
from collections import Counter
import random

class Person:
    def __init__(self, sex, age, genotype, parents):
        if not sex in ['male', 'female']:
            raise ValueError(f'Input error -> only female or male')
        if not age in range(0, 110):
            raise ValueError(f'Input error -> invalid age')
        if genotype not in ['AA', 'A0', '0A', 'BB', 'B0', '0B', 'AB', 'BA', '00']:
            raise ValueError(f'Input error -> invalid genotype')

        self.sex = sex
        self.age = age
        self.genotype = genotype
        self.phenotype = self.det_phenotype()

        self.can_mate = 13 <= age <= 50
        self.parents = parents

    def det_phenotype(self):
        if self.genotype in ['AA', 'A0', '0A']:
            return 'A'
        elif self.genotype in ['BB', 'B0', '0B']:
            return 'B'
        elif self.genotype in ['00']:
            return '0'
        elif self.genotype in ['AB', 'BA']:
            return 'AB'

    def __str__(self):
        return f"{self.age}, {self.sex}, {self.genotype} -> {self.phenotype}"



class Population():
    def __init__(self):
        self.population = []

    def initialize_population(self, pop_size: int):
        for i in range(1, pop_size + 1):
            sex = random.choice(['male', 'female'])
            age = random.randint(0, 100)
            x = random.choice(['A', 'B', '0'])
            y = random.choice(['A', 'B', '0'])
            genotype = x + y
            self.population.append(Person(sex, age, genotype, None))

    def age_population(self):
        for person in self.population:
            person.age += 1
            if person.age >= 100:
                self.population.remove(person)

    def __str__(self):
        return '\n'.join(str(person) for person in self.population)


def create_offspring(p1 : Person, p2 : Person):
    if not p1.can_mate and not p2.can_mate:
        raise AssertionError(f"Zu jung oder zu alt um Kinder zu bekommen")
    elif (p1.sex, p2.sex) not in [('male', 'female'), ('female', 'male')]:
        raise AssertionError(f"Geht halt biologisch nicht...")
    elif p1.parents[0] in p2.parents:
        raise AssertionError(f"Das wäre Inzest..")
    elif p1.parents[1] in p2.parents:
        raise AssertionError(f"Das wäre Inzest..")
    else:
        sex = random.choice(['male', 'female'])
        par_types = [(p1.genotype[0], p1.genotype[1]), (p2.genotype[0], p2.genotype[1])]
        possible_genotypes = [x + y for x in par_types[0] for y in par_types[1]]
        genotype = random.choice(possible_genotypes)

        return Person(sex, 0, genotype, (p1, p2))



pop = Population()
pop.initialize_population(20)

print(pop)

for time in range(10):
    pop.age_population()

print("\n")
print(pop)