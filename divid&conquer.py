print('mod :', 64 % 40)

print('mod :', 104 % 40)

def hcf(a, b):
    remainder = a % b
    if remainder == 0:
        return b
    else:
        return str(remainder) + ' ' + str(hcf(b, remainder))

print(hcf(64, 40))

total_area = 64 * 40
print(total_area)
number_of_squares = total_area/(8**2)

print(number_of_squares)


#### Euclid's algorithm

######quicksort uses D & C

lst = [33, 15, 10]

sorted = [15, 10] + [33] +  []


def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[1]

        less = [num for num in lst[:1] + lst[2:] if num <= pivot]
        greater = [num for num in lst[:1] + lst[2:] if num > pivot]
        print(f"pivot:  {pivot}")
        print(f"less:  {less}")
        print(f"greater:  {greater}")


    return quicksort(less) + [pivot] + quicksort(greater)

print([10, 5, 2, 3, 4, 4, 20])
print(quicksort[10, 5, 2, 3, 4, 4, 20])














