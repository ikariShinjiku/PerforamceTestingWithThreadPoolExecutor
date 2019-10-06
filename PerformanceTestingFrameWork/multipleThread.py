from concurrent.futures import ThreadPoolExecutor
import time
postResponseList = []
getResponseList = []
class multipleThread:
    def pressureEachTime(pressure, httpFucntion, getUrl, postUrl, getHeaders, postHeader, getTimeout, postTime, postParameters, getParameters):
        startTime=time.time()
        process = ThreadPoolExecutor(max_workers=pressure)
        for i in range(pressure):
            process.submit(httpFucntion(getUrl, postUrl, getHeaders, postHeader, getTimeout, postTime, postParameters, getParameters))
        process.shutdown(wait=True)
        endTime=time.time()
        print("This thread end in :"+str(endTime-startTime))
        time.sleep(1)

    def executedWithacerlate(accerlate,pressure, httpFucntion, getUrl, postUrl, getHeaders, postHeader, getTimeout, postTime, postParameters, getParameters):
        executedTime=accerlate
        while(executedTime<pressure):
            multipleThread.pressureEachTime(executedTime, httpFucntion, getUrl, postUrl, getHeaders, postHeader, getTimeout, postTime, postParameters, getParameters)
            executedTime=executedTime+accerlate
        if(executedTime+accerlate>pressure and executedTime<pressure):
            multipleThread.pressureEachTime(pressure, httpFucntion)
