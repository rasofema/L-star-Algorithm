from abc import abstractmethod

class Oracle():
    @abstractmethod
    def query(self, input):
        raise NotImplementedError
