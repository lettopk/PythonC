### DATES ### 

from datetime import datetime

now = datetime.now() #Extraer datos de tiempo actual
def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
    
print_date(now)


timestamp = now.timestamp() #Tiempo especifico en formato float
print(timestamp)

year_2025 = datetime(2025, 1, 1) #Setear un momento en el tiempo

print_date(year_2025)

from datetime import time

current_time =time(21, 6, 00)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 10, 4)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month +1, current_date.day) #Actualizacion o cambio de fecha setiada

print(current_date.month)
diff = year_2025 - now
print(diff)
diff = year_2025.date() - current_date
print(diff)

from datetime import timedelta #Trabajamos con franjas horarias cualquiera

init_time_delta = timedelta(200,100,100, weeks=10)
end_time_delta = timedelta(300,100,100, weeks=13)
print(end_time_delta - init_time_delta)
print(end_time_delta + init_time_delta)