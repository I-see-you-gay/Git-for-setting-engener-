# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""




ip_address = input('Введите IP-адресс в формате 10.10.10.1 :').split('.')
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
          print('unused')

