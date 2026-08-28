class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Check whether palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2 == 1:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Characters needed for the left half
        half_count = [c // 2 for c in count]
        half_len = n // 2

        # ------------------------------------------------
        # Function to build palindrome from left half
        # ------------------------------------------------
        def make_palindrome(left):
            left = "".join(left)
            right = left[::-1]
            return left + middle + right

        # ------------------------------------------------
        # 1. Try to keep target's left half exactly same
        # ------------------------------------------------
        remaining = half_count[:]
        possible = True

        for ch in target[:half_len]:
            idx = ord(ch) - ord('a')

            if remaining[idx] == 0:
                possible = False
                break

            remaining[idx] -= 1

        if possible:
            left = list(target[:half_len])
            candidate = make_palindrome(left)

            if candidate > target:
                return candidate

        # ------------------------------------------------
        # 2. Change one character from right to left
        # ------------------------------------------------
        for i in range(half_len - 1, -1, -1):

            # Recalculate remaining characters for target[:i]
            remaining = half_count[:]

            possible = True

            for ch in target[:i]:
                idx = ord(ch) - ord('a')

                if remaining[idx] == 0:
                    possible = False
                    break

                remaining[idx] -= 1

            if not possible:
                continue

            # Try a character greater than target[i]
            current = ord(target[i]) - ord('a')

            for j in range(current + 1, 26):

                if remaining[j] == 0:
                    continue

                # Use this larger character
                remaining[j] -= 1

                left = list(target[:i])
                left.append(chr(j + ord('a')))

                # Fill the rest with smallest characters
                for k in range(26):
                    left.extend(
                        [chr(k + ord('a'))] * remaining[k]
                    )

                candidate = make_palindrome(left)

                if candidate > target:
                    return candidate

                # Undo
                remaining[j] += 1

        return ""
