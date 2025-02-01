# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = dict(
access = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
],

trunk = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
)
vlan_info = {
  'access': 'Введите номер VLAN: ',
    'trunk': 'Введите разрешенные VLANы: '
}
interface_mode = input("Введите режим работы интерфейса (access/trunk): ")
interface_type = input('Введите тип и номер интерфейса: ')
vlan_list = input(vlan_info[interface_mode])
print('interface {}'.format(interface_type))
print('\n'.join(access_template[interface_mode]).format(vlan_list))
