# quiz_simples
Um projeto que eu fiz para praticar conceitos aprendidos em aula. Nele eu uso conceitos como a criação de funções, o uso da função main no Python, loops, listas, condições, variáveis locais e globais, erros e exceções.

Para executar o quiz, clique no botão verde "Code" e depois em Download Zip, extraia o arquivo e dentro da pasta "quiz_simples-master" clique duas vezes no arquivo
"quiz_simples.py".
Se quiser executar pelo cmd faça o download do zip, extraia em alguma pasta e no cmd vá até o diretório da pasta com o comando "cd", ex se a pasta
tiver na área de trabalho: digite "cd Desktop", depois digite: "cd quiz_simples-master" e para executar o programa digite: python quiz_simples.py

Uso: Ao iniciar o programa, o usuário será perguntado se quer jogar um quiz, se a resposta for "sim" o programa irá continuar, se for "não" o programa será encerrado.
Se o usuário digitar uma resposta inválida ex: um número ou caracteres aleatórios que não sejam s ou n, o programa irá exibir um aviso e só dará continuidade se o input
for válido. Após o usuário digitar "sim", o programa irá fazer as perguntas e a cada resposta certa a contagem de resposta irá aumentar, se a resposta for invalida, ou seja,
não for um número inteiro, o usuário receberá um aviso. Ao responder todas as perguntas, o usuário poderá ver quantas perguntas acertou.

Dentro do código é possível adicionar mais perguntas usando a função ```perguntas(pergunta, resposta)``` que tem como argumentos: a própria pergunta e a resposta.
