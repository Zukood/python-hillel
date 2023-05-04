def sum_range(start, end):

    if start > end:
        start, end = end, start

    total_sum = 0

    for num in range(start, end + 1):
        total_sum += num


    return total_sum

print(sum_range(102, 15))
