import multitask
print 'multitask'
def f1():
    v = 0;
    while True:
        print 'f1'
        yield v;
        v +=1
def f2():
    v = 0;
    while True:
        print 'f2'
        yield v;
        v +=1
def f3():
    v = 0;
    while True:
        print 'f3'
        yield v;
        v +=1
if __name__ == "__main__":
    multitask.add(f1())
    multitask.add(f2())
    multitask.add(f3())
    multitask.run()
