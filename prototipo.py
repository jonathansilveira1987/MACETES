from datetime import datetime
a = datetime.now().strftime('\n%d-%m-%Y %H:%M:%S\n')
print(a)


b = str(datetime.now())
print(b)
#'2011-05-03 17:45:35.177000'