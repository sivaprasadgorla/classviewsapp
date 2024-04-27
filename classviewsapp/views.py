from django.shortcuts import render
from django.views import View
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'input.html')
class Add(View):
        def get(self,request):
            x=(request.GET["t1"])
            y=(request.GET["t2"])
            z=x+y
            con_dict={"res":z}
            return render(request,"result.html",context=con_dict)
        def post(self,request):
            x=(request.POST["t1"])
            y=(request.POST["t2"])
            z=x+y
            con_dict={'res':z}
            return render(request,"result.html",context=con_dict)

