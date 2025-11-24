import sys
import random
from typing import List, Dict, Callable, Optional
from sorting_algorithms import merge_sort, insertion_sort, timsort_sorted, timsort_sort


def generate_test_data(size: int, data_type: str = "random") -> List[int]:
    """
    Generate test data of specified size and type.
    
    Args:
        size (int): Size of the data set
        data_type (str): Type of data - "random", "sorted", "reverse_sorted"
        
    Returns:
        List[int]: Generated test data
    """
    if data_type == "random":
        return [random.randint(0, 10000) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reverse_sorted":
        return list(range(size, 0, -1))
    else:
        raise ValueError("Invalid data_type. Use 'random', 'sorted', or 'reverse_sorted'")


def measure_sorting_time(sort_function: Callable[[List[int]], List[int]], data: List[int], number: int = 10) -> float:
    """
    Measure the execution time of a sorting function.
    
    Args:
        sort_function (Callable): Sorting function to test
        data (List[int]): Data to sort
        number (int): Number of times to run the test
        
    Returns:
        float: Average execution time in seconds
    """
    # Use a more direct approach to measure time
    import time
    total_time = 0.0
    
    for _ in range(number):
        test_data = data.copy()
        start_time = time.perf_counter()
        sort_function(test_data)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    
    return total_time / number


def compare_algorithms(sizes: Optional[List[int]] = None, data_types: Optional[List[str]] = None) -> Dict[str, Dict[int, Dict[str, float]]]:
    """
    Compare all sorting algorithms on different data sizes and types.
    
    Args:
        sizes (List[int]): List of data sizes to test
        data_types (List[str]): List of data types to test
        
    Returns:
        Dict: Results of the comparison
    """
    if sizes is None:
        sizes = [100, 1000, 5000, 10000]
    
    if data_types is None:
        data_types = ["random", "sorted", "reverse_sorted"]
    
    algorithms = {
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
        "Timsort (sorted)": timsort_sorted,
        "Timsort (sort)": timsort_sort
    }
    
    results: Dict[str, Dict[int, Dict[str, float]]] = {}
    
    for data_type in data_types:
        print(f"\nData Type: {data_type.replace('_', ' ').title()}")
        print("-" * 30)
        
        results[data_type] = {}
        
        for size in sizes:
            print(f"\nArray size: {size}")
            test_data = generate_test_data(size, data_type)
            results[data_type][size] = {}
            
            for name, algorithm in algorithms.items():
                # Skip insertion sort for large arrays as it's too slow
                if name == "Insertion Sort" and size > 5000:
                    time_taken = "Skipped (too slow)"
                    print(f"{name:20}: {time_taken}")
                    results[data_type][size][name] = float('inf')
                    continue
                
                try:
                    # Use fewer iterations for large data or slow algorithms
                    iterations = 3 if (size > 1000 or name == "Insertion Sort") else 10
                    time_taken = measure_sorting_time(algorithm, test_data, iterations)
                    
                    print(f"{name:20}: {time_taken:.6f} seconds")
                    results[data_type][size][name] = time_taken
                    
                except Exception as e:
                    print(f"{name:20}: Error - {str(e)}")
                    results[data_type][size][name] = float('inf')
    
    return results

def print_summary(results: Dict[str, Dict[int, Dict[str, float]]]) -> None:
    """
    Print a summary of the performance comparison.
    
    Args:
        results (Dict): Results from compare_algorithms function
    """
    
    # Find the fastest algorithm for each scenario
    print("\nFASTEST ALGORITHM BY SCENARIO:")
    for data_type in results:
        print(f"\n   {data_type.replace('_', ' ').title()} data:")
        
        for size in sorted(results[data_type].keys()):
            if size in results[data_type]:
                times = results[data_type][size]
                # Exclude insertion sort for large arrays
                valid_times = {k: v for k, v in times.items() 
                              if v != float('inf') and k != "Insertion Sort" or size <= 1000}
                
                if valid_times:
                    fastest = min(valid_times.keys(), key=lambda x: valid_times[x])
                    print(f"     Size {size}: {fastest}")



def main():
    # Check if data type is specified via command line
    if len(sys.argv) > 1:
        data_type = sys.argv[1].lower()
        if data_type in ["random", "sorted", "reverse_sorted"]:
            print(f"Running performance comparison for {data_type} data only...")
            # Run only the specified data type
            results = compare_algorithms(data_types=[data_type])
            print_summary(results)
        else:
            print("Invalid data type. Use: random, sorted, or reverse_sorted")
            return
    else:
        # Run all data types if no argument provided
        print("Running complete performance comparison...")
        results = compare_algorithms()
        print_summary(results)


if __name__ == "__main__":
    main()


# Command to run the script with a specific data type
# python3 task-1.py random
# python3 task-1.py sorted
# python3 task-1.py reverse_sorted
