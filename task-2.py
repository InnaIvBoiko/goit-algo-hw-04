from typing import List


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Merge k sorted lists into one sorted list using merge sort approach.
    
    Args:
        lists (List[List[int]]): List of sorted lists to merge
        
    Returns:
        List[int]: Merged sorted list
    """
    if not lists:
        return []
    
    # Filter out empty lists
    non_empty_lists = [lst for lst in lists if lst]
    
    if not non_empty_lists:
        return []
    
    if len(non_empty_lists) == 1:
        return non_empty_lists[0].copy()
    
    # Use divide and conquer approach similar to merge sort
    return _merge_k_lists_divide_conquer(non_empty_lists)


def _merge_k_lists_divide_conquer(lists: List[List[int]]) -> List[int]:
    """
    Helper function that uses divide and conquer to merge lists.
    
    Args:
        lists (List[List[int]]): Non-empty sorted lists
        
    Returns:
        List[int]: Merged sorted list
    """
    if len(lists) == 1:
        return lists[0].copy()
    
    if len(lists) == 2:
        return _merge_two_sorted_lists(lists[0], lists[1])
    
    # Divide the lists into two halves
    mid = len(lists) // 2
    left_half = lists[:mid]
    right_half = lists[mid:]
    
    # Recursively merge each half
    left_merged = _merge_k_lists_divide_conquer(left_half)
    right_merged = _merge_k_lists_divide_conquer(right_half)
    
    # Merge the two merged lists
    return _merge_two_sorted_lists(left_merged, right_merged)


def _merge_two_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
    """
    Merge two sorted lists into one sorted list.
    
    Args:
        list1 (List[int]): First sorted list
        list2 (List[int]): Second sorted list
        
    Returns:
        List[int]: Merged sorted list
    """
    result: List[int] = []
    i = j = 0
    
    # Merge elements while both lists have elements
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Add remaining elements from list1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    
    # Add remaining elements from list2
    while j < len(list2):
        result.append(list2[j])
        j += 1
    
    return result


if __name__ == "__main__":
    # Example usage
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Merged list:", merged_list)
