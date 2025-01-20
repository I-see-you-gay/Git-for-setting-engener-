# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_address = input('Введите IP: ')
ip_address = ip_address.split('.')
prefix_mask = ip_address[-1][-2:]
mask = int(prefix_mask) * "1" + "0" * (32 - int(prefix_mask))
mask = '''{0:08b}{1:08b}{2:08b}{3:08b}'''.format(int(mask[:8],2), int(mask[8:16],2), int(mask[16:24],2), int(mask[24:],2))
ip_address_host = '.'.join(ip_address)[:-3].split('.')
ip_address_bin = '''{0:08b}{1:08b}{2:08b}{3:08b}'''.format(int(ip_address_host[0]),int(ip_address_host[1]), int(ip_address_host[2]), int(ip_address_host[3]))
ip_address_network = ip_address_bin[:mask.count('1')]+'0'*(32-mask.count('1')) 
print('Network:')
print('''{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}'''.format(int(ip_address_network[0:8],2), int(ip_address_network[8:16],2), int(ip_address_network[16:24],2), int(ip_address_network[24:],2)))
m10 = '''{0:<8}  {1:<8}  {2:<8}  {3:<8}'''.format(int(mask[0:8],2), int(mask[8:16],2), int(mask[16:24],2), int(mask[24:],2))
mask2 = '''{0:08b}  {1:08b}  {2:08b}  {3:08b}'''.format(int(mask[:8],2), int(mask[8:16],2), int(mask[16:24],2), int(mask[24:],2))
print('Mask:','\n'+'/'+ prefix_mask+'\n'+m10+'\n'+mask2)


