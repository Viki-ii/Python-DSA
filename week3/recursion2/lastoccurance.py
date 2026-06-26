def last_occurrence(arr, target, index=0):
	if index == len(arr):
		return -1

	pos = last_occurrence(arr, target, index + 1)
	if pos != -1:
		return pos

	return index if arr[index] == target else -1


# Example usage
if __name__ == "__main__":
	arr = [1, 2, 3, 2, 4, 2, 5]
	target = 2
	print(last_occurrence(arr, target))  # Output: 5
