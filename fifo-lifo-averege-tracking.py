'''
Read input.
Store in arrays.
for each transaction:
    create object


'''

'''
CSV FORMAT

Starting with row #2.

A,B,C,D,E,F...
A: Quantity of BTC purchased/sold
B: Price in USD
C: Fee (Amount paid to the Exchange company)
D: Other fee (e.g. bank fee) (Enter 0 if none.)
E: Datetime (Format TBD)
F,G,...: Optional other details (e.g. which exchange used, other comment)

In order for FIFO and LIFO to methods to be calculated currectly, transactions must be listed in the CSV by ascending order chronologoically.
(Oldest transactions first. Newest transactions last.
'''

import csv
import math

# Validation??

'''
# round to 8 decimal places
def round(num):
    return math.ceil(num*100000000)/100000000
'''

# transaction class
class Transaction:
    def __init__(self,q,p,f,of):
        self.quantity = round(float(q),8) #BTC
        self.price = float(p) # USD per BTC
        self.fee = float(f) # in USD
        self.otherFee = of # For example, bank transfer fee. Not part of cost basis. (in USD)
        # self.date = d

    def getQuant(self):
        return self.quantity
    def getPrice(self):
        return self.price
    def getFee(self):
        return self.fee    

transactions = []

# holding class
# properties: quantity, cost, date
class Holding:
    def __init__(self,q,b,bwf):
        # self.id = ???
        self.quantity = q
        self.basis = b
        self.basisWithFees = bwf

    def getQuant(self):
        return self.quantity
    def getBasis(self):
        return self.basis
    def getBWF(self):
        return self.basisWithFees

# AvgHolding class extends Holding class, adding weight

holdings_fifo = []
holdings_lifo = []
holdings_avg = []

# METHODS

# Read
def read():
    ifile  = open('sample-transactions.csv', "rU")
    reader = csv.reader(ifile)

    for row in reader:
        quantity = row[0]
        price = row[1]
        commission = row[2]
        fee = row[3]
        t = Transaction(quantity,price,commission,fee)
        transactions.append(t)


# Add
def addToHoldings(t):
    quantity = t.getQuant()
    price = t.getPrice()
    fee = t.getFee()
    priceWithFeesPerUnit = round(((price*quantity) + fee) / quantity, 8)
    h = Holding(quantity,price,priceWithFeesPerUnit)
    holdings_fifo.append(h)
    holdings_lifo.append(h)
    # add to average

# Remove
def removeFromHoldings_fifo(t):
    quantity = t.getQuant()
    price = t.getPrice()
    fee = t.getFee()
    
    transactionFullyAccountedFor = False
    while transactionFullyAccountedFor != True:
        # Check if there are enough in first holding
            # if exactly enough, remove first holding & done w/ removing holdings
            # if so, subtract, update first holding, & done w/ removing holdings
            # if not, updtate sought quantity to difference., remove first, repeat
            # if none left, error(ran out of holdings / suggest
        transactionFullyAccountedFor = True

def removeFromHoldings_lifo(t):
    quantity = t.getQuant()
    price = t.getPrice()
    fee = t.getFee()
    
    transactionFullyAccountedFor = False
    while transactionFullyAccountedFor != True:
        # Check if there are enough in last holding
            # if exactly enough, remove last holding & done w/ removing holdings
            # if so, subtract, update last holding, & done w/ removing holdings
            # if not, updtate sought quantity to difference., remove last, repeat
        transactionFullyAccountedFor = True

def removeFromHoldings_avg(t):
    quantity = t.getQuant()
    price = t.getPrice()
    fee = t.getFee()

    # assign proportional portions of the transaction to each holding:
    
    # update holdings
    transactionFullyAccountedFor = False
    while transactionFullyAccountedFor != True:
        # for each AvgHolding in list:
            # multiply(each.getWeight(), quantity)
            # subtract that value from the AvgHolding.quantity
            # ????? to update price
            # subtract quant from leftToProcess variable
        #check wether leftToProcess variable = 0. if not, error
        transactionFullyAccountedFor = True

# Calculate gain/loss

# known error
# 1: Ran out of holdings to complete transaction (report line # from CSV). Suggestion: Is there an un accounted for donation?

# Write
# write (starting and) final holdings
# write gain or loss

# report



# EXECUTION

# LOAD TRANSACTIONS
read()

# PROCESS TRANSACTIONS
total_holdings = 0

for i in transactions:
    quantity = i.getQuant()
    total_holdings += quantity # Update holdings
    if quantity > 0:
        addToHoldings(i)
    else:
        removeFromHoldings_fifo(i)
        removeFromHoldings_lifo(i)
        removeFromHoldings_avg(i)

# Print or write summary
# ...


print "Current holdings: " + str(total_holdings) + " BTC. If this does not match your current holdings, there is a transaction missing."

#troubleshooting
index = 1

for t in transactions:
    print str(index) + ": Quantity: " + str(t.quantity) + "\n"
    index += 1


print holdings_fifo[1].getBasis()
