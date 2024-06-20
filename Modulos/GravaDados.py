import builtins
import json

class GravaDados:
    usuariosCadast = {
    #  "chave"   :  "valor"
      "loginArm" : "cliente",
      "senhaArm" : "1234",
      "nomeUsuario" : "João do Santos",
    }
    def salvaDados(self):
        #open(nomeArquivo, modoAbertura) é uma função do python3 que lê e escreve arquivos
        #w - write - escrita
        # r - read - leitura
        # r+ - escreita/leitura
        with open("Lanchonete\\Modulos\\dados.txt", "w") as dados:
         # converter o vetor em json
          dadosJson= json.dumps(self.usuariosCadast)
        #open é para abrir o arquivo dados.txt em modo white
        # as quer dizer como
        #dados é apelido
          dados.write(dadosJson)
          dados.close()
        print("Dados Armazenados")

    def leDados(self):     
        # builtins que vai trazer os dados
        # para ler usamos a classe builtins do Python3
        with builtins.open("Lanchonete\\Modulos\\dados.txt", "r") as dados:
         print(f"no arquivo temos : \n{dados}")
         # for é um laço de repetição
         #para cada linha do arquivo de texto
         for linha in dados.readlines():
            print(linha.rstrip())
         
    def adicionaCadast(self, novoUsuario):
        #pegamos o json no arquivo de dados
        with builtins.open("Lanchonete\\Modulos\\dados.txt", "r") as dados:

       #adicionando um novo item ao nosso vetor     
    def exportaDados(self):

        print("")

dados = GravaDados()
dados.adicionaCadast()
dados.salvaDados()
dados.leDados()
    