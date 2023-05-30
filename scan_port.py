
import nmap3
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("149.100.30.118")
print(results)
#imprimir en formato json

# And you would get your results in json