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


numbers = {
'一':['yi1'],
'二':['er4'],
'三':['san1'],
'四':['si4'],
'五':['wu3'],
'六':['liu4'],
'七':['qi1'],
'八':['ba1'],
'九':['jiu3'],
'十':['shi2']
}

positions = {

}

family = {

}

verbs = {
    '想':['xiang3'],
    '喝':['he1'],
    '要':['yao4'],
    '':[''],
}

questions = {
'几':['ji3'],
}

jobs = {
    '医生':['yi1sheng1','doctor','curar-nacer'],
    '学生':['xue2sheng1','student'],
    '老师':['lao3shi1','teacher','profesiones que se necesitan técnicas o conocimientos'],
}

countries = {
    '中国':['zhong1guo2','china'],
    '国家':['guo2jia1','country'],
    '西班牙':['xi1ban1ya2','spain'],
    '法国':['fa3guo2','france'],
    '德国':['de2guo2','germany'],
    '英国':['ying1guo2','uk','united kingdom'],
    '美国':['mei3guo2','usa'],
    '奥地利':['ao4di4li4','austria','?-dueño-ventaja'],
    '意大利':['yi4da4li4','italy'],
    '加拿大':['jia1na2da4','canada','sumar-coger-grande'],
    '俄国':['e4guo2','russia'],
}

drinks = {
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
    '葡萄酒':['pu2tao2jiu3','wine']
}

colours = {
    '红':['hong2','red'],
    '黄':['huang2','yellow'],
    '蓝':['lan2','blue'],
    '绿':['lv4','green'],
    '黑':['hei1','black'],
    '白':['bai2','wite']
}

sentences = {
    '你们好，你们要喝什么?':['ni3men2hao3, ni3men2yao4he1shen2me',''],
    '我想要喝茶， 谢谢':['wo3xiang3yao4he1cha2, xie4xie4'],
    '我不想喝茶，我想要喝咖啡':['wo3bu4xiang3he1cha2, wo3xiang3yao4he1ka1fei1'],
    '林娜，这是谁？':['lin2na4, zhe4shi4shei2'],
    '这是我妹妹':['zhe4shi4wo3mei4mei'],
    '你好，你们想要喝什么？':['ni3hao3, ni3menxiang3yao4he1shen2me'],
    '我要喝可乐':['wo3yao4he1ke3le4'],
    '好的，你们都喝可乐':['hao3de, ni3mendou1he1ke3le4'],
    '你是哪国人？':['ni3shi4na3guo2ren2'],
    '我是中国人':['wo3shi4zhong1guo2ren2'],
    '你几岁':['ni3ji3sui4'],
    '我二十五岁':['wo3er4shi2wu4sui4'],
    '你想吃什么?':['ni3xiang3chi1shen2me'],
    '我想吃面':['wo3xiang3chi1mian4'],
    '我想要吃米饭':['wo3xiang3yao4chi1mi3fan4'],
    '对不求，我没有米饭':['dui4bu4qi3, wo3mei2you3mi3fan4'],
    '没关系我吃面':['mei2guan1xi1, wo3chi1mian4'],
    '我不忙，你男朋友呢？':['wo3bu4mang2, ni3nan2peng2you3ne']
}


lessons = {
    1:{},
    2:{},
    3:{},
    4:{},
    5:{},
    6:{},
    7:{},
    8:{},
    9:{},
    10:{},
    11:{},
    12:{},
    13:{
        '匕':['bi3','cuchara','spoon'],
        '耂':['lao3','viejo','old'],
        '说':['shuo1','hablar','talk'],
        '匚':['fang1','caja','box'],
        '语言':['yu3yan4','idioma','language'],
        '手扌':['shou3','hand','mano'],
        '拿':['na2','coger','grab'],
        '加':['jia1','sumar','sum'],
        '刀刂':['dao1','knife','daga'],
        '渴':['ke3','sed','thirsty'],
        '奥地利':['ao4di4li4','austria','?-dueño-ventaja'],
        '意大利':['yi4da4li4','italy'],
        '加拿大':['jia1na2da4','canada','sumar-coger-grande'],
        '俄国':['e4guo2','russia'],
        '饿':['e4','hambre','starvation'],
        '医生':['yi1sheng1','doctor','curar-nacer'],
        '学生':['xue2sheng1','student'],
        '学习':['xue2xi2','aprender genérico','generic learn'],
        '学':['xue2','aprender','to learn'],
        '外语':['wai4yu3','idioma extranjero','foreign language'],
        '老师':['lao3shi1','teacher','profesiones que se necesitan técnicas o conocimientos'],
        '出生':['chu1sheng1','nacer','born','salir-nacer'],
        '会':['hui4','can'],
        '工作':['gong1zuo4','trabajo','job'],
        '日本人':['ri4ben3ren2','japanese'],
        '日语':['ri4yu3','japansese language'],
        '可是':['ke3shi3','but']
    },
    14:{
        '辶':['chuo4','walk'],
        '艹':['cao3','grass'],
        '匕':['bi3','spoon','cuchara'],
        '马':['ma3','caballo','horse'],
        '言':['yan2','discurso'],
        '冫':['bing1','hielo'],
        '手':['shou3','mano'],
        '饣':['shi2','food'],
        '贝':['bei4','concha'],
        '米':['mi3','arroz','rice'],
        '刀刂':['dao1','daga','knife'],
        '认识':['ren2shi4','know'],
        '高兴':['gao1xing4','happy'],
        '可以':['ke3yi3','may','permission'],
        '出去':['chu1qu4','to exit','salir'],
        '去':['qu4','go','ir'],
        '来':['lai2','come','venir'],
        '请':['quing3','por favor','please'],
        '坐':['zuo4','sentarse','to sit'],
        '问':['wen4','preguntar','ask'],
        '姓':['xing4','apellidarse'],
        '名字':['ming2zi1','nombrarse'],
        '汉字':['han4zi','chinese character'],
        '贵':['gui4','caro','expensive'],
        '您贵':['nin2gui4','apreciado'],
    },
    15:{
        '认识':['ren4shi','conocer (a alguien)'],
        '高兴':['gao1xing4','encantado, contento'],
        '可以':['ke3yi3','poder'],
        '进来':['jin4lai','entrar'],
        '进':['jin4','entrar'],
        '来':['lai2','venir'],
        '请':['qing2','por favor'],
        '记者':['ji4zhe3','periodista'],
        '请问':['qing2wen','podría preguntarle...?'],
        '贵姓':['gui4xing4','cómo se llama'],
        '叫':['jiao4','llamarse'],
        '先生':['xian1sheng','señor']
    },
    16:{
        '餐厅':['',''],
        '宿舍':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
    },
    21:{
        '前':['qian2','delante'],
        '五年前':['wu3nian2qian2','hace 5 años'],
        '前天':['qian2tian1','anteayer'],
        '前年':['qian2nian2','hace dos años'],
        '时间':['shi2jian1','hora de time'],
        '时候':['shi2hou3','momento'],
        '天气':['tian1qi4','tiempo de meteorología'],
        '时':['shi2','hora de duración'],
        '点':['dian3',"o'clock"],
        '游泳':['you2yong3','swim'],
        '再':['zai4','volver a'],
        '打球':['da3qiu2','jugar a la pelota'],
        '遍':['bian4','número de veces de una acción'],
        '意思':['yi4si','significado'],
        '有意思':['you3yi4si','es interesante'],
        '没意思':['mei2yi4si','poco interesante'],
        '再说一遍':['zai4shuo1yi1bian4','Dilo de nuevo'],
        '再听一遍':['zai4ting1yi1bian4','Escucha de nuevo'],
        '游一个小时泳':['you2yi1gexiao3shi2yong3','Nadar por una hora'],
        '怎么样':['zen3meyang4','¿qué tal?'],
        '太':['tai4','demasiado'],
        '现在':['xian4zai4','ahora'],
        '知道':['zhi1dao4','saber'],
        '没关系':['mei2guan1xi','no importa'],
        '':['',''],
    },
    22:{},
    23:{
        '武术':['wu3shu4','arte marcial'],
        '跑步':['pao3bu4','correr paso = correr'],
        '踢':['ti1','dSar patada'],
        '足球':['zu2qiu2','pie pelota= fútbol'],
        '篮球':['lan2qiu2','cesta pelota = baloncesto'],
        '写':['xie3','write'],
        '元':['yuan2','yuan'],
        '皮':['pi2','piel'],
        '片':['pian4','slice'],
        '弓':['gong1','arco'],
        '巴':['ba1',''],
        'β':['fu4','oreja'],
        '长':['chang2','long'],
        '隹':['zhui1','bird'],
        '舌':['she2','tongue'],
        '专':['zhuan1','expert'],
    },
    24:{
        '因为':['yin1wei4','because'],
        '为什么':['wei4shen2me','why'],
        '下雨':['xia4yu3','caer lluvia'],
        '礼物':['li3wu4','regalo'],
        '给':['gei3','dar'],
        '专业':['zhuan1ye4','experto+tareas'],
        '专心':['zhuan1xin1','estar atento'],
        '我给你打电话':['wo3gei3ni3da4dian4hua4','I call you'],
        '系':['xi4',''],
        '美术':['mei3shu4','bellas artes'],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
        '':['',''],
    },
}




reverted_lessons = {
    1:{},
    2:{},
    3:{},
    4:{},
    5:{},
    6:{},
    7:{},
    8:{},
    9:{},
    10:{},
    11:{},
    12:{},
    13:{
        'bi3':['匕','y'],
        'lao3':['耂','y'],
        'shuo1':['说','y'],
        'fang1':['匚','y'],
        'yu3yan4':['语言','y'],
        'shou3':['手扌','y'],
        'na2':['拿','y'],
        'jia1':['加','y'],
        'dao1':['刀刂','y'],
        'ke3':['渴','y'],
        'ao4di4li4':['奥地利','y'],
        'yi4da4li4':['意大利','y'],
        'jia1na2da4':['加拿大','y'],
        'e4guo2':['俄国','y'],
        'e4':['饿','y'],
        'yi1sheng1':['医生','y'],
        'xue2sheng1':['学生','y'],
        'xue2xi2':['学习','y'],
        'xue2':['学','y'],
        'wai4yu3':['外语','y'],
        'lao3shi1':['老师','y'],
        'chu1sheng1':['出生','y'],
        'hui4':['会','y'],
        'gong1zuo4':['工作','y'],
        'ri4ben3ren2':['日本人','japanese'],
        'ri4yu3':['日语','japansese language'],
        'ke3shi3':['可是','but']
    },
    14:{},
    21:{
        'delante':['qian2','前'],
        'hace 5 años':['wu3nian2qian2','五年前'],
        'anteayer':['qian2tian1','前天'],
        'hace dos años':['Qian2nian2','前年'],
        'hora de time':['shi2jian1','时间'],
        'momento':['shi2hou3','时候'],
        'tiempo de meteorología':['tian1qi4','天气'],
        'hora de duración':['shi2','时'],
        "o'clock":['dian3',"点"],
        'swim':['you2yong3','游泳'],
        'volver a':['zai4','再'],
        'jugar a la pelota':['da3qiu2','打球'],
        'número de veces de una acción':['bian4','遍'],
        'significado':['yi4si','意思'],
        'es interesante':['you3yi4si','有意思'],
        'poco interesante':['mei2yi4si','没意思'],
        'dilo de nuevo':['zai4shuo1yi1bian4','再说一遍'],
        'Escucha de nuevo':['zai4ting1yi1bian4','再听一遍'],
        'Nadar por una hora':['you2yi1gexiao3shi2yong3','游一个小时泳'],
        '':['',''],
    },
    23:{
        'wu3shu4':['武术','arte marcial'],
        'pao3bu4':['跑步','correr paso = correr'],
        'ti1':['踢','dar patada'],
        'zu2qiu2':['足球','pie pelota= fútbol'],
        'lan2qiu2':['篮球','cesta pelota = baloncesto'],
        'xie3':['写','write'],
        'yuan2':['元','yuan'],
        'pi2':['皮','piel'],
        'pian4':['片','slice'],
        'gong1':['弓','arco'],
        'ba1':['巴',''],
        'fu4':['β','oreja'],
        'chang2':['长','long'],
        'zhui1':['隹','bird'],
        'she2':['舌','tongue'],
        'zhuan1':['专','expert'],
    },
}

