'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0: return 0
        leftBarrier=[0]*len(height)
        rightBarrier=[0]*len(height)
        lmax=height[0]
        for ind in range(1,len(height)):
            leftBarrier[ind]=lmax
            if lmax<height[ind]: lmax=height[ind]
        rmax=height[-1]
        for ind,elem in reversed(list(enumerate(height))):
            if ind==len(height)-1: continue
            rightBarrier[ind]=rmax
            if rmax<height[ind]: rmax=height[ind]
        minBarrier=([min(tup[0],tup[1]) for tup in zip(leftBarrier,rightBarrier)])
        return sum([tup[0]-tup[1] if tup[0]>tup[1] else 0 for tup in zip(minBarrier,height)])


    def test(self):
        assert self.trap([0,1,0,2,1,0,1,3,2,1,2,1])==6
        assert self.trap([])==0
        assert self.trap([5])==0
        assert self.trap([10,100])==0
        print 'tests pass'

if __name__=='__main__':
    sol=Solution()
    sol.test()