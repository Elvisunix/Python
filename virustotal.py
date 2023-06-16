from virus_total_apis import PublicApi
import  requests
import json

API_KEY = "21843cd83304289ab21395cb7278608dee9e6d1751c57bfbbf518bc1f0c75326"

imput_url = input("Introduce la URL: ")


url = "https://www.virustotal.com/api/v3/domains/" + imput_url

headers = {
    "accept": "application/json",
    "x-apikey": "21843cd83304289ab21395cb7278608dee9e6d1751c57bfbbf518bc1f0c75326",
    "content-type": "application/x-www-form-urlencoded"
}

response = requests.get(url, headers=headers)

#mostrar el json completo ordenado
print(json.dumps(response.json(), indent=4, sort_keys=True))

if response.status_code == 200:
    data = response.json()
    bitdefender_result = data["data"]["attributes"]["categories"]["BitDefender"]
    malicious_result = data["data"]["attributes"]["last_analysis_stats"]["malicious"]
    print("Resultado de Bitdefender:", bitdefender_result +  " - " + "Malicious:", malicious_result)
    print("RESULTADOS DE LOS SERVIDORES ESCANEADOS:")
    for i in data["data"]["attributes"]["last_analysis_results"]:
        print(i, data["data"]["attributes"]["last_analysis_results"][i]["result"])
else:
    print("Error en la solicitud:", response.status_code)