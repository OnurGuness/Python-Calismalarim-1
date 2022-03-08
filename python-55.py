#Regular Expressions
#Regex

#Standart re kütüphanesi kullanılır
#import re

# findall()
# search()
# split()
# sub()

# [] Karakter seti  "[a-l]"
# \  Özel karakter ayrımı "\"
# .  Herhangi bir karakter "he..o"
# ^  Başlayan kelime-harf  "^hello"
# $  Biten kelime-harf "world$"
# *  Hiç tekrar etmiş mi "aix*"
# +  En az bir defa tekrar "aix+"
# {} Belirtilen sayıda tekrar etmiş mi "al{2}"
# |  Veya    "falls|stays"

import re

s = "bugün hava çok güzel"

a = re.findall("[a-d]",s)
print(a)

a = re.search("h..a",s)
print(a)

a = re.findall("^bugün",s)
print(a)

a = re.findall("okx+",s)
print(a)

a = re.split("\s",s)
print(a)

a = re.sub("h..a","ders",s)
print(a)

