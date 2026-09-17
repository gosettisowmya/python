class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = shortest valid subarray
        # that ends at or before index i
        best = [float('inf')] * n

        prefix = 0
        last = {0: -1}

        ans = float('inf')
        min_len = float('inf')

        for i in range(n):
            prefix += arr[i]

            if prefix - target in last:
                prev = last[prefix - target]

                # Current subarray is prev+1 ... i
                length = i - prev

                # Previous subarray must end at or before prev
                if prev >= 0 and best[prev] != float('inf'):
                    ans = min(ans, length + best[prev])

                # Save current valid subarray
                min_len = min(min_len, length)

            # Best valid subarray up to i
            if i == 0:
                best[i] = min_len
            else:
                best[i] = min(best[i - 1], min_len)

            last[prefix] = i

        return -1 if ans == float('inf') else ans
