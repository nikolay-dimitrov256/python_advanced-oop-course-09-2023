import time

nums = [int(num) for num in input().split()]
target = int(input())

start = time.time()
values_map = {}
targets = set()

for num in nums:
    result = target - num

    if num in targets:
        targets.remove(num)
        result = values_map[num]
        del values_map[num]
        print(f'{result} + {num} = {target}')

    else:
        result = target - num
        targets.add(result)
        values_map[result] = num

end = time.time()
print(f'Time range: {end - start}')
