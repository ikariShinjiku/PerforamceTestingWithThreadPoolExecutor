import requests

class HttpRequest:


    def getMethod(url, Headers={} , timeoutlength=0.001, **kwargs):
        FullUrl = url+'?'
        for key, value in kwargs.items():
            FullUrl = FullUrl+"{0}={1}".format(key, value)+'&'
        FullUrl=FullUrl.rstrip('&')
        postresponse = requests.get(FullUrl, headers=Headers, timeout=timeoutlength)
        return postresponse

    def postMethod(url, Headers={}, postJson={}, timeoutlength=0.001, **kwargs):
        FullUrl = url + '?'
        for key, value in kwargs.items():
            FullUrl = FullUrl + "{0}={1}".format(key, value) + '&'
        FullUrl=FullUrl.rstrip('&')
        postresponse = requests.post(FullUrl, headers=Headers, json=postJson, timeout=timeoutlength)
        return postresponse



