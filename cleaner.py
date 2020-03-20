import os
import colorama
import random
dir="/var/log/"
def main():
 find(dir)
def random_symbols():
 symbols="" 
 sym=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y''z','1','2','3','4','5','6','7','8','9','0','!','@','#']
 for i in range(0,100):
  symbols+=random.choice(sym)
 return symbols
def clean(path_to_file):
 with open (path_to_file,'w') as file:
  for u in range(0,20):
   file.write(random_symbols()) 
# os.remove(path_to_file)
#def delete(path_to_file): 
def find(dir):
 for name in os.listdir(dir):
  if  os.path.isfile(os.path.join(dir,name)):
    #print ("File:"+os.path.join(dir,name))
    clean(os.path.join(dir,name))
    #delete(os.path.join(dir,name))
  elif os.path.isdir(os.path.join(dir,name)):
    find(os.path.join(dir,name))
