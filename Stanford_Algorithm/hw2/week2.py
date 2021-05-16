count = 0


def readData(filename):
    data = []
    with open(filename) as f:
        for row in f.readlines():
            data.append(int(row))
    return data


def mergeSort(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    nums = merge(left, right)
    return nums


def merge(left, right):
    mid = (len(left) + len(right)) // 2
    tmp = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
            global count
            count += mid - i
    while i < len(left):
        tmp.append(left[i])
        i += 1
    while j < len(right):
        tmp.append(right[j])
        j += 1

    return tmp


def main():
    # data = [5, 4, 3, 2, 1]
    # data = [1, 20, 6, 4, 5]
    data = readData("data.txt")
    # data = [5, 3, 8, 6, 2, 7, 1, 4]
    data = mergeSort(data)
    print(count)


if __name__ == "__main__":
    main()
