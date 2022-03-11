from custom_exceptions.insufficient_funds import InsufficientFunds
from entities.accounts import Account
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dal.account_dao_interface import AccountsDAOInterface


class AccountsDAOImplementation(AccountsDAOInterface):
    pass


    account_list = [Account(1, 500, 1), Account(2, 100, 2)]
    account_id_gen = 3

    def create_account(self, account: Account) -> Account:
        account.account_id = self.account_id_gen
        self.account_id_gen += 1
        AccountDAOImp.account_list.append(account)
        return account

    def get_account_by_id(self, account_id: int) -> Account:
        for account in self.account_list:
            if account.account_id == account_id:
                return account
        raise IdNotFound("Account not found. Please try again!")

    def update_account_info_by_id(self, account: Account) -> Account:
        for prior_account_info in self.account_list:
            if prior_account_information_account_id == account.account_id:
                prior_account_information = account
                return prior_account_information
        raise IdNotFound("Account not found. Please try again!")

    def delete_account_by_id(self, account_id: int) -> bool:
        for account in self.account_list:
            if account.account_id == account_id:
                self.account_list.remove(account)
                return True
        raise IdNotFound("Account not found, please try again!")

    def withdraw_from_account_by_id(self, withdraw_amount: int, account_id) -> Account:
        if withdraw_amount < 0:
            raise ValueError("Withdraw request can not be a negative number.")
        for account in self.account_list:
            if account.account_id == account_id:
                if withdraw_amount <= account.account_balance:
                    account.account_balance -= withdraw_amount
                print("Withdraw successful. Your new balance is" + str(account.account_balance) + ".")
                return account
            raise IdNotFound("Incorrect account information. Please try again.")

    def deposit_to_account_by_id(self, account_id, deposit_amount) -> Account:
        if deposit_amount < 0:
            raise ValueError("Deposit request can not be a negative number.")
        for account in self.account_list:
            if account_id == account.account_id:
                account.account_balance += deposit_amount
                print("Deposit successful. Your updated balance is" + str(account.account_balance) + ".")
                return account
        raise IdNotFound("Incorrect account information. Please try again.")

    def transfer_between_accounts_by_id(self, transfer_from_account, deposit_to_account, transfer_amount: float):
        withdraw_account = Account(1, 500, 1)
        deposit_to_account = Account(2, 100, 2)
        for account in self.account_list:
            if account.account_id == transfer_from_account:
                withdraw_account = account
            if account.customer_id == deposit_to_account:
                deposit_to_account = account
        if withdraw_account.account_balance - transfer_amount < 0:
            raise InsufficientFunds("You have insufficient funds for this operation.")
        else:
            withdraw_account.account_balance = withdraw_account.account_balance - transfer_amount
            deposit_to_account.account_balance = deposit_to_account.account_balance + transfer_amount
            return deposit_to_account.account_balance


class AccountsDAOImplementation:
    pass