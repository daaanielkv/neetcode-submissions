class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        i, j = 0, len(numbers) - 1

        while True:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            elif sum < target:
                i += 1
            else:
                j -= 1