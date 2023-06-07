
import random

def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        index = random.choice(range(len(lst)-1))
        pivot = lst[index]
        less = [num for num in lst[:index] + lst[index+1:] if num <= pivot]
        greater = [num for num in lst[:index] + lst[index+1:] if num > pivot]

        print(f"Pivot: {pivot}")
        print(f"Less: {less}")
        print(f"Greater: {greater}")

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([12, 25, 10, 14]))






















