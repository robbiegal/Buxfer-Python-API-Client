from __future__ import print_function
from locale import currency
import time
from winreg import QueryValue
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from personal_data import buxfer_password, buxfer_username
import requests as rq
import swagger_client.models as models


token  = rq.post('https://www.buxfer.com/api/login', data={'username': buxfer_username, 'password': buxfer_password}).json()
try:
    token = token["response"]["token"]
except KeyError:
    print("Error: {}".format(token["error"]["message"]))
    exit()

# create an instance of the API class
api_instance = swagger_client.GetDataApi(swagger_client.ApiClient())

try:
    # Get Accounts information
    account_data = api_instance.accounts_get(token=token)
    accounts_array=[]
    for account in account_data["response"]["accounts"]:
        if "last_updated" in account.keys():
            last_updated = account["last_updated"]
        else:
            last_updated = None
        curr_account = models.AccountData(id = account["id"],name = account["name"],bank = account["bank"],balance = account["balance"],last_synced = last_updated)
        accounts_array.append(curr_account)
    print("Accounts:")
    for account in accounts_array:
        print(account)
except ApiException as e:
    print("Exception when calling GetDataApi->accounts_get: %s\n" % e)



try:
    # Get Tags information
    tags_data = api_instance.tags_get(token=token)
    tags_array=[]
    for tag in tags_data["response"]["tags"]:
        curr_tag = models.TagData(id = tag["id"],name = tag["name"],parent_id=tag["parentId"])
        tags_array.append(curr_tag)
    print("Tags:")
    for tag in tags_array:
        print(tag)
except ApiException as e:
    print("Exception when calling GetDataApi->tags_get: %s\n" % e)


try:
    # Get Budgets information
    budget_data = api_instance.budgets_get(token=token)
    budgets_array=[]
    for budget in budget_data["response"]["budgets"]:
        curr_tag_id = budget['tagId']
        curr_tag = next((tag for tag in tags_array if tag.id == curr_tag_id), None)
        if "remaining" in budget.keys():
            remaining = budget["remaining"]
        else:
            remaining = None
        curr_budget = models.BudgetData(id = budget["budgetId"],name = budget["name"],limit = budget["limit"],remaining = remaining,period=budget["period"], tags = curr_tag)
        budgets_array.append(curr_budget)

    print("Budgets:")
    for budget in budgets_array:
        print(budget)
except ApiException as e:
    print("Exception when calling GetDataApi->budgets_get: %s\n" % e)

try:
    # Get Contacts information
    contacts = api_instance.contacts_get(token=token)
    print("Contacts:")
    pprint(contacts)
except ApiException as e:
    print("Exception when calling GetDataApi->contacts_get: %s\n" % e)


try:
    # Get Groups information
    groups = api_instance.groups_get(token=token)
    print("Groups:")
    pprint(groups)
except ApiException as e:
    print("Exception when calling GetDataApi->groups_get: %s\n" % e)

try:
    # Get Loans information
    loans = api_instance.loans_get(token=token)
    print("Loans:")
    pprint(loans)
except ApiException as e:
    print("Exception when calling GetDataApi->loans_get: %s\n" % e)


try:
    # Get Reminders information
    reminders = api_instance.reminders_get(token=token)
    print("Reminders:")
    pprint(reminders)
except ApiException as e:
    print("Exception when calling GetDataApi->reminders_get: %s\n" % e)

pass