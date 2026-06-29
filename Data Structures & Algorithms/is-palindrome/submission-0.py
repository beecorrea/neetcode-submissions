class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1 

        while i < j:
            # Skip non-alphanumeric
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            
            # Check if is palindrome
            if s[i].lower() != s[j].lower():
                return False

            # Update pointers
            i += 1
            j -= 1

        # Never returned false, therefore s is a valid palindrome.
        return True