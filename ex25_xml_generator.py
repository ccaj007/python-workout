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
#    print(len(args))
#    print(kwargs)
    new_xml = []
    for kw in kwargs:
        print f{kw}'="{kwargs[kw]}"'

    new_xml.append(f"<{args[0]}>")
    
    for i in range(1, len(args)):
        new_xml.append(args[i])

    new_xml.append(f"</{args[0]}>")
    str = ''
    print(str.join(new_xml))

if __name__ == "__main__":
    myxml('foo', 'bar', a=1, b=2, c=3)

