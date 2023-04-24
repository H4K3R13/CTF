from pwn import *
p = remote("spaceheroes-death-star.chals.io", 443, ssl=True, sni="spaceheroes-death-star.chals.io")
p.interactive()
