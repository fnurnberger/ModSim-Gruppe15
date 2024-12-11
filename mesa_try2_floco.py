import mesa
from mesa.datacollection import DataCollector
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random

class Person(mesa.Agent):
    """Individual with traits"""
    def __init__(self, model, sex, gentype : [str, str]):
        super().__init__(model)

        self.sex = sex
        self.gentype = gentype
        self.phentype = self.get_phentype()

    def get_phentype(self):
        """Determine the blood type from alleles"""
        if 'A' in self.gentype and 'B' in self.gentype:
            return 'AB'
        elif 'A' in self.gentype:
            return 'A'
        elif 'B' in self.gentype:
            return 'B'
        else:
            return 'O'


class BloodTypeModel(mesa.Model):
    """The model with a number of agents"""
    def __init__(self, N, seed = None):
        super().__init__(seed = seed)

        self.num_agents = [self.create_person() for _ in range(N)]
        self.datacollector = DataCollector(agent_reporters={'BloodType':"phentype"})
        self.mutation_chance = {'A':0.03,'B':0.02}
        self.death_probabilities = {'A': 0.03, 'B': 0.01, 'AB': 0.015, 'O': 0.01}

    def create_person(self):
        sex = random.choice(['M', 'F'])
        return Person(self, sex, ['0', '0'])

    def reproduce(self):
        """Randomly selects a male and a female from self.num_agents,
        randomly selects one allele from each parent's genotype,
        and creates a new offspring."""
        a = random.uniform(0, 0.25)
        a = round(a*len(self.num_agents))
        for i in range(a):
            males = [person for person in self.num_agents if person.sex == 'M']
            females = [person for person in self.num_agents if person.sex == 'F']

            if not males or not females:
                raise ValueError("Not enough males or females in the population to create offspring.")

            father = random.choice(males)
            mother = random.choice(females)

            allele_from_father = random.choice(father.gentype)
            allele_from_mother = random.choice(mother.gentype)

            child_gentype = [allele_from_father, allele_from_mother]


            if random.random() < self.mutation_chance['A']:  # Mutate with the given probability
                mutation_allele = 'A'  # Mutation turns one allele into 'A'
                mutation_index = random.randint(0, 1)  # Randomly select which allele to mutate
                child_gentype[mutation_index] = mutation_allele

            if random.random() < self.mutation_chance['B']:  # Mutate with the given probability
                mutation_allele = 'B'  # Mutation turns one allele into 'A'
                mutation_index = random.randint(0, 1)  # Randomly select which allele to mutate
                child_gentype[mutation_index] = mutation_allele

            child_sex = random.choice(['M', 'F'])
            child = Person(self, child_sex, child_gentype)
            self.num_agents.append(child)

    def death(self):
        """Kills individuals based on their blood type and a death chance."""
        agents_to_remove = []
        for agent in self.num_agents:
            death_probability = self.death_probabilities.get(agent.phentype, 0)

            if random.random() < death_probability:
                agents_to_remove.append(agent)
        for agent in agents_to_remove:
            self.num_agents.remove(agent)


    def step(self):
        self.datacollector.collect(self)
        self.reproduce()
        self.death()


model = BloodTypeModel(10, seed=42)
for i in range(20):
    model.step()

# Collecting the data
data = model.datacollector.get_agent_vars_dataframe()

# Calculate the count of each blood type at each step
blood_type_counts = data.groupby(['Step', 'BloodType']).size().unstack(fill_value=0)
print(blood_type_counts)

# Visualize the data
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Line plot
blood_type_counts.plot(kind='line', ax=ax1)
ax1.set_title('Evolution of Blood Types Over Time')
ax1.set_xlabel('Time Step')
ax1.set_ylabel('Number of Individuals')
ax1.grid(True)
ax1.legend(title='Blood Type')

# Pie chart (using the last time step data)
ax2.pie(blood_type_counts.iloc[-1], labels=blood_type_counts.columns, autopct='%1.1f%%')
ax2.set_title('Distribution of Blood Types at Final Time Step')

# Show the plots
plt.tight_layout()
plt.show()
