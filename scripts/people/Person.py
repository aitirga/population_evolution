import random

class Person:
    idx = 0
    def __init__(self,
                 sex_probablity=0.5,
                 life_expectancy_mean=80,
                 life_expectancy_std=10,
                 fertility_range_mean=20,
                 fertility_range_std=5,
                 fertility_start_age=13,
                 ):
        self.sex = 'F' if random.random() > sex_probablity else 'M'
        self.age = 0
        self.life_expectancy = int(random.gauss(life_expectancy_mean, life_expectancy_std))
        self.idx = Person.idx
        fertility_range = int(random.gauss(fertility_range_mean, fertility_range_std))
        self.fertility_range = [fertility_start_age, fertility_start_age + fertility_range]
        Person.idx += 1
        self.n_children = 0

    def is_fertile(self):
        if self.sex == 'M':
            return False
        return self.age > self.fertility_range[0] and self.age < self.fertility_range[1]


