from custom_exceptions.id_not_found import IdNotFound
from dal_layer.accounts_dao_implementation import AccountsDAOImplementation
from entities.accounts import Accounts

accounts_dao = AccountsDAOImplementation()

def test_create_checking_account_success():
    test_checking_account= Accounts(0,"checking")
    result = accounts_dao.create_accounts(test_accounts)
    assert result.account_id !=0

def test_catch_non_unique_id():
    test_account = Account(1,"checking","savings", balance)
    result = accounts_dao.create_accounts(test_accounts)
    assert result. accounts_id != 1

def test_get_accounts_information_by_id_success():
    result = accounts_dao.get_accounts_information_by_id(1)
    assert result.account_id == 1

def test_get_accounts_using_non_existant_id():
    try:cj
        accounts_dao.get_accounts_information_by_id(0)
    except IdNotFound as e:
        assert str(e) == "No account matches Id given. Please try again!"

def test_update_accounts_by_id_success():
    new_checking_account = Accounts(1,"checking")
    result = checking_account_dao.update_checking-account_by_id(new_checking_account_by_id)
    assert result.checking_account == "Moreno"

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

