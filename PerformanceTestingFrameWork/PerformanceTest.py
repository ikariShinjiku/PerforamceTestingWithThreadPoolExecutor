import multipleThread
import UserTask
import random

if __name__ == '__main__':
    getUrl = 'http://127.0.0.1:5000/GET'
    postUrl = 'http://127.0.0.1:5000/POST'
    getHeaders = None
    postHeader = {'Content-Type': 'application/json'}
    getTimeout = 0.1
    postTime = 0.1
    Price = random.randint(1, 1000)
    Coupon = random.randint(1, 1000)
    postParameters = {'Price': str(Price), 'Coupon': str(Coupon)}
    getParameters = {'Coupon': str(Coupon)}
    multipleThread.multipleThread.executedWithacerlate(10, 100, UserTask.UserTask.GetAndPost, getUrl, postUrl, getHeaders, postHeader, getTimeout, postTime, postParameters, getParameters)
    # for i in multipleThread.getResponseList:
    #     print("Get status is: "+str(i)+'\r\n')
    # for i in multipleThread.postResponseList:
    #     print("Post status is: "+str(i)+'\r\n')
