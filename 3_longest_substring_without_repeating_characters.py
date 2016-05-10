class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        start = 0
        maxlen = 0
        for end in range(len(s)):
            if s[end] in map:
                start = max(start, map[s[end]])
            map[s[end]] = end + 1
            maxlen = max(maxlen, end - start + 1)
        return maxlen

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("au"))
    print(Solution().lengthOfLongestSubstring("aab"))
    print(Solution().lengthOfLongestSubstring("dvdf"))
    print(Solution().lengthOfLongestSubstring("tmmzuxt"))
