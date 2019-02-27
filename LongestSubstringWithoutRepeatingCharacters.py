#-*- coding:utf8 -*-


'''REF: https://leetcode.com/problems/longest-substring-without-repeating-characters/'''

'''WAY01'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        if s == '':
            return 0
        s_list = list(s)
        max = 1
        anchor = 0
        for idx, val in enumerate(s_list, 1):
            # print("a:%s, idx:%s, sub:%s" % (anchor, idx, s_list[anchor:idx]))
            sub_s = s_list[anchor:idx]
            # 如果子字符串有重复，则锚点前移
            if len(sub_s) > len(set(sub_s)):
                anchor += 1
                continue
            # 如果子字符没有重复，查看此时长度
            if len(sub_s) > max:
                max = len(sub_s)
        return max

def main():
    sstr = "pwwkew" #"bbbbb" # "abcabcbb"
    s = Solution()
    ret = s.lengthOfLongestSubstring(sstr)
    print(ret)


if __name__ == '__main__':
    main()


