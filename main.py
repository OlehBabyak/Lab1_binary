import time
start_time = time.time()
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [i for i in range(1000000)]  # дані обов’язково повинні бути відсортовані
print(binary_search(my_list,43553))

print("--- %s секунд ---" % (time.time() - start_time))