from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def step(self):
        pass