#!/usr/bin/env python3
import crypt as cr
import sys, random
def method_selection():
  possible = ["sha512", "sha256", "blowfish", "md5", "crypt"]
  method=random.choice(possible)
  if(method.lower()=="sha512"):
    cr.METHOD_SHA512
  elif(method.lower()=="sha256"):
    cr.METHOD_SHA256
  elif(method.lower()=="blowfish"):
    cr.METHOD_BLOWFISH
  elif(method.lower()=="md5"):
    cr.METHOD_MD5
  elif(method.lower()=="crypt"):
    cr.METHOD_CRYPT
  elif(method.lower() not in possible):
    print("[404] Not a valid method")
    sys.exit(-1)

method_selection()  
def crypt(password):
  return cr.crypt(password)

password = str(random.randint(100, 200))
filename = "password"
possibleargs = ["-r", "-w"]
if(len(sys.argv)<2):
  print("USAGE: ./main.py -r OR ./main.py -w")
  sys.exit(-1)
if(sys.argv[1]=="-r"):
  print(crypt(password))
elif(sys.argv[1]=="-w"):
  with open(filename, "w") as f:
    f.write(crypt(password))
    f.write("\n")
    print("Password written to %s" % filename)
elif(sys.argv[1] not in possibleargs):
  print("USAGE: ./main.py -r OR ./main.py -w")



