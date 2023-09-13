￼￼￼
def isleapYear(year):
￼ if (year  % 4 == 0 and year  % 100 !=0) or year  % 400 ==0:
   return False
else:
year = 2013
if isleapYear (year):
  print('{} is a leap year.'.format(year)) 
else:
  print('{} is not aleap year. '.format(year))
