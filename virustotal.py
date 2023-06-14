from virus_total_apis import PublicApi
import  requests

API_KEY = "21843cd83304289ab21395cb7278608dee9e6d1751c57bfbbf518bc1f0c75326"

imput_url = input("Introduce la URL: ")


url = "https://www.virustotal.com/api/v3/domains/" + imput_url

headers = {
    "accept": "application/json",
    "x-apikey": "21843cd83304289ab21395cb7278608dee9e6d1751c57bfbbf518bc1f0c75326",
    "content-type": "application/x-www-form-urlencoded"
}

response = requests.get(url, headers=headers)
print(response.text)

#Selccionamos el campo que queremos mostrar
property = response.json()['data']['attributes']['last_analysis_stats']['malicious']

print(property)


