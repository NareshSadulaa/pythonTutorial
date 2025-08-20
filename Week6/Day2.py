#Regular Expression (RE)--
# import re

import re
str="My insta Usernmae are nvr59 , gader87 , breqw22 , @gmail.com , 1234sh , jh6"
you=re.findall("[a-z]+\d+",str)
print(you)

# import re
# data="My age is 53 and Friend age is 43"
# give=re.findall("\d+",data)
# print(give)

# #To find the Perfect Password among these Password-
# import  re
# aa="My Password is admin@123 , 53891429 , quastech@95 , quastech"
# give=re.findall("[a-z]+@+\d+",aa)
# print(give)

# import re
# gg="the contact for customers only via xyz34@gmail.com and abc1@yahoo.com or amit34@quastech.in"
# give=re.findall("[a-z]+\d+@+[a-z]+.[a-z]+",gg)
# print(give)

# import re
# pano="there are some customers pan no GKLHN4567K ,ABCSF8989P,ADMIN0909, and Gmail5COM4"
# give=re.findall("[A-Z]+\d+[A-Z]",pano)
# print(give)

# import re
# email="ata=there are some href links for different website https://www.gmail.com and paytm.in also https://www.netflix.in some are www.xyz#.com and last https://www.amzon.org"
# give=re.findall("https://[a-z]+.[a-z]+.[a-z]+",email)
# print(give)

# import re
#
# t="some students born in 01/05/2005 , 14/12/2006 ,12-7-19 01-05-2003 "
# give=re.findall("\d+\d+\d+",t)
# print(give)