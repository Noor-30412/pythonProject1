import pytest as pytest
def sumofNaturalnumbers(n):
    return (n*(n+1))/2;

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def factors(n):
    a=[]
    for i in range(1,n+1):
        if n%i==0:
            a.append(i)
    return  a
@pytest.mark.parametrize("m,output",[(1,1),(2,3),(3,6),(4,10)])
def test_sumofnatural(m,output):
    assert sumofNaturalnumbers(m)==output

@pytest.mark.parametrize("k,output",[(1,1),(2,2),(3,6),(5,120)])
def test_factorial(k,output):
    assert factorial(k)== output

@pytest.mark.parametrize("l,output",[(1,[1]),(2,[1,2]),(3,[1,3]),(5,[1,5])])
def test_testcase5(l,output):
    assert factors(l)== output