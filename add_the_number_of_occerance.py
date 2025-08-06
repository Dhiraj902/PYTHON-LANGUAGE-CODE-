# Count The Value Pair from the Array 
# add the number of occerence  


def count_value_pair(arr):
    key_pair = {}

    for i in range(len(arr)):
        if arr[i] in key_pair:
            key_pair[arr[i]] += 1
        else:
            key_pair[arr[i]] = 1

    return key_pair

arr = [1, 2, 3, 4, 53, 1, 2, 3, 6, 9, 6, 7, 0, 6, 7]
print(count_value_pair(arr))
