class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenmap={
            '{':'}','(':')','[':']'
        }
        mystack=[]
        for paren in s:
            try:
                if paren==parenmap[mystack[-1]]: mystack.pop()
                else: mystack.extend([paren])
            except (IndexError,KeyError):
                mystack.extend([paren])
        return mystack==[]

    def test(self):
        assert self.isValid('{}')==True
        assert self.isValid('')==True
        assert self.isValid('{{}[]()[{}()[]]}')==True
        assert self.isValid('{}[)')==False
        assert self.isValid('){}(')==False
        print 'tests pass'

if __name__=="__main__":
    sol=Solution()
    sol.test()