print("Hello")
"""a = int(input('Введите значение "a" :')) 
if a == 19:
    print('да, a = 19')
elif a < 19:
    print("a меньше 19")
elif 400 > a > 19:
    print('a больше 19 ')
else:
    print('a вне диапазона')"""


"""list_to_test = []
list_to_test2 = []

if list_to_test:
    print('В списке есть обкекты')

if list_to_test2:
    print('Объектов в списке нет')
string = 'Лох позорный'
print('Лох' in string)
listos = [0,0,0]
print(0 or listos)"""



"""username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

while True:
    if len(password) < 8:
        print('Пароль слишком короткий')
    elif username.lower() in password.lower():
        print('Пароль содержит имя пользователя')
    else:
        print('Пароль для пользователя {} установлен'.format(username))
        break
    password = input('Введите пароль ещё раз: ')"""

#kk = [4,5,2,8,4]
#print(True if len(kk) == 4 else False)


"""words = ['list', 'dict', 'tuple']
upper_words = []
for word in words:
    upper_words.append(word.upper())
print(upper_words)
"""

"""words = ['viktor','vlad','egor']
upper_words = []
upper_words.append(words[0])
print(upper_words)
upper_words.append(words[1].upper())
print(upper_words)
x = 15
for i in range(x):
    print(f'FastEthernet0/{i}')"""     #Буква f в Python означает, что строка является f-строкой.
                                    #Такие строки позволяют включать переменные в строки, заменяя имена переменных в фигурных скобках на их значения при выводе строки. 

"""dela = ['встать','пожрать','лечь спать обратно']
day = ['Понедельник','Вторник','Среду','Четверг','Пятницу','Субботу','Воскресенье']
for rasp in day:
    if rasp == 'Вторник':
        x = 'Во'
    else:
        x = 'В'
    print('{} {} надо:'.format(x, rasp))
    for do in dela:
        print('{}'.format(do))"""




inputs = input('Введите ip: ')
ip_address = inputs.split('.')
ip_list = []
x = -1  
for number in ip_address:
    try:
         ip_list.append(int(number))
         x += 1 
         if ip_list[x] > 255:
            print('Неправильный IP адрес')
            quit()
    except ValueError:
         print('Неправильный IP адресс')
         quit()
else:   
    if len(ip_address) == 4:
        print('Да лен')   
        if int(ip_address[0]) != 0 and int(ip_address[0]) <= 223:
            print('unicast')
        elif int(ip_address[0]) > 223 and int(ip_address[0]) <=239:
            print('multicast')
        elif inputs== '255.255.255.255':
            print('local broadcast')
        elif inputs== '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
    else:
        print('Неправильный IP адресс')        
        

