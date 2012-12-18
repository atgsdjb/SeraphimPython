#generator study 
'''
author  seraphim
'''
class SeraphExcption(Exception):
    pass
def  one_dimenstional(step):
    for v in step :
        print 'I am One'
        yield v
def two_dimenstional(step):
    for v in step:
        print 'I am Two'
        yield v
def test_send():
    try:
        i = 0
        print('----begin-------')
        while i<3:
            msg = (yield '-------'+str(i))
            print '123'
            i +=1
            print type(msg)
            print msg
    except Exception:
        print 'except'
        pass
    except SeraphExcption:
        print 'SeraphExcption'
        pass
    finally:
        print 'finally'
        pass
    print "fuction end"
    print '-----'
if __name__ == "__main__":
    print __doc__
#    for i in two_dimenstional(one_dimenstional(range(2,15))):
#        print i
    array = [i for i in range(12)]
    v =test_send()
    v.throw(SeraphExcption())
    print('main ------begin')
    msg = v.next()
    print 'begin send-------'
    print msg
    for i in range(4):
        msg = v.send(i)
        print msg