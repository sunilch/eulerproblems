# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
import random
#predefined
def pick(num,myseed=5):
    return 3
    random.seed(myseed)
    return random.randint(1,num)

def guesstemplate(guess,actual):
    return (-1 if guess < actual else
            1 if guess > actual else
            0)


def main(n):
    #picking
    picked=pick(n,20)
    #defining guess
    def guess(myguess): return guesstemplate(myguess,picked)

    def guessNumber(n):
        """
        :type n: int
        :rtype: int
        """
        def findmiddle(a,b):
            return a+(b-a)/2 if b-a%2==0 else a+(b-a+1)/2

        def search(a,b):
            print 'searching in {},{}'.format(a,b)
            intlen=b-a
            myguess=findmiddle(a,b)
            myguessresult = guess(myguess)
            print 'guess is {} and result is {}'.format(myguess,myguessresult)
            x = raw_input()
            if myguessresult==0: return myguess
            elif intlen==0: raise
            elif myguessresult==1: search(a,myguess-1)
            else: search(myguess+1,b)

        return search(1,n)

    return guessNumber(n)

print main(10)