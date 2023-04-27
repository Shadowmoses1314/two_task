from typing import List, Tuple


def find_monotonic_subarray(arr: List[int]) -> Tuple[int, int]:
    n = len(arr)
    dp_inc = [1] * n
    dp_dec = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            dp_inc[i] = dp_inc[i - 1] + 1
        if arr[n - i - 1] > arr[n - i]:
            dp_dec[n - i - 1] = dp_dec[n - i] + 1

    max_inc = max(dp_inc)
    max_dec = max(dp_dec)
    idx_inc = dp_inc.index(max_inc)
    idx_dec = dp_dec.index(max_dec)

    if max_inc >= max_dec:
        return idx_inc - max_inc + 1, idx_inc
    else:
        return idx_dec, idx_dec + max_dec - 1


arr = list(map(int, input().replace(',', '').split()))
left, right = find_monotonic_subarray(arr)
print(f'{left}, {right}')
