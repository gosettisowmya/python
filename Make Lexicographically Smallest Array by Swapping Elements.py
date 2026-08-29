class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original_index)
        arr = sorted((nums[i], i) for i in range(n))

        ans = [0] * n
        i = 0

        while i < n:
            j = i + 1

            # Find one connected group
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            # Original indices of this group
            indices = sorted(index for value, index in arr[i:j])

            # Put sorted values into sorted indices
            for k in range(len(indices)):
                ans[indices[k]] = arr[i + k][0]

            i = j

        return ans
