#!/bin/python
# module
try:
   import os,sys,time,requests,bs4
   from bs4 import BeautifulSoup
   from time import sleep
   from os import system
except:
      system("pip install requests bs4")
# code warna
b='\033[34;1m'
g='\033[32;1m'
p='\033[35;1m'
c='\033[36;1m'
r='\033[31;1m'
w='\033[37;1m'
y='\033[33;1m'
# tampilan
def jalan():
    tampil = """
\033[36;1m==============================================
 \033[33;1mAuthor \033[35;1m: \033[31;1mPanglima Jateng
 \033[33;1mTeam   \033[35;1m: \033[31;1mMafia Teknologi
 \033[33;1mNo Wa  \033[35;1m: \033[31;1m+62881024978351
\033[36;1m=============================================="""
    system("clear")
    sleep(1)
    system("figlet GOOGLE | lolcat")
    sleep(2)
    print(tampil)
    print()
    # isi data
    file = input("\033[32;1mMasukan Pencarian\033[36;1m:\033[37;1m ")
    ulr = f"https://www.google.com/search?&q={file}"
    r = requests.get(ulr)
    cari = BeautifulSoup(r.text,"html.parser")
    a = cari.find("div",class_="BNeawe").text
    # hasil pencarian
    print()
    sleep(2)
    print("\033[35;1mHasil \033[31;1m=\033[36;1m>\033[33;1m ",a)

jalan()
