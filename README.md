## Projeto "Python_Chat"

- Autor Moisés Ademir Chiaretto
  
- Descrição das explicações de cada item da 'estrutura do projeto "Python_Chat" desenvolvido'.

**Objetivo:**

- Enviar uma Massa de Dados de Mensagens personalizadas, via Whatsapp Web, para os "nomes" e "telefones" informados.


<br>

|Python           |IDE PyCharm              |Whatsapp Web          |HTML / CSS / JS  	|XPATH	  	|
|-----------------|-------------------------|----------------------|------------------|-----------|
| ![04_Python](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/85379dcd-9c54-435b-806c-3a32f9c3379a) | <img width="194" alt="PyCharm" src="https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/3b559cdd-52a3-4d99-8c3a-bad81aaa7731"> | <img width="258" alt="00_Whatsapp_Web" src="https://github.com/moiseschiaretto/Python_Chat/assets/84775466/e073a334-293b-4d27-a759-024d32a78c27"> | <img width="236" alt="00_HTML_CSS_JS" src="https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/950d0762-c8b2-4d30-9d6e-af34006b3ac9"> | <img width="142" alt="00_XPATH" src="https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/c89d3bdd-4d14-4f43-ac2c-93d7382cafdc"> |

<br>

## Estrutura do Projeto "Python_Chat"
<br>

<img width="205" alt="01_Estrutura_Projeto" src="https://github.com/moiseschiaretto/Python_Chat/assets/84775466/a882a52a-2aee-402e-b871-b0147830d968">



## Sobre o "Projeto chat", envio de mensagens via Whatsapp Web
<br>

**1.** Este é um dos métodos de enviar mensagem no WhatsApp em massa, ou seja, para várias pessoas / candidatos.

Não é a forma mais indicada porque, neste momento de envio de mensagens NÃO É ACONSELHÁVEL UTILIZAR O NOTEBOOK / A MÁQUINA, senão o sistema se perde!

**2** O melhor método é através da API do WhatsApp

Analisar a documentação da API do WhatsApp Web e elaborar um outro método de envio de mensagens em massa.


****


## Importante

**- Constar na mesma pasta do Projento APP os seguintes arquivos:**

- **app.py**, contém o código em Python.

- **candidatos.xlsx**, será lido com as informações do candidato [candidato/nome, telefone, data, hora]

- **log_erros.csv**, arquivo de log para armazenar o candidato/nome e telefone que não foi enviada a mensagem em caso de erro.


## Arquivo 'requeriments.txt'

Constam todas as 'bibliotecas' do projeto para serem instaladas.

- A biblioteca openpyxl em Python é usada para manipular com arquivos Excel (.xlsx).

- A biblioteca PyAutoGUI em Python permite automatizar interações com o mouse e o teclado, facilitando tarefas de automação de GUI.

```

openpyxl>==3.1.3

pyautogui>==0.9.54

```
<br>

### Execução enviando as mensagens via Whatsapp Web
<br>

<img width="680" alt="02_MSG_Enviada_Chat_Whatsapp_Web" src="https://github.com/moiseschiaretto/Python_Chat/assets/84775466/cdf43452-0ffc-4c79-9d8e-20ff31e5999c">


<br>



