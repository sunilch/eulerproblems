class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1dict={}
        num2dict={}
        result=[]
        for num in nums1: num1dict[num]=num1dict.get(num,0)+1
        for num in nums2: num2dict[num]=num2dict.get(num,0)+1
        for num,val in num1dict.iteritems():
            times=min(val,num2dict.get(num,0))
            result+=[num]*times
        return result

    def test(self):
        assert self.intersect([1],[1,1])==[1]
        assert self.intersect([1,2,2,3],[1,1,2,3,3,4])==[1,2,3]
        print 'tests pass'

if __name__=="__main__":
    sol=Solution()
    sol.test()