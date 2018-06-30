
def addbits(onebit,twobit,carryinbit):
    result={
        ('1','1','1'):  ('1','1'),
        ('1','1','0'): ('0','1'),
        ('1','0','1'): ('0','1'),
        ('0', '1', '1'): ('0', '1'),
        ('0', '0', '1'): ('1', '0'),
        ('0', '1', '0'): ('1', '0'),
        ('1', '0', '0'): ('1', '0'),
        ('0', '0', '0'): ('0', '0')
    }
    return result[(onebit,twobit,carryinbit)]

def subbits(onebit,twobit,carryinbit):
    result={
        ('0', '1', '0'): ('1', '-1'),
        ('0', '1', '-1'): ('0', '-1'),
        ('1', '0', '0'): ('1', '0'),
        ('1', '0', '-1'): ('0', '0'),
        ('0', '0', '0'): ('0', '0'),
        ('0', '0', '-1'): ('1', '-1'),
        ('1', '1', '0'): ('0', '0'),
        ('1', '1', '-1'): ('1', '-1')
    }
    return result[(onebit,twobit,carryinbit)]

def add(a,b):
    if (a<0)==(b<0): myfunc=addbits
    else:
        myfunc=subbits
        if abs(a)<abs(b):
            temp=a
            a=b
            b=temp
    neg=(a<0)
    a_bin=bin(a)[2:] if a>0 else bin(a)[3:]
    print 'a bin',a_bin,a
    b_bin=bin(b)[2:] if b>0 else bin(b)[3:]
    print 'b bin', b_bin, b
    carrybit='0'
    outlist=[]
    for ind in range(max(len(a_bin),len(b_bin))):
        try:
            abit=a_bin[-1-ind]
        except IndexError:
            abit='0'
        try:
            bbit=b_bin[-1-ind]
        except IndexError:
            bbit='0'
        resbit,carrybit=myfunc(abit,bbit,carrybit)
        outlist.append(resbit)
    outlist.append(carrybit)
    print 'func is',myfunc.__name__
    print outlist
    mult=-1 if neg else 1
    print mult*int(''.join(outlist)[::-1],2)
    return mult*int(''.join(outlist)[::-1],2)

def tests():
    assert add(2,3)==5
    assert add(0,0) == 0
    assert add(12, 35) == 47
    assert add(125,6604) == 125+6604
    assert add(-12,23) == -12+23
    assert add(12,-35) == 12-35
    assert add(-15,-5) == -15-5
    assert add(-5,0) == -5
    print 'tests pass'

tests()