
from abc import abstractmethod, ABC

from entities.customer import Customer

class CustomerDAOInterface(ABC):

    @abstractmethod
    def create_customer(self, customer: Customer)-> Customer:
        pass

    @abstractmethod
    def get_customer_information_by_id(self,customer_id:int)-> Customer:
        pass

    @abstractmethod
    def update_customer_by_id(self,customer:Customer)-> Customer:
        pass

    @abstractmethod
    def delete_customer_by_id(self,customer_id:int)-> bool:
        pass

