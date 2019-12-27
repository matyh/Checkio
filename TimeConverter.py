def time_converter(time: str):
    h, m = (int(i) for i in time.split(':'))
    suffix = 'a.m.'
    if h > 12:
        h -= 12
        suffix = 'p.m.'
    elif h == 12:
        suffix = 'p.m.'
    elif h == 0:
        h = 12
    return f"{h}:{m:02} {suffix}"


print(time_converter('12:28'))
print(time_converter('23:54'))
print(time_converter('08:00'))
print(time_converter('00:30'))
