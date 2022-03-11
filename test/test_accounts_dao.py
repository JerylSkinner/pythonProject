from custom_exceptions.id_not_found import IdNotFound
from dal_layer.accounts_dao_implementation import AccountsDAOImplementation
from entities.accounts import Account

accounts_dao = AccountsDAOImplementation()

def test_create_account_success():
    new_account = Account(1, 0, 1)
    result = account_dao.create_account(new_account)
    assert result.account_id != 1


def test_catch_non_unique_account_id():
    test_account = Account(1, 100, 1)
    result = account_dao.create_account(test_account)
    assert result.account_id != 1


def test_get_account_information_by_id_success():
    result = account_dao.get_account_by_id(1)
    assert result.account_id == 1


def test_get_account_information_non_existent_id():
    try:
        account_dao.get_account_by_id(0)
        assert True

    except IdNotFound as e:
        assert str(e) == "Account not found. Please try again!"


def test_update_account_by_id_success():
    new_account_owner = Account(1, 0, 2)
    result = account_dao.update_account_info_by_id(new_account_owner)
    assert result.customer_id == 2


def test_update_account_using_non_existent_id():
    try:
        new_account_owner = Account(0, 0, 2)
        account_dao.update_account_information_by_id(new_account_owner)
        assert True
    except IdNotFound as e:
        assert str(e) == "Account not found. Please try again!"


def test_delete_account_by_id_success():
    try:
        result = account_dao.delete_account_by_id(2)
        assert result
    except IdNotFound as e:
        assert str(e) == "Account not found. Please try again!"


def test_delete_account_by_id_non_existent():
    try:
        account_dao.delete_account_by_id(0)
        assert True
    except IdNotFound as e:
        assert str(e) == "Account not found. Please try again!"

