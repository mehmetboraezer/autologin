#!/usr/bin/env python

passwd = raw_input().strip()
key = [125, 137, 82, 35, 210, 188, 221, 234, 163, 185, 31]
key_len = len(key)

passwd = [ord(x) for x in list(passwd)]

r = len(passwd) % key_len

if r > 0:
    passwd += [0] * (key_len - r)

for i in range(0, len(passwd), len(key)):
    ki = 0
    for j in range(i, min(i + len(key), len(passwd))):
        passwd[j] = passwd[j] ^ key[ki]
        ki += 1

passwd = [chr(x) for x in passwd]
final_key = "".join(passwd)
fd = open("/etc/kcpassword", "w+", 0666)
fd.write(final_key)
fd.close()
