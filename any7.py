from torch import true_divide


def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    counter = 0
    # YOUR CODE HERE
    for n in nums:
        if n == 7:
            return True
        counter = +1
    if counter >= 1:
        return False


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
