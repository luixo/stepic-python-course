import datetime
print((datetime.date(*list(map(lambda x: int(x), input().split()))) + datetime.timedelta(int(input()))).strftime('%Y %-m %-d'))
# Если возникает ошибка ValueError: Invalid format string, придется переписать с помощью ручного форматирования