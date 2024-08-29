def search_element(arr, key):
    for i, element in enumerate(arr):
        if element == key:
            return i
    return -1

# Example usage:
arr = [10, 20, 30, 40, 50]
key = 30
index = search_element(arr, key)
if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found in the array.")
