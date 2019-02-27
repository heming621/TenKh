#-*- coding:utf8 -*- 


'''REF:https://leetcode.com/problems/two-sum/ 求数组某两元素之和为指定值的下标'''

'''WAY01: 暴力，两层循环'''
class Solution:
    def twoSum(self, nums, target):
        for idx_a, a in enumerate(nums):
            for idx_b, b in enumerate(nums):
                if idx_a == idx_b:
                    continue
                if a+b == target:
                    return [idx_a, idx_b]

'''WAY02: 预建立字典，循环一次'''
class Solution:
    def twoSum(self, nums, target):
        dic = dict((v,k) for k, v in enumerate(nums))
        for idx_val, val in enumerate(nums):
            other_val = target - val
            if other_val in nums and dic[other_val] != idx_val:
                return [idx_val, dic[other_val]]
                
'''WAY03: 动态建立字典，循环一次，节省空间，又避免同一个值使用2次'''
class Solution:
    def twoSum(self, nums, target):
        dic = dict()
        for idx, val in enumerate(nums):
            o_val = target - val
            if o_val in dic.keys():
                return [dic[o_val], idx]
            else:
                dic[val] = idx


def main():
    nums = [2, 7, 11, 15] # [3, 3] 
    target = 9
    ret = Solution()
    rlt = ret.twoSum(nums, target)
    print(rlt)

if __name__ == '__main__':
    main()



