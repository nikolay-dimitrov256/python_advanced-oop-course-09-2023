def negatives_vs_positives(*args):
    negatives = []
    positives = []

    for num in args:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)

    negative_sum = sum(negatives)
    positive_sum = sum(positives)

    print(negative_sum)
    print(positive_sum)

    if abs(negative_sum) > positive_sum:
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


nums_list = [int(num) for num in input().split()]

negatives_vs_positives(*nums_list)
