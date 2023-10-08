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