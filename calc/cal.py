from cgi import parse_qs
from tem import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]

    product = 0
    response_body = html
    response_body = html % {
        'sum' : '***',
        'product' : '***',
    }
    if a.isdigit() and b.isdigit():   
        a, b = int(a), int(b)
        for i in range(b):
            product += a
        sum = a+b 
        response_body = html % {
            'sum' : sum,
            'product' : product,
        } 
    start_response('200 OK', [
        ('Content-Type', 'text/html'),    
	('Content-Length', str(len(response_body)))
    ])
    return [response_body] 
