numbers = [7, 24, 985, 3, 4, 0, 6, 1, 8974, 689, 45]
chart_arr = ["a", "b", "c", "d", "e", "f", "G"]


def swap_el_of_arr(arr: list, index_f: int, index_s: int) -> list:
    third_el = arr[index_f]
    arr[index_f] = arr[index_s]
    arr[index_s] = third_el

    return arr


def choose_sort(arr: list) -> list:
    arr_len = len(arr)

    for f_i in range(arr_len):
        for s_i in range(arr_len):

            if arr[f_i] > arr[s_i]:
                swap_el_of_arr(arr, f_i, s_i)

    return arr


def buble_sort(arr: list) -> list:
    arr_len = len(arr)
    arr_range = range(arr_len)

    for el in arr_range:
        for next_el in arr_range:
            prev = next_el - 1

            if not arr[prev] and arr[prev] != 0:
                continue

            if arr[el] < arr[prev]:
                swap_el_of_arr(arr, el, prev)

    return arr


def charters_algo(arr: list):
    for el in arr:
        for i in arr:
            print(el, ":", i)
        print("----\n")


print(choose_sort(numbers))
print(buble_sort(numbers))
charters_algo(chart_arr)
