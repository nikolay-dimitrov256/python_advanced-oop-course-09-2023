clothes = [int(num) for num in input().split()]
stand_capacity = int(input())

stands_needed = 0

while clothes:
    stands_needed += 1
    current_stand_capacity = stand_capacity

    while clothes:
        if clothes[-1] <= current_stand_capacity:
            current_stand_capacity -= clothes.pop()
        else:
            break

print(stands_needed)
