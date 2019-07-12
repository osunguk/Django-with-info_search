from django.shortcuts import render, redirect
import math
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle


def home(request):
    return render(request,'oper/home.html')

def processing(request):
    if request.method == 'GET': #request.method의 기본값이 GET 이기 때문에 POST를 제외한 흐름 조정
        try :
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc1.txt','r',encoding='UTF-8') as r:
                doc1 = r.read()
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc2.txt','r',encoding='UTF-8') as r:
                doc2 = r.read()
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc3.txt','r',encoding='UTF-8') as r:
                doc3 = r.read()
            return render(request, 'oper/processing.html',{'doc1':doc1,'doc2':doc2,'doc3':doc3, 'process' : '입력'})
        except FileNotFoundError:
            return render(request, 'oper/processing.html', {'doc1': '파일을 찾을 수 없습니다', 'doc2': '파일을 찾을 수 없습니다', 'doc3': '파일을 찾을 수 없습니다'})
    else : #POST 방식으로 request가 오면 실행
        doc1 = request.POST['doc1']
        doc2 = request.POST['doc2']
        doc3 = request.POST['doc3']
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc1.txt','w',encoding='UTF-8') as w:
            w.write(doc1)
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc2.txt', 'w',encoding='UTF-8') as w:
            w.write(doc2)
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc3.txt', 'w',encoding='UTF-8') as w:
            w.write(doc3)
        return render(request,'oper/processing.html',{'doc1':doc1,'doc2':doc2,'doc3':doc3})

def token(request):
    try:
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc1.txt','r',encoding='UTF-8') as r:
            doc1 = r.readlines()
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc2.txt','r',encoding='UTF-8') as r:
            doc2 = r.readlines()
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc3.txt','r',encoding='UTF-8') as r:
            doc3 = r.readlines()
        token_doc1 = word_tokenize(doc1[0])
        token_doc2 = word_tokenize(doc2[0])
        token_doc3 = word_tokenize(doc3[0])
        if len(doc1) == 1: #readlines로 파일을 읽었을 때 len가 1일때만 token한 파일을 write 하기 위한 조건문
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc1.txt','a',encoding='UTF-8') as w:
                w.write('\n')
                for x in token_doc1:
                    if x == '.' or x == ',': #온점, 반점 제거
                        continue
                    w.write(x.lower()+' ') #문자를 소문자로 전환 .lower()
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc2.txt', 'a',encoding='UTF-8') as w:
                w.write('\n')
                for x in token_doc2:
                    if x == '.' or x == ',':
                        continue
                    w.write(x.lower()+' ')
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc3.txt', 'a',encoding='UTF-8') as w:
                w.write('\n')
                for x in token_doc3:
                    if x == '.' or x == ',':
                        continue
                    w.write(x.lower()+' ')

        return render(request, 'oper/processing.html', {'process': '토큰화','token_doc1': token_doc1, 'token_doc2': token_doc2, 'token_doc3': token_doc3})
    except FileNotFoundError:
        return redirect('/home')

def normalization(request):
    try:
        shortword = re.compile(r'\W*\b\w{1,2}\b') #텍스트가 영어일때를 가정, len가 1~2인 단어는 대부분 불용어라 제거하기 위한 re 설정
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc1.txt','r',encoding='UTF-8') as r:
            tmp = r.readlines()
            token_doc1 = tmp[1].split()
            str = ''
            for x in token_doc1:
                str = str+' '+x #str 자료형으로 .sub('변경할 내용',변경될 스트링)가 실행되기 때문에 스트링으로 변환하는 코드
            str = shortword.sub('',str) #길이 2이하의 문자 제거

            new1 = str.split()
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc2.txt','r',encoding='UTF-8') as r:
            tmp = r.readlines()
            token_doc1 = tmp[1].split()
            str = ''
            for x in token_doc1:
                str = str+' '+x
            str = shortword.sub('',str)

            new2 = str.split()
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc3.txt','r',encoding='UTF-8') as r:
            tmp = r.readlines()
            token_doc1 = tmp[1].split()
            str = ''
            for x in token_doc1:
                str = str+' '+x
            str = shortword.sub('',str)

            new3 = str.split()
        if len(tmp) == 2:
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc1.txt','a',encoding='UTF-8') as w:
                w.write('\n')
                for x in new1:
                    w.write(x+' ')
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc2.txt', 'a',encoding='UTF-8') as w:
                w.write('\n')
                for x in new2:
                    w.write(x+' ')
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc3.txt', 'a',encoding='UTF-8') as w:
                w.write('\n')
                for x in new3:
                    w.write(x+' ')

        return render(request, 'oper/processing.html', {'process': '정제 및 정규화','token_doc1': new1, 'token_doc2': new2, 'token_doc3': new3})
    except FileNotFoundError:
        return redirect('/home')

def stop_word(request):
    try:
        stop_words = set(stopwords.words('english'))
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc1.txt','r',encoding='UTF-8') as r:
            tmp = r.readlines()
            token_doc1 = tmp[2].split()
            result1 = []
            for w in token_doc1:
                if w not in stop_words:
                    result1.append(w)
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc2.txt','r',encoding='UTF-8') as r:
            tmp = r.readlines()
            token_doc2 = tmp[2].split()
            result2 = []
            for w in token_doc2:
                if w not in stop_words:
                    result2.append(w)
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc3.txt','r',encoding='UTF-8') as r:
            tmp = r.readlines()
            token_doc3 = tmp[2].split()
            result3 = []
            for w in token_doc3:
                if w not in stop_words:
                    result3.append(w)

        if len(tmp) == 3:
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc1.txt','a',encoding='UTF-8') as w:
                w.write('\n')
                for x in result1:
                    w.write(x+' ')
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc2.txt', 'a',encoding='UTF-8') as w:
                w.write('\n')
                for x in result2:
                    w.write(x+' ')
            with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc3.txt', 'a',encoding='UTF-8') as w:
                w.write('\n')
                for x in result3:
                    w.write(x+' ')
    except FileNotFoundError:
        return redirect('/home')
    return render(request, 'oper/processing.html',{'process': '불용어 제거', 'token_doc1': result1, 'token_doc2': result2, 'token_doc3': result3})

def mkdic(request):
    try:
        stop_words = set(stopwords.words('english'))
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc1.txt','r',encoding='UTF-8') as r:
            tmp = r.readlines()
            token_doc1 = tmp[3].split()
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc2.txt','r',encoding='UTF-8') as r:
            tmp = r.readlines()
            token_doc2 = tmp[3].split()
        with open('C:/Users/osk/DjangoProject/info_search/oper/data/datadoc3.txt','r',encoding='UTF-8') as r:
            tmp = r.readlines()
            token_doc3 = tmp[3].split()

        dic1 = {} #사전 작업을 위한 초기화
        dic2 = {}
        dic3 = {}

        for x in token_doc1:
            if x in dic1.keys(): #키가 존재하면 cnt ++
                dic1[x] += 1
            else: # 존재하지 않으면 새롭게 key, value 설정
                dic1[x] = 1
        for x in token_doc2:
            if x in dic2.keys():
                dic2[x] += 1
            else:
                dic2[x] = 1
        for x in token_doc3:
            if x in dic3.keys():
                dic3[x] += 1
            else:
                dic3[x] = 1

        total_token_dic = list(dic1.keys())+list(dic2.keys())+list(dic3.keys()) #total_token_dic 생성

        indexing = {}

        for x in dic1:
            if x in indexing:
                indexing[x].append('doc1')
            else:
                indexing[x] = ['doc1']
        for x in dic2:
            if x in indexing:
                indexing[x].append('doc2')
            else:
                indexing[x] = ['doc2']
        for x in dic3:
            if x in indexing:
                indexing[x].append('doc3')
            else:
                indexing[x] = ['doc3']


        with open('C:/Users/osk/DjangoProject/info_search/oper/data/indexing_dic','wb') as w:
            pickle.dump(indexing,w)

        print_dic =[]
        for x,y in indexing.items():
            for z in y:
                x += ' ['+z+']'
            print_dic.append(x)

        return render(request, 'oper/processing.html', {'process': '인덱싱 사전 생성','index':print_dic})
    except FileNotFoundError:
        return redirect('/home')

def indexing(request):
    query = request.GET['search']

    with open('C:/Users/osk/DjangoProject/info_search/oper/data/indexing_dic', 'rb') as r:
        indexing = pickle.load(r)
    D1_cnt = 0
    D2_cnt = 0
    D3_cnt = 0
    Query_split = query.split()
    for x in Query_split:
        if x in indexing:
            for y in indexing[x]:
                if y == 'doc1':
                    D1_cnt += 1
                elif y == 'doc2':
                    D2_cnt += 1
                elif y == 'doc3':
                    D3_cnt += 1
                else:
                    pass
    result = {}
    result['doc1'] = D1_cnt
    result['doc2'] = D2_cnt
    result['doc3'] = D3_cnt

    print_dic = sorted(result.items(), key=lambda x: x[1], reverse=True)

    return render(request,'oper/indexing.html',{'similarity':print_dic})

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
