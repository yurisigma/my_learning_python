
million = [i for i in range(1, 1000001)]
print(min(million), max(million), sum(million))


odds = [odd for odd in range(1, 20, 2)]
print(odds)

three_times = [three_times*3 for three_times in range(1, 11)]
for i in three_times:
    print(i)

squares = [square ** 2 for square in range(1, 11)]
print(squares)
