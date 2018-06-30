'''
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3
([2,3] => [5,4] => [6,7]).
'''

class Solution(object):

    def memo(self,f):
        """Decorator that caches the return value for each call to f(args).
        Then when called again with same args, we can just look it up."""
        cache = {}

        def _f(*args):
            try:
                return cache[args]
            except KeyError:
                result = f(*args)
                cache[args] = result
                return result
            except TypeError:
                # some element of args can't be a dict key
                return f(*args)

        _f.cache = cache
        return _f

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if envelopes==[[]]: return 0
        envastuples=set([tuple(env) for env in envelopes])
        wlist,hlist=zip(*envelopes)
        #wlist=[key[0] for key in envelopes]
        #hlist=[key[0] for key in envelopes]
        wlist=sorted(list(set(wlist)),reverse=True)
        hlist=sorted(list(set(hlist)),reverse=True)
        wlistdict={key:False for key in wlist}
        hlistdict={key:False for key in hlist}
        #print 'envelopes are',envelopes
        #print 'wlist is',wlist
        #print 'hlist is',hlist
        numw=len(wlist)
        numh=len(hlist)

        def rdollsof(wnum,hnum,tnum=0):
            width = wlist[wnum]
            height = hlist[hnum]
            #print '--->' * tnum, width,height,wlistdict,hlistdict,wlistdict[width],hlistdict[height]
            wsidecount = rdollsof(wnum + 1, hnum, tnum + 1) if wnum < numw - 1 else 0
            hsidecount = rdollsof(wnum, hnum + 1, tnum + 1) if hnum < numh - 1 else 0
            if (width,height) in envastuples and (not wlistdict[width]) and (not hlistdict[height]):
                currentcount=1
                wlistdict[width]=True
                hlistdict[height]=True
            else: currentcount=0
            #print '<---' * tnum, width, height, '=', max(wsidecount, hsidecount) + currentcount
            return max(wsidecount,hsidecount)+currentcount

        rdollsof=self.memo(rdollsof)
        return rdollsof(0,0)

    def test(self):
        '''
        assert self.maxEnvelopes([[11,12],[10,13]])==1
        assert self.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])==3
        assert self.maxEnvelopes([[1,1]])==1
        assert self.maxEnvelopes([[1,1],[1,1]])==1
        assert self.maxEnvelopes([[1,2],[2,1]])==1
        assert self.maxEnvelopes([[]])==0
        '''
        assert self.maxEnvelopes([[30,50],[12,2],[3,4],[12,15]])==3
        print 'tests pass'

if __name__=="__main__":
    sol=Solution()
    sol.test()