import random
s = "asdfgghhjjkl1234567890qwertyuiopzxcvbnm,./';()*&^%$#@!?:}{]"
passlen = 8
p= "".join(random.sample(s,passlen))
print(p)
