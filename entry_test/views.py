from django.shortcuts import render
from random import shuffle
from django.http import HttpResponse
from . import models

def index(request):
    qs=models.Riddle.objects.all()
    ll=list(qs)
    shuffle(ll)
    ll_op=[]
    for topic in ll:
        rr = models.Riddle.objects.get(id=topic.id)
        rr_qs=rr.option_set.all()
        l_op=[]
        for op in rr_qs:
            l_op.append(op.text)
        shuffle(l_op)
        ll_op.append(l_op)
    remembrancies=ll
    remembrancies1=ll_op
    data = {"header": "Память", "remembrancies": remembrancies , "remembrancies1": remembrancies1}

    return render(request, "entry_test/index.html", context=data)
def index1(request):
    if request.method == "POST":
        name = request.POST
        ss=set()
        if len(name)==1:
            name1="Ваш заказ пуст"
        else:
            name1=''
            
            for ii in name:
                if ii != 'csrfmiddlewaretoken':
                    #name1+=(', '+ ii)
                    ss.add(ii)
            for ii in ss:
                name1+=(', '+ ii)
            name1=name1[2:]

        qs=models.Riddle.objects.all()
        ll=list(qs)
        s_op_n=set()
        name2=''
        for topic in ll:
            rr = models.Riddle.objects.get(id=topic.id)
            rr_qs=rr.option_set.all()
            for op in rr_qs:
                if op.correct:
                    s_op_n.add(op.text)
        for ii in s_op_n:
            name2+=(' '+ str(ii))
            #name2=name2[2:]

        if (len(ss & s_op_n) == len(s_op_n) and (len(ss | s_op_n) == len(s_op_n)) and len(ss)>0):
            #name3="Вы выполнили тест верно"
            data = {"res": "Вы выполнили тест верно","res1": 5}
        else:
            data = {"res": "Вы выполнили тест неправильно","res1": 0}
            #name3="Вы выполнили тест неправильно"

        return render(request, "entry_test/index1.html", context=data)
    
        #return HttpResponse("<h2>Ваш заказ:</h2><p> {0}!</p<p> {1}!</p> <p> {2}!</p>".format(name1,name2,name3))
