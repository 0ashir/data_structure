# this bucket sort code will work only if you have elements in between 0 and 1
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def bucket_sort(arr):
    sorted_arr = []
    buckets = [[] for _ in range(10)]
    for i in arr:
        index = int(10 * i)
        buckets[index].append(i)
    for i in range(len(buckets)):
        sorted_buckets = bubblesort(buckets[i])
        sorted_arr.append(sorted_buckets)
    for i in sorted_arr:
        for j in i:
            print(j, end=', ')


if __name__ == "__main__":
    arr = [0.12, 0.11, 0.23, 0.25, 0.67, .89]
    bucket_sort(arr)
