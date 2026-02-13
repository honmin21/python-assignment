from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def rate_of_interest(self):
        pass
class SBI(Bank):
    def rate_of_interest(self):
        print("rate of interest is: is 75")