from abc import abstractmethod

class Oracle():
    @abstractmethod
    def accepts(self, input):
        raise NotImplementedError
