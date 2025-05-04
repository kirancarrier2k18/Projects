def bubble_sort(arr):              # Define a function named bubble_sort
    n = len(arr)                   # Find how many elements are in the list
    for i in range(n):             # Loop over the list n times
        for j in range(n - 1 - i): # Loop from 0 to n-1-i (to avoid already sorted end)
            if arr[j] > arr[j + 1]:              # If left number is bigger than right
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap them
    return arr                     # Return the sorted list

print(bubble_sort([5, 1, 4, 2, 8]))