transactions = [500, -200, 1000, -150, 300, -100]

balance = 0

for amount in transactions:
    balance += amount

print("Total Deposits:", sum(x for x in transactions if x > 0))
print("Total Withdrawals:", abs(sum(x for x in transactions if x < 0)))
print("Final Balance:", balance)
print("Total Transactions:", len(transactions))