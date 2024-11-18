def quick_sort(arr, key_func, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Choose the pivot and reorder the array
        pivot = key_func(arr[high])  # Last element as pivot
        i = low - 1  # Smaller element index
        
        for j in range(low, high):
            if key_func(arr[j]) <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap smaller element to the left
        
        # Place the pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_index = i + 1

        # Recursively sort the partitions
        quick_sort(arr, key_func, low, pivot_index - 1)
        quick_sort(arr, key_func, pivot_index + 1, high)
