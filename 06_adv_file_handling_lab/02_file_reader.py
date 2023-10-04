with open('numbers.txt', 'r') as file:
    data = file.readlines()
    numbers = [int(num.strip()) for num in data]
    print(sum(numbers))
