def linear_search(arr, target):
    index = 0
    for element in arr:
        if element == target:
            return index
        index += 1
    return -1

# Example usage
arr = [3, 5, 2, 4, 9]
target = 4

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found")
