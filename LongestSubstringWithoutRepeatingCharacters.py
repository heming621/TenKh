#-*- coding:utf8 -*-


'''REF: https://leetcode.com/problems/longest-substring-without-repeating-characters/'''

'''WAY01'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        if s == '':
            return 0
        max = 1
        anchor = 0
        for idx, val in enumerate(s, 1):
            # print("a:%s, idx:%s, sub:%s" % (anchor, idx, s[anchor:idx]))
            sub_s = s[anchor:idx]
            # 如果子字符串有重复，则锚点前移
            if len(sub_s) > len(set(sub_s)):
                anchor += 1
                continue
            # 如果子字符没有重复，查看此时长度
            if len(sub_s) > max:
                max = len(sub_s)
        return max


'''WAY02 slide window, still need to improve, 0.5h+ cost'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        if s == '':
            return 0
        s_list = list(s)
        # set max=1, len(s)>=1
        sub_str, max_len = [], 1
        i, j, lens = 0, 1, len(s_list)
        while i < lens and j < lens:
            sub_str = s[i:j]
            max_len = max(len(sub_str), max_len)
            # print("%s - [%s, %s], %s" % (sub_str, i, j, s[j]))
            if s[j] in sub_str:
                i += 1
                j = i+1 
            else:       
                j += 1
                max_len = max(len(sub_str)+1, max_len)    
        return max_len

'''WAY03 extra dict used. The best way.'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        start, dic = 0, {}
        max_len, lens = 0, len(s)
        for i in range(lens):
            # 如果在字典，则取对应重复元素+1为初始点
            if s[i] in dic:
                start = max(dic[s[i]]+1, start)
            dic[s[i]] = i
            max_len = max(max_len, i - start + 1) 
        return max_len

def main():
    sstr = "abcabcbb" #" " #"dvdf" #"pwwkew" #"auc" #    "bbbbb" #        
    s = Solution()
    ret = s.lengthOfLongestSubstring(sstr)
    print(ret)


if __name__ == '__main__':
    main()


