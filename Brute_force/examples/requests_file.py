import requests
# import requests

sites = ['https://ya.ru', 'https://google.com', 'https://geekbrains.ru', 'https://skillbox.ru', 'https://https://discord.com/']

for site in sites:
    count = 0
    while count < 20:
        response = requests.get(site)
        print(f'Response {response} from the {site}')
        count += 1
