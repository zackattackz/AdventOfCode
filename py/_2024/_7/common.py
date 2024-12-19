from itertools import product

def parse(file):
    for line in file:
        test_val, nums = line.strip().split(":")
        yield int(test_val), map(int, nums.strip().split(" "))

def valid_ops(test_val, ops, nums):
    res = ops[0](*nums[:2])
    for i, num in enumerate(nums[2:]):
        res = ops[i+1](res, num)
    return res == test_val

def sum_valid_test_vals(equations, allowed_ops):
    res = 0
    for test_val, nums in equations:
        nums = list(nums)
        possible_ops = product(allowed_ops, repeat=len(nums) - 1)
        for ops in possible_ops:
            if valid_ops(test_val, ops, nums):
                res += test_val
                break
    return res

