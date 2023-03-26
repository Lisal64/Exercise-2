# Exercise 1

numbers = []  # creating empty list to store the user input in
integer = int


def count_integer(numbers, integer):
    i = int(
        input("Please enter the amount of values in your list: "))  # specifying the amount so that the loop has an end
    for n in range(0, i):
        print("Enter number at index:", n, )  # making it possible to enter the number at every index
        user_number = [int(input())]
        # an empty input to enter the number for the given index, needs to be a list to join it with the original
        numbers = numbers + user_number
    integer = int(input("Please enter the number you want counted: "))
    count = int(0)
    for v in range(0, i):  # need to loop through all the numbers to find equal ones
        if numbers[v] == integer:
            count += 1  # adding +1 for every number found
    if count != 0:  # if the for-loop found matches, return the count established in the for-loop
        return count
    else:
        not_found = int(42)
        return not_found


print(count_integer(numbers, integer))


# Exercise 2

def list_func(numbers, integer):
    j = int(input("Please enter the amount of values in your list: "))
    for n in range(0, j):
        print("Enter number at index:", n, )
        user_list2 = int(input())
        numbers.append(user_list2)
    integer = int(input("Please enter the number you want to replace with 6 in your list: "))
    count = 0
    # adding a count to have a condition for the 2nd if-statement (not very elegant but the only thing I could think of)
    for v in range(0, j):
        if numbers[v] == integer:
            count += 1
            numbers[v] = 6
    if count != 0:
        reversed_list = numbers[::-1]  # copying the list from start to finish in reverse order
        print(reversed_list)
        return numbers
    else:
        empty_list = []
        return empty_list


print(list_func(numbers, integer))

# Exercise 3
list1 = []
list2 = []


def compare_lists(list1, list2):
    i = int(input("Please enter the amount of values in your first list: "))
    for n in range(0, i):
        print("Enter number at index:", n, )
        first_list = int(input())
        list1.append(first_list)
    j = int(input("Please enter the amount of values in your second list: "))
    for a in range(0, j):
        print("Enter number at index:", a, )
        second_list = int(input())
        list2.append(second_list)
    list1.sort()
    list2.sort()
    list1 = [v for v in list1 if v in list2]
    # using list comprehension as it only prints contents of the list if they're the same
    return list1


print(compare_lists(list1, list2))

# Exercise 4
lst = []


def remove_duplicates(lst):
    i = int(input("Please enter the amount of values in your list: "))
    for n in range(0, i):
        print("Enter number at index:", n, )
        us_list = int(input())
        lst.append(us_list)
    lst = list(
        dict.fromkeys(lst))  # converting it into a dictionary to remove duplicates as dictionaries don't allow those
    # & changing the type back into a list, since the return is supposed to be one
    return lst


print(remove_duplicates(lst))

# Exercise 5
dictionary = {}


def dict_func(dictionary):
    dictionary["Type"] = input("Please enter the type of your PC: ") or dictionary.setdefault("Type", "unknown type")
    dictionary["Brand"] = input("Please enter the brand of your PC: ") or dictionary.setdefault("Brand",
                                                                                                "unknown brand")
    dictionary["Price"] = input("Please enter the price of your PC: ") or dictionary.setdefault("Price",
                                                                                                "unknown price")
    dictionary["OS"] = input("Please enter the operating system of your PC: ") or dictionary.setdefault("OS", "Linux")
    type = dictionary.get("Type")
    brand = dictionary.get("Brand")
    price = dictionary.get("Price")
    print(f"You have a {type} from {brand} that costs {price}.")
    return dictionary


print(dict_func(dictionary))
