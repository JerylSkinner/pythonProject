from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dao_interface import CustomerDAOInterface

from entities.customer import Customer

class CustomerDAOImplementation(CustomerDAOInterface):

        customer_list = []
        id_generator = 2

        def __init__(self):
            customer_needed_for_id_catch = Customer(1, "Ashley", "Meyer")
            self.customer_list.append(customer_needed_for_id_catch)

        def create_customer(self, customer: Customer)-> Customer:
            customer.customer_id = self.id_generator
            self.id_generator +=1
            self.customer_list.append(customer)
            return customer

        def get_customer_information_by_id(self, customer_id: int)-> Customer:
            for customer in self.customer_list:
                if customer.customer_id == customer_id:
                    return customer
            raise IdNotFound("No customer matches Id given. Please try again!")

        def update_customer_by_id(self, customer: Customer)-> Customer:
            for customer_in_list in self.customer_list:
                if customer.customer_id == customer_in_list.customer_id:
                    customer_in_list = customer
                    return customer_in_list

        def delete_customer_by_id(self, customer_id: int)-> bool:
            for customer in self.customr_list:
                if customer.customer_id == customer_id:
                    self.customer_list.remove(customer)
                    return True
            raise IdNotFound("No customer matches Id given. Please try again!")
