from abc import ABC, abstractmethod

from entities.accounts import Accounts

class AccountsDAOInterface(ABC):

    @abstractmethod
    def create_accounts(self, accounts: Accounts) -> Accounts:
        pass

    @abstractmethod
    def get_accounts_by_id(self, accounts_id: int) -> Accounts:
        pass

    @abstractmethod
    def update_accounts_by_id(self, account: Accounts) -> Accounts:
        pass

    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass