from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge sort implementation using divide and conquer approach.
    
    Args:
        arr (list): List to be sorted
        
    Returns:
        list: Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves and merge them
    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        left (list): First sorted array
        right (list): Second sorted array
        
    Returns:
        list: Merged sorted array
    """
    merged: List[int] = []
    left_index = 0
    right_index = 0
    
    # Compare elements and merge in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add remaining elements from left array
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    # Add remaining elements from right array
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion sort implementation.
    
    Args:
        arr (list): List to be sorted
        
    Returns:
        list: Sorted list (modifies original array)
    """
    # Create a copy to avoid modifying the original array
    arr_copy = arr.copy()
    
    # Start from the second element (index 1)
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        
        # Move elements that are greater than key one position ahead
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        
        # Insert key at its correct position
        arr_copy[j + 1] = key
    
    return arr_copy


def timsort_sorted(arr: List[int]) -> List[int]:
    """
    Python's built-in sorted() function using Timsort algorithm.
    
    Args:
        arr (list): List to be sorted
        
    Returns:
        list: Sorted list
    """
    return sorted(arr)


def timsort_sort(arr: List[int]) -> List[int]:
    """
    Python's built-in list.sort() method using Timsort algorithm.
    
    Args:
        arr (list): List to be sorted
        
    Returns:
        list: Sorted list
    """
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy
