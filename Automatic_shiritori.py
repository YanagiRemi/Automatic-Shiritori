def shiritori(s,mylist):                    #文字sではじまる単語をランダムに選ぶ関数
    mychoice=[]                             #空のリストmychoice作成
    for i in mylist:
        if i.startswith(s)==True:           #mylistの中からsで始まる単語をmychoiceに追加していく
            mychoice.append(i)
    if mychoice==[]:                        #mychoiceが空のままなら文字endを返す．
        return 'end'
    import random
    x=random.choice(mychoice)               #mychoiceの中からランダムに選んだ単語をxに格納
    mylist.remove(x)                        #mylistからxを削除
    return x                                #xを返す

with open('dic.txt',encoding='utf-8') as f:  #ファイルdic.txtを開く
    for line in f:
        mylist=f.readlines()                 #ファイルから読み込んだ単語をmylistに格納していく
f.close()          #ファイル閉じる
for m in range(0,len(mylist)):
    mylist[m]=mylist[m].strip('\n')         #mylistの中の改行文字を削除していく
begin=input()                               #しりとりの始めの文字の入力要求しbeginに格納
word=shiritori(begin,mylist)                #しりとり関数に引数としてbeginを渡し戻り値をwordに格納
if word=='end':
    print('その文字から始めることはできません．')  #指定した文字から始まる単語がなければ文を表示し終了
    import sys
    sys.exit()
else:
    print(word)                             #wordに格納された単語を表示

while True:                                    #ここからはwhile文でプログラムが終了するまで繰り返す
    if word[len(word)-1:]=="ン":               #wordの語尾がンならプログラム終了
        import sys
        sys.exit()
    elif word[len(word)-1:]=="ー":             #wordの語尾がーならconnectにーの前の文字を格納
        connect=word[len(word)-2]
    else:
        connect=word[len(word)-1]              #wordの語尾がンでもーでもなければ語尾をconnectに格納

    word=shiritori(connect,mylist)             #connectとmylistを引数に渡しshiritori関数実行し戻り値をwordに格納
    if word=='end':
        import sys                             #word=endならプログラム終了
        sys.exit
    else:
        print('->')
        print(word)                            #wordを表示する
