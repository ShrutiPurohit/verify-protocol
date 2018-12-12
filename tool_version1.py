#!/bin/python3

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
    self.localObjects=[]
    
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
    print(principal[i].localObjects)

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
      principal[k].localObjects.append(object1[i].assigno)

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
  print("\nEnter name of object",i+1,end=" ")
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
    fd.write(":(")
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
  PrintState(0)

def AddObjecttoLocal(p1,assignobj):
  j = int(assignobj[1:len(assignobj)])
  i = dictpri[p1]
  principal[i].localObjects.append(object1[j].assigno)
  print("The object",object1[j].nameo,"is stored as",assignobj,"and should be referred as the same in further references")
  print("The initial label of the object ",assignobj,"is",object1[j].nameo,": (",object1[j].ownero,",",object1[j].readero,",",object1[j].writero,")")

def CheckDowngrade(p1,r,w,p2):
  flag = 0
  for p in p2:
    if p not in r:
      flag = 1
      break
  if flag == 0:
    return 0

  r = Union(r,w)
  for p in p2:
    if p not in r:
      flag = 0
      break

  if w == [p1] or flag == 1:
    print("Principals",p2,"added as readers for the new object\n")
    return 0
  else:
    print("Allowing principals",p2,"to read the new object was a security threat\n")
    print("Do you still wish to allow principals",p2,"to read the new object? (y/n)")
    choice = input()
    if choice == 'y':
      print("Adding principals",p2,"as readers as per request\n")
      return 0
    else:
      return 1

def CheckObject(obj):
  start = obj.find('(')
  if start == -1:
    return "simple"
  if obj[len(obj)-1] != ')':
    return "incorrect"
  return "complex"

def ParseComplex(p1,obj):
  start = obj.find('(')
  potential = obj[start+1:len(obj)-1]
  objlist = potential.split(",")
  i = dictpri[p1]

  for o in objlist:
    if o not in principal[i].localObjects:
      print(obj,"is not a wellformed complex object\n")
      return []

  return objlist

def CreateObject(p1,obj,p2):
  LabelChange = 0
  i = dictpri[p1]
  readers = list(principal[i].readerp)
  writers = list(principal[i].writerp)

  objectType = CheckObject(obj)
  if objectType == "incorrect":
    print("The object",obj,"is not well formed\n")
    return 1
  if objectType == "complex":
    objList = ParseComplex(p1,obj)
    if len(objList)==0:
      return 1
    else:
      for o in objList:
        v=int(o[1:len(o)])
        readers = Intersection(readers,object1[v].readero)
        writers = Union(writers,object1[v].writero)
      LabelChange = 1

  p2 = p2.split(",")
  if CheckDowngrade(p1,readers,writers,p2) == 1:
    return 1

  if LabelChange == 1:
    principal[i].readerp = list(readers)
    principal[i].writerp = list(writers)

  global count
  assignobj = "O" + str(count)
  object1.append(Object(assignobj,obj,principal[i].ownerp,Union(principal[i].readerp,p2),principal[i].writerp))
  count += 1
  AddObjecttoLocal(p1,assignobj)
  return 0

def SendObject(p1,obj,p2):
  i = dictpri[p1]
  if obj not in principal[i].localObjects:
    print(obj,"is not in the local space of principal",p1,"\n")
    return 1

  v=int(obj[1:len(obj)])
  readers = list(principal[i].readerp)
  writers = list(principal[i].writerp)
  readers = Intersection(readers,object1[v].readero)
  writers = Union(writers,object1[v].writero)
  if CheckDowngrade(p1,readers,writers,[p2]) == 1:
    return 1

  principal[i].readerp = list(readers)
  principal[i].writerp = list(writers)

  global count
  assignobj = "O" + str(count)

  object1.append(Object(assignobj,obj,principal[i].ownerp,Union(principal[i].readerp,[p2]),principal[i].writerp))
  count += 1
  AddObjecttoLocal(p1,assignobj)
  print("The object being sent is referenced as",assignobj,"\n")
  return 0

def ReceiveObject(p1,obj):
  #-----change
  global count
  v=int(obj[1:len(obj)])
  if p1 not in object1[v].readero:
    print("------Error-----principal",p1,"is not allowed to read object",obj,"\n")
    return 1

  i=dictpri[p1]
  principal[i].readerp = Intersection(principal[i].readerp,object1[v].readero)
  principal[i].writerp = Union(principal[i].writerp,object1[v].writero)

  j=count
  assign = "O"+str(j)
  object1.append(Object(assign,object1[v].nameo,principal[i].ownerp,principal[i].readerp,principal[i].writerp))#--change
  count += 1
  AddObjecttoLocal(p1,assign)

def Checkcreates(msgparts):
  if len(msgparts) != 5:
    print("Wrong Language.\n")
    return 1
  if msgparts[3] != "for":
    print("Wrong Language.\n")
    return 1
  p1 = msgparts[0]
  p2 = msgparts[4].split(",")
  if CheckPrincipals([p1])==1:
    return 1
  if CheckPrincipals(p2)==1:
    return 1
  return 0

def Checksends(msgparts):
  if len(msgparts) != 5:
    print("Wrong Language.\n")
    return 1
  if msgparts[3] != "to":
    print("Wrong Language.\n")
    return 1
  p1 = msgparts[0]
  obj = msgparts[2]
  p2 = msgparts[4]
  if CheckPrincipals([p1,p2])==1:
    return 1
  i = dictpri[p1]
  if obj not in principal[i].localObjects:
    print("-----ERROR----Object :",obj," not in local space of principal",p1,"\n")
    return 1
  return 0

def Checkreceives(msgparts):
  if len(msgparts) != 3:
    print("Wrong Language.\n")
    return 1
  p1 = msgparts[0]
  if CheckPrincipals([p1])==1:
    return 1
  if int(msgparts[2][1:len(msgparts[2])]) >= count:
    print("-----ERROR----Object :",msgparts[2],"does not exist\n")
    return 1
  return 0

def Checkmsg(msgparts):
  if msgparts[1]=="creates":
    if Checkcreates(msgparts) == 1:
      return "error"
    else:
      return "creates"
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
  else:
    return "error"

def stmt(protocol,ifd):
  step = 1
  ff=open(protocol,"a+")
  while True:
    print("\nEnter Step",step,"of the Protocol:")
    msg = MyInput()
    if msg=="exit":
      break
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

    if fnc == "sends":
      if SendObject(msgparts[0],msgparts[2],msgparts[4]) == 1:
        continue
      else:
        ff.write(msg)
        ff.write("\n")
        PrintState(step)
        printIFD(ifd,step,msg)
        step += 1

    if fnc == "receives":
      if ReceiveObject(msgparts[0],msgparts[2])==1:
        continue
      else:
        ff.write(msg)
        ff.write("\n")
        PrintState(step)
        printIFD(ifd,step,msg)
        step += 1

  ff.close()

if __name__ == '__main__':
  auto=int(input("enter\n 1 to process from file \n 0 to enter protocol manually "))
  if auto == 1:
    ProcessingFile=input("enter filename from which input to be processed ")
    fp=open(ProcessingFile,"r")
    protocol = fp.readline()
    protocol = protocol[0:len(protocol)-1]
  else:
    protocol=input("enter name of the protocol: ")
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