class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_str = s.strip(" ")
        try:
            index_last_space = new_str.rindex(" ")
        except Exception:
            return len(new_str)
        return len(new_str[index_last_space + 1 :])
