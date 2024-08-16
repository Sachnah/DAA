# Global counters to count merge_sort calls and while loop executions
merge_sort_call_count = 0
while_loop_count = 0

def merge_sort(arr):
    global merge_sort_call_count
    merge_sort_call_count += 1

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    global while_loop_count
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        while_loop_count += 1
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append remaining elements from left, if any
    while i < len(left):
        while_loop_count += 1
        sorted_array.append(left[i])
        i += 1

    # Append remaining elements from right, if any
    while j < len(right):
        while_loop_count += 1
        sorted_array.append(right[j])
        j += 1

    return sorted_array

# Example Usage
arr = [38, 27, 43, 3, 9, 82, 10, 25, 17, 30]
sorted_arr = merge_sort(arr)
print("Original array :",arr)
print("Sorted array:", sorted_arr)
print("merge_sort was called = ", merge_sort_call_count, "times")
print("while loops were executed = ", while_loop_count, "times")