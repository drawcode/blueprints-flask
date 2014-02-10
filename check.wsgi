# This is the WSGI check, it sees if your wsgi is set us up correctly.

import sys

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!!'

    #output = output + 'sys' + sys.prefix
    #output = output + 'sys' + sys.path

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    print >> sys.stderr, 'sys.prefix = %s' % repr(sys.prefix)
    print >> sys.stderr, 'sys.path = %s' % repr(sys.path)


    return [output]