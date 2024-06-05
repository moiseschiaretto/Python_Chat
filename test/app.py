import openpyxl
import pyautogui
from urllib.parse import quote
import webbrowser
from time import sleep
import datetime

# Acessa a página do Whatsapp Web
webbrowser.open('https://web.whatsapp.com/')
# Aguarda 20 segundos para a autenticação / login do WhatsApp por QRCode, na primeira vez que é logado
sleep(20)

# Ler a planilha e guardar as informações sobre candidato, telefone, data e hora de bate-papo (entrevista).
workbook = openpyxl.load_workbook('candidatos.xlsx')
dados_candidatos = workbook['Planilha1']

# Realiza a leitura dos dados dos candidatos da planilha a partir da segunda linha >> (min_row=2)
for linha in dados_candidatos.iter_rows(min_row=2):
    # candidato, telefone, data e hora
    candidato = linha[0].value
    print(candidato)
    # telefone do candidato
    telefone = linha[1].value
    print(telefone)
    # data do bate-papo (entrevista)
    data = linha[2].value
    # Realiza a conversação e a formatação da data dd/mm/aaaa
    data_correspondente = datetime.datetime(1899, 12, 30) + datetime.timedelta(days=data)
    data_formatada = data_correspondente.strftime('%d/%m/%Y')
    print(data_formatada)
    # hora do bate-papo (entrevista)
    hora = linha[3].value
    print(hora)
    # Formatação da mensagem que será enviada via Whatsapp
    mensagem = f'TESTE MOISÉS .... Olá {candidato}. Me chamo YYY aqui da empresa XYZ TI, você se candidatou para atuar na vaga de ZZZ, podemos bater um papo na data {data_formatada}, na hora {hora}? Fico no aguardo!'
    print(mensagem)
    # Criar os links personalizados do whatsapp e enviar mensagens para cada candidato
    try:
        # Filtra no WhatsApp o "telefone" e "insere a mensagem"
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(15)
        # Envia a mensagem formatada, abre o console do navegador/browser e envia mensagem
        pyautogui.hotkey('ctrl', 'shift', 'i')
        sleep(5)
        script = """
        XYZ TI
        (41) 9999-99999
        """
        pyautogui.write(script)
        sleep(5)
        # Fecha as guias de cada telefone/candidato
        pyautogui.hotkey('alt', 'F4')
        sleep(5)
        # Confirma a saída da tela atual
        pyautogui.press("enter")
    except:
        # Caso houver algum erro será salvo um log no arquivo "log_erros.csv" com o candidato (nome) e telefone
        # Log com os dados do candidato que "não" foi enviada a mensagem
        print(f'Não foi possível enviar mensagem para {candidato}')
        with open('log_erros.csv', 'a+') as history:
            linha = str(candidato) + ';' + str(telefone) + ';\n'
            history.write(linha)
            history.close()
