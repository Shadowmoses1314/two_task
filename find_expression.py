from itertools import product


def find_expression(n, m):
    nums = [str(i) for i in range(1, n+1)]
    result = [num for num in ''.join(nums) if num != '0']
    count = len(result)
    zero_idx = ''.join(nums).find('0')
    for p in product(['', '+'], repeat=count-1):
        expr = ''
        for i in range(count-1):
            expr += result[i] + p[i]
        expr += result[count-1]
        if eval(expr) == m:
            second_one_idx = expr.find('1', 1)
            num_plus = expr[:second_one_idx].count('+')
            new_zero_idx = zero_idx + num_plus + 1
            if zero_idx != -1:
                return expr[:new_zero_idx] + '0' + expr[new_zero_idx:]
            return expr
    return None


n, m = map(int, input().split())
expression = find_expression(n, m)
if expression:
    print(expression + '=' + str(m))
else:
    print('No valid expression found.')
