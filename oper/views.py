from django.shortcuts import render
import math


def home(request):
    return render(request,'oper/home.html')

def tf(request):
    if request.method == 'GET':
        return render(request, 'oper/tf.html')
    else:
        cnt = 0
        L = request.POST['content'].split()
        for i in request.POST['content'].split():
            if request.POST['search'] in i: cnt += 1
        return render(request, 'oper/tf_result.html',{'split': L,'search':request.POST['search'],'count':cnt})


def df(request):
    if request.method == 'GET':
        return render(request, 'oper/df.html')
    else:
        L = []
        L.append(request.POST['doc1'])
        L.append(request.POST['doc2'])
        L.append(request.POST['doc3'])
        L.append(request.POST['doc4'])

        cnt = 0
        for i in L:
            if request.POST['search'] in i: cnt += 1

        return render(request, 'oper/df_result.html', {'doc':L,'search':request.POST['search'], 'count':cnt})

def idf(request):
    if request.method == 'GET':
        return render(request, 'oper/idf.html')
    else:
        L = []
        L.append(request.POST['doc1'])
        L.append(request.POST['doc2'])
        L.append(request.POST['doc3'])
        L.append(request.POST['doc4'])

        cnt = 0
        for i in L:
            if request.POST['search'] in i: cnt += 1

        return render(request, 'oper/idf_result.html', {'doc':L,'search':request.POST['search'], 'count':math.log(4/cnt)})
