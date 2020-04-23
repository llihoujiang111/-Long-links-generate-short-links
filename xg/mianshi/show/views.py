import re
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from show.models import Shorturl
from base.base import get_hash_key


# Create your views here.
# 产生短连接
def generateurl(request):
    if request.method == "POST":
        hq = request.POST
        curl = hq.get('curl')  # 长连接
        zdurl = hq.get('zdurl')  # 自定义写的短url
        durls = get_hash_key(curl)  # 生成的短连接
        h = re.findall(pattern='(.*?)://', string=curl)
        durl = h.pop() + '://' + durls.pop(2)
        if zdurl != '' and curl != '':
            if Shorturl.objects.filter(durl=zdurl):
                return HttpResponse('Hello Word')
            else:
                Shorturl.objects.create(curl=curl, durl=zdurl)

                return JsonResponse({
                    'durl':zdurl
                })
        elif len(zdurl) == 0 and len(curl) != 0:
            if Shorturl.objects.filter(durl=durl):
                return HttpResponse('Hello Word')
            else:
                Shorturl.objects.create(curl=curl, durl=durl)

                return JsonResponse({
                    'durl': durl
                })
    else:
        return render(request, 'index.html')


# 使用短连接进行跳转
def useurl(request):
    if request.method =='GET':
        return render(request ,'index.html')
    if request.method == 'POST':
        a=request.POST.get('zdurl')
        print(a)
        obje = Shorturl.objects.filter(durl=a)
        if obje:

            curl = obje.values('curl')[0]
            num = obje.values('number')[0]
            print(curl)
            print(num.get('number'))
            obje.update(number=(int(num.get('number')) + 1))  # 访问一次计数器加一
            return HttpResponseRedirect(curl.get('curl'))  # 302 跳转
