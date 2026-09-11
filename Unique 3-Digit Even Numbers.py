class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        nums = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):

                    # Cannot use the same position twice
                    if i == j or i == k or j == k:
                        continue

                    # First digit cannot be 0
                    if digits[i] == 0:
                        continue

                    # Last digit must be even
                    if digits[k] % 2 != 0:
                        continue

                    number = digits[i] * 100 + digits[j] * 10 + digits[k]
                    nums.add(number)

        return len(nums)
