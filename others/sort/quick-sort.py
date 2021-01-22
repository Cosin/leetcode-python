# @File : quick-sort.py
# @Author : Shane Shek
# @Date : 2019/10/29 14:57
# @Desc : Quick sort

def swap(array: list, i: int, j: int):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def partition(array: list, left: int, right: int):
    if right < left:
        return
    pivot = array[left]
    pivot_pos = left
    for i in range(right - left):
        if array[left + i + 1] < pivot:
            swap(array, pivot_pos, left + i + 1)
            pivot_pos = left + i + 1
    return pivot_pos


def quickSort(array: list, left: int, right: int):
    if len(array) < 2:
        return array
    pivot_pos = partition(array, left, right)

    quickSort(array, left, pivot_pos - 1)
    quickSort(array, pivot_pos + 1, right)


if __name__ == "__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    quickSort(a, 0, len(a) - 1)
    print(a)
