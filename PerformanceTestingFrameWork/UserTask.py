import json
import HttpRequest
import multipleThread

class UserTask:

    def GetAndPost(getUrl,postUrl,getHeaders = None ,postHeader= None ,getTimeout=0.001, postTime=0.001, postParameters = None, getParameters = None):
        GetResponse = HttpRequest.HttpRequest.getMethod(url=getUrl, Headers=getHeaders, timeoutlength=getTimeout, **postParameters)
        multipleThread.getResponseList.append(GetResponse.status_code)
        PostResponse = HttpRequest.HttpRequest.postMethod(url=postUrl, Headers=postHeader, timeoutlength=postTime, postJson=json.loads(GetResponse.content), **getParameters)
        multipleThread.postResponseList.append(PostResponse.status_code)



