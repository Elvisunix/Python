#Comprobar si la direccion ip introducida esta en una lista negra

import pydnsbl
ip = str(input("ingrese una ip para comprobar: "))
ip_checker = pydnsbl.DNSBLIpChecker()    
blacklist = ip_checker.check(f'{ip}')
print(blacklist)