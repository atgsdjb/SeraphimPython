# python startup file
import readline
import rlcompleter
import atexit
import os
# tab completion
readline.parse_and_bind('tab: complete')
# history file
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
try:
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.write_history_file, histfile)
del os, histfile, readline, rlcompleter 
>>> import md5
>>> md5.<tab>
md5.__class__         md5.__file__         md5.__name__         md5.__repr__         md5.digest_size         
md5.__delattr__       md5.__getattribute__ 
md5.__new__       md5.__setattr__       md5.md5       
md5.__dict__          md5.__hash__          md5.__reduce__          md5.__str__          md5.new          
md5.__doc__           md5.__init__           md5.__reduce_ex__           md5.blocksize
tarek@luvdit:~$ ipython 
Python 2.4.4 (#2, Apr 
5 2007, 20:11:18) 
Type "copyright", "credits" or "license" for more information.
IPython 0.7.2 -- An enhanced Interactive Python.
?       -> Introduction to IPython's features.
%magic 
-> Information about IPython's 'magic' % functions.
help    -> Python's own help system.
object? -> Details about 'object'. ?object also works, ?? prints more.
In [1]: 
[build] 
compiler = mingw32

./configure --enable-multibyte 
make
sudo make install 
set encoding=utf8
set paste
set expandtab
set textwidth=0
set tabstop=4
set softtabstop=4
set shiftwidth=4
set autoindent
set backspace=indent,eol,start
set incsearch
set ignorecase
set ruler
set wildmenu
set commentstring=\ #\ %s
set foldlevel=0
set clipboard+=unnamed   
syntax on
>>> numbers = range(10)
>>> size = len(numbers)
>>> evens = []
>>> i = 0
>>> while i < size:
...     if i % 2 == 0:
...         evens.append(i)
...     i += 1
... 
>>> evens
[0, 2, 4, 6, 8]
>>> [i for i in range(10) if i % 2 == 0]
[0, 2, 4, 6, 8]
>>> i = 0
>>> seq = ["one", "two", "three"]
>>> for element in seq:
...     seq[i] = '%d: %s' % (i, seq[i])
...     i += 1
... 
>>> seq
['0: one', '1: two', '2: three']
>>> seq = ["one", "two", "three"]
>>> for i, element in enumerate(seq):
...     seq[i] = '%d: %s' % (i, seq[i])
... 
>>> seq
['0: one', '1: two', '2: three']
>>> def _treatment(pos, element):
...     return '%d: %s' % (pos, element)
... 
>>> seq = ["one", "two", "three"]
>>> [_treatment(i, el) for i, el in enumerate(seq)]
['0: one', '1: two', '2: three']
>>> i = iter('abc')
>>> i.next()
'a'
>>> i.next()
'b'
>>> i.next()
'c'
>>> i.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> class MyIterator(object):
...     def __init__(self, step):
...         self.step = step
...     def next(self):
...         """Returns the next element."""
...         if self.step == 0:
...             raise StopIteration
...         self.step -= 1
...         return self.step
...     def __iter__(self):
...         """Returns the iterator itself."""
...         return self
... 
>>> for el in MyIterator(4):


...     print el
... 
3
2
1
0
>>> import tokenize
>>> reader = open('amina.py').next
>>> tokens = tokenize.generate_tokens(reader)
>>> tokens.next()
(1, 'from', (1, 0), (1, 4), 'from amina.quality import similarities\n')
>>> tokens.next()
(1, 'amina', (1, 5), (1, 10), 'from amina.quality import similarities\n')
>>> tokens.next()
>>> def power(values):
...     for value in values:
...         print 'powering %s' % value
...         yield value
... 
>>> def adder(values):
...     for value in values:
...         print 'adding to %s' % value
...         if value % 2 == 0:
...             yield value + 3
...         else:
...             yield value + 2
... 
>>> elements = [1, 4, 7, 9, 12, 19]
>>> res = adder(power(elements))
>>> res.next()
powering 1
adding to 1
3
>>> res.next()
powering 4
adding to 4
7
>>> res.next()
powering 7
adding to 7
9
>>> def psychologist():
...     print 'Please tell me your problems'
...     while True:
...         answer = (yield)
...         if answer is not None:
...             if answer.endswith('?'):
...                 print ("Don't ask yourself " 
...                        "too much questions")
...             elif 'good' in answer:
...                 print "A that's good, go on"
...             elif 'bad' in answer:
...                 print "Don't be so negative"
... 
>>> free = psychologist()
>>> free.next()
Please tell me your problems
>>> free.send('I feel bad')
Don't be so negative
>>> free.send("Why I shouldn't ?")
Don't ask yourself too much questions
>>> free.send("ok then i should find what is good for me")
A that's good, go on
>>> def my_generator():
...     try:
...         yield 'something' 
...     except ValueError:
...         yield 'dealing with the exception'
...     finally:
...         print "ok let's clean"
... 
>>> gen = my_generator()
>>> gen.next()
'something'
>>> gen.throw(ValueError('mean mean mean'))
'dealing with the exception'
>>> gen.close()
ok let's clean
>>> gen.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> import multitask
>>> import time
>>> def coroutine_1():
...     for i in range(3):
...         print 'c1'
...         yield i
... 
>>> def coroutine_2():
...     for i in range(3):
...         print 'c2'
...         yield i
... 
>>> multitask.add(coroutine_1())
>>> multitask.add(coroutine_2())
>>> multitask.run()
c1
c2
c1
c2
c1
c2
from __future__ import with_statement
from contextlib import closing
import socket
import multitask

def client_handler(sock):
    with closing(sock):
        while True:
            data = (yield multitask.recv(sock, 1024))
            if not data:
                break
            yield multitask.send(sock, data)


def echo_server(hostname, port):
    addrinfo = socket.getaddrinfo(hostname, port, 
                                                 
socket.AF_UNSPEC,
                                  socket.SOCK_STREAM)
    (family, socktype, proto, 
     canonname, sockaddr) = addrinfo[0]

    with closing(socket.socket(family,
                               socktype, 
                               proto)) as sock:
        sock.setsockopt(socket.SOL_SOCKET, 
                        socket.SO_REUSEADDR, 1)
        sock.bind(sockaddr)
        sock.listen(5)
        while True:
            multitask.add(client_handler((
                     yield multitask.accept(sock))[0]))

if __name__ == '__main__':
    import sys

    hostname = None
    port = 1111

    if len(sys.argv) > 1:
        hostname = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])

    multitask.add(echo_server(hostname, port))
    try:
        multitask.run()
    except KeyboardInterrupt:
        pass
>>> import itertools
>>> def starting_at_five():
...     value = raw_input().strip()
...     while value != '':
...         for el in itertools.islice(value.split(), 
...                                    4, None):
...             yield el
...         value = raw_input().strip()
... 
>>> iter = starting_at_five()
>>> iter.next()
one two three four five six
'five'
>>> iter.next()
'six'
>>> iter.next()
one two
one two three four five six
'five'
>>> iter.next()
'six'
>>> iter.next()
one
one two three four five six seven eight
'five'
>>> iter.next()
'six'
>>> iter.next()
'seven'
>>> iter.next()
'eight'
>>> import itertools
>>> def with_head(iterable, headsize=1):
...     a, b = itertools.tee(iterable)
...     return list(itertools.islice(a, headsize)), b
... 
>>> with_head(seq)
([1], <itertools.tee object at 0x100c698>)
>>> with_head(seq, 4)
([1, 2, 3, 4], <itertools.tee object at 0x100c670>)
>>> from itertools import groupby
>>> def compress(data):
...     return ((len(list(group)), name)
...             for name, group in groupby(data))
... 
>>> def decompress(data):
...     return (car * size for size, car in data)
... 
>>> list(compress('get uuuuuuuuuuuuuuuuuup'))
[(1, 'g'), (1, 'e'), (1, 't'), (1, ' '), 

(18, 'u'), (1, 'p')]
>>> compressed = compress('get uuuuuuuuuuuuuuuuuup')
>>> ''.join(decompress(compressed))
'get uuuuuuuuuuuuuuuuuup'
>>> class WhatFor(object):
...     def it(cls):
...         print 'work with %s' % cls
...     it = classmethod(it)
...     def uncommon():
...         print 'I could be a global function'
...     uncommon = staticmethod(uncommon)
... 
>>> class WhatFor(object):
...     @classmethod
...     def it(cls):
...         print 'work with %s' % cls
...     @staticmethod
...     def uncommon():


...         print 'I could be a global function'
... 
>>> this_is = WhatFor()
>>> this_is.it()
work with <class '__main__.WhatFor'>
>>> this_is.uncommon()
I could be a global function
def mydecorator(arg1, arg2):
    def _mydecorator(function):
        def __mydecorator(*args, **kw):
            # do some stuff before the real 
            # function gets called 
            res = function(*args, **kw)
            # do some stuff after
            return res
        # returns the sub-function
        return __mydecorator
    return _mydecorator
>>> from threading import RLock
>>> lock = RLock()
>>> def synchronized(function):
...     def _synchronized(*args, **kw):
...         lock.acquire()
...         try:
...             return function(*args, **kw)
...         finally:
...             lock.release()
...     return _synchronized
...
>>> @synchronized
... def thread_safe():    # make sure it locks the resource
...     pass
... 
>>> hosts = file('/etc/hosts')
>>> try:
...     for line in hosts:
...         if line.startswith('#'):
...             continue
...         print line
... finally:
...     hosts.close()
... 
127.0.0.1       localhost
255.255.255.255 broadcasthost
::1             localhost 


>>> from __future__ import with_statement
>>> with file('/etc/hosts') as hosts:
...     for line in hosts:
...         if line.startswith('#'):
...             continue
...         print line
...
127.0.0.1       localhost
255.255.255.255 broadcasthost
::1             localhost 

>>> class Context(object):
...     def __enter__(self):
...         print 'entering the zone'
...     def __exit__(self, exception_type, exception_value, 
...                  exception_traceback):
...         print 'leaving the zone'
...         if exception_type is None:
...             print 'with no error'
...         else:
...             print 'with an error (%s)' % exception_value
... 
>>> with Context():
...     print 'i am the zone'
... 
entering the zone
i am the zone
leaving the zone
with no error
>>> with Context():
...     print 'i am the buggy zone'
...     raise TypeError('i am the bug')
... 
entering the zone
i am the buggy zone
leaving the zone
with an error (i am the bug)
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
TypeError: i am the bug
>>> import logging
>>> from __future__ import with_statement
>>> from contextlib import contextmanager
>>> @contextmanager
... def logged(klass, logger):
...     # logger
...     def _log(f):
...         def __log(*args, **kw):
...             logger(f, args, kw)
...             return f(*args, **kw)
...         return __log
...
...     # let's equip the class
...     for attribute in dir(klass):
...         if attribute.startswith('_'):
...             continue
...         element = getattr(klass, attribute)
...         setattr(klass, '__logged_%s' % attribute, element)
...         setattr(klass, attribute, _log(element))
...
...     # let's work
...     yield klass
...
...     # let's remove the logging


...     for attribute in dir(klass):
...         if not attribute.startswith('__logged_'):
...             continue
...         element = getattr(klass, attribute)
...         setattr(klass, attribute[len('__logged_'):], 
...                 element)                 
...         delattr(klass, attribute)
... 

>>> class One(object):
...     def _private(self):
...         pass
...     def one(self, other):
...         self.two()
...         other.thing(self)
...         self._private()
...     def two(self):
...         pass
... 
>>> class Two(object):
...     def thing(self, other):
...         other.two()
... 
>>> calls = []
>>> def called(meth, args, kw):
...     calls.append(meth.im_func.func_name)
... 
>>> with logged(One, called):
...     one = One()
...     two = Two()
...     one.one(two)
... 
>>> calls
['one', 'two', 'two']


>>> class distinctdict(dict):
...     def __setitem__(self, key, value):
...         try:
...             value_index = self.values().index(value)
...             # keys() and values() will return
...             # corresponding lists 
...             # as long as the dict is not changed
...             # between the two calls
...             # otherwise the dict type does not guarantee
...             # the ordering.
...             existing_key = self.keys()[value_index]
...             if existing_key != key:
...                 raise DistinctError(("This value already 
...                                     "exists for '%s'") % \
...                                        str(self[existing_key]))
...         except ValueError:
...             pass
...
...         super(distinctdict, self).__setitem__(key, value)
... 
>>> my = distinctdict()
>>> my['key'] = 'value'
>>> my['other_key'] = 'value'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 14, in __setitem__
DistincErrorError: This value already exists for 'value'
>>> my['other_key'] = 'value2'
>>> my
{'other_key': 'value2', 'key': 'value'}
>>> class folder(list):
...     def __init__(self, name):
...         self.name = name
...     def dir(self):
...         print 'I am the %s folder.' % self.name
...         for element in self:
...             print element
... 
>>> the = folder('secret')
>>> the
[]
>>> the.append('pics')
>>> the.append('videos')
>>> the.dir()
I am the secret folder:
pics
videos 
>>> class Mama(object):     # this is the old way
...     def says(self):
...         print 'do your homework'
... 
>>> class Sister(Mama):
...     def says(self): 
...         Mama.says(self)
...         print 'and clean your bedroom'
... 
>>> anita = Sister()
>>> anita.says()
do your homework
and clean your bedroom
>>> class Sister(Mama): 
# this is the new way
...     def says(self):
...         super(Sister, self).says()
...         print 'and clean your bedroom'
... 
>>> class Base1: 
...     pass 
... 
>>> class Base2: 
...     def method(self): 
...         print 'Base2' 
... 
>>> class MyClass(Base1, Base2): 
...     pass 
... 
>>> here = MyClass() 
>>> here.method() 
Base2
>>> class BaseBase: 
...     def method(self): 
...         print 'BaseBase' 
... 


>>> class Base1(BaseBase): 
...     pass 
... 
>>> class Base2(BaseBase): 
...     def method(self): 
...         print 'Base2' 
... 
>>> class MyClass(Base1, Base2): 
...     pass 
... 
>>> here = MyClass() 
>>> here.method() 
BaseBase
>>> class BaseBase(object):
...     def method(self):
...         print 'BaseBase'
... 
>>> class Base1(BaseBase):
...     pass
... 
>>> class Base2(BaseBase):
...     def method(self):
...         print 'Base2'
... 
>>> class MyClass(Base1, Base2):
...     pass
... 
>>> here = MyClass()
>>> here.method()
Base2
L[MyClass(Base1, Base2)] = 
       MyClass + merge(L[Base1], L[Base2], Base1, Base2)
the linearization of C is the sum of C plus the merge of the linearizations of the parents and the list of the parents
Take the 

Then repeat the operation until all the class are removed or it is impossible to find good heads. In this case, it is impossible to construct the merge, Python 2.3 will refuse to create the class MyClass and will raise an exception.
>>> def L(klass):
...     return [k.__name__ for k in klass.__mro__]
... 
>>> L(MyClass)
['MyClass', 'Base1', 'Base2', 'BaseBase', 'object']
>>> class A(object):
...     def __init__(self):
...         print "A"
...         super(A, self).__init__()
... 
>>> class B(object):
...     def __init__(self):
...         print "B"
...         super(B, self).__init__()
... 
>>> class C(A,B):
...     def __init__(self):
...         print "C"
...         A.__init__(self)
...         B.__init__(self)
... 
>>> print "MRO:", [x.__name__ for x in C.__mro__]
MRO: ['C', 'A', 'B', 'object']
>>> C()
C A B B
<__main__.C object at 0xc4910>
>>> from SimpleHTTPServer import SimpleHTTPRequestHandler
>>> SimpleHTTPRequestHandler.__mro__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: class SimpleHTTPRequestHandler has no attribute '__mro__'
>>> from collections import deque
>>> deque.__mro__
(<type 'collections.deque'>, <type 'object'>)
>>> from random import Random
>>> random.Random.__mro__
(<class 'random.Random'>, <type '_random.Random'>, <type 'object'>)
>>> from zope.app.container.browser.adding import Adding
>>> Adding.__mro__
(<class 'zope.app.container.browser.adding.Adding'>, 

<class 'zope.publisher.browser.BrowserView'>, 

<class 'zope.location.location.Location'>, 

<type 'object'>)
>>> class BaseBase(object):
...     def __init__(self):
...         print 'basebase'
...         super(BaseBase, self).__init__()         
... 
>>> class Base1(BaseBase):
...     def __init__(self):
...         print 'base1'
...         super(Base1, self).__init__()         
... 
>>> class Base2(BaseBase):
...     def __init__(self, arg):
...         print 'base2'
...         super(Base2, self).__init__()         
... 
>>> class MyClass(Base1 , Base2):
...     def __init__(self, arg):
...         print 'my base'
...         super(MyClass, self).__init__(arg) 
... 
>>> m = MyClass(10)
my base
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in __init__
TypeError: __init__() takes exactly 1 argument (2 given) 
>>> class BaseBase(object):
...     def __init__(self, *args, **kw):
...         print 'basebase'
...         super(BaseBase, self).__init__(*args, **kw) 

... 
>>> class Base1(BaseBase):
...     def __init__(self, *args, **kw):
...         print 'base1'
...         super(Base1, self).__init__(*args, **kw)         
... 
>>> class Base2(BaseBase):
...     def __init__(self, arg, *args, **kw):
...         print 'base2'
...         super(Base2, self).__init__(*args, **kw) 
... 
>>> class MyClass(Base1 , Base2):
...     def __init__(self, arg):
...         print 'my base'
...         super(MyClass, self).__init__(arg)
... 
>>> m = MyClass(10)
my base
base1
base2
basebase
>>> class MyClass(object):
...     __secret_value = 1
... 
>>> instance_of = MyClass()
>>> instance_of.__secret_value
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyClass' object has no attribute '__secret_value'
>>> dir(MyClass)
['_MyClass__secret_value', '__class__', '__delattr__', '__dict__', '__doc__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__str__', '__weakref__']
>>> instance_of._MyClass__secret_value
1
# 1- looking for definition
if hasattr(MyClass, 'attribute'):
    attribute = MyClass.attribute
    AttributeClass = attribute.__class__

    # 2 - does attribute definition have a getter ?    
    readable = hasattr(AttributeClass, '__get__')

    # 3 - does attribute definition have a setter,
    #     or 'attribute' is not found in __dict__
    writable = (hasattr(AttributeClass, '__set__') or 
                'attribute' not in instance.__dict__)

    if readable and writable:
        # 4 – let’s call the descriptor 
        return AttributeClass.__get__(attribute,
                                      instance, MyClass)

# 5 - regular access with __dict__
return instance.__dict__['attribute']
>>> class UpperString(object):
...     def __init__(self):
...         self._value = ''
...     def __get__(self, instance, klass):
...         return self._value 
...     def __set__(self, instance, value):
...         self._value = value.upper()
... 
>>> class MyClass(object):
...    attribute = UpperString()
... 
>>> instance_of = MyClass()
>>> instance_of.attribute
''
>>> instance_of.attribute = 'my value'
>>> instance_of.attribute
'MY VALUE'
>>> instance.__dict__ = {}
>>> instance_of.new_att 
= 1
>>> instance_of.__dict__
{'new_att': 1}
>>> MyClass.new_att = UpperString()
>>> instance_of.__dict__
{'new_att': 1}
>>> instance_of.new_att 
''
>>> instance_of.new_att = 'other value'
>>> instance_of.new_att 
'OTHER VALUE'
>>> instance_of.__dict__
{'new_att': 1}
>>> class Whatever(object):
...     def __get__(self, instance, klass):
...         return 'whatever'
... 
>>> MyClass.whatever = Whatever()
>>> 
{'new_att': 1}
>>> instance_of.whatever
'whatever'
>>> instance_of.whatever = 1
>>> instance_of.__dict__
{'new_att': 1, 'whatever': 1}
# 1- looking for definition
if hasattr(MyClass, 'attribute'):
    attribute = MyClass.attribute
    AttributeClass = attribute.__class__

    # 2 - does attribute definition has a setter ?    
    if hasattr(AttributeClass, '__set__'):
        # let's use it
        AttributeClass.__set__(attribute, instance, 
                               value)
        return
# 3 - regular way
instance.__dict__['attribute'] = value
>>> class API(object):
...     def _print_values(self, obj):
...         def _print_value(key):
...             if key.startswith('_'):
...                 return ''
...             value = getattr(obj, key)
...             if not hasattr(value, 'im_func'):
...                 doc = type(value).__name__
...             else:
...                 if value.__doc__ is None:
...                     doc = 'no docstring'
...                 else:
...                     doc = value.__doc__
...             return '             %s : %s' % (key, doc)
...         res = [_print_value(el) for el in dir(obj)]
...         return '\n'.join([el for el in res 
...                           if el != ''])
...     def __get__(self, instance, klass):
...         if instance is not None:
...             return self._print_values(instance)
...         else:
...             return self._print_values(klass)
... 
>>> class MyClass(object):
...     __doc__ = API()
...     def __init__(self):
...         self.a = 2
...     def meth(self):
...         """my method"""
...         return 1
... 
>>> MyClass.__doc__
'    meth : my method'
>>> instance = MyClass()
>>> print instance.__doc__
    a : int
    meth : my method
>>> class Chainer(object):
...     def __init__(self, methods, callback=None):
...         self._methods = methods
...         self._callback = callback
...     def __get__(self, instance, klass):
...         if instance is None:
...             # only for instances
...             return self
...         results = []
...         for method in self._methods:
...             results.append(method(instance))
...             if self._callback is not None:
...                 if not self._callback(instance,
...                                       method,
...                                       results):
...                     break
...         return results 
>>> class TextProcessor(object):
...     def __init__(self, text):
...         self.text = text
...     def normalize(self):
...         if isinstance(self.text, list):
...             self.text = [t.lower() 
...                          for t in self.text]
...         else:
...             self.text = self.text.lower()
...     def split(self): 
...         if not isinstance(self.text, list):
...             self.text = self.text.split()
...     def treshold(self):
...         if not isinstance(self.text, list):
...             if len(self.text) < 2:
...                 self.text = ''
...         self.text = [w for w in self.text 
...                      if len(w) > 2]
... 
>>> def logger(instance, method, results):
...     print 'calling %s' % method.__name__
...     return True
... 
>>> def add_sequence(name, sequence): 
...     setattr(TextProcessor, name,
...             Chainer([getattr(TextProcessor, n) 
...                      for n in sequence], logger))
... 
>>> add_sequence('simple_clean', ('split', 'treshold'))
>>> my = TextProcessor(' My Taylor is   Rich ')
>>> my.simple_clean
calling split
calling treshold
[None, None]
>>> my.text
['Taylor', 'Rich']

>>> # let's perform another sequence
...
>>> add_sequence('full_work', ('normalize',
...                                        'split', 'treshold'))
>>> my.full_work
calling normalize
calling split
calling treshold
[None, None, None]
>>> my.text
['taylor', 'rich']
>>> class MyClass(object):
...     def __init__(self):
...         self._my_secret_thing = 1
...
...     def _i_get(self):
...         return self._my_secret_thing
...
...     def _i_set(self, value):
...         self._my_secret_thing = value
...
...     def _i_delete(self):
...         print 'neh!'
...
...     my_thing = property(_i_get, _i_set, _i_delete, 
...                                 
'the thing')
... 
>>> instance_of = MyClass()
>>> instance_of.my_thing
1
>>> instance_of.my_thing = 3
>>> instance_of.my_thing
3
>>> del instance_of.my_thing
neh !
>>> help(instance_of)
Help on MyClass in module __main__ object:
class MyClass(__built-in__.object)

| 
Methods defined here:

| 


| 
__init__(self)

| 


| 
----------------------------------------------------

| 
Data descriptors defined here:

| 
...

| 
my_thing

|      the thing
>>> class FirstClass(object):
...     def _get_price(self):
...         return '$ 500'
...     price = property(_get_price)
... 
>>> class SecondClass(FirstClass):
...     def _get_price(self):
...         return '$ 20'
...   
... 
>>> plane_ticket = SecondClass()
>>> plane_ticket.price
'$ 500'
>>> class FirstClass(object):
...     def _get_price(self):
...         return '$ 500'
...     def _get_the_price(self):
...         return self._get_price()
...     price = property(_get_the_price)
... 
>>> class SecondClass(FirstClass):
...     def _get_price(self):
...         return '$ 20'
... 
>>> plane_ticket = SecondClass()
>>> plane_ticket.price
'$ 20'
>>> class FirstClass(object):
...     def _get_price(self):
...         return '$ 500'
...     price = property(_get_price)
... 
>>> class SecondClass(FirstClass):
...     def _cheap_price(self):
...         return '$ 20'
...     price = property(_cheap_price)
... 
>>> plane_ticket = SecondClass()
>>> plane_ticket.price
'$ 20'
>>> class Frozen(object):
...     __slots__ = ['ice', 'cream']
... 
>>> '__dict__' in dir(Frozen)
False
>>> 'ice' in dir(Frozen)
True
>>> glagla = Frozen()
>>> glagla.ice = 1
>>> glagla.cream = 1
>>> glagla.icy = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>


AttributeError: 'Frozen' object has no attribute 'icy'
>>> class MyC<text:span text:style-name="T39">lass(object):</text:span>
...     def __new__(cls):
...         print '__new__ called'
...         return object.__new__(cls) 
# default factory
...     def __init__(self):
...         print '__init__ called'
...         self.a = 1
...     
>>> instance = MyClass()
__new__ called
__init__ called
>>> class MyOtherClassWithoutAConstructor(MyClass):
...     pass
... 
>>> instance = MyOtherClassWithoutAConstructor()
__new__ called
__init__ called
>>> class MyOtherClass(MyClass):
...     def __init__(self):
...         print 'MyOther class __init__ called'
...         super(MyOtherClass, self).__init__()
...         self.b = 2
... 
>>> instance = MyOtherClass()
__new__ called
MyOther class __init__ called
__init__ called
>>> from threading import Thread
>>> class MyThread(Thread):
...     def __init__(self):
...         pass
... 
>>> MyThread()
Traceback (most recent call last):


  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/threading.py", line 416, in __repr__
    assert self.__initialized, "Thread.__init__() was not called"
AssertionError: Thread.__init__() was not called
>>> def method(self):
...     return 1
... 
>>> klass = type('MyClass', (object,), {'method': method})
>>> instance = klass()
>>> instance.method()
1
>>> class MyClass(object):
...     def method(self):
...         return 1
... 
>>> instance = MyClass()
>>> instance.method()
1
>>> def equip(classname, base_types, dict):
...     if '__doc__' not in dict:
...         dict['__doc__'] = API()
...     return type(classname, base_types, dict)
... 
>>> class MyClass(object):
...     __metaclass__ = equip
...     def alright(self):
...         """the ok method"""


...         return 'okay'
... 
>>> ma = MyClass()
>>> ma.__class__
<class '__main__.MyClass'>
>>> ma.__class__.__dict__['__doc__']   # __doc__ is replaced !
<__main__.API object at 0x621d0>
>>> ma.y = 6
>>> print ma.__doc__
    alright : the ok method
    y : int
>>> def enhancer_1(klass):
...     c = [l for l in klass.__name__ if l.isupper()] 

...     klass.contracted_name = ''.join(c) 
... 
>>> def enhancer_2(klass):
...     def logger(function):
...         def wrap(*args, **kw):
...             print 'I log everything !'
...             return function(*args, **kw)
...         return wrap
...     for el in dir(klass):
...         if el.startswith('_'):
...             continue
...         value = getattr(klass, el)
...         if not hasattr(value, 'im_func'):
...             continue
...         setattr(klass, el, logger(value))
... 
>>> def enhance(klass, *enhancers):
...     for enhancer in enhancers:
...         enhancer(klass)
... 
>>> class MySimpleClass(object):
...     def ok(self):
...         """I return ok"""
...         return 'I lied'
... 
>>> enhance(MySimpleClass, enhancer_1, enhancer_2)
>>> thats = MySimpleClass()
>>> thats.ok()
I log everything !
'I lied'
>>> thats.score
>>> thats.contracted_name
'MSC'
>>> if 'd' not in my_list:
...     my_list.append('d')
... 
>>> from doctest import IGNORE_EXCEPTION_DETAIL
>>> from doctest import REPORT_ONLY_FIRST_FAILURE
>>> import os
>>> try:
...     os._exit(0)
... except os.EX_SOFTWARE:
...     print 'internal softwar error'
...     raise
... 
>>> import doctest
>>> TEST_OPTIONS = (doctest.ELLIPSIS |
...                 doctest.NORMALIZE_WHITESPACE | 
...                 doctest.REPORT_ONLY_FIRST_FAILURE)
# config.py
SQL_USER = 'me'
SQL_USER = 'tarek'
SQL_PASSWORD = 'secret'
SQL_URI = 'postgres://%s:%s@localhost/db' % \
              (SQL_USER, SQL_PASSWORD)
MAX_THREADS = 4
>>> OPTIONS = {}
>>> def register_option(name):
...     return OPTIONS.setdefault(name, 1 << len(OPTIONS))
... 
>>> def has_option(options, name):
...     return bool(options & name)
... 
>>> # now defining options
... 
>>> BLUE = register_option('BLUE')
>>> RED = register_option('RED')
>>> WHITE = register_option('WHITE')
>>> 
>>> # let's try them
... 
>>> SET = BLUE | RED
>>> has_option(SET, BLUE)
True
>>> has_option(SET, WHITE)
False
>>> _observers = []
>>> def add_observer(observer):
...     _observers.append(observer)
... 
>>> def get_observers():
...     """Makes sure _observers cannot be modified."""
...     return tuple(_observers)
...
>>> class Citizen(object):
...     def __init__(self):
...         self._message = 'Go boys'
...     def _get_message(self):
...         return self._message
...     kane = property(_get_message)
... 
>>> Citizen().kane
'Go boys'
>>> class MeanElephant(object):
...     def __init__(self):
...         self._people_to_kill = []
...     def is_slapped_on_the_butt_by(self, name):
...         self._people_to_kill.append(name)
...         print 'Ouch!'
...     def revenge(self):
...         print '10 years later...'
...         for person in self._people_to_kill:
...             print 'Me kill %s' % person 

... 
>>> joe = MeanElephant()
>>> joe.is_slapped_on_the_butt_by('Tarek')
Ouch!


>>> joe.is_slapped_on_the_butt_by('Bill')
Ouch!
>>> joe.revenge()
10 years later...
Me kill Tarek
Me kill Bill
>>> class Base(object):
...     def __secret(self):
...         print "don't tell"
...     def public(self):
...         self.__secret()
... 
>>> Base.__secret
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Base' has no attribute '__secret'
>>> dir(Base)
['_Base__secret', ..., 'public']
>>> class Derived(Base):
...     def __secret(self):
...         print "never ever"
... 
>>> Derived().public()
don’t tell
>>> class Base(object):
...     def _Base_secret(self):     # don’t do this !!!
...         print "you told it ?"
... 
>>> class weirdint(int):
...     def __add__(self, other):
...         return int.__add__(self, other) + 1
...     def __repr__(self):
...         return '<weirdo %d>' % self
...     
...     #
...     # public API
...     #
...     def do_this(self):
...         print 'this'
...     def do_that(self):
...         print 'that'
>>> class BadHabits(object):
...     def __my_method__(self):
...         print 'ok'
... 
>>> class Connection(object):
...     _connected = []


...     def connect(self, user):
...         self._connected.append(user)
...     def _connected_people(self):
...         return '\n'.join(self._connected)
...     connected_people = property(_connected_people)
... 
>>> my = Connection()
>>> my.connect('Tarek')
>>> my.connect('Shannon')
>>> print my.connected_people
Tarek
Shannon
>>> class Database(object):
...     def open(self):
...         pass
... 
>>> class User(object):
...     pass
...     
>>> user = User()
>>> db = Database()
>>> db.open()
>>> class DB(object):
...     is_connected = False
...     has_cache = False
... 


>>> database = DB()
>>> database.has_cache
False
>>> if database.is_connected:
...     print "That's a powerful class"
... else:
...     print "No wonder..."
... 
No wonder...
>>> class DB(object):
...     connected_users = ['Tarek']
...     tables = {'Customer': ['id', 'first_name',
...                            'last_name']}
... 
>>> def bad_citizen():
...     os = 1
...     import pdb; pdb.set_trace()
...     return os
... 
>>> bad_citizen()
> <stdin>(4)bad_citizen()
(Pdb) os
1


(Pdb) import os
(Pdb) c
<module 'os' from '/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/os.pyc'>
<text:span text:style-name="Code_20_In_20_Text_20__5b_PACKT_5d_"><text:span text:style-name="T6">>>> def factory(klass, *args, **kw):</text:span></text:span>
...     return klass(*args, **kw)
... 
>>> def fuzzy_thing(**kw):
...     if 'do_this' in kw:
...         print 'ok i did'
...     if 'do_that' in kw:
...         print 'that is done'
...     print 'errr... ok'
... 
>>> fuzzy_thing()
errr... ok
>>> fuzzy_thing(do_this=1)
ok i did
errr... ok
>>> fuzzy_thing(do_that=1)
that is done
errr... ok


>>> fuzzy_thing(hahahahaha=1)
errr... ok
>>> def sum(*args):       # okay
...     total = 0
...     for arg in args:
...         total += arg
...     return total
... 
>>> def sum(sequence):    # better !
...     total = 0
...     for arg in sequence:
...         total += arg
...     return total
...
>>> def make_sentence(**kw):
...     noun = kw.get('noun', 'Bill')
...     verb = kw.get('verb', 'is')
...     adj = kw.get('adjective', 'happy')
...     return '%s %s %s' % (noun, verb, adj)
... 
>>> def make_sentence(noun='Bill', verb='is', adjective='happy'):
...     return '%s %s %s' % (noun, verb, adjective)
... 
>>> def log_request(request):     # version 1
...     print request.get('HTTP_REFERER', 'No referer')
... 
>>> def log_request(request):     # version 2
...     print request.get('HTTP_REFERER', 'No referer<text:span text:style-name="T6">'</text:span>)
...     print request.get('HTTP_HOST', 'No host')
... 
>><text:span text:style-name="Code_20_In_20_Text_20__5b_PACKT_5d_">> import logging</text:span>
<text:span text:style-name="Code_20_In_20_Text_20__5b_PACKT_5d_">>>> def log(**context):</text:span>
<text:span text:style-name="Code_20_In_20_Text_20__5b_PACKT_5d_">...     logging.info('Context is:\n%s\n' % str(context))</text:span>
<text:span text:style-name="Code_20_In_20_Text_20__5b_PACKT_5d_">... </text:span>
>>> SMTP.smtp_send() 
# redundant information in the namespace
>>> SMTP.send()       # more readable and mnemonic       
<text:span text:style-name="T6">>>> </text:span>import smtp<text:span text:style-name="T38">lib</text:span>
<text:span text:style-name="T6">>>> </text:span>import url<text:span text:style-name="T38">lib</text:span>
>>> import telnet<text:span text:style-name="T38">lib</text:span>
>>> from widgets.stringwidgets import TextWidget    # bad
>>> from widgets.strings import TextWidget   # better
from module1 import feature1, feature2
from module2 import feature3
>>> from foo import feature1
>>> from foo import feature2, feature3
>>> from script_engine import make_context
<text:span text:style-name="T6">>>> </text:span>from script_engine import compile
<text:span text:style-name="T6">>>> </text:span>from script_engine import execute
<text:span text:style-name="T6">>>> </text:span>context = make_context({'a': 1, 'b':3})
<text:span text:style-name="T6">>>> </text:span>byte_code = compile('a + b')
<text:span text:style-name="T6">>>> </text:span>print execute(byte_code)
4
>>> from script_engine import run
>>> print run('a + b', context={'a': 1, 'b':3}) 
4
>>> from acme.templates import Template


>>> from acme.sqlengine import SQLEngine
>>> from acme.pdfgen import PDFGen
>>> SQL_URI = 'sqlite:///:memory:'
>>> def generate_pdf(query, template_name):
...     data = SQLEngine(SQL_URI).execute(query)
...     template = Template(template_name)
...     return PDFGen().create(data, template)     
>>> from acme import templates
>>> from acme.sqlengine import SQLEngine
>>> from acme.pdf import generate
>>> SQL_URI = 'sqlite:///:memory:'
>>> def generate_pdf(query, template_name):
...     data = SQLEngine(SQL_URI).execute(query)
...     template = templates.generate(template_name)
...     return generate(data, template)     
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
>>> class SomeClass(object):            # version 1
...     def run_script(self, script, context):
...         print 'doing the work'
... 
>>> import warnings
>>> class SomeClass(object):            # version 1.5
...     def run_script(self, script, context):
...         warnings.warn(("'run_script' will be replaced "
...                        "by 'run' in version 2"), 
...                       DeprecationWarning)
...         return self.run(script, context)
...     def run(self, script, context=None):
...         print 'doing the work'
... 
>>> SomeClass().run_script('a script', {})
__main__:4: DeprecationWarning: 'run_script' will be replaced by 'run' in version 2
doing the work
>>> SomeClass().run_script('a script', {})
doing the work
>>> class SomeClass(object):            # version 2
...     def run(self, script, context=None):
...         print 'doing the work'
...
from setuptools import setup
setup(name='acme.sql')
from setuptools import setup
setup(name='acme.sql', version='0.1.1')
include HISTORY.txt
include README.txt
include CHANGES.txt
include CONTRIBUTORS.txt
include LICENSE
recursive-include *.txt *.py
from setuptools import setup
setup(name='acme.sql', version='0.1.1', 
      install_requires=['pysqlite', 'SQLAlchemy'])
[server-index]
username: tarek
password: secret
[distutils]


index-servers =
    pypi
    alternative-server
    alternative-account-on-pypi
[pypi]
username:tarek
password:secret
[alternative-server]
username:tarek
password:secret
repository:http://example.com/pypi
setup(name="my.command",
          entry_points="""
             [distutils.commands]
             my_command 
= my.command.module.Class 
          """)
import os
from setuptools import setup, find_packages
version = '0.1.0'
README = os.path.join(os.path.dirname(__file__), 'README.txt')
long_description = open(README).read() + '\n\n'
setup(name='acme.sql',
      version=version,
      description=("A package that deals with SQL, "
                   "from ACME inc"),
      long_description=long_description,
      classifiers=[
        "Programming Language :: Python",
        ("Topic :: Software Development :: Libraries :: 
         "Python Modules"),
        ],
      keywords='acme sql',
      author='Tarek',


      author_email='tarek@ziade.org',
      url='http://ziade.org',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['acme'],
      install_requires=['pysqlite','SQLAchemy']
      )
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
from setuptools import setup, find_packages
version = '0.1.0'
classifiers = [
    "Programming Language :: Python",
    ("Topic :: Software Development :: "
     "Libraries :: Python Modules")]
setup(name='pbp.skels',
      version=version,
      description=("PasteScript templates for the Python "
                   "Best Practice Book."),
      classifiers=classifiers,
      keywords='paste templates',
      author='Tarek Ziade',
      author_email='tarek@ziade.org',
      url='http://atomisator.ziade.org',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pbp'],
      include_package_data=True,
      install_requires=['setuptools', 
                        'PasteScript'],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      pbp_package = pbp.skels.package:Package
      """)
from paste.script.templates import var


from paste.script.templates import Template
class Package(Template):
    """Package template"""
    _template_dir = 'tmpl/package'
    summary = "A namespaced package with a test environment"
    use_cheetah = True
    vars = [
        var('namespace_package', 'Namespace package',
            default='pbp'),
        var('package', 'The package contained', 

            default='example'),
        var('version', 'Version', default='0.1.0'),
        var('description', 
            'One-line description of the package'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('keywords', 'Space-separated keywords/tags'),
        var('url', 'URL of homepage'),
        var('license_name', 'License name', default='GPL')
        ]
    def check_vars(self, vars, command):
        if not command.options.no_interactive and \
           not hasattr(command, '_deleted_once'):
            del vars['package']
            command._deleted_once = True
        return Template.check_vars(self, vars, command)
from setuptools import setup, find_packages
import os
version = ${repr($version) or "0.0"}
long_description = open("README.txt").read()
classifiers = [
    "Programming Language :: Python",
    ("Topic :: Software Development :: "
     "Libraries :: Python Modules")]
setup(name=${repr($project)},
      version=version,
      description=${repr($description) or $empty},
      long_description=long_description,
      classifiers=classifiers,
      keywords=${repr($keywords) or $empty},
      author=${repr($author) or $empty},
      author_email=${repr($author_email) or $empty},


      url=${repr($url) or $empty},
      license=${repr($license_name) or $empty},
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=[${repr($namespace_package)}],
      include_package_data=True,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
[egg_info]
tag_build = dev
[egg_info]
tag_build = dev
tag_svn_revision = true
...
setup(name='atomisator.parser',
      version=version,
      description=("A thin layer on the top of "
                   "the Universal Feed Parser"),
      long_description=long_description,
      classifiers=classifiers,
      keywords='python best practices',
      author='Tarek Ziade',
      author_email='tarek@ziade.org',
      url='http://atomisator.ziade.org',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['atomisator'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          '<text:span text:style-name="T38">feedparser</text:span>'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
...
=================
atomisator.parser
=================
The parser knows how to return a feed content, with
the `parse` function, available as a top-level function::
    >>> from atomisator.parser import parse
This function takes the feed url and returns an iterator
over its content. A second parameter can specify a maximum
number of entries to return. If not given, it is fixed to 10::



    >>> res = parse('http://example.com/feed.xml')
    >>> res
    <generator ...>
Each item is a dictionary that contain the entry::
    >>> res.next()
...
>>> res = parse(os.path.join(test_dir, '<text:a xlink:type="simple" xlink:href="http://example.com/feed.xml">sample.xml</text:a>'))
...
from feedparser import parse as feedparse
from itertools import islice
from itertools import imap
                                                                           
def _filter_entry(entry):
    """Filters entry fields."""     
    entry['links'] = [link['href'] for link in entry['links']]     
    return entry     
                                                                           
def parse(url, size=10):                                                   
    """Returns entries of the feed."""     
    result = feedparse(url)     
    return islice(imap(_filter_entry, 
                        result['entries']), size)
...
Each item is a dictionnary that contain the entry::
    >>> entry = res.next()
    >>> entry['title']
    u'CSSEdit 2.0 Released'
The keys available are:
    >>> keys = sorted(entry.keys())
    >>> list(keys)
    ['id', 'link', 'links', 'summary', 'summary_detail', 
     'tags', 'title', 'title_detail']
>>> if big_daddy_server:


...     sqluri = 'postgres://tarek@localhost/database' 

... else:
...     sqluri = 'sqlite://relative/path/to/database.db'
from sqlalchemy import *                                                                            
from sqlalchemy.orm import *
from sqlalchemy.orm import mapper
    
metadata = MetaData()       
link = Table('atomisator_link', metadata,
             Column('id', Integer, primary_key=True),              
             Column('url', String(300)),              
             Column('atomisator_entry_id', Integer,              
                    ForeignKey('atomisator_entry.id')))                     
                                                                           
class Link(object):
    def __init__(self, url):     
        self.url = url
    
    def __repr__(self):     
        return "<Link('%s')>" % self.url         


                                                                           
mapper(Link, link)                                                         
                                                                           
tag = Table('atomisator_tag', metadata,                                    
            Column('id', Integer, primary_key=True),             
            Column('value', String(100)),             
            Column('atomisator_entry_id', Integer,             
                   ForeignKey('atomisator_entry.id')))                    
                                                                           
class Tag(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return "<Tag('%s')>" % self.value
mapper(Tag, tag)
entry = Table('atomisator_entry', metadata,
              Column('id', Integer, primary_key=True),
              Column('url', String(300)),
              Column('date', DateTime()),
              Column('summary', Text()),
              Column('summary_detail', Text()),
              Column('title', Text()),
              Column('title_detail', Text()))
class Entry(object):
    def __init__(self, title, url, summary, summary_detail='',
                 title_detail=''):
        self.title = title
        self.url = url
        self.summary = summary
        self.summary_detail = summary_detail
        self.title_detail = title_detail
    def add_links(self, links):
        for link in links:
            self.links.append(Link(link))
    def add_tags(self, tags):
        for tag in tags:
            self.tags.append(Tag(tag))
    def __repr__(self):
        return "<Entry(%r)>" % self.title
mapper(Entry, entry, properties={
       'links':relation(Link, backref='atomisator_entry'),
       'tags':relation(Tag, backref='atomisator_entry'),
       })
=============
atomisator.db
=============                                                               
This package provides a few mappers to store feed entries                  
in a SQL database.                                                         
The SQL uri is provided in the config module::                             
    >>> from atomisator.db import config     
    >>> config.SQLURI = 'sqlite://:memory:'     
Let's create an entry::                                                    
                                                                           
    >>> from atomisator.db import create_entry     
    >>> entry = {'url': 'http://www.python.org/news',     
    ...     'summary': 'Summary goes here',     
    ...     'title': 'Python 2.6alpha1 and 3.0alpha3 released',     
    ...     'links': ['http://www.python.org'],     
    ...     'tags': ['cool', 'fun']}     
    >>> id_ = create_entry(entry)
    >>> type(id_)
    <type 'int'>
We get the database id back. Now let's look for entries::
    >>> from atomisator.db import get_entries
    >>> entries = get_entries() 
# returns a generator object
    >>> entries.next()
    <Entry('Python 2.6alpha1 and 3.0alpha3 released')>
Some filtering can be done ::
    >>> entries = \ 
    ...     get_entries(url='http://www.python.org/news')
    >>> entries.next()
    <Entry('Python 2.6alpha1 and 3.0alpha3 released')>
When no entry is found, the generator is empty::
    >>> entries = get_entries(url='xxxx')
    >>> entries.next()
    Traceback (most recent call last):
    ...
    StopIteration
<?xml version="1.0" encoding="utf-8"?>


<rss version="2.0" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<channel>
<title><![CDATA[${channel.title}]]></title>
<description><![CDATA[${channel.description}]]></description>
<link>${channel.link}</link>
<language>en</language>
<copyright>Copyright 2008, Atomisator</copyright>
<pubDate>${publication_date}</pubDate>
<lastBuildDate>${build_date}</lastBuildDate>
#for $entry in $entries
  <item>
    <title><![CDATA[${entry.title}]]></title>
    <description><![CDATA[${entry.summary}]]></description>
    <link><![CDATA[${entry.url}]]></link>
    <pubDate>${entry.date}</pubDate>
  </item>
#end for
</channel>
</rss>
===============
atomisator.feed
===============
Generates a feed using a template::
    >>> from atomisator.feed import generate
    >>> print generate('feed', 'the feed', 'http://link')
    <?xml version="1.0" encoding="utf-8"?>
    <rss version="2.0" xmlns:rdf="...">
    <channel>
    <title><![CDATA[feed]]></title>
    <description><![CDATA[the feed]]></description>
    <link>http://link</link>
    <language>en</language>
    ...
    <item>
      <title><![CDATA[Python 2.6alpha1 and 
                        3.0alpha3 released]]></title>
      <description><![CDATA[Summary goes here]]></description>
      <link><![CDATA[http://www.python.org/news]]></link>
      <pubDate>...</pubDate>
    </item>
    ...
    </channel>
    </rss>
[atomisator]
# feeds to read 
sites = 
    sample1.xml


    sample2.xml
# database location
database = sqlite:///atomisator.db
# fields used for the channel
title = My Feed
description = The feed
link = the link
# name of the generated file
file = atomisator.xml
from atomisator.main.config import parser
from atomisator.parser import parse 
from atomisator.db import config
from atomisator.db import create_entry
from atomisator.feed import generate
config.SQLURI = parser.database
def _log(msg):
    print msg
def load_feeds():
    """Fetches feeds."""
    for count, feed in enumerate(parser.feeds):
        _log('Parsing feed %s' % feed)
        for entry in parse(feed):
            count += 1
            create_entry(entry) 
    _log('%d entries read.' % count+1)
def generate_feed():
    """Creates the meta-feed."""    
    _log('Writing feed in %s' % parser.file) 
    feed = generate(parser.title, 
                    parser.description, parser.link) 
    f = open(parser.file, 'w')
    try:
        f.write(feed)
    finally:
        f.close()
    _log('Feed ready.')
def atomisator():
    """Calling both."""
    load_feeds()
    generate_feed()
...
entry_points = {
    "console_scripts": [
        "load_feeds = atomisator.main:load_feeds",
        "generate_feed = atomisator.main:generate_feed",
        "atomisator = atomisator.main:atomisator"
    ]
}


...
[buildout]
parts =
    part1
    part2
[part1]
recipe = my.recipe1
[part2]
recipe = my.recipe2
[buildout]
parts = 
develop = 
    /home/tarek/dev/atomisator.feed
find-links = 
    <text:a xlink:type="simple" xlink:href="http://acme.com/packages/index">http://acme.com/packages/index</text:a>
[buildout]
parts = 
develop = 
    /home/tarek/dev/atomisator.feed
[buildout]
parts = 
    test
develop = 
    /home/tarek/dev/atomisator.feed



[test]
recipe = zc.recipe.egg
eggs =
    nose
[buildout]
parts = 
    test
     other
develop = 
    /home/tarek/dev/atomisator.feed
[test]
recipe = zc.recipe.egg
eggs =
    nose
[other]
recipe = zc.recipe.egg
eggs =
    elementtree
    PIL
...
[buildout]
develop = 
    ../packages/atomisator.main
    ../packages/atomisator.db
    ../packages/atomisator.feed
    ../packages/atomisator.parser
parts = 
    test


[test]
recipe = pbp.recipe.noserunner
eggs = 
    atomisator.main
    atomisator.db
    atomisator.feed
    atomisator.parser 
...
[atomisator-configuration]
recipe = atomisator.recipe.installer

sites = 
    sample1.xml
    sample2.xml

database = sqlite:///${buildout:directory}/var/

title = My Feed
description = The feed
link = the link

file = ${buildout:directory}/var/atomisator.xml
...
$ python setup.py sdist
running sdist
...
Writing atomisator.db-0.1.0/setup.cfg
tar -cf dist/atomisator.db-0.1.0.tar atomisator.db-0.1.0
gzip -f9 dist/atomisator.db-0.1.0.tar
removing 'atomisator.db-0.1.0' (and everything under it)
$ ls dist/
atomisator.db-0.1.0.tar.gz
[buildout]
extends = buildout.cfg
develop = 
parts = 


    atomisator
    eggs
download-cache = downloads
[atomisator]
recipe = zc.recipe.eggs
eggs = 
    atomisator.main
    atomisator.db
    atomisator.feed
    atomisator.parser
$ bin/buildout -c release.cfg -v
Installing 'zc.buildout', 'setuptools'.
...
Installing atomisator.
Installing 'atomisator.db', 'atomisator.feed', 'atomisator.parser', 'atomisator.main'.
...
Picked: setuptools = 0.6c8
[collections]
repositories/ = repositories/
[web]
style = gitweb
push_ssl = false
AddHandler cgi-script .cgi
ScriptAliasMatch        ^/hg(.*)        /home/mercurial/atomisator/hgwebdir.cgi$1
<Directory /home/mercurial/atomisator>
  Options ExecCGI FollowSymLinks
  AllowOverride None
  AuthType Basic
  AuthName "Mercurial"
  AuthUserFile /home/mercurial/atomisator/passwords
  <LimitExcept GET>
    Require valid-user
  </LimitExcept>
</Directory>
<VirtualHost *:80>
  ServerName hg-atomisator.ziade.org
  CustomLog /home/mercurial/atomisator/access_log combined
  ErrorLog 
/home/mercurial/atomisator/error.org.log
  AddHandler cgi-script .cgi
  RewriteEngine On
  DocumentRoot /home/mercurial/atomisator
  ScriptAliasMatch ^/(.*) /home/mercurial/atomisator/hgwebdir.cgi/$1
  <Directory /home/mercurial/atomisator>
    Options ExecCGI FollowSymLinks
    AllowOverride None
    AuthType Basic
    AuthName "Mercurial"
    AuthUserFile /home/mercurial/atomisator/passwords
    <LimitExcept GET>
      Require valid-user


    </LimitExcept>
  </Directory>
</VirtualHost>
[ui]
username = Tarek Ziade



[paths]
default 
= http://tarek:secret@atomisator.ziade.org/hg/unstable
unstable = http://tarek:secret@atomisator .ziade.org/hg/unstable
stable = http://tarek:secret@atomisator.ziade.org/hg/stable
[buildout]
parts =
    buildmaster
    linux
    atomisator
[buildmaster]
recipe = collective.buildbot:master<text:span text:style-name="T28"> </text:span>
project-name = Atomisator project buildbot
project-url = http://atomisator.ziade.org
port = 8999
wport = 9000
url = http://atomisator.ziade.org/buildbot
slaves = 
    linux     ty54ddf32
[linux]
recipe = collective.buildbot:slave
host = localhost
port = ${buildmaster:port}
password = ty54ddf32
[atomisator]
recipe = collective.buildbot:project
slave-names = linux
repository=http://hg-atomisator.ziade.org/unstable
vcs = hg
build-sequence = 
    ./build
test-sequence = 
    buildout/bin/nosetests 

email-notification-sender = <text:a xlink:type="simple" xlink:href="mailto:tarek@ziade.org">tarek@ziade.org</text:a>
email-notification-recipient = <text:a xlink:type="simple" xlink:href="mailto:tarek@ziade.org">tarek@ziade.org</text:a>



[poller]
recipe = collective.buildbot:poller
repository=<text:a xlink:type="simple" xlink:href="http://atomisator.ziade.org/hg/instable">http://hg-atomisator.ziade.org/unstable</text:a>
vcs = hg
user=anonymous
#!/bin/sh
cd buildout
python bootstrap.py
bin/buildout -v
[web]
style = gitweb
description = Unstable branch
contact = Tarek <tarek@ziade.org>
push_ssl = false
allow_push = *
[hooks]
changegroup.buildbot = python:buildbot.changes.hgbuildbot.hook
[hgbuildbot]
master = atomisator.ziade.org:8999
<VirtualHost *:80>
  ServerName atomisator-buildbot.ziade.org
  CustomLog /var/log/apache2/bot-access_log combined
  ErrorLog 
/var/log/apache2/bot-error.org.log
  RewriteEngine On
  RewriteRule ^(.*) http://localhost:9000/$1
</VirtualHost>
[buildout]
parts =
    buildmaster
    linux
    trac
[buildmaster]
...
[buildslave]
...


[trac]
recipe = pbp.recipe.trac
project-name = Atomisator
project-url = ${buildmaster:project-url}
repos-type = hg
repos-path = /home/mercurial/atomisator/repositories/unstable
buildbot-url = http://buildbot-atomisator.ziade.org/
components = 
    atomisator.db     tarek
    atomisator.feed     tarek
    atomisator.main     tarek
    atomisator.parser     tarek
    pbp.recipe.trac     tarek
header-logo = atomisator.png
<VirtualHost *:80>
  ServerName atomisator.ziade.org
  <Location />
    SetHandler mod_python
    PythonHandler trac.web.modpython_frontend
    PythonOption TracEnv /home/mercurial/atomisator/buildbot/parts/trac
    PythonOption TracUriRoot /
    PythonPath "sys.path + ['/home/mercurial/atomisator/buildbot/parts/trac', '/home/mercurial/atomisator/buildbot/eggs']"
  </Location>
  <Location "/login">
    AuthType Basic
    AuthName "Trac login"
    AuthUserFile /home/mercurial/atomisator/passwords
    Require valid-user
  </Location>
</VirtualHost>
We have a parse function::
The parser knows how to return a feed content, with
the `parse` function, available as a top-level function::
=====
Title
=====


Section 1
=========
This *word* has emphasis.
Section 2
=========
Subsection
::::::::::
Text. 
$ more text.txt 
Title
=====
content.
$ rst2html.py text.txt > text.html
$ more text.html
<?xml version="1.0" encoding="utf-8" ?>
...
<html ...>
<head>
...
</head>
<body>
<div class="document" id="title">
<h1 class="title">Title</h1>
<p>content.</p>
</div>
</body>
</html>
=====


Title
=====
Section 1
=========
xxx
Subsection A
------------
xxx
Subsection B
------------
xxx
Section 2
=========
xxx
Subsection C
------------
xxx
Bullet list:
- one
- two
- three
Enumerated list:
1. one
2. two
#. auto-enumerated
Definition list:
one
    one is a number.
two
    two is also a number.
This is a code example
::
    >>> 1 + 1
    2
Let's continue our text
This is a code example::
    >>> 1 + 1
    2



Try `Plone CMS`_, it is great ! It is based on Zope_.
.. _`Plone CMS`: http://plone.org
.. _Zope: <text:a xlink:type="simple" xlink:href="http://zope.org/">http://zope.org</text:a>
=====
Title
=====
Section 1
=========
xxx
Subsection A
------------
xxx
Subsection B
------------
-> go back to `Subsection A`_
Section 2
=========
xxx
=========================================
Database specifications for atomisator.db 
=========================================
:Author: Tarek
:Tags: database mapping sql
:abstract:
    Write here a small abstract about your design document. 
.. contents ::
Who should read this ?
::::::::::::::::::::::
Explain here who is the target readership.
Content
:::::::
Write your document here. Do not hesitate to split it in several sections.
References
::::::::::
Put here references, and links to other documents.
========================
How to use atomisator.db 
========================
:Author: Tarek
:Tags: atomisator db
.. contents ::
Who should read this ?
::::::::::::::::::::::
Explain here who is the target readership.
Prerequisites
:::::::::::::



Put here the prerequisites for people to follow this recipe.
Problem
:::::::
Explain here the problem resolved in a few sentences.
Solution
::::::::
Put here the solution.
References
::::::::::
Put here references, and links to other recipes.
==========
Operations
==========
This section contains operations documents :
========
Cookbook
========
Welcome to the CookBook.
Available recipes:
.. toctree::
  :glob:
  *
=======
session
=======
.. module:: db.session


The module session...
=======
session
=======
.. module:: db.session
.. index::
    Database Access
    Session
The module session...
:mod:`db.session`
>>> import unittest
>>> class MyTests(unittest.TestCase):
...     def test_average(self):
...         self.assertEquals(average(1, 2, 3), 2)
...         self.assertEquals(average(1, -3), -1)
...         self.assertEquals(average(0, 1), 0.5)
...         self.assertRaises(TypeError, average)
... 
>>> unittest.main()
.
--------------------------------------------------------
Ran 1 test in 0.000s

OK
import unittest
from utils import average

class UtilsTests(unittest.TestCase):
    def test_average(self):
        self.assertEquals(average(1, 2, 3), 2)
        self.assertEquals(average(1, -3), -1)
        self.assertEquals(average(0, 1), 0.5)
        self.assertRaises(TypeError, average)

if __name__ == '__main__':
    unittest.main()
import unittest
from utils import average

class MyTests(unittest.TestCase):
    def test_average(self):
        self.assertEquals(average(1, 2, 3), 2)
        self.assertEquals(average(1, -3), -1)
        self.assertEquals(average(0, 1), 0.5)
        self.assertRaises(TypeError, average)

class MyTests2(unittest.TestCase):

    def test_another_test(self):
        pass

def test_suite():
    """builds the test suite."""
    def _suite(test_class):
        return unittest.makeSuite(test_class)
    suite = unittest.TestSuite()
    suite.addTests((_suite(MyTests), _suite(MyTests2)))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite') 
Check that the computer CPU is not getting too hot::

    >>> 1 + 1
    2

>>> import doctest
>>> doctest.testfile('test.txt', verbose=True)
Trying:
    1 + 1
Expecting:
    2
ok
1 items passed all tests:
   1 tests in test.txt
1 tests in 1 items.
1 passed and 0 failed.
Test passed.
*** DocTestRunner.merge: 'test.txt' in both testers; summing outcomes.
(0, 1)
$ easy_install nose
Searching for nose
Reading http://pypi.python.org/simple/nose/
Reading http://somethingaboutorange.com/mrl/projects/nose/
...
Processing dependencies for nose
Finished processing dependencies for nose
$ nosetests -v
test_average (test_utils.MyTests) ... ok
test_another_test (test_utils.MyTests2) ... ok
builds the test suite. ... ok
--------------------------------------------------------------
Ran 3 tests in 0.010s
OK
def setup():
    # setup code, launched for the whole module
    ...
def teardown():
    # tear down code, launched for the whole module
    ... 
def set_ok():
    # setup code launched only for test_ok
    ...
@with_setup(set_ok)
def test_ok():
    print 'my test'
setup(
    ...
    test_suite = 'nose.collector' 
    ...)


$ easy_install py
Searching for py
Best match: py 0.9.0
Finished processing dependencies for py
def setup_module(module):    
    """ setup up any state specific to the execution     
        of the given module.         
    """
def teardown_module(module):    
    """ teardown any state that was previously setup     
        with a setup_module method.         
    """
def setup_class(cls):    
    """ setup up any state specific to the execution     
        of the given class (which usually contains tests).         
    """ 
def teardown_class(cls):    
    """ teardown any state that was previously setup 
        with a call to setup_class.         
    """ 
def setup_method(self, method):    
    """ setup up any state tied to the execution of the given     
        method in a class. setup_method is invoked for every         
        test method of a class.         
    """ 
def teardown_method(self, method):    
    """ teardown any state that was previously setup     
        with a setup_method call.         
    """
class TestEgSomePosixStuff:    
    disabled = sys.platform == 'win32'     
    def test_xxx(self):     
        ...
def _disabled():
    # complex work here
    return 0
class Test_2:
         
    disabled = _disabled()
         
    def test_one(self):
        pass
import smtplib
import email.Message
def send(sender, to, subject='None', body='None',
         server='localhost'):
    """sends a message."""
    message = email.Message.Message()
    message['To'] = to
    message['From'] = sender
    message['Subject'] = subject
    message.set_payload(body)
    server = smtplib.SMTP(server)
    try:
        res = server.sendmail(sender, to, message.as_string())
    finally:
        server.quit()
    return res
from mailer import send
from nose.tools import *
def test_send():
    
    res = send('tarek@ziade.org', 'tarek@ziade.org', 
               'topic', 'body')
    assert_equals(res, {})
from mailer import send
from nose.tools import *
import smtplib
def patch_smtp():
    class FakeSMTP(object):
        pass
    smtplib._SMTP = smtplib.SMTP
    smtplib.SMTP = FakeSMTP
def unpatch_smtp():
    smtplib.SMTP = smtplib._SMTP
    delattr(smtplib, '_SMTP')
@with_setup(patch_smtp, unpatch_smtp)
def test_send():
    res = send('tarek@ziade.org', 'tarek@ziade.org', 
               'topic', 'body')
    assert_equals(res, {})


class FakeSMTP(object):
    def __init__(self, *args, **kw):
        # we don't care
        pass
    def quit(self):
        pass
    def sendmail(self, *args, **kw):
        return {}
from mailer import send
from nose.tools import *
import smtplib
from minimock import mock, restore, Mock

def patch_smtp():
    mock('smtplib.SMTP', 
         returns=Mock('smtp_connection', 
                      sendmail=Mock('sendmail',
                                    returns={})
                     )
         )

def unpatch_smtp():
    restore()


<text:span text:style-name="Normal_20__5b_PACKT_5d__20_Char"/>
@with_setup(patch_smtp, unpatch_smtp)
def test_send():
    res = send('tarek@ziade.org', 
               'tarek@ziade.org', 'topic', 'body')
    assert_equals(res, {})
=================
atomisator.parser
=================
The parser knows how to return a feed content with
a function available as a top-level function.



This function takes the feed url and returns an iterator
on its content. A second parameter can specify how
much entries has to be returned before the iterator is
exhausted. If not given, it is fixed to 10
=================
atomisator.parser
=================
The parser knows how to return a feed content, with
the `parse` function, available as a top-level function::
    >>> from atomisator.parser import parse
This function takes the feed url and returns an iterator
on its content. A second parameter can specify how
much entries has to be returned before the iterator is
exhausted. If not given, it is fixed to 10::
    >>> res = parse('http://example.com/feed.xml')
    >>> res
    <generator ...>
>>> def test_speed():
...     import time
...     start = time.time()
...     the_code()
...     end = time.time() - start
...     assert end < 10, \
...         
"sorry this code should not take 10 seconds !"
... 
import time

def lighter():
    time.sleep(0.01)

def light():
    time.sleep(0.001)

def heavy():
    for i in range(100):
        light()
        lighter()
        lighter()
    time.sleep(2)

def main():
    for i in range(2):
        heavy()

if __name__ == '__main__':
    main()
>>> from myapp import main
>>> import cProfile
>>> profiler = cProfile.Profile()
>>> profiler.runcall(main)
>>> profiler.print_stats()
         1209 function calls in 10.140 CPU seconds

   Ordered by: standard name

   ncalls 
tottime 
cumtime 
percall file
        1         0.000         10.140         10.140 myapp.py:16(main)
      400       0.005       4.093       0.010 myapp.py:3(lighter)
      200       0.002       2.042       0.010 myapp.py:6(light)
        2         0.005         10.140         5.070 myapp.py:9(heavy)
        3         0.000         0.000         0.000 {range}
      602       10.128       10.128       0.017 {time.sleep}
>>> cProfile.run('main()', 'myapp.stats')
>>> import pstats
>>> p = pstats.Stats('myapp.stats')
>>> p.total_calls
1210
>>> p.sort_stats('time').print_stats(3)
Thu Jun 19 23:56:08 2008    myapp.stats
         1210 function calls in 10.240 CPU seconds
   Ordered by: internal time
   List reduced from 8 to 3 due to restriction <3>
   ncalls 
tottime 
cumtime 
percall filename:lineno(function)
      602       10.231       10.231       0.017 {time.sleep}
        2         0.004         10.240         5.120 myapp.py:9(heavy)
      400       0.004       4.159       0.010 myapp.py:3(lighter)
>>> p.print_callees('lighter')
   Ordered by: internal time
   List reduced from 8 to 1 due to restriction <'lighter'>
Function             called...
                         ncalls 
tottime 
cumtime
myapp.py:3(lighter) 
->     400     4.155     4.155 
{time.sleep}
>>> p.print_callers('light')          
   Ordered by: internal time
   List reduced from 8 to 2 due to restriction <'light'>
Function             was called by...
                         ncalls 
tottime 
cumtime
myapp.py:3(lighter) 
<-     400     0.004     4.159 
myapp.py:9(heavy)


myapp.py:6(light)    <-    200    0.002    2.073 
myapp.py:9(heavy)
>>> import tempfile, os, cProfile, pstats
>>> def profile(column='time', list=5):
...     def _profile(function):
...         def __profile(*args, **kw):
...             s = tempfile.mktemp()
...             profiler = cProfile.Profile()
...             profiler.runcall(function, *args, **kw)
...             profiler.dump_stats(s)
...             p = pstats.Stats(s)
...             p.sort_stats(column).print_stats(list)
...         return __profile
...     return _profile
... 
>>> from myapp import main
>>> @profile('time', 6)
... def main_profiled():
...     return main()
... 
>>> main_profiled()
Fri Jun 20 00:30:36 2008   ...
         1210 function calls in 10.129 CPU seconds
   Ordered by: internal time
   List reduced from 8 to 6 due to restriction <6>
   ncalls 
tottime 
cumtime 
percall filename:lineno(function)
      602       10.118       10.118       0.017 {time.sleep}
        2         0.005         10.129         5.065 myapp.py:9(heavy)
      400       0.004       4.080       0.010 myapp.py:3(lighter)
      200       0.002       2.044       0.010 myapp.py:6(light)
        1         0.000         10.129         10.129 myapp.py:16(main)
        3         0.000         0.000         0.000 {range}
>>> from myapp import lighter
>>> p = profile()(lighter)
>>> p()
Fri Jun 20 00:32:40 2008    /var/folders/31/31iTrMYWHny8cxfjH5VuTk+++TI/-Tmp-/tmpQjstAG
         3 function calls in 0.010 CPU seconds
   Ordered by: internal time
   ncalls 
tottime 
cumtime 
percall filename:lineno(function)
        1         0.010         0.010         0.010 {time.sleep}
        1         0.000         0.010         0.010 myapp.py:3(lighter)
>>> from myapp import light
>>> import timeit
>>> t = timeit.Timer('main()')


>>> t.timeit(number=5)
10000000 loops, best of 3: 0.0269 usec per loop
10000000 loops, best of 3: 0.0268 usec per loop
10000000 loops, best of 3: 0.0269 usec per loop
10000000 loops, best of 3: 0.0268 usec per loop
10000000 loops, best of 3: 0.0269 usec per loop
5.6196951866149902
>>> import time
>>> import sys
>>> if sys.platform == 'win32':    # same condition in timeit
...     timer = time.clock
... else:
...     timer = time.time
>>> stats = {}
>>> def duration(name='stats', stats=stats):
...     def _duration(function):
...         def __duration(*args, **kw):
...             start_time = timer()             
...             try:
...                 return function(*args, **kw)
...             finally:
...                 stats[name] = timer() - start_time 
...         return __duration
...     return _duration
... 
>>> from myapp import heavy
>>> heavy = duration('this_func_is')(heavy)
>>> heavy()
>>> print stats['this_func_is']
1.50201916695
>>> stats = {}
>>> from myapp import light
>>> import myapp
>>> myapp.light = duration('myapp.light')(myapp.light)
>>> myapp.main()
>>> stats
{'myapp.light': 0.05014801025390625}
>>> from test import pystone
>>> pystone.pystones()
(1.0500000000000007, 47619.047619047589)
>>> from test import pystone
>>> benchtime, pystones = pystone.pystones()
>>> def seconds_to_kpystones(seconds):
...     if seconds == 0:
...         return 0
...     return (pystones*seconds) / 1000 
... 
>>> seconds_to_kpystones(0.03)
1.4563106796116512
>>> seconds_to_kpystones(1)
48.543689320388381
>>> seconds_to_kpystones(2)
97.087378640776762
>>> def duration(name='stats', stats=stats):
...     def _duration(function):
...         def __duration(*args, **kw):
...             start_time = timer()             
...             try:
...                 return function(*args, **kw)
...             finally:
...                 total = timer() - start_time
...                 kstones = <text:span text:style-name="T36">seconds_to_kpystones</text:span>(total)
...                 stats[name] = total, kstones 
...         return __duration
...     return _duration
>>> @duration()
... def some_code():
...     time.sleep(0.5)
... 
>>> some_code()
>>> stats
{'stats': (0.50012803077697754, 24.278059746455238)}
>>> def my_function(argument={}):    # bad practice
...     if '1' in argument:
...         argument['1'] = 2
...     argument['3'] = 4
...     return argument
... 
>>> my_function()
{'3': 4}
>>> res = my_function()
>>> res['4'] = 'I am still alive!'
>>> print my_function()
{'3': 4, '4': 'I am still alive!'}
>>> def my_function(argument=None):    # better practice
...     if argument is None:
...         argument = {} 
# a fresh dict is created everytime
...     if '1' in argument:
...         argument['1'] = 2
...     argument['3'] = 4
...     return argument
... 


>>> my_function()
{'3': 4}
>>> res = my_function()
>>> res['4'] = 'I am still alive!'
>>> print my_function()
{'3': 4}
>>> from guppy import hpy
>>> profiler = hpy()
>>> profiler.heap()
Partition of a set of 22723 objects. Total size = 1660748 bytes.

Index 
Count   %   Size   % Cumulative 
% Kind (class / dict of class)
     0      9948 
44      775680 
47      775680 
47 str
     1      5162 
23      214260 
13      989940 
60 tuple
     2      1404      6      95472      6      1085412 
65 types.CodeType
     3      61      0      91484      6      1176896 
71 dict of module
     4      152      1      84064      5      1260960 
76 dict of type
     5      1333      6      79980      5      1340940 
81 function


     6      168      1      72620      4      1413560 
85 type
     7      119      1      68884      4      1482444 
89 dict of class
     8      76      0      51728      3      1534172 
92 dict (no owner)
     9      959      4      38360      2      1572532 
95 __builtin__.wrapper_descriptor
<43 more rows. Type e.g. '_.more' to view.>
>>> import random
>>> def eat_memory():
...     memory = []
...     def _get_char():
...         return chr(random.randint(97, 122))
...     for i in range(100):
...         size = random.randint(20, 150)
...         data = [_get_char() for i in xrange(size)]
...         memory.append(''.join(data))
...     return '\n'.join(memory)
... 
>>> profiler.iso(eat_memory())
Partition of a set of 1 object. Total size = 8840 bytes.

Index 
Count   %   Size   % Cumulative 
% Kind 
     0      1 100      8840 100      8840 100 str
>>> profiler.iso(eat_memory()+eat_memory())
Partition of a set of 1 object. Total size = 17564 bytes.

Index 
Count   %   Size   % Cumulative 
% Kind 
     0      1 100      17564 100      17564 100 str
>>> g = hpy()
>>> g.setrelheap()
>>> g.heap().size
1120
>>> g.heap().size
1200
>>> g.heap().size
1144
import time
import sys
from test import pystone
from guppy import hpy
benchtime, stones = pystone.pystones()
def secs_to_kstones(seconds):
    return (stones*seconds) / 1000 
stats = {}
if sys.platform == 'win32':
    timer = time.clock
else:
    timer = time.time
def profile(name='stats', stats=stats):
    """Calculates a duration and a memory size."""
    def _profile(function):
        def __profile(*args, **kw):
            start_time = timer()
            profiler = hpy()
            profiler.setref()
        
            # 12 corresponds to the initial memory size
            # after a setref call
            start = profiler.heap().size + 12
            try:
                return function(*args, **kw)
            finally:
                total = timer() - start_time
                     
kstones = secs_to_kstones(total)
                memory = profiler.heap().size - start
                stats[name] = {'time': total, 
                               'stones': kstones, 

                               'memory': profiler.heap().size}
        return __profile
    return _profile
>>> import profiler
>>> import random
>>> eat_it = profiler.profile('you bad boy!')(eat_memory)
>>> please = eat_it()
>>> profiler.stats
{'you bad boy!': {'stones': 14.306935999128555, 'memory': 8680, 'time': 0.30902981758117676}}
>>> REPEAT = 100
>>> def memory_grow(function, *args, **kw):
...     """checks if a function makes the memory grows"""
...     profiler = hpy()
...     profiler.setref() 
...     # 12 corresponds to the initial memory size
...     # after a setref call
...     start = profiler.heap().size + 12
...     for i in range(REPEAT):
...         function(*args, **kw)
...     return profiler.heap().size - start
...
>>> def stable():
...     return "some"*10000
... 
>>> d = []
>>> def greedy():
...     for i in range(100):
...         d.append('ouhuvugcgc'*i)
... 
>>> memory_grow(stable)
24
>>> memory_grow(greedy)
5196468
def optimize():
    """Recommended optimization"""
    assert got_architecture_right(), "fix architecture"
    assert made_code_work(bugs=None), "fix bugs"
    while code_is_too_slow():
        wbn = find_worst_bottleneck(just_guess=False,
                                    profile=True)
        is_faster = try_to_optimize(wbn,
                                    run_unit_tests=True,
                                    new_bugs=None)
        if not is_faster:
            undo_last_code_change()
>>> def function(n):
...     for i in range(n):
...         print i
...
>>> def function(n):
...     if some_test:
...         print 'something'
...     else:
...         for i in range(n):
...             print i
... 
>>> def function(n):
...     for i in range(n):
...         for j in range(n):
...             print i, j
...
>>> def function(n):
...     for i in range(n):
...         print i
... 
>>> def other_function(n):
...     if some_test:
...         for i in range(n):
...             function(n)
...     else:
...         function(n)
... 
>>> def function(n):
...     for i in range(n*2):
...         print i
...
>>> def find(seq, el):
...     pos = 
bisect(seq, el)
...     if pos==0 or (pos==len(seq) and seq[-1]!=el):
...         return -1
...     return pos - 1
... 
>>> seq = [2, 3, 7, 8, 9]
>>> find(seq, 9)
4
>>> find(seq, 10)
-1
>>> find(seq, 0)
-1
>>> find(seq, 7)
2
>>> seq = ['a', 'a', 'b', 'c', 'c', 'd']
>>> res = []
>>> for el in seq:
...     if el not in res:
...         res.append(el)
... 
>>> res
['a', 'b', 'c', 'd']
>>> seq = ['a', 'a', 'b', 'c', 'c', 'd']
>>> res = set(seq)
>>> res
set(['a', 'c', 'b', 'd'])
>>> from pbp.scripts.profiler import profile, stats
>>> from collections import deque
>>> my_list = range(100000)
>>> my_deque = deque(range(100000))
>>> @profile('by_list')
... def by_list():
...     my_list[500:502] = []
... 


>>> @profile('by_deque')
... def by_deque():
...     my_deque.rotate(500)
...     my_deque.pop()
...     my_deque.pop()
...     my_deque.rotate(-500)
...     
... 
>>> by_list();by_deque()
>>> print stats['by_list']
{'stones': 47.836141152815379, 'memory': 396, 

'time': 1.0523951053619385}
>>> print stats['by_deque']
{'stones': 19.198688593777742, 'memory': 552, 

'time': 0.42237114906311035}
>>> from collections import deque
>>> from pbp.scripts.profiler import profile, stats
>>> import sys
>>> queue = deque()
>>> def d_add_data(data):
...     queue.appendleft(data)
... 
>>> def d_process_data():
...     queue.pop()
... 
>>> BIG_N = 1000000
>>> @profile('deque')
... def sequence():
...     for i in range(BIG_N):
...         d_add_data(i)
...     for i in range(BIG_N/2):
...         d_process_data()
...     for i in range(BIG_N):
...         d_add_data(i)
... 
>>> lqueue = []
>>> def l_add_data(data):
...     lqueue.append(data)
... 
>>> def l_process_data():
...     lqueue.pop(-1)
... 
>>> @profile('list')
... def lsequence():
...     for i in range(BIG_N):
...         l_add_data(i)
...     for i in range(BIG_N/2):
...         l_process_data()
...     for i in range(BIG_N):
...         l_add_data(i)
... 
>>> sequence(); lsequence()
>>> print stats['deque']
{'stones': 86.521963988031672, 'memory': 17998920, 'time': 1.9380919933319092}
>>> print stats['list']
{'stones': 222.34191851956504, 'memory': 17994312, 'time': 4.9804589748382568}
>>> from collections import defaultdict
>>> from pbp.scripts.profiler import profile, stats
>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), 
...      ('blue', 4), ('red', 1)]
>>> @profile('defaultdict')
... def faster():
...     d = defaultdict(list)
...     for k, v in s:
...         d[k].append(v)
...   
... 
>>> @profile('dict')
... def slower():
...     d = {}
...     for k, v in s:
...         d.setdefault(k, []).append(v)
... 
>>> slower(); faster()
>>> stats['dict']
{'stones': 16.587882671716077, 'memory': 396, 

'time': 0.35166311264038086}
>>> stats['defaultdict']
{'stones': 6.5733464259021686, 'memory': 552, 

'time': 0.13935494422912598}
>>> lg = defaultdict(long)
>>> lg['one']
0L
>>> from collections import namedtuple 
>>> Customer = namedtuple('Customer', 
...                       'firstname lastname
>>> c = Customer(u'Tarek', u'Ziadé')
>>> c.firstname
u'Tarek'
#!/usr/bin/python
for i in range(100000):
     i = str(i) + "y"*10000 
>>> from Queue import Queue


>>> import logging
>>> import time 
>>> import subprocess
>>> q = Queue()
>>> def index_file(filename):
...     logging.info('indexing %s' % filename)
...     f = open(filename)
...     try:
...         content = f.read()
...         # external process is here
...         subprocess.call(['converter.py'])
...         time.sleep(0.5)
...     finally:
...         f.close()
... 
>>> def worker():
...     while True:
...         index_file(q.get())
...         q.task_done()
... 
from threading import Thread
import os
import subprocess
from Queue import Queue
import logging
import time 
import sys
from pbp.scripts.profiler import profile, print_stats
dirname = os.path.realpath(os.path.dirname(__file__))
CONVERTER = os.path.join(dirname, 'converter.py')
q = Queue()
def index_file(filename):
    f = open(filename)
    try:
        content = f.read()
        # process is here
        subprocess.call([CONVERTER])
    finally:
        f.close()
def worker():
    while True:
        index_file(q.get())


        q.task_done()
def index_files(files, num_workers):
    for i in range(num_workers):
        t = Thread(target=worker)
        t.setDaemon(True)
        t.start()
    for file in files:
        q.put(file)
    q.join()
def get_text_files(dirname):
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if os.path.splitext(file)[-1] != '.txt':
                continue
            yield os.path.join(root, file)
@profile('process')
def process(dirname, numthreads):
    dirname = os.path.realpath(dirname)
    if numthreads > 1:
        index_files(get_text_files(dirname), numthreads)
    else:
        for f in get_text_files(dirname):
            index_file(f)             
if __name__ == '__main__':    
    process(sys.argv[1], int(sys.argv[2])) 
    print_stats()
>>> import os
>>> a = []
>>> def some_work():
...     a.append(2)
...     child_pid = os.fork()
...     if child_pid == 0:
...         a.append(3)
...         print "hey, i am the child process"
...         print "my pid is %d" % os.getpid()
...         print str(a)
...     else:
...         a.append(4)
...         print "hey, i am the parent"
...         print "the child is pid %d" % child_pid 
...         print "I am the pid %d " % os.getpid()
...         print str(a)
... 
>>> some_work()
hey, i am the parent
the child is pid 25513
I am the pid 25411 
[2, 4]
hey, i am the child process
my pid is 25513
[2, 3]
>>> from processing import Process
>>> import os
>>> def work():
...     print 'hey i am a process, id: %d' % os.getpid()
... 
>>> ps = []
>>> for i in range(4):
...     p = Process(target=work)
...     ps.append(p)
...     p.start()
... 
hey i am a process, id: 27457
hey i am a process, id: 27458
hey i am a process, id: 27460
hey i am a process, id: 27459
>>> ps
[<Process(Process-1, stopped)>, <Process(Process-2, stopped)>, <Process(Process-3, stopped)>, <Process(Process-4, stopped)>]
>>> for p in ps:
...     p.join()
... 
>>> import processing
>>> import Queue
>>> print 'this machine has %d CPUs' \
...         % processing.cpuCount()
this machine has 2 CPUs
>>> def worker():
...     file = q.get_nowait()
...     return 'worked on ' + file
... 
>>> q = processing.Queue()
>>> pool = processing.Pool()


>>> for i in ('f1', 'f2', 'f3', 'f4', 'f5'):
...     q.put(i)
... 
>>> while True:
...     try:
...         result = pool.apply_async(worker)
...         print result.get(timeout=1)
...     except Queue.Empty:
...         break
... 
worked on f1
worked on f2
worked on f3
worked on f4
worked on f5
>>> import random, timeit
>>> from pbp.scripts.profiler import profile, print_stats
>>> cache = {}
>>> def square(n):
...     return n * n


... 
>>> def cached_factory(n):
...     if n in cache:
...         cache[n] = square(n)
...     return cache[n]
... 
>>> @profile('not cached')
... def factory_calls():
...     for i in xrange(100):
...         square(random.randint(1, 10))
... 
>>> @profile('cached')
... def cached_factory_calls():
...     n = [random.randint(1, 10) for i in range(100)]
...     ns = [cached_factory(i) for i in n]
... 
>>> factory_calls(); cached_factory_calls();
>>> print_stats()
cached : 6.07 kstones, 0.142 secondes, 480 bytes
not cached : 20.51 kstones, 0.340 secondes, 396 bytes
>>> def cache_me(a, b, c, d):
...     # we don't care about d for the key 
...     key = 'cache_me:%s:%s:%s' % (a, b, c)
...     if key not in cache:
...         print 'caching'
...         cache[key] = complex_calculation(a, b, c, d)
...     print d     # d is just use for display
...     return cache[key]
... 
>>> cache = {}
>>> def get_key(function, *args, **kw):
...     key = '%s.%s:' % (function.__module__,
...                       function.__name__)
...     hash_args = [str(arg) for arg in args]
...     # of course, will work only if v is hashable
...     hash_kw = ['%s:%s' % (k, hash(v)) 
...                for k, v in kw.items()]
...     return '%s::%s::%s' % (key, hash_args, hash_kw)     
... 
>>> def memoize(get_key=get_key, cache=cache):
...     def _memoize(function):
...         def __memoize(*args, **kw):
...             key = get_key(function, *args, **kw)
...             try:


...                 return cache[key] 
...             except KeyError:
...                 cache[key] = function(*args, **kw) 
...                 return value
...         return __memoize
...     return _memoize
...             
... 
>>> @memoize()
... def factory(n):
...     return n * n
... 
>>> factory(4)
16
>>> factory(4)
16
>>> factory(3)
9
>>> cache
{"__main__.factory:::['3']::[]": 9,

"__main__.factory:::['4']::[]": 16}
>>> import md5 
>>> def get_key(function_called, n):
...     return md5.md5(str(n)).hexdigest()
... 
>>> @memoize(get_key)
... def cached_factory(n):
...     return n * n
... 
>>> factory_calls(); cached_factory_calls();
>>> print_stats()
cached : 6.96 kstones, 0.143 secondes, 1068 bytes
not cached : 7.61 kstones, 0.157 secondes, 552 bytes
def memoize(get_key=get_key, storage=cache, age=0):


    def _memoize(function):
        def __memoize(*args, **kw):
            key = get_key(function, *args, **kw)
            try:
                value_age, value = storage[key]
                deprecated = (age != 0 and 
                             (value_age+age) < time.time())                              
            except KeyError:
                deprecated = True 
            
            if not deprecated:
                return value
            storage[key] = time.time(), function(*args, **kw)             
            return storage[key][1]
        return __memoize
    return _memoize 
>>> from datetime import datetime
>>> @memoize(age=30)
... def what_time():
...     return datetime.now().strftime('%H:%M')
... 
>>> what_time()
'19:36'
>>> cache
{'__main__.what_time:::[]::[]': (1212168961.613435, '19:36')}
>>> MyType = type('MyType', (object,), {'a': 1})


>>> ob = MyType()
>>> type(ob)
<class '__main__.MyType'>
>>> ob.a
1
>>> isinstance(ob, object)
True
>>> class Singleton(object):
...     def __new__(cls, *args, **kw):
...         if not hasattr(cls, '_instance'):
...              orig = super(Singleton, cls)              

...             cls._instance = orig.__new__(cls, *args, **kw)
...         return cls._instance
... 
>>> class MyClass(Singleton):
...     a = 1
... 
>>> one = MyClass()
>>> two = MyClass()
>>> two.a = 3
>>> one.a
3
>>> class MyOtherClass(MyClass):
...     b = 2
... 
>>> three = MyOtherClass()
>>> three.b
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
AttributeError: 'MyClass' object has no attribute 'b'
>>> class Borg(object):
...     _state = {}
...     def __new__(cls, *args, **kw):
...         ob = super(Borg, cls).__new__(cls, *args, **kw)
...         ob.__dict__ = cls._state
...         return ob
... 
>>> class MyClass(Borg):
...     a = 1
... 
>>> one = MyClass()
>>> two = MyClass()
>>> two.a = 3
>>> one.a
3
>>> class MyOtherClass(MyClass):
...     b = 2
... 
>>> three = MyOtherClass()
>>> three.b
2
>>> three.a
3
>>> three.a = 2
>>> one.a
2
>>> from StringIO import StringIO
>>> my_file = StringIO(u'some content')
>>> my_file.read()
u'some content'
>>> my_file.seek(0)
>>> my_file.read(1)
u's'
>>> from os.path import split, splitext


>>> class DublinCoreAdapter(object):
...     def __init__(self, filename):
...         self._filename = filename
...     def title(self):
...         return splitext(split(self._filename)[-1])[0]
...     def creator(self):
...         return 'Unknown'         # we could get it for real
...     def languages(self):
...         return ('en',)
... 
>>> class DublinCoreInfo(object):
...     def summary(self, dc_ob):
...         print 'Title: %s' % dc_ob.title()
...         print 'Creator: %s' % dc_ob.creator()
...         print 'Languages: %s' % \
...                   ', '.join(dc_ob.languages())
... 
>>> adapted = DublinCoreAdapter('example.txt')
>>> infos = DublinCoreInfo()
>>> infos.summary(adapted)
Title: example
Creator: Unknown
Languages: en
>>> class Url(object):
...     def __init__(self, location):
...         self._url = urlopen(location)
...     def headers(self):
...         return dict(self._url.headers.items())
...     def get(self):
...         return self._url.read()
... 
>>> python_org = Url('http://python.org')
>>> python_org.headers()
{'content-length': '16399', 'accept-ranges': 'bytes', 'server': 'Apache/2.2.3 (Debian) DAV/2 SVN/1.4.2 mod_ssl/2.2.3 OpenSSL/0.9.8c', 'last-modified': 'Mon, 09 Jun 2008 15:36:07 GMT', 'connection': 'close', 'etag': '"6008a-400f-91f207c0"', 'date': 'Tue, 10 Jun 2008 22:17:19 GMT', 'content-type': 'text/html'}
>>> ubuntu_iso = Url('http://ubuntu.mirrors.proxad.net/hardy/ubuntu-8.04-desktop-i386.iso')
>>> ubuntu_iso.headers['last-modified']
'Wed, 23 Apr 2008 01:03:34 GMT'
>>> class Event(object):
...     _observers = []
...     def __init__(self, subject):
...         self.subject = subject
...
...     @classmethod
...     def register(cls, observer):
...         if observer not in cls._observers:
...             cls._observers.append(observer)
...
...     @classmethod
...     def unregister(cls, observer):
...         if observer in cls._observers:
...             self._observers.remove(observer)
...
...     @classmethod
...     def notify(cls, subject):
...         event = cls(subject)
...         for observer in cls._observers:
...             observer(event)
...
>>> class WriteEvent(Event):
...     def __repr__(self):
...         return 'WriteEvent'
... 
>>> def log(event):
...     print '%s was written' % event.subject
... 
>>> WriteEvent.register(log)
>>> class AnotherObserver(object):
...     def __call__(self, event): 
...         print 'Yeah %s told me !' % event
... 
>>> WriteEvent.register(AnotherObserver())
>>> WriteEvent.notify('a given file')
a given file was written
Yeah WriteEvent told me !
>>> class vlist(list):
...     def accept(self, visitor):
...         visitor.visit_list(self)
...   
... 
>>> class vdict(dict):
...     def accept(self, visitor):
...         visitor.visit_dict(self)
... 
>>> class Printer(object):
...     def visit_list(self, ob):
...         print 'list content :'
...         print str(ob)
...     def visit_dict(self, ob):
...         print 'dict keys: %s' % ','.join(ob.keys())
... 
>>> a_list = vlist([1, 2, 5])
>>> a_list.accept(Printer())
list content :
[1, 2, 5]
>>> a_dict = vdict({'one': 1, 'two': 2, 'three': 3})
>>> a_dict.accept(Printer())
dict keys: one,three,two
>>> def visit(visited, visitor):
...     cls = visited.__class__.__name__
...     meth = 'visit_%s' % cls
...     method = getattr(visitor, meth, None)
...     if method is None:
...         method(visited)
... 
>>> visit([1, 2, 5], Printer())
list content :
[1, 2, 5]
>>> visit({'one': 1, 'two': 2, 'three': 3}, Printer())
dict keys: three,two,one
>>> def visit(directory, visitor):
...     for root, dirs, files in os.walk(directory):


...         for file in files:
...             # foo.txt <text:span text:style-name="T48">→</text:span> .txt
...             ext = os.path.splitext(file)[-1][1:]
...             if hasattr(visitor, ext):
...                 getattr(visitor, ext)(file)
... 
>>> class FileReader(object):
...     def pdf(self, file):
...         print 'processing %s' % file
... 
>>> walker = visit('/Users/tarek/Desktop', FileReader())
processing slides.pdf
processing sholl23.pdf
...     def process(self, text):
...         text = self._normalize_text(text)
...         words = self._split_text(text)
...         words = self._remove_stop_words(words)
...         stemmed_words = self._stem_words(words)
...         return self._frequency(stemmed_words)
...     def _normalize_text(self, text):
...         return text.lower().strip()
...     def _split_text(self, text):
...         return text.split()
...     def _remove_stop_words(self, words):
...         raise NotImplementedError
...     def _stem_words(self, words):
...         raise NotImplementedError
...     def _frequency(self, words):
...         counts = {}
...         for word in words:
...             counts[word] = counts.get(word, 0) + 1
>>> from itertools import groupby
>>> class BasicIndexer(Indexer):
...     _stop_words = ('he', 'she', 'is', 'and', 'or')
...     def _remove_stop_words(self, words):
...         return (word for word in words 
...                 if word not in self._stop_words)
...     def _stem_words(self, words): 
...         return ((len(word) > 2 and word.rstrip('aeiouy') 
...                  or word)
...                 for word in words)
...     def _frequency(self, words):
...         freq = {}
...         for word in words:
...             freq[word] = freq.get(word, 0) + 1
... 
>>> indexer = BasicIndexer()
>>> indexer.process(('My Tailor is rich and he is also '
...                  'my friend'))
{'tailor': 1, 'rich': 1, 'my': 2, 'als': 1, 'friend': 1}
