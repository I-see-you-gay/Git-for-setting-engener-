# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_address = input('Введите IP-адресс в формате 10.10.10.1 :').split('.')
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
