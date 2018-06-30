class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.initializedata()
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    val=int(board[i][j])-1
                    if self.rowdata[i][val]==1: self.rowdata[i][val]=0
                    else: return False
                    if self.coldata[j][val]==1: self.coldata[j][val]=0
                    else: return False
                    if self.bucdata[self.whichbucket(i,j)][val]==1: self.bucdata[self.whichbucket(i,j)][val]=0
                    else: return False
        return True

    def initializedata(self):
        self.rowdata=[[1]*9 for ind in range(9)]
        self.coldata=[[1]*9 for ind in range(9)]
        self.bucdata=[[1]*9 for ind in range(9)]

    def whichbucket(self,indi,indj):
        bucketmap={
            (0,0):0,
            (0,1):1,
            (0,2):2,
            (1,0):3,
            (1,1):4,
            (1,2):5,
            (2,0):6,
            (2,1):7,
            (2,2):8
        }
        return bucketmap[(indi/3,indj/3)]

    def test(self):
        assert self.isValidSudoku([['.']*9]*9)==True
        print 'tests pass'

if __name__=='__main__':
    sol=Solution()
    sol.test()