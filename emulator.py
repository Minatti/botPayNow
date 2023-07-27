import requests as r
import time

url = "https://cloud.bluestacks.com/api/getdownloadnow?platform=win&win_version=10&mac_version=&client_uuid=c7672ef4-a5c2-44a7-94fb-37e0548325e1&app_pkg=&platform_cloud=%257B%2522description%2522%253A%2522Chrome%2520114.0.0.0%2520on%2520Windows%252010%252064-bit%2522%252C%2522layout%2522%253A%2522Blink%2522%252C%2522manufacturer%2522%253Anull%252C%2522name%2522%253A%2522Chrome%2522%252C%2522prerelease%2522%253Anull%252C%2522product%2522%253Anull%252C%2522ua%2522%253A%2522Mozilla%252F5.0%2520(Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F114.0.0.0%2520Safari%252F537.36%2522%252C%2522version%2522%253A%2522114.0.0.0%2522%252C%2522os%2522%253A%257B%2522architecture%2522%253A64%252C%2522family%2522%253A%2522Windows%2522%252C%2522version%2522%253A%252210%2522%257D%257D&preferred_lang=pt-br&utm_source=&utm_medium=&gaCookie=GA1.2.517197434.1690410795&gclid=&clickid=&msclkid=&affiliateId=&offerId=&transaction_id=&aff_sub=&first_landing_page=https%253A%252F%252Fwww.bluestacks.com%252Fpt-br%252Findex.html&referrer=&download_page_referrer=&utm_campaign=homepage-dl-button-pt-br&user_id=&exit_utm_campaign=bsx-install-button-home-pt-br&incompatible=false&bluestacks_version=bs5&device_memory=8&device_cpu_cores=4"

def download_emulator(url):
    download='C:/users/workcarminatti/Downloads/BlueStacksInstaller.exe'
    response = r.get(url, allow_redirects=True)
    with open(download,'wb') as file:
        file.write(response.content)
    return True


def install_emulator():
    if(download_emulator(url)):
        print("Bluestacks foi instalado com sucesso")
        time.sleep(3)
    else:
        print("Favor, verificar qual o motivo de não ter instalado")
