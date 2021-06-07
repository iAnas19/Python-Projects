from array import *
import re

arr1 = array('i')
arr2 = array('i')

physicalSize = 100


sizeOfArray1 = 0
filledIndexArray1 = 0
emptyIndexArray1 = 0
isArray1Full = True
isArray1Empty = True
isArray1Created = False


sizeOfArray2 = 0
filledIndexArray2 = 0
emptyIndexArray2 = 0
isArrayFull = False
isArray2Empty = True
isArray2Created = False

arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def userInput(message):
    choice = input(message)
    if re.findall('[0-9]+', choice):
        return int(choice)
    else:
        print("wrong input type")
        print('--------------------')
        menu()


def menu():
    global arr1, isArray1Created, isArray1Empty, isArray1Full, filledIndexArray1, emptyIndexArray1
    global arr2, isArray2Created, isArray2Empty, isArray2Full, filledIndexArray2, emptyIndexArray2
    print("1.Create Array          2.Size")
    print("3.Insert Element        4.Update Element")
    print("5.Delete                6.Traverse ")
    print("7.Sort                  8.End ")
    userChoice = userInput("Enter your choice: ")

    if userChoice == 1:
        choice = userInput("Which array do you want to create? 1 or 2: ")
        CreateArray(choice)
        print("-------------")
        menu()

    elif userChoice == 2:
        choice = userInput("Which array do you want to declare? 1 or 2: ")
        SizeOfArray(choice)
        print("-------------")
        menu()

    elif userChoice == 3:
        choice = userInput("Which array to work for?1 or 2:  ")
        insertElement(choice)
        print("----------------")
        menu()

    elif userChoice == 4:
        choice = userInput("Which array you want to append for?1 or 2:  ")
        UpdateArr(choice)
        print("----------------")
        menu()

    elif userChoice == 5:
        choice = userInput('Which array to delete, 1 or 2? ')
        DeleteArray(choice)
        print("-------------")
        menu()

    elif userChoice == 6:
        if isArray1Created or isArray2Created:
            choice = userInput('Which array to show? 1 or 2? ')
            traverse(choice)
        else:
            print("Create array first")

        print("-------------")
        menu()

    elif userChoice == 7:
        choice = userInput('Which array to sort, 1 or 2? ')
        sort(choice)
        print("-------------------")
        menu()

    elif userChoice == 8:  # End of an element
        print("program End here ")
        print("----------------------")

    else:
        print("wrong input")
        print("-----------------")
        menu()


def CreateArray(choice):
    if choice == 1:
        global filledIndexArray1, isArray1Full, isArray1Empty, filledIndexArray1, isArray1Created
        filledIndexArray1 = 0
        isArray1Full = False
        isArray1Empty = True
        isArray1Created = True
        print("Array 1  created ")
        print("-------------------")

    elif choice == 2:
        global arr2, isArray2Created, isArray2Empty, isArray2Full, filledIndexArray2, emptyIndexArray2
        print("Do something")
        filledIndexArray2 = 0
        isArray2Full = False
        isArray2Empty = True
        isArray2Created = True
        print("Array 2  created ")
        print("-------------------")

    else:
        print("Wrong input")
        print("--------------")


def traverse(choice):
    if choice == 1:
        if isArray1Created:
            showinfo(arr1, sizeOfArray1,
                     emptyIndexArray1, filledIndexArray1)
        else:
            print("Create array first to view")
    elif choice == 2:
        if isArray2Created:
            showinfo(arr2, sizeOfArray2,
                     emptyIndexArray2, filledIndexArray2)
    else:
        print("Choose between 1 and 2 array only")


def showinfo(arr, sizeOfArray, emptyIndexArray, filledIndexArray):

    print(f"size of array is {sizeOfArray}")
    print(f"empty spaces of array is {emptyIndexArray}")
    print(f"filled spaces of array is {filledIndexArray}")
    for i in range(0, filledIndexArray):
        print(f"{arr[i]   }", end=" "),


# def UpdateArr(choice):
#     if choice == 1:
#         if isArray1Created:
#             update(arr1)
#         else:
#             print("Create Array to update")

#     elif choice == 2:
#         if isArray2Created:
#             update(arr2)
#         else:
#             print("Create Array to update")
#     else:
#         print("Wrong Choice")


# def update(arr):
#     i = 0
#     new_var = userInput("Which element you want to add? ")
#     new_arr = []
#     new_arr += []
#     i += 1
#     while i < len(arr):
#         new_arr1 = arr[i]
#         i += 1
#     return arr[i]


def UpdateArr(choice):
    global arr1, isArray1Created, isArray1Empty, isArray1Full
    global arr2, isArray2Created, isArray2Empty, isArray2Full
    if choice == 1:
        if isArray1Created:
            updatevar = userInput("write element to append")
            arr1 = int(arr1.append(updatevar))
            return arr1
            # print(f"update array is {arr1}.")
        else:
            print("Create your array first")

    elif choice == 2:

        if isArray2Created:
            updatevar = userInput("write element to append")
            arr1 = int(arr2.append(updatevar))
            return arr2
        else:
            print("Create your array first")
    else:
        print("Array doesn't exist")


def SizeOfArray(choice):
    if choice == 1:
        if isArray1Created:
            choice = userInput("Enter size of array between 1 to 50: ")
            if choice > 50 or choice < 1:
                print("Enter valid size for array")
                print("----------------------")
            else:
                global sizeOfArray1, filledIndexArray1, emptyIndexArray1
                sizeOfArray1 = choice
                filledIndexArray1 = 0
                emptyIndexArray1 = choice
                print(f"size of array 1 is decleared to be: {sizeOfArray1}",)
        else:
            print("Array 1 is not created")
            print("----------------------")
    elif choice == 2:
        if isArray2Created:
            choice = userInput("Enter size of array between 1 to 50")
            if choice > 50 or choice < 1:
                print("Enter valid size for array")
                print("----------------------")
            else:
                global sizeOfArray2, filledIndexArray2, emptyIndexArray2
                sizeOfArray2 = choice
                filledIndexArray2 = 0
                emptyIndexArray2 = choice
                print(f"size of array 2 is decleared to be: {sizeOfArray2}",)
        else:
            print("Array 1 is not created")
            print("----------------------")


def insertElement(choice):
    global arr1, emptyIndexArray1, filledIndexArray1, isArray1Empty
    if choice == 1:
        if isArray1Created and sizeOfArray1 > 0:
            choices = userInput("how many values do you want to insert? ")
            if choices <= emptyIndexArray1:
                isArray1Empty = False
                insertMenu()
                choice = userInput("enter your choice ")
                if choice == 1:
                    if filledIndexArray1 > 0:
                        for i in range(0, choices):
                            elementAlreadyInserted()
                    else:
                        insertElementAtFirstIndex(choices)
                elif choices == 2:
                    insertAtLastIndex(choices)
                    print("data Inserted")
                    print("-------------")
                elif choices == 3:
                    startingindex = userInput(
                        "At what index you want to add elements: ")
                    if filledIndexArray1 > 0:
                        for i in range(startingindex, choices):
                            elementAlreadyInserted()
                    else:

                        insertElementAfterCertainIndex(choices)

                else:
                    print("Wrong choice")
                    print("-------------")
                    menu()

        else:
            print("Either array not created and memory size is not defined.")
    elif choice == 2:
        print("do something ")
    else:
        print("wrong choice ")
        print("--------------------")


def insertElementAfterCertainIndex(choices):
    global arr1, emptyIndexArray1, filledIndexArray1
    for i in range(filledIndexArray1, choices):
        arr1[i] = userInput(f"Enter value at index {i}:")
        emptyIndexArray1 -= 1
        filledIndexArray1 += 1


def insertElementAtFirstIndex(choices):
    global arr1, emptyIndexArray1, filledIndexArray1
    for i in range(0, choices):
        arr1[i] = userInput(f"Enter value at index {i}:")
        emptyIndexArray1 -= 1
        filledIndexArray1 += 1


def insertAtLastIndex(choices):
    global arr1, filledIndexArray1, emptyIndexArray1
    for i in range(filledIndexArray1, filledIndexArray1+choices):
        arr1[i] = userInput(f"Enter value at first index {i} : ")
        emptyIndexArray1 -= 1
        filledIndexArray1 += 1


def elementAlreadyInserted():
    global arr1, emptyIndexArray1, filledIndexArray1
    for i in range(filledIndexArray1-1, -1, -1):
        arr1[i+1] = arr1[i]

    arr1[0] = userInput(f"Enter value at first index 0: ")
    emptyIndexArray1 -= 1
    filledIndexArray1 += 1


def DeleteArray(choice):
    global isArray1Created, arr1
    global isArray2Created, arr2
    if choice == 1:
        if isArray1Created:
            del arr1
            print('Array 1 is removed successfully')
            print("----------")

        elif choice == 2:
            if isArray2Created:
                del arr2
                print('Array 2 is removed successfully')
                print("----------")
        else:
            print("Array does not exist")
            print("----------")


def sort(choice):
    if choice == 1:
        if isArray1Created:
            choices = userInput(
                "What sorting do you want? 1. Bubble or 2. Merge: ")
            if choices == 1:
                bubbleSort(arr1)

            elif choices == 2:
                mergeSort(arr1)

            else:
                print("Select given type")

    elif choice == 2:
        if isArray2Created:
            choices = userInput(
                "What sorting do you want? 1. Bubble or 2. Merge: ")
            if choices == 1:
                bubbleSort(arr2)

            elif choices == 2:
                mergeSort(arr2)

            else:
                print("Select given type")
    else:
        print("Wrong choice")


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        for i in range(len(arr)):
            print("%d" % arr[i], end=" ")


def insertMenu():
    print("1. Insert at first index ")
    print("2. Insert at last index ")
    print("3. Insert at after certain index ")
    # print("4. Insert at particular index ")
    print("------------------------------")


menu()





# def UpdateArr(choice):
#     if choice == 1:
#         if isArray1Created:
#             update(arr1)
#         else:
#             print("Create Array to update")

#     elif choice == 2:
#         if isArray2Created:
#             update(arr2)
#         else:
#             print("Create Array to update")
#     else:
#         print("Wrong Choice")


# def update(arr):
#     i = 0
#     new_var = userInput("Which element you want to add? ")
#     new_arr = []
#     new_arr += []
#     i += 1
#     while i < len(arr):
#         new_arr1 = arr[i]
#         i += 1
#     return arr[i]


# def UpdateArr(choice):
#     global arr1, isArray1Created, isArray1Empty, isArray1Full
#     global arr2, isArray2Created, isArray2Empty, isArray2Full
#     if choice == 1:
#         if isArray1Created:
#             updatevar = userInput("write element to append")
#             arr1 = int(arr1.append(updatevar))
#             return arr1
#             # print(f"update array is {arr1}.")
#         else:
#             print("Create your array first")

#     elif choice == 2:

#         if isArray2Created:
#             updatevar = userInput("write element to append")
#             arr1 = int(arr2.append(updatevar))
#             return arr2
#         else:
#             print("Create your array first")
#     else:
#         print("Array doesn't exist")

