from abc import ABC, abstractmethod
from entities.accounts_class_information import Account

class AccountsDAOInterface(ABC):

    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def update_account_information_by_id(self, account: Account) -> Account:
        pass

    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def withdraw_from_account_by_id(self, withdraw_amount: int, account_id) -> Account:
        pass

    @abstractmethod
    def deposit_to_account_by_id(self, account_id, deposit_amount) -> Account:
        pass

    @abstractmethod
    def transfer_between_accounts_by_id(self, transfer_from_account, deposit_to_account, transfer_amount) -> bool:
        pass