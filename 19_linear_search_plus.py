""" 
Write a Program to enter the numbers and find Linear Search, Binary Search, 
Lowest Number and Selection Sort using array code.
"""

ARRAY = []

def selection_sort(array: list):
    __len = len(array)
    # Traverse thru list
    for i in range(0, __len):
        __select = i
        # traverse through the unsorted part,
        for j in range(i+1, __len):
            if array[__select] > array[j]:
                __select = j  # __select becomes the index of the lowest element
        # swap i th with the lowest currently
        array[i], array[__select] = array[__select], array[i]

    return array


def linear_search(array: list, element: int):
    # doesnt need sorted array
    for i in range(len(array)):
        if array[i] == element:
            return i

    return -1  # This is not reached if element is present


def binary_search_recursion(array: list, element: int, start_index: int, end_index: int):
    # needs sorted array
    
    if end_index >= start_index:  # prevents infinite recursion
        if len(array[start_index:end_index]) == 0:
            return -1
        middle = start_index + (end_index - start_index) // 2
        if array[middle] == element:
            return middle
        elif array[middle] > element:
            return binary_search_recursion(array, element, start_index, middle - 1)
        elif array[middle] < element:
            return binary_search_recursion(array, element, middle + 1, end_index)
        else:
            return -1
    else:
        return -1


def binary_search_iteration(array: list, element: int):
    #needs sorted array
    
    start = 0
    end = len(array) - 1
    
    while end >= start:
        mid = (end + start) // 2
        if array[mid] == element:
            return mid
        elif array[mid] > element:  # element comes before mid
            end = mid - 1
        elif array[mid] < element:  # element comes after mid
            start = mid + 1
    # if we reach here element was not present
    return -1

def lowest_number(array:list):
    __min = 0
    for element in array:
        if __min > element:
            __min = element
    return __min

def main():
    global ARRAY
    __choice = 0
    while __choice != 99:
        print(""" 
+----------MENU----------+
| 1. Populate Array      |
| 2. Print Array         |
| 3. Selection Sort      |
| 4. Linear Search       |
| 5. Binary Search - R   |
| 6. Binary Search - I   |
| 7. Lowest Term         |
| 99. Quit               |
+------------------------+
        """)
        __choice = int(input(">>> "))
        if __choice == 1:
            __input = input('Comma Seperated Integers: ')
            ARRAY += [int(item) for item in __input.split(',')]
        elif __choice == 2:
            print(ARRAY)
        elif __choice == 3:
            print(f"BEFORE SORT: {ARRAY}")
            print(f"AFTER SORT:  {selection_sort(ARRAY)}")
        elif __choice == 4:
            __array = selection_sort(ARRAY)
            print(f"ARRAY = {__array}")
            __element = int(input('Enter Search Term: '))
            __result = linear_search(__array, __element)
            if __result != -1:
                print(f"{__element} is at {__result} position")
            else:
                print("Search yielded no results.")
        
        elif __choice == 5:
            __array = selection_sort(ARRAY)
            print(f"ARRAY = {__array}")
            __element = int(input('Enter Search Term: '))
            __result = binary_search_recursion(__array, __element, 0, len(__array))
            if __result != -1:
                print(f"{__element} is at {__result} position")
            else:
                print("Search yielded no results.")
        
        elif __choice == 6:
            __array = selection_sort(ARRAY)
            print(f"ARRAY = {__array}")
            __element = int(input('Enter Search Term: '))
            __result = binary_search_iteration(__array, __element)
            if __result != -1:
                print(f"{__element} is at {__result} position")
            else:
                print("Search yielded no results.")
        
        elif __choice == 7:
            print(f"Lowest Term in Array is {lowest_number(ARRAY)}")
            
if __name__ == "__main__":
    main()