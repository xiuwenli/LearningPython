#!/usr/bin/python
import re
phone = "602-343-8747"
s = "The phone number is 602-343-8747"
match = re.findall(r'(\d.*2)' , phone)
if match:
   a = (match)
   print 'The area code is:' + str(a)
