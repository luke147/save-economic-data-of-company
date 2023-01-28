#!/usr/bin/ env python3

def calculate_ev(market_cap, debt, cash):
    ev = market_cap + debt - cash
    return ev

market_cap = float(input("Enter the company's market capitalization: "))
debt = float(input("Enter the company's debt: "))
cash = float(input("Enter the company's cash and cash equivalents: "))

ev = calculate_ev(market_cap, debt, cash)
print("The company's enterprise value is: ", ev)

