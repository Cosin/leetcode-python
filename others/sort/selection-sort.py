# @File : selection-sort.py
# @Author : Shane Shek
# @Date : 2019/10/18 9:40
# @Desc : selection sort

# find the max number in the array
def findMax(arr: list) -> list:
    list = [arr[0], 0]
    for pos, num in enumerate(arr[1:], 1):
        if num > list[0]:
            list[0] = num
            list[1] = pos
    return list


if __name__ == "__main__":
    arr = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
    print(arr)
    for i in range(len(arr) - 1):
        list = findMax(arr[i + 1:])
        print(f"the max num is [{list[0]}] on the position [{list[1]+i+1}]\n")
        if list[0] > arr[i]:
            # swap
            temp = arr[i]
            arr[i] = list[0]
            arr[list[1]+i+1] = temp
        print(arr)


