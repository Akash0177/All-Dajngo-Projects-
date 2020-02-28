class ExecutionFlowMiddleWare(object):

    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print("This line printed at pre-processing of request")
        response=self.get_response(request)
        print("This line printed at post processing of request")
        return response

from django.http import HttpResponse
class AppMaintenanceMiddelware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        return HttpResponse('<h1>Currently Application Under maintenance please after two days</h1>')

class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        s1='<h1>Currently we are facing some technical problems..please try after some time</h1><hr>'
        s2='<h2>Raised Exception:{}</h2>'.format(exception.__class__.__name__)
        s3='<h2>Exception Description/Message:{}</h2>'.format(exception)
        return HttpResponse(s1+s2+s3)

class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print("This line printed by first middleware  at pre processing of request")
        response=self.get_response(request)
        print("This line printed by first middleware at the post processing of request")
        return response

class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print("This line printed by Second middleware  at pre processing of request")
        response=self.get_response(request)
        print("This line printed by second middleware at the post processing of request")
        return response

class ThirdMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print("This line printed by third middleware  at pre processing of request")
        response=self.get_response(request)
        print("This line printed by third middleware at the post processing of request")
        return response
