## Projeto
O projeto é uma iniciativa do uso de criptografia com python utilizando a cifra de hill. A Cifra de Hill é um tipo de cifra de substituição baseado em álgebra linear usado para codificação de mensagens.

## Requisitos do projeto

Para rodar esta aplicação, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python + pip](https://www.python.org/downloads/) e [virtualenv](https://virtualenv.pypa.io/en/latest/).

## Execute o projeto

Execute os comandos abaixo:
```bash
# Clone este repositório
$ git clone https://github.com/Daniel-Alencar/Cifra-de-Hill

# Acesse a pasta do projeto no terminal/cmd
$ cd Cifra-de-Hill

# Crie um ambiente virtual para instalar as dependências
$ virtualenv myENV

# Entre no ambiente virtual
$ source myENV/bin/activate

# Instale as dependências
$ pip3 install -r requirements.txt

# Execute a aplicação
$ python3 hill_cipher.py
```

## Criptografar mensagem

- Se quiser, mude o valor da chave (variável key) no arquivo config.py
  - Deve ser uma matriz quadrada de ordem N
- Altere o arquivo 'textoclaro.txt' com a mensagem que você quiser criptografar
  - A quantidade de letras do texto deve ser múltipla de N
- Execute o seguinte comando:

```
python3 "hill_cipher.py" -encrypt textoclaro.txt -output textocifrado.txt
```

## Descriptografar mensagem

- Mude o valor da chave (variável key) no arquivo config.py
  - Deve ser a mesma chave que foi usada para criptografar o texto
- Altere o arquivo 'textocifrado.txt' com a mensagem criptografada
- Execute o seguinte comando:

```
python3 "hill_cipher.py" -decrypt textocifrado.txt -output textoclaro.txt
```
