class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        vlist1=[self.myint(sec) for sec in version1.split('.')]
        vlist2=[self.myint(sec) for sec in version2.split('.')]
        whichside=0
        while whichside==0:
            manyexcepts=0
            try: v1=vlist1.pop(0)
            except:
                v1=0
                manyexcepts+=1
            try: v2=vlist2.pop(0)
            except:
                v2=0
                manyexcepts+=1
            if v1>v2: whichside=1
            elif v1<v2: whichside=-1
            if manyexcepts==2: break
        return whichside

    def myint(self,inp):
        return 0 if inp=='' else int(inp)

    def test(self):
        #assert self.compareVersion('1.2','1.1.1')==1
        #assert self.compareVersion('1.10','1.1')==1
        assert self.compareVersion('.1.25','1.0.1')==-1
        assert self.compareVersion('1.1','1.1.0')==0
        assert self.compareVersion('','')==0
        print 'tests pass'

if __name__=='__main__':
    sol=Solution()
    sol.test()