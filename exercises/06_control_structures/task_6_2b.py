# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

"""ip_address = input('Введите IP-адресс в формате 10.10.10.1 :').split('.')
ip_int = []
for control in ip_address:
   try:
       ip_int.append(int(control))
   except ValueError:
       print('неправильный IP-адрес')
       break           
   if not len(ip_address) == 4:
       print('неправильный IP-адрес')
       break
   if int(control) < 0 or int(control) > 255:
       print("Неправильный IP-адрес")
       break
else:
   if ip_address[0] > '0' and ip_address[0]<= '223':
       print('unicast')
   elif ip_address[0] > '223' and ip_address[0] <= '239':
      print('multicast')
   elif  ip_address[0] == '255' and ip_address[1] == '255' and ip_address[2] == '255' and ip_address[3] == '255':
      print('local broadcast')
   elif ip_address[0] == '0' and ip_address[1] == '0'and ip_address[2] == '0' and ip_address[3] == '0':
       print('unassigned')
   else:
          print('unused')"""
























ip_address = input('Введитите IP-адрес: ').split('.')
address_corect = False
empty = []
x = 0
while not address_corect:
    for add in ip_address: 
        try:
            empty.append(int(add))
        except ValueError:
            empty.append(add)
        if type(empty[x]) != int:
            empty.clear()
            x = 0
            print("Неправильный IP-адрес")
            ip_address = input('Введите адреc ещё раз: ').split('.')
            break
        elif empty[x] < 0 or empty[x] > 255:
            empty.clear()
            x == 0
            print("Неправильный IP-адрес")
            ip_address = input('Введите адрес ещё раз: ').split('.')
            break
        elif len(ip_address) != 4:
            empty.clear()
            x == 0
            print("Неправильный IP-адрес")
            ip_address = input('Введите адрес ещё раз: ').split('.')
            break
        else:
            x += 1
            if x == 4:
                address_corect = True
                break
if ip_address[0] > '0' and ip_address[0]<= '223':
   print('unicast')
elif ip_address[0] > '223' and ip_address[0] <= '239':
   print('multicast')
elif  ip_address[0] == '255' and ip_address[1] == '255' and ip_address[2] == '255' and ip_address[3] == '255':
   print('local broadcast')
elif ip_address[0] == '0' and ip_address[1] == '0'and ip_address[2] == '0' and ip_address[3] == '0':
   print('unassigned')
else:
   print('unused')
    

