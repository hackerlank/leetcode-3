class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        lookup = {}
    	for i, n in enumerate(num):
    		if (target - n) in lookup:
    			return (lookup[target-n]+1, i+1)   
    		lookup[n] = i
