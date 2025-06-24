#!/usr/bin/env python3
from pwn import *

context.log_level = "debug"

hostch = "challenge03.root-me.org"
portch = 2223
userch = "app-systeme-ch63"
passch = "app-systeme-ch63"

s=ssh(host=hostch,user=userch,password=passch,port=portch)
p=s.process('./ch63')

p.interactive()
