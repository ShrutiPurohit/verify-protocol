#!/bin/python3

#This version has 5 basic functionalities: creates, reads, sends, learns, unpacks
#creates: creates a new local object
#reads: reads an existing local object
#sends: sends a local object to other principal(s)
#learns: learns and stores an object received
#unpacks: unpacks and stores different parts of the object.

#You are to initially specify the number of principals taking part in the protocol and the intial objects.

import math
import os
import random
import re
import sys
import time

class Tree(object):
  def __init__(self):
    self.child = []
    self.data = None
  def printtree(self,level):
        print("\t"*level+repr(self.data))
        nochild = len(self.child)
        for chld in range(nochild):
            self.child[chld].node.printtree(level+1)
  def Checkreaders(self,pri,obj,level):
    u=len(obj)
    v=int(obj[1:u])
    if pri not in object1[v].readero:
      print("Principal",pri,"is not allowed to read",obj,":",object1[v].node.data)
      print("Do you want to add principal",pri,"to the readers list of",obj,"?(y/n)")
      update = input()
      if update == 'y':
        object1[v].readero.append(pri)
        print("The label of the object now is",object1[v].assigno,":",object1[v].nameo,"(",object1[v].ownero,",",object1[v].readero,",",object1[v].writero,")")
    nochild = len(self.child)
    for chld in range(nochild):
      self.child[chld].node.Checkreaders(pri,self.child[chld].assigno,level+1)


class Principal:
  def __init__(self,namep,ownerp,readerp,writerp):
    self.namep=namep
    self.ownerp=ownerp
    self.readerp=readerp
    self.writerp=writerp
    self.dictobj = dict()
  def add_to_dict(self,assignob,nameob):
    self.dictobj[assignob]=nameob
    
class Object:
  def __init__(self,assigno,nameo,ownero,readero,writero):
    self.assigno=assigno
    self.nameo=nameo
    self.ownero=ownero
    self.readero=readero
    self.writero=writero
    self.node = Tree()
    
def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list 

def Intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
  
principal = []
namepr = []
object1 = []
nameobj = []
dictpri = dict()
count = 0
auto = 0
ProcessingFile=""
offset=0
fp = None

def Init_Principals(i):
  owner = namepr[i]
  readerlist = namepr
  writerlist = []
  writerlist.append(namepr[i])
  print("The initial label of the principal ",namepr[i],": (",owner,",",readerlist,",",writerlist,")")
  principal.append(Principal(namepr[i],owner,readerlist,writerlist))

def CheckPrincipals(principal_list):
  pn=len(principal_list)
  cnt = 0
  for j in range(pn):
    if principal_list[j] not in namepr:
      print("-----ERROR-----",principal_list[j]," not in principal list\n")
    else:
      cnt += 1
  if cnt != pn:
    return 1
  else:
    return 0
  
def PrintState(step):
  print("\n---------------------STATE",step,"----------------------")
  prn = len(principal)
  for i in range(prn):
    print(principal[i].namep,"(",principal[i].ownerp,",",principal[i].readerp,",",principal[i].writerp,")")
  obn = len(object1)
  for i in range(obn):
    print(object1[i].assigno,":",object1[i].nameo,"(",object1[i].ownero,",",object1[i].readero,",",object1[i].writero,")")
    #object1[i].node.printtree(0)
  for i in range(prn):
    print("\nobjects that are present in the local space of principal",principal[i].namep)
    print(principal[i].dictobj)

def MyInput():
  global auto
  if auto == 1:
    global fp
    inp = fp.readline()
    if len(inp)>0:
      #input()
      inp = inp[0:len(inp)-1]
      print(inp)
      time.sleep(0.5)
      return inp
    else:
      auto = 0
      fp.close()
      print("Finished processing from file. Switching to manual mode.")
      print("If you wish to exit enter 'exit', otherwise answer the above question.")
      return input()
  return input()

def Init_Objects(i):
  print("\nEnter the initial label of the object : ",nameobj[i])
  #owners
  while 1:
    print("Enter the owner of the object ")
    owner = MyInput()
    if CheckPrincipals([owner])==1:
      print("Re enter the owner\n")
      continue
    else:
      break

  #readers
  while 1:
    print("Enter the principals who can read the object ")
    readerlist = MyInput().split(",")
    if CheckPrincipals(readerlist)==1:
      print("Re enter the readers")
      continue
    else:
      break

  #writers
  while 1:
    print("Enter the principals who have influenced the object ")
    writerlist = MyInput().split(",")
    if CheckPrincipals(writerlist)==1:
      print("Re enter the writers")
      continue
    else:
      break

  assign = "O"+str(i)
  print("The object",nameobj[i],"is stored as",assign,"and should be referred as the same in further references")
  print("The initial label of the object ",assign,"is",nameobj[i],": (",owner,",",readerlist,",",writerlist,")")
  object1.append(Object(assign,nameobj[i],owner,readerlist,writerlist))
  object1[i].node.data = nameobj[i]

def CreateInitLocal():
  prn = len(principal)
  obn = len(object1)
  for i in range(prn):
    dictpri[principal[i].namep]=i
    
  label = []
  for i in range(obn):
    readn = len(object1[i].readero)
    for j in range(readn):
      k = dictpri[object1[i].readero[j]]
      principal[k].add_to_dict(object1[i].assigno,object1[i].nameo)
  PrintState(0)

def getnop():
  print("Enter the number of principals in the system ")
  NoP = int(MyInput())
  return NoP

def getprincipal(i):
  print("Enter name of principal",i+1,end=" ")
  pr = MyInput()
  return pr

def getnoobj():
  print("\nEnter the number of initial objects in the system ")
  NoObj = int(MyInput())
  return NoObj

def getobject(i):
  print("Enter name of object",i+1,end=" ")
  ob = MyInput()
  return ob

def printIFD(ifd,step,msg):
  fd=open(ifd,"a+")
  fd.write("\n---------------------STATE")
  fd.write(str(step))
  fd.write("----------------------\n")
  fd.write(">>>>> :")
  fd.write(msg)
  fd.write("\n")
  prn = len(principal)
  for i in range(prn):
    fd.write(principal[i].namep)
    fd.write(",")
    fd.write(principal[i].ownerp)
    fd.write(",[")
    fd.write(','.join(principal[i].readerp))
    fd.write("],[")
    fd.write(','.join(principal[i].writerp))
    fd.write("])\n")
  obn = len(object1)
  for i in range(obn):
    fd.write(object1[i].assigno)
    fd.write(",")       
    fd.write(object1[i].nameo)
    fd.write(",")
    fd.write(object1[i].ownero)
    fd.write(",[")
    fd.write(','.join(object1[i].readero))
    fd.write("],[")
    fd.write(','.join(object1[i].writero))
    fd.write("])\n")
  fd.close()
    
def init(protocol,ifd):
  ff=open(protocol,"a+")
  NoP = getnop()
  ff.write(str(NoP))
  ff.write("\n")
  for i in range(NoP):
    pr = getprincipal(i)
    namepr.append(pr)
    ff.write(pr)
    ff.write("\n")
  for i in range(NoP):
    Init_Principals(i)

  NoObj = getnoobj()
  ff.write(str(NoObj))
  ff.write("\n")
  global count
  count = NoObj
  for i in range(NoObj):
    ob = getobject(i)
    nameobj.append(ob)
    Init_Objects(i)
    ff.write(object1[i].nameo)
    ff.write("\n")
    ff.write(object1[i].ownero)
    ff.write("\n")
    ff.write(','.join(object1[i].readero))
    ff.write("\n")
    ff.write(','.join(object1[i].writero))
    ff.write("\n")
  ff.close()
  msg="----INITIALIZATION---\n"
  printIFD(ifd,0,msg)
  CreateInitLocal()

def AddObjecttoLocal(p1,obj):
  global count
  j = count
  assignobj = "O" + str(j)
  i = dictpri[p1]
  principal[i].add_to_dict(object1[j].assigno,object1[j].nameo)
  print("The object",obj,"is stored as",assignobj,"and should be referred as the same in further references")
  print("The initial label of the object ",assignobj,"is",object1[j].nameo,": (",object1[j].ownero,",",object1[j].readero,",",object1[j].writero,")")
  count += 1

def Checkdowngrade(p1,p,obj):
  j = count
  u=len(obj)
  v=int(obj[1:u])
  owner=object1[v].ownero
  readers=object1[v].readero
  writers=object1[v].writero
  i = dictpri[p1]
  if principal[i].ownerp == owner:
    if principal[i].readerp == readers:
      if writers == [p1]:
        object1[v].readero.append(p)
        return "yes"
      else:
        if p in writers:
          object1[v].readero.append(p)
          return "yes"
  return "no"

def Downgrade(p1,p2,obj):
  j = count
  u=len(obj)
  v=int(obj[1:u])
  owner=object1[v].ownero
  readers=object1[v].readero
  writers=object1[v].writero
  assignobj = "O" + str(j)
  ws=[]
  ws=p2.split(",")
  for g in range(len(ws)):
    if ws[g] not in readers:
      #downgrading
      dg = Checkdowngrade(p1,ws[g],obj)
      if dg == "yes":
        print("Allowing Principal",ws[g],"to read object",object1[v].assigno,"could have been a security threat")
        print("But as per request, we allowed principal",ws[g],"to read it")
        print("Now object referred as",object1[v].assigno,"use this reference to for further references") #----change clarification for sends
      else:
        print("Allowing Principal",ws[g],"to read object",object1[v].assigno,"could have been a security threat and was not allowed to do so")
        print(object1[v].assigno,":",object1[v].nameo,"(",object1[v].ownero,",",object1[v].readero,",",object1[v].writero,")")
        print("Do you still want Principal",ws[g],"to read object",obj,"?(y/n)")
        choice = input()
        if choice == 'y':
          object1[v].readero.append(ws[g])
          print("Now object referred as",object1[v].assigno,"use this reference to for further references") #----change clarification for sends
        else:
          return 1
  return 0

def ComplexObject(p1,obj,p2):
  j = count
  assignobj = "O" + str(j)
  i = dictpri[p1]  
  writers=[]
  lenobj = len(obj)

  if obj[1]=='(' and obj[lenobj-1]==')':
    objs=obj[2:lenobj-1]
    objlist = objs.split(",")
    objno = len(objlist)
    readers = namepr
    children = []

    for k in range(objno):
      if objlist[k] not in principal[i].dictobj:
        print(objlist[k],"is not present in the local space of principal",p1)
        return 1
      else:
        u=len(objlist[k])
        v=int(objlist[k][1:u])
        children.append(v)
        readers = Intersection(readers,object1[v].readero)
        writers = Union(writers,object1[v].writero)

    #principal p1 reads all the objects of objlist--------
    principal[i].readerp=Intersection(readers,principal[i].readerp)
    principal[i].writerp=Union(writers,principal[i].writerp)

    object1.append(Object(assignobj,obj,principal[i].ownerp,list(principal[i].readerp),list(principal[i].writerp)))

    for k in range(objno):
      object1[j].node.child.append(object1[children[k]])
    lench = len(object1[j].node.child)
    x = 'f('+object1[j].node.child[0].node.data
    for i in range(1,lench):
      x = x + ',' + object1[j].node.child[i].node.data
    x = x + ')'
    object1[j].node.data=x
    object1[j].nameo = x

    if Downgrade(p1,p2,object1[j].assigno)==1:
      return 1
    return 0
  else:
    print("Invalid format of function definition")
    return 1

def SimpleObject(p1,obj,p2):
  #j = count
  global count
  assignobj = "O" + str(count)
  i = dictpri[p1]
  readers = list(principal[i].readerp)
  writers = list(principal[i].writerp)
  object1.append(Object(assignobj,obj,principal[i].ownerp,readers,writers))
  object1[count].node.data = obj
  if Downgrade(p1,p2,assignobj)==1:
    return 1
  return 0

def CreateObject(p1,obj,p2):
  if obj[0]=='f':
    if ComplexObject(p1,obj,p2)==1:
      return 1
    else:
      AddObjecttoLocal(p1,obj)
      return 0
  else:
    if SimpleObject(p1,obj,p2)==1:
      return 1
    else:
      AddObjecttoLocal(p1,obj)
      return 0

def ReadObject(p1,obj):
  i = dictpri[p1]
  u=len(obj)
  v=int(obj[1:u])
  if p1 in object1[v].readero:
    principal[i].readerp = Intersection(principal[i].readerp,object1[v].readero)
    principal[i].writerp = Union(principal[i].writerp,object1[v].writero)
    return 0
  else:
    print("Principal",p1,"is not allowed to read the object",obj)
    return 1

def SendObject(p1,obj,p2):
  u=len(obj)
  v=int(obj[1:u])
  ReadObject(p1,obj)
  object1[v].node.Checkreaders(p2,obj,0)
  if p2 not in object1[v].readero:
    #---create a new object and then append p2 into readers to new object
    j=count
    assign = "O"+str(j)
    object1.append(Object(assign,object1[v].nameo,object1[v].ownero,object1[v].readero,object1[v].writero))#--change
    object1[j].node = object1[v].node
    AddObjecttoLocal(p1,assign)
    print(p2,"not authorized to read object",obj)
    print("---Attempting to authorize the read---")
    if Downgrade(p1,p2,object1[j].assigno,object1[j].ownero,object1[j].readero,object1[j].writero) == 1:#---chnage
      return 1
  return 0

#-----using change made
def Check_principal_readobj(p1,obj):
  i=dictpri[p1]
  u=len(obj)
  v=int(obj[1:u])
  if p1 in object1[v].readero:
    print("principal",p1,"is allowed to read object",obj)
    return 0
  else:
    print("Principal",p1,"is not allowed to read the object",obj)
    return 1

def ReceiveObject(p1,obj):
  #-----change
  Check_principal_readobj(p1,obj)
  i=dictpri[p1]
  u=len(obj)
  v=int(obj[1:u])
  principal[i].readerp = Intersection(principal[i].readerp,object1[v].readero)
  principal[i].writerp = Union(principal[i].writerp,object1[v].writero)
  j=count
  assign = "O"+str(j)
  object1.append(Object(assign,object1[v].nameo,principal[i].ownerp,principal[i].readerp,principal[i].writerp))#--change
  object1[j].node = object1[v].node
  AddObjecttoLocal(p1,obj)
  #ReadObject(p1,assign)  

#---change
def LearnObject(p1,obj1,obj2):
  u=len(obj2)
  v=int(obj2[1:u])
  flag = 0
  lenobj = len(object1[v].node.child)
  for i in range(lenobj):
    if obj1 == object1[v].node.child[i].node.data:
      flag = 1
      break
  if flag == 0:
    print("-----ERROR-----object :",obj1,"not a part of msg :",obj2,"\n")
    return 1
  if p1 not in object1[v].node.child[i].readero:
    print("Principal",p1,"is not allowed to read",obj1,"\n")
    return 1
  ReadObject(p1,obj2)
  ReadObject(p1,object1[v].node.child[i].assigno)
  j=count
  t = dictpri[p1]
  assign = "O"+str(j)
  object1.append(Object(assign,obj1,principal[t].ownerp,principal[t].readerp,principal[t].writerp))
  object1[j].node = object1[v].node.child[i].node
  AddObjecttoLocal(p1,obj1)

def Unpackobj(p1,obj):
  print(obj)
  u=len(obj)
  v=int(obj[1:u])
  t=dictpri[p1]
  flag = 0
  lenobj = len(object1[v].node.child)
  for i in range(lenobj):
    if p1 not in object1[v].node.child[i].readero:
      print("Principal",p1,"is not allowed to read",object1[v].node.child[i].nameo,"\n")
      flag =1
  if flag == 1:
    print("principal",p1," is not allowed to unpack object",obj)
    return 1
  ReadObject(p1,obj)
  for i in range(lenobj):
    print(object1[v].node.child[i].assigno)
    ReadObject(p1,object1[v].node.child[i].assigno)
    j=count
    assign = "O"+str(j)
    object1.append(Object(assign,object1[v].node.child[i].nameo,principal[t].ownerp,principal[t].readerp,principal[t].writerp))
    object1[j].node = object1[v].node.child[i].node
    AddObjecttoLocal(p1,object1[v].node.child[i].assigno)
  

def Checkcreates(msgparts):
  if msgparts[1] != "creates" or msgparts[3] != "for" or len(msgparts) != 5:
    print("Wrong Language.\n")
    return 1
  p1 = msgparts[0]
  p2=msgparts[4].split(",")
  if CheckPrincipals([p1])==1:
    return 1
  if CheckPrincipals(p2)==1:
    return 1
  return 0

def Checkreads(msgparts):
  if msgparts[1] != "reads" or len(msgparts) != 3:
    print("Wrong Language.\n")
    return 1
  p1 = msgparts[0]
  obj = msgparts[2]
  if CheckPrincipals([p1]):
    return 1
  else:
    i = dictpri[p1]
    if obj not in principal[i].dictobj:
      print("-----ERROR----Object :",obj," not in local space of principal",p1,"\n")
      return 1
  return 0

def Checksends(msgparts):
  if msgparts[1] != "sends" or msgparts[3] != "to" or len(msgparts)!=5:
    print("Wrong Language.\n")
    return 1
  p1 = msgparts[0]
  obj = msgparts[2]
  p2 = msgparts[4]
  if CheckPrincipals([p1])==1:
    return 1
  else:
    i = dictpri[p1]
    if obj not in principal[i].dictobj:
      print("-----ERROR----Object :",obj," not in local space of principal",p1,"\n")
      return 1
  if CheckPrincipals([p2])==1:
    return 1
  return 0

def Checkreceives(msgparts):
  if msgparts[1] != "receives" or len(msgparts)!=3:
    print("Wrong Language.\n")
    return 1
  p1 = msgparts[0]
  if CheckPrincipals([p1])==1:
    return 
  return 0

def Checklearns(msgparts):
  if msgparts[1] != "learns" or msgparts[3]!="from" or len(msgparts)!=5:
    print("Wrong Language.\n")
    return 1
  p1 = msgparts[0]
  obj1 = msgparts[2]
  obj2 = msgparts[4]
  t = dictpri[p1]
  if CheckPrincipals([p1])==1:
    return 1
  if obj2 not in principal[t].dictobj:
    print("-----ERROR----object :",obj1,"not in local space of principal of :",p1,"\n")
    return 1
  return 0

def Checkunpack(msgparts):
  if msgparts[1]!= "unpack" or len(msgparts)!=3:
    print("Wrong Language. \n")
    return 1
  p1=msgparts[0]
  obj=msgparts[2]
  t=dictpri[p1]
  if CheckPrincipals([p1])==1:
    return 1
  if obj not in principal[t].dictobj:
    print("-----ERROR----object :",obj,"not in local space of principal of :",p1,"\n")
    return 1
  return 0

def Checkmsg(msgparts):
  if msgparts[1]=="creates":
    if Checkcreates(msgparts) == 1:
      return "error"
    else:
      return "creates"
  elif msgparts[1]=="reads":
    if Checkreads(msgparts) == 1:
      return "error"
    else:
      return "reads"
  elif msgparts[1]=="sends":
    if Checksends(msgparts) == 1:
      return "error"
    else:
      return "sends"
  elif msgparts[1]=="receives":
    if Checkreceives(msgparts) == 1:
      return "error"
    else:
      return "receives"
  elif msgparts[1]=="learns":
    if Checklearns(msgparts) == 1:
      return "error"
    else:
      return "learns"
  elif msgparts[1]=="unpack":
    if Checkunpack(msgparts) == 1:
      return "error"
    else:
      return "unpack"
  else:
    return "error"

def ProceedStep():
  global auto
  proceed = "yes"
  if auto == 0 :
    proceed = input("\nAre there any further steps in the protocol (yes/no)?")
  return proceed

def stmt(protocol,ifd):
  proceed = 'yes'
  step = 1
  ff=open(protocol,"a+")
  while proceed == 'yes':
    print("\nEnter Step",step,"of the Protocol:")
    msg = MyInput()
    if msg=="exit":
      break
    print("msg :",msg)
    msgparts = msg.split()
    fnc = Checkmsg(msgparts)

    if fnc == "error":
      print("Step does not follow language guidelines\n")
      continue

    if fnc == "creates":
      if CreateObject(msgparts[0],msgparts[2],msgparts[4]) == 1:
        continue
      else:
        ff.write(msg)
        ff.write("\n")
        PrintState(step)
        printIFD(ifd,step,msg)
        step += 1
        proceed = ProceedStep()

    if fnc == "reads":
      if ReadObject(msgparts[0],msgparts[2]) == 1:
        continue
      else:
        ff.write(msg)
        ff.write("\n")
        PrintState(step)
        printIFD(ifd,step,msg)
        step += 1
        proceed = ProceedStep()

    if fnc == "sends":
      if SendObject(msgparts[0],msgparts[2],msgparts[4]) == 1:
        continue
      else:
        ff.write(msg)
        ff.write("\n")
        PrintState(step)
        printIFD(ifd,step,msg)
        step += 1
        proceed = ProceedStep()

    if fnc == "receives":
      if ReceiveObject(msgparts[0],msgparts[2])==1:
        continue
      else:
        ff.write(msg)
        ff.write("\n")
        PrintState(step)
        printIFD(ifd,step,msg)
        step += 1
        proceed = ProceedStep()

    if fnc == "learns":
      if LearnObject(msgparts[0],msgparts[2],msgparts[4]) == 1:
        continue
      else:
        ff.write(msg)
        ff.write("\n")
        PrintState(step)
        printIFD(ifd,step,msg)
        step += 1
        proceed = ProceedStep()

    if fnc == "unpack":
      if Unpackobj(msgparts[0],msgparts[2]) == 1:
        continue
      else:
        ff.write(msg)
        ff.write("\n")
        PrintState(step)
        printIFD(ifd,step,msg)
        step += 1
        proceed = ProceedStep()
  ff.close()

if __name__ == '__main__':
  auto=int(input("enter\n 1 to process from file \n 0 to enter protocol manually "))
  if auto == 1:
    ProcessingFile=input("enter filename from which input to be processed ")
    fp=open(ProcessingFile,"r")
    protocol = fp.readline()
    protocol = protocol[0:len(protocol)-1]
  else:
    protocol=input("enter name of the protocol:")
  ts=time.time()
  protocolfile=protocol+"_"+str(ts)

  ff=open("%s.txt" % protocolfile,"w+")
  ff.write(protocol)
  ff.write("\n")
  ff.close()

  ifdfile=protocol+"_ifd_"+str(ts)
  fd=open("%s.txt" % ifdfile,"w+")
  fd.write("******IFD*******\n")
  fd.close()

  init("%s.txt" % protocolfile,"%s.txt" % ifdfile)
  stmt("%s.txt" % protocolfile,"%s.txt" % ifdfile) 
