def escapeCharacters():
    #single quote
    print '\'Hello\''
    #double quote
    print '\"Hello\"'
    #new line
    print 'Hello\nWorld'
    #backslash
    print 'Hello\\World'
    #backspace
    print 'Hello \bWorld'
    #carriage return
    print 'Hello\rWorld'
    #horizontal tab
    print 'Hello\tWorld'
    #vertical tab
    print 'Hello\vWorld'
    #octal
    print '\110\145\154\154\157'
    #hex
    print '\x48\x65\x6c\x6c\x6f'

if __name__ == "__main__":
    try:
        escapeCharacters()
    except Exception as e:
        print e


