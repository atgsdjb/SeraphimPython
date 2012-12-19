from contextlib import closing
class test_with:
    def __init__(self):
        print 'I am test_with'
    def __enter__(self):
        print 'test_with:__enter__'
        return self
    def show(self):
        print "---------------"
    def throw_e(self):
        print '---------throw_e'
        raise TypeError
    def __exit__(self,*args):
        print 'test_with:__exit__'
        return True
if __name__ =="__main__":
#    with  test_with()  as t:
#        t.show()
#        t.throw_e()
#        print 'ok'
    file = open('seraphim.log','w+')
    with closing(file) as f:
        str = f.read()
        print str