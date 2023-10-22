def stock_availability(inventory: list, command: str, *args):
    def delivery():
        for item in args:
            inventory.append(item)

    def sell(inventory_: list):
        if len(args) == 0:
            inventory_.pop(0)
        else:
            for item in args:
                if isinstance(item, int):
                    for _ in range(item):
                        inventory_ = inventory_[item:]

                else:
                    while item in inventory_:
                        inventory_.remove(item)
        return inventory_

    if command == 'delivery':
        delivery()
    elif command == 'sell':
        inventory = sell(inventory)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
