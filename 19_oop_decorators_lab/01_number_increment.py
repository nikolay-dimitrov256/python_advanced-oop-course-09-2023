def number_increment(numbers):
    def increase():
        my_list = []
        for num in numbers:
            my_list.append(num + 1)

        return my_list

    return increase()


print(number_increment([1, 2, 3]))
