import pinyin,random,time
import numpy as np

from IPython.display import Markdown, display
from IPython.display import clear_output

'''
import pinyin

mystr = "个萄七葡木业语红是汁那哥咖明十他期人五几月和日物食要氵灬果里老料忄国在我色爷包冰水只大住米她饱父犬的奶喝六妳花岁想妈男惊吃酒这忙饭狗今家去茶休们姐门二九田心乐谁雨牛饣啡婆师你讠中禾好公面白猫冷哪爸小也作外天妹手四言目星可母三文不八儿土热弟一纟汉力饮吗火啤扌"
mysounds = [pinyin.get(e,format='numerical') for e in mystr]
myconcat = ["'"+st+"':['"+so+"']" for st,so in zip(mystr,mysounds)]
",".join(myconcat)

'''


mydict = {
'个':['ge4','ge5','ge'],'萄':['tao2'],'七':['qi1'],'葡':['pu2'],'木':['mu4'],'业':['ye4'],'语':['yu3'],'红':['hong2'],'是':['shi4'],'汁':['zhi1'],'那':['na4'],'哥':['ge1'],'咖':['ka1'],'明':['ming2'],'十':['shi2'],'他':['ta1'],'期':['qi1'],'人':['ren2'],'五':['wu3'],'几':['ji3'],'月':['yue4'],'和':['he2'],'日':['ri4'],'物':['wu4'],'食':['shi2'],'要':['yao4'],'氵':['r shui3'],'灬':['r hou3'],'果':['guo3'],'里':['li3'],'老':['lao3'],'料':['liao4'],'忄':['r xin1'],'国':['guo2'],'在':['zai4'],'我':['wo3'],'色':['se4'],'爷':['ye2'],'包':['bao1'],'冰':['bing1'],'水':['shui3'],'只':['zhi3'],'大':['da4'],'住':['zhu4'],'米':['mi3'],'她':['ta1'],'饱':['bao3'],'父':['fu4'],'犬':['quan3'],'的':['de5','de'],'奶':['nai3'],'喝':['he1'],'六':['liu4'],'妳':['ni3'],'花':['hua1'],'岁':['sui4'],'想':['xiang3'],'妈':['ma1'],'男':['nan2'],'惊':['jing1'],'吃':['chi1'],'酒':['jiu3'],'这':['zhe4'],'忙':['mang2'],'饭':['fan4'],'狗':['gou3'],'今':['jin1'],'家':['jia1'],'去':['qu4'],'茶':['cha2'],'休':['xiu1'],'们':['men5','men'],'姐':['jie3'],'门':['men2'],'二':['er4'],'九':['jiu3'],'田':['tian2'],'心':['xin1'],'乐':['le4'],'谁':['shui2'],'雨':['yu3'],'牛':['niu2'],'饣':['shi2'],'啡':['fei1'],'婆':['po2'],'师':['shi1'],'你':['ni3'],'讠':['yan2'],'中':['zhong1'],'禾':['he2'],'好':['hao3'],'公':['gong1'],'面':['mian4'],'白':['bai2'],'猫':['mao1'],'冷':['leng3'],'哪':['na3'],'爸':['ba4'],'小':['xiao3'],'也':['ye3'],'作':['zuo4'],'外':['wai4'],'天':['tian1'],'妹':['mei4'],'手':['shou3'],'四':['si4'],'言':['yan2'],'目':['mu4'],'星':['xing1'],'可':['ke3'],'母':['mu3'],'三':['san1'],'文':['wen2'],'不':['bu4'],'八':['ba1'],'儿':['er2'],'土':['tu3'],'热':['re4'],'弟':['di4'],'一':['yi1'],'纟':['si1'],'汉':['han4'],'力':['li4'],'饮':['yin3'],'吗':['ma5'],'火':['huo3'],'啤':['pi2'],'扌':['r shou3']
}

mydict_meanings = {}

mydict_examples = {}

mydict = {
'饮料':['yin3liao4','bebida','drink'],
'可乐':['ke3le4','cola','coke'],
'水':['shui3','water'],
'茶':['cha2','tea'],
'果汁':['guo3zhi1','fruit juice'],
'咖啡':['ka1fei1','coffee'],
'牛奶':['niu2nai3','milk'],
'喝酒':['he1jiu3','drink alcohol'],
'啤酒':['pi2jiu3','beer'],
'葡萄':['pu2tao2','grape'],
'葡萄酒':['pu2tao2jiu3','wine'],
'红':['hong2','red'],
'白':['bai2','wite']
}

def printmd(mystr):
    display(Markdown(mystr))
    

def print_instructions():
    printmd('### Welcome to MYCHINESE CHAR app')
    printmd('----')
    printmd("please type ** finish ** to exit the app")
    printmd("This app has dynamic probabilities per char that are updated following your score.")
    printmd('----')
print_instructions()
    
def normalize_w(weights):
    return weights/np.sum(weights)
    
def update_w(weights,indx,isCorrect,probab_coef=0.05):
    mydelta = probab_coef*(1/len(weights))
    if isCorrect:
        weights[indx] = weights[indx] - mydelta
    else:
        weights[indx] = weights[indx] + mydelta
    return normalize_w(weights)

def askarandom(mydict=mydict,probab_coef=0.05):
    #TODO, with memory, choose the ones that have more failures
    # https://stackoverflow.com/questions/4113307/pythonic-way-to-select-list-elements-with-different-probability
    keys = [k for k in mydict]
    values = [mydict[k] for k in mydict]
    weights = np.ones(len(keys))
    weights = normalize_w(weights)
    please_continue = True
    while please_continue:
        rand_index = int( np.random.choice(len(keys),size=1,replace=True,p=weights) )
        myrnd = keys[rand_index]
        true_ans = values[rand_index]
        #true_ans = pinyin.get(myrnd, format="numerical")
        printmd('# '+myrnd)
        ans = input("Type the pinyin of the character below >")
        #
        weights = update_w(weights,rand_index,ans in true_ans,probab_coef=0.05)
        #
        if ans in true_ans:
            printmd("<font color='green'> ** correct ** " + str(true_ans)+" </font>")
        elif ans in ['END','FINISH','finish','stop','STOP']:
            please_continue = False
            break
        else:
            printmd("<font color='red'> ** wrong, answer is > "+str(true_ans)+" ** </font>")
        ans = input("Continue [ANY KEY] or Finish ['finish']")
        if ans in ['END','FINISH','finish','stop','STOP']:
            please_continue = False
            break
        clear_output()
        print_instructions()