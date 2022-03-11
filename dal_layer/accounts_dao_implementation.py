from custom_exceptions.id_not_found import IdNotFound
from dal_layer.accounts_dao.accounts_dao_interface import AccountsDAOInterface
from entities.accounts_class_information import Accounts


class AccountsDAOImplementation(AccountsDAOInterface):
    accounts_list = [Accounts(1, "checking", "savings", "balance")]
    id_generator = 2

    # Create
    def create_accounts(self, accounts: Accounts) -> Accounts:
        accounts.accounts_id = self.id_generator
        self.id_generator += 1
        self.accounts_list.append(accounts)
        return accounts

    # Read
    def get_accounts_by_id(self, accounts_id: int) -> Accounts:
        for accounts in self.accounts_list:
            if accounts.accounts_id == accounts_id:
                return accounts
        raise IdNotFound("No account matches the id given: please try again!")

    # Update
    def update_accounts_by_id(self, accounts: Accounts) -> Accounts:
        for prior_account in self.account_list:
            if prior_account.account_id == account.account_id:
                prior_account = account
                return prior_account
        raise IdNotFound("No account matches the id given: please try again!")

    # Delete
    def delete_accounts_by_id(self, accounts_id: int) -> bool:
        for accounts in self.accounts_list:
            if accounts.accounts_id == accounts_id:
                self.accounts_list.remove(accounts)
                return True
        raise IdNotFound("No account matches the id given: please try again!")