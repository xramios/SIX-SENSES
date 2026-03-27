def heapify(arr, i, n):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # If left child exists and is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child exists and is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify
        heapify(arr, largest, n)


if __name__ == "__main__":
    arr = [10, 5, 15, 2, 20, 30]
    print("Original array:", end=" ")
    for i in range(len(arr)):
        print(arr[i], end=" ")

    # Build max-heap
    for i in range(len(arr)//2 - 1, -1, -1):
        heapify(arr, i, len(arr))

    # Print array after max-heapify
    print("\nMax-Heap after heapify operation:", end=" ")
    for i in range(len(arr)):
        print(arr[i], end=" ")