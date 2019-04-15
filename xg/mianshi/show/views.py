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



