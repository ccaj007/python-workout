"""

Call                                        Return value
myxml('foo')                                <foo></foo>
myxml('foo', 'bar')                         <foo>bar</foo>
myxml('foo', 'bar', a=1, b=2, c=3)          <foo a="1" b="2" c="3">bar</foo>

Notice that in all cases, the first argument is the name of the tag. In the latter two
cases, the second argument is the content (text) placed between the opening and
closing tags. And in the third case

"""

def myxml(*args, **kwargs):
#    for kw in kwargs:
#        print(kw, '-', kwargs[kw])
    print(len(args))
    print(kwargs)

if __name__ == "__main__":
    myxml('foo', 'bar', a=1, b=2, c=3)

