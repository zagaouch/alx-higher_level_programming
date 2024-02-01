#!/usr/bin/python3
""" Script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response """
if __name__ == "__main__":
    from urllib import request, parse
    import sys
    values = {'email': sys.argv[2]}  # email is the second argument
    data = parse.urlencode(values).encode('ascii')  # encode data to ascii
    req = request.Request(sys.argv[1], data)  # create request object
    with request.urlopen(req) as response:  # open url and read response
        print(response.read().decode('utf-8'))  # print response body as utf-8
