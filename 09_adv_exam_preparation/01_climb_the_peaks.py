from collections import deque

food_stack = [int(num) for num in input().split(', ')]
stamina_queue = deque(int(num) for num in input().split(', '))

peaks = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}
conquered_peaks = []

for peak, difficulty in peaks.items():

    while food_stack and stamina_queue:
        result = food_stack.pop() + stamina_queue.popleft()

        if result >= difficulty:
            conquered_peaks.append(peak)
            break

if len(conquered_peaks) == len(peaks):
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if conquered_peaks:
    print('Conquered peaks:')
    print('\n'.join(conquered_peaks))
