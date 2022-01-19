from brownie import FundMe
from scripts.helpful_script import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(F"The current entrance fee is {entrance_fee}")
    print("Funding")
    fund.fund({"from": account, "value": entrance_fee})
    print("Funded!")

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()