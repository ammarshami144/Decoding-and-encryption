import hashlib
def a():
 print('''  _____                                     
 | ____|_ __   ___ _ __ _   _ _ __ | |_(_) ___  _ __  
 |  _| | '_ \ / __| '__| | | | '_ \| __| |/ _ \| '_ \ 
 | |___| | | | (__| |  | |_| | |_) | |_| | (_) | | | |
 |_____|_| |_|\___|_|   \__, | .__/ \__|_|\___/|_| |_|
                    |___/|_|                    


"Code by Ammar Shami
fb:www.facebook.com/ammar.shami.gov
''')


 # hashing module
 import hashlib
 class hashtext:
    def hashingtext(self,text,hash_type):
        text = text.encode ("utf-8")
        hash_hash = hashlib.new(hash_type)
        hash_hash.update(text)
        return hash_hash.hexdigest()

 text = str(input ("plz your text > "))
 while text == '':
    print("plz your text ''")
    text = str(input ("plz your txt > "))
 hashtype = str(input("plz hashtype >"))

 while hashtype == '':
    print("plz your hashtype ''")
    hashtype = str(input("plz your hashtype > "))

 h = hashtext()
 print(h.hashingtext(text,hashtype))

 
 
def b():
  print('''                                             
|  _ \  ___  ___ _ __ _   _ _ __ | |_(_) ___  _ __  
| | | |/ _ \/ __| '__| | | | '_ \| __| |/ _ \| '_ \ 
| |_| |  __/ (__| |  | |_| | |_) | |_| | (_) | | | |
|____/ \___|\___|_|   \__, | .__/ \__|_|\___/|_| |_|
                      |___/|_|
 
Code by Ammar Shami
fb:www.facebook.com/ammar.shami.gov
''')

  
  the_hash = str(input("the hash :"))
  the_wordlist = str(input("the wordlist :"))
  the_hash_type= str(input("the hash type :"))
  #read the wordlists
  class Readw:
    def Readwlist(self,wordlist):
        OR = open(wordlist,"r")
        return OR.readlines()
    
  RR = Readw()
  readall = RR.Readwlist(the_wordlist)

  # hashing text module
  import hashlib
  class hashingtxt:
    def hashtext(self,text,hash_type):
        text = text.encode ("utf-8")
        hash_hash = hashlib.new(hash_type)
        hash_hash.update(text)
        return hash_hash.hexdigest()

  HH = hashingtxt()
  for i in readall:
    i = i.rstrip("\n")
    hashT = (HH.hashtext(i,the_hash_type))
    if the_hash == hashT:
        print("{0}::{1}".format(the_hash,i))

		
	
while(True):
 print("""
 1 ) Encrypt 
 2 ) Decrypt 
 """)
 chooes = str(input(" Enter Chooes : "))
 if chooes == "1":
   a()
 if chooes == "2":
   b()
