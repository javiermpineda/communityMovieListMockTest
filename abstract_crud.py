from abc import ABC, abstractmethod

class AbstractCRUD(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def read(self, identifier):
        pass

    @abstractmethod
    def update(self, identifier, data):
        pass

    @abstractmethod
    def delete(self, identifier):
        pass
