
import UserTask
import random
import time

postResponseList = []
getResponseList = []

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
    for i in range(100):
        eachstart=time.time()
        UserTask.UserTask.GetAndPost(getUrl, postUrl, getHeaders, postHeader, getTimeout, postTime, postParameters, getParameters)
        eachend=time.time()
        print(eachend-eachstart)
