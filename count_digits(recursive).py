def digits_count(num):
    a = int(num/10)
    if a == 0:
        return 1
    else:
        return digits_count(a) + 1

print(digits_count(0))
