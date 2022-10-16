from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from personal_data import buxfer_password, buxfer_username
import requests as rq
import swagger_client.models as models
from datetime import datetime


class Buxfer:
    def __init__(self, username, password):

        token_data  = rq.post('https://www.buxfer.com/api/login', data={'username': username, 'password': password}).json()
        try:
            self.token = token_data["response"]["token"]
        except KeyError:
            raise("Error: {}".format(token_data["error"]["message"]))
        # create an instance of the API class
        self.api_instance = swagger_client.GetDataApi(swagger_client.ApiClient())
        self.get_tags()
        self.get_accounts()
        self.get_budgets()
        self.get_contacts()
        self.get_groups()
        self.get_loans()
        self.get_reminders()


    def get_accounts(self):    
        try:
            # Get Accounts information
            account_data = self.api_instance.accounts_get(token=self.token)
            self.accounts=[]
            for account in account_data["response"]["accounts"]:
                if "lastUpdated" in account.keys():
                    last_updated = account["lastUpdated"]
                elif  "lastSynced" in account.keys():
                    last_updated = account["lastSynced"]
                else:
                    # get transactions for current account id and get the last updated date from the first transction
                    transactions = self.get_transactions(account_id=account["id"])
                    if len(transactions) > 0:
                        last_updated = transactions[0]._date
                    else: #no transactions for this account
                        last_updated = None
                curr_account = models.AccountData(id = account["id"],name = account["name"],bank = account["bank"],balance = account["balance"],last_updated = last_updated)
                self.accounts.append(curr_account)
                self.accounts.append(curr_account)
        except ApiException as e:
            raise("Exception when calling GetDataApi->accounts_get: %s\n" % e)

    def get_tags(self):
        try:
            # Get Tags information
            tags_data = self.api_instance.tags_get(token=self.token)
            self.tags=[]
            for tag in tags_data["response"]["tags"]:
                curr_tag = models.TagData(id = tag["id"],name = tag["name"],parent_id=tag["parentId"])
                self.tags.append(curr_tag)
        except ApiException as e:
            raise("Exception when calling GetDataApi->tags_get: %s\n" % e)

    def get_transactions(self, account_id=None, account_name =None, tag_id=None, tag_name =None, start_date=None, end_date=None, month=None,budget_id=None, budget_name=None, contact_id=None, contact_name=None, group_id=None, group_name=None,status=None, page=None):
        try:
            # build a list of parameters that are not None
            params = {}
            if account_id is not None:
                params["account_id"] = str(account_id)
            if account_name is not None:
                params["account_name"] = account_name
            if tag_id is not None:
                params["tag_id"] = str(tag_id)
            if tag_name is not None:
                params["tag_name"] = tag_name
            if start_date is not None:
                params["start_date"] = start_date
            if end_date is not None:
                params["end_date"] = end_date
            if month is not None:
                params["month"] = month
            if budget_id is not None:
                params["budget_id"] = str(budget_id)
            if budget_name is not None:
                params["budget_name"] = budget_name
            if contact_id is not None:
                params["contact_id"] = str(contact_id)
            if contact_name is not None:
                params["contact_name"] = contact_name
            if group_id is not None:
                params["group_id"] = str(group_id)
            if group_name is not None:
                params["group_name"] = group_name
            if status is not None:
                params["status"] = status
            if page is not None:
                params["page"] = page
            # Get Transaction information for the given parameters
            transaction_data = self.api_instance.transactions_get(token=self.token, **params)
            transactions_array = []
            for transaction in transaction_data["response"]["transactions"]:
                curr_tags = transaction['tags']
                curr_tag_names=transaction['tagNames']
                curr_tag_elenets=[]
                if type(curr_tags) ==str:
                        curr_tags = [curr_tags]
                for curr_tag in curr_tags:
                    if curr_tag =="":
                        continue
                    curr_tag_element = next((tag for tag in self.tags if tag.name == curr_tag), None)
                    curr_tag_elenets.append(curr_tag_element)
                if transaction["type"]=="transfer":
                    try:
                        curr_to_accout = next((account for account in self.accounts if account.name == transaction["toAccount"]['name']), None)
                    except KeyError:
                        curr_to_accout = None
                    try:
                        curr_from_accout = next((account for account in self.accounts if account.name == transaction["fromAccount"]['name']), None)
                    except KeyError:
                        curr_from_accout = None
                    curr_transaction = models.TransactionData(id = transaction["id"],description = transaction["description"],_date = datetime.strptime(transaction["date"], '%Y-%m-%d') ,type = transaction["type"],amount = transaction["amount"],expense_amount = transaction["expenseAmount"],from_account = curr_from_accout, to_account=curr_to_accout,tags = curr_tags,tag_names = curr_tag_names,status = transaction["status"],is_future_dated = transaction["isFutureDated"],is_pending = transaction["isPending"])
                else:
                    curr_transaction = models.TransactionData(id = transaction["id"],description = transaction["description"],_date = datetime.strptime(transaction["date"], '%Y-%m-%d'),type = transaction["type"],amount = transaction["amount"],expense_amount = transaction["expenseAmount"],account_id = transaction["accountId"],account_name = transaction["accountName"],tags = curr_tags,tag_names = curr_tag_names,status = transaction["status"],is_future_dated = transaction["isFutureDated"],is_pending = transaction["isPending"])
                transactions_array.append(curr_transaction)
        except ApiException as e:
            raise("Exception when calling GetDataApi->transactions_get: %s\n" % e)
        return transactions_array


    def get_budgets(self):
        try:
            # Get Budgets information
            budget_data = self.api_instance.budgets_get(token=self.token)
            self.budgets=[]
            for budget in budget_data["response"]["budgets"]:
                curr_tag_id = budget['tagId']
                curr_tag = next((tag for tag in self.tags if tag.id == curr_tag_id), None)
                if "remaining" in budget.keys():
                    remaining = budget["remaining"]
                else:
                    remaining = None
                curr_budget = models.BudgetData(id = budget["budgetId"],name = budget["name"],limit = budget["limit"],remaining = remaining,period=budget["period"], tags = curr_tag)
                self.budgets.append(curr_budget)
        except ApiException as e:
            raise("Exception when calling GetDataApi->budgets_get: %s\n" % e)

    def get_contacts(self):
        try:
            # Get Contacts information
            contact_data = self.api_instance.contacts_get(token=self.token)
            self.contacts=[]
        except ApiException as e:
            raise("Exception when calling GetDataApi->contacts_get: %s\n" % e)

    def get_groups(self):
        try:
            # Get Groups information
            group_data = self.api_instance.groups_get(token=self.token)
            self.groups=[]
        except ApiException as e:
            raise("Exception when calling GetDataApi->groups_get: %s\n" % e)
    
    def get_loans(self):
        try:
            # Get Loans information
            loan_data = self.api_instance.loans_get(token=self.token)
            self.loans=[]
        except ApiException as e:
            raise("Exception when calling GetDataApi->loans_get: %s\n" % e)

    def get_reminders(self):
        try:
            # Get Reminders information
            reminder_data = self.api_instance.reminders_get(token=self.token)
            self.reminders=[]
        except ApiException as e:
            raise("Exception when calling GetDataApi->reminders_get: %s\n" % e)

    def accounts(self):
        return self.accounts
    
    def tags(self):
        return self.tags
    
    def transactions(self):
        return self.transactions
    
    def budgets(self):
        return self.budgets
    
    def contacts(self):
        return self.contacts
    
    def groups(self):
        return self.groups
    
    def loans(self):
        return self.loans
    
    def reminders(self):
        return self.reminders
    

curr_accout_data = Buxfer(buxfer_username,buxfer_password)

pprint(curr_accout_data.accounts)
# pprint(curr_accout_data.tags)
# pprint(curr_accout_data.transactions)
# pprint(curr_accout_data.budgets)
pass