import json
import requests

with open('./files/base_tdspy.json') as file:
    jsonFile = json.load(file)

def remove_com(enumerated_url):
    index, url = enumerated_url
    url_sem_com = url.split(".")[0]
    return f"{index + 1} - {url_sem_com.capitalize()}"

# code
#   - variables
is_valid = False
insert_rm = None
option_select = None

#   - get RM
while not is_valid:
    insert_rm = input('\nDigite os números do seu RM (Ex.:123456): ')

    if insert_rm in jsonFile:
        is_valid = True
    else:
        print("\nPor favor, digite um RM valido.\n")

number_loop = 1
while number_loop == 1:

    #   - getting options and turning options into string
    is_valid = False
    urls = jsonFile[insert_rm]
    result_array = list(map(remove_com, enumerate(urls)))
    result_string = "\n".join(result_array)

    #   - getting selected option
    while not is_valid:
        print("\nEssas são suas opções:")
        print(result_string)
        option_select = int(input("Escolha uma delas usando o número na frente delas: ")) - 1

        if option_select >= 0 and option_select <= len(urls):
            is_valid = True
        else:
            print("\nPor favor, escolha uma opção válida.")

    #   - getting site
    print("\nPegando seus dados na nuvem...")
    headers = {'User-Agent': 'Chrome/39.0.2171.95'}
    response = requests.get(f'https://www.{urls[option_select]}', headers=headers)
    print("Ok, tudo certo, dados pegos com sucesso!\nSalvando os dados...")
    file_html = response.content


    #   - saving file
    name_html = urls[option_select].split(".")[0]
    with open('./files/' + name_html + '.html', 'w') as file_site:
        file_site.write(str(file_html))
    print("Dados salvos!\n")
    number_loop = int(input("Digite 1 para salvar outra HTML\nDigite 2 para sair do programa: "))
    break