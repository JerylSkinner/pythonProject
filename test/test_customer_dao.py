from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dao_implementation import CustomerDAOImplementation
from entities.customer import Customer

customer_dao = CustomerDAOImplementation()

def test_create_customer_success():
    test_customer= Customer(0,"Jeryl", "Skinner")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id !=0

def test_catch_non_unique_id():
    test_customer = Customer(1,"Ashley","Meyer")
    result = customer_dao.create_customer(test_customer)
    assert result. customer_id != 1

def test_get_customer_information_by_id_success():
    result = customer_dao.get_customer_information_by_id(1)
    assert result.customer_id == 1

def test_get_customer_using_non_existant_id():
    try:
        customer_dao.get_customer_information_by_id(0)
    except IdNotFound as e:
        assert str(e) == "No customer matches Id given. Please try again!"

def test_update_customer_by_id_success():
    new_customer_last_name = Customer(1,"Ashley","Moreno")
    result = customer_dao.update_customer_by_id(new_customer_last_name)
    assert result.customer_last_name == "Moreno"

def test_update_customer_using_non_existant_id():
    try:
        new_customer_last_name = Customer(0,"Ashley", "Moreno")
        customer_dao.update_customer_by_id(new_customer_last_name)
    except IdNotFound as e:
        assert str(e) == "No customer matches the Id given. Please try again!"

def delete_customer_customer_by_id(self,customer_id:int)-> bool:
    for customer in customer_dao.customer_list:
        if customer.customer_id == customer_id:
            customer_dao.customer_in_list.rempytove(customer)
            return True
    raise IdNotFound("No customer matches Id given.")





