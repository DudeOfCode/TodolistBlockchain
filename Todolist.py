from web3 import Web3
import json

url = "HTTP://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(url))
w3.eth.defaultAccount = w3.eth.accounts[0]
print(w3.isConnected())
address = "0xcE33A3f608c8d3878111E5C836d24ffC20C10e99"
abi = json.loads(
    '[{"inputs":[],"stateMutability":"payable","type":"constructor"},{"inputs":[{"internalType":"string","name":"_action","type":"string"},{"internalType":"uint256","name":"_day","type":"uint256"},{"internalType":"uint256","name":"_month","type":"uint256"},{"internalType":"uint256","name":"_year","type":"uint256"}],"name":"addtolist","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"allTod","outputs":[{"components":[{"internalType":"string","name":"action","type":"string"},{"internalType":"uint256","name":"day","type":"uint256"},{"internalType":"uint256","name":"month","type":"uint256"},{"internalType":"uint256","name":"year","type":"uint256"}],"internalType":"struct TodoList.Todo[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"},{"internalType":"uint256","name":"_day","type":"uint256"}],"name":"editDay","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"},{"internalType":"uint256","name":"_month","type":"uint256"}],"name":"editMonth","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"},{"internalType":"uint256","name":"_year","type":"uint256"}],"name":"editYear","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"},{"internalType":"string","name":"_action","type":"string"}],"name":"editaction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"},{"internalType":"string","name":"_action","type":"string"},{"internalType":"uint256","name":"_day","type":"uint256"},{"internalType":"uint256","name":"_month","type":"uint256"},{"internalType":"uint256","name":"_year","type":"uint256"}],"name":"editwholeindex","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getamnt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getfromlist","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getlast","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"remfromtodo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"showaction","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"showday","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"showmonth","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"showyear","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
)
cont = w3.eth.contract(address=address, abi=abi)

print(
    "1. Fetch from list\n2. Add to list\n3. Remove from list"
    "\n4. Edit list \n5. Get total number of saved items\n6. Get all things on list"
)


pao = int(input("Pick an option: "))
if pao == 1:
    print("Fetch from list")
    print("Please note that the numbering starts from zero")
    index = int(input("Which index of the list:"))
    getfomli = cont.functions.getfromlist(index).call()
    print(getfomli)
elif pao == 2:
    print("Add To list")
    Action = str(input("Enter the action : "))
    Day = int(input("Enter the day in numbers: "))
    Month = int(input("Enter the Month in numbers: "))
    Year = int(input("Enter the year in numbers: "))
    add = cont.functions.addtolist(Action, Day, Month, Year).transact()
    resit = w3.eth.waitForTransactionReceipt(add)
    new = cont.functions.getlast().call()
    print("newly added {} ".format(new))
elif pao == 3:
    cont.functions.remfromtodo(
        int(input("Enter the index you wish to remove: "))
    ).transact()
elif pao == 5:
    print(
        "You currently have "
        + str(cont.functions.getamnt().call())
        + " items on your list"
    )
elif pao == 4:
    print(
        "1. Edit whole index\n2. Edit Action\n3. Edit day\n4. Edit Month\n5. Edit year"
    )
    ada = int(input("Pick an option: "))
    if ada == 1:
        print("Edit Whole index")
        print("Please note that the numbering starts from zero")

        index = int(input("Which index would you like to edit (number): "))
        Action = str(input("Enter the action: "))

        Day = int(input("Enter the day in numbers: "))
        Month = int(input("Enter the Month in numbers: "))
        Year = int(input("Enter the year in numbers: "))
        edall = cont.functions.editwholeindex(
            index, Action, Day, Month, Year
        ).transact()
        resit = w3.eth.waitForTransactionReceipt(edall)
        getfomli = cont.functions.getfromlist(index).call()
        print("updated list: {}".format(getfomli))

    elif ada == 2:
        print("Edit Action")
        print("Please note that the numbering starts from zero")
        index = int(input("Which index's action would you like to edit (number): "))
        Action = str(input("Enter the action: "))
        edac = cont.functions.editaction(
            index,
            Action,
        ).transact()
        resit = w3.eth.waitForTransactionReceipt(edac)
        getfomli = cont.functions.getfromlist(index).call()
        print("updated list: {}".format(getfomli))

    elif ada == 3:
        print("Edit Day")
        print("Please note that the numbering starts from zero")
        index = int(input("Which index's day would you like to edit (number): "))
        Day = int(input("Enter the day in numbers: "))
        edd = cont.functions.editDay(
            index,
            Day,
        ).transact()
        resit = w3.eth.waitForTransactionReceipt(edd)
        getfomli = cont.functions.getfromlist(index).call()
        print("updated list: {}".format(getfomli))

    elif ada == 4:
        print("Edit Month")
        print("Please note that the numbering starts from zero")
        index = int(input("Which index's month would you like to edit (number): "))
        Month = int(input("Enter the Month in numbers: "))
        edm = cont.functions.editMonth(
            index,
            Month,
        ).transact()
        resit = w3.eth.waitForTransactionReceipt(edm)
        getfomli = cont.functions.getfromlist(index).call()
        print("updated list: {}".format(getfomli))

    elif ada == 5:
        print("Edit Year")
        print("Please note that the numbering starts from zero")
        index = int(input("Which index's year would you like to edit (number): "))
        Year = int(input("Enter the year in numbers: "))
        edy = cont.functions.editYear(
            index,
            Year,
        ).transact()
        resit = w3.eth.waitForTransactionReceipt(edy)
        getfomli = cont.functions.getfromlist(index).call()
        print("updated list: {}".format(getfomli))
if pao == 6:
    all = cont.functions.allTod().call()
    print(all)
