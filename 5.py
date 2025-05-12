str1= input()
str2= input()
str3= input()

set1 = set(str1)
set2 = set(str2)
set3 = set(str3)


ustr1 = set1 - (set2 | set3)
ustr2 = set2 - (set1 | set3)
ustr3 = set3 - (set1 | set2)


unique_chars = ustr1 | ustr2 | ustr3

print(unique_chars)
