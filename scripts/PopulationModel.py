from .BaseModel import BaseModel
from .people import Person
import random
from tqdm import tqdm

class PopulationModel(BaseModel):
    def __init__(self,
                 n_initial,
                 child_probability=0.3,
                 ):
        super().__init__()
        self.population = [Person() for _ in range(n_initial)]
        self.n_history = [self.n]
        self.child_probability = child_probability
        self.n_child_per_person = []

    def step(self):
        # Make one step in the simulation
        # For each step, evolve each individual with a probability
        for person in self.population:
            person.age += 1
            if person.age > person.life_expectancy:
                self.population.remove(person)
            if person.sex == 'F':
                if person.age > person.fertility_range[0] and person.age < person.fertility_range[1]:
                    if random.random() < self.child_probability:
                        self.population.append(Person())
                        person.n_children += 1


        # Add new individuals

        # Update the history
        self.n_history.append(self.n)
        self.n_child_per_person.append(self.mean_children())
        # print(self.mean_children())

    @property
    def n(self):
        return len(self.population)

    def n_male(self):
        # Sum total amount of males in a population
        return sum([1 if person.sex == 'M' else 0 for person in self.population])

    def n_female(self):
        return self.n - self.n_male()

    def evolve(self, n_steps):
        # Evolve the model for n_steps
        for _ in tqdm(range(n_steps), desc=f'Evolving model for {n_steps} steps'):
            self.step()

    def plot(self):
        import matplotlib.pyplot as plt
        # Plot the evolution of the model
        plt.plot(self.n_history)
        plt.xlabel('Steps [-]')
        plt.ylabel('Population')
        plt.show()

    def plot_children_per_person(self):
        import matplotlib.pyplot as plt
        # Plot the evolution of the model
        plt.plot(self.n_child_per_person)
        plt.xlabel('Steps [-]')
        plt.ylabel('Children per person')
        plt.show()

    def mean_children(self):
        # Compute the mean number of children per person
        n_children = 0
        n_woman_not_child = 1
        for person in self.population:
            if person.sex == 'F' and person.age > person.fertility_range[0]:
                n_woman_not_child += 1
                n_children += person.n_children

        return n_children / n_woman_not_child





