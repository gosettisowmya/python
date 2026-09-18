class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        # First and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Try to create a valid substring starting at
        # the first occurrence of each character
        for i in range(n):
            idx = ord(s[i]) - ord('a')

            # Only first occurrence can start a candidate
            if first[idx] != i:
                continue

            l = i
            r = last[idx]
            valid = True

            j = l
            while j <= r:
                c = ord(s[j]) - ord('a')

                # This character appeared before l,
                # so substring cannot contain all its occurrences
                if first[c] < l:
                    valid = False
                    break

                # Need to include all occurrences of this character
                r = max(r, last[c])
                j += 1

            if valid:
                intervals.append((l, r))

        # Choose non-overlapping intervals
        intervals.sort(key=lambda x: x[1])

        result = []
        end = -1

        for l, r in intervals:
            if l > end:
                result.append(s[l:r + 1])
                end = r

        return result
