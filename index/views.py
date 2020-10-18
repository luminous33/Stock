from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse

from .models import CompanyInfo
from .models import DailyPrice
from .models import Merge

def index(request):
    # companies = CompanyInfo.objects.all()
    # context = {'companies':companies}
        # context에 모든 회사 정보를 저장

    # names = CompanyInfo.objects.values_list('company')
    #
    # prices = DailyPrice.objects.filter(date="2020-09-29")

    # q1 = CompanyInfo.objects.extra(tables=['DailyPrice'], where=['CompanyInfo.code=DailyPrice.code'])
    # q2 = CompanyInfo.objects.extra(tables=['DailyPrice'], where=['CompanyInfo.code=DailyPrice.code']).filter(data="2020-09-29")

    # results = list(chain(names, prices))
    # results = names.union(prices)

    # qs1 = CompanyInfo.objects.values_list('company', flat=True)
    # qs2 = DailyPrice.objects.filter(date="2020-09-29").values_list('code', 'date', 'open', 'high', 'low', 'close', 'diff', 'volume', flat=True)
    #
    # results = qs1.union(qs2)

    merges = Merge.objects.filter(date="2020-09-29").values('company', 'code', 'date', 'open', 'high', 'low', 'close', 'diff', 'volume')
    context = {'merges':merges}

    return render(request, 'index.html', context)
    
def empty(request):
    return render(request, 'empty.html')
    
def chart(request):
    return render(request, 'chart.html')
    
def introduce(request):
    return render(request, 'introduce.html')
    
def trading(request):
    return render(request, 'trading.html')


