




# Observações:
# 1) Este é um dos métodos de enviar mensagem no WhatsApp em massa, ou seja, para várias pessoas/candidatos
# Não é a forma mais indicada porque, neste momento de envio de mensagens NÃO É ACONSELHÁVEL UTILIZAR O NOTEBOOK/A MÁQUINA
# Senão o sistema se perde!
# 2) O melhor método é através da API do WhatsApp
# Estarei estudando a documentação da API do WhatsApp e elaborando este outro método de envio de mensagens em massa
###############################################################################################################################
# Importante:
# Constar na mesma pasta do Projento APP os seguintes arquivos:
# app.py >> contém este código em Python
# candidatos.xlsx >> que será lido com as informações do candidato [candidato/nome, telefone, data, hora]
# log_erros.csv >> arquivo de log para armazenar o candidato/nome e telefone que não foi enviada a mensagem em caso de erro
# seta.png >> neste código não será utilizada, porém é outra forma de clicar no botão da SETA / ENVIAR mensagem no WhatsApp
# #############################################################################################################################
# IDE pode ser PyCharm ou VSCode
# É necessário instalar as seguintes biliotecas neste Projeto App do Python:
# openpyxl
# pyautogui
