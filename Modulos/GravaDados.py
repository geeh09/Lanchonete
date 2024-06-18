import builtins

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
        with open("C:\\Users\\geovana.scsantos1\\Downloads\\Python\\Lanchonete\\Modulos\\dados.txt", "w") as dados:
        #open é para abrir o arquivo dados.txt em modo white
        # as quer dizer como
        #dados é apelido
         dados.write("self.usuariosCadast")
         dados.close()
        print("Dados Armazenados")

    def leDados(self):     
        # builtins que vai trazer os dados
        # para ler usamos a classe builtins do Python3
        with builtins.open("C:\\Users\\geovana.scsantos1\\Downloads\\Python\\Lanchonete\\Modulos\\dados.txt", "r") as dados:
         print(f"no arquivo temos : \n{dados}")
         # for é um laço de repetição
         #para cada linha do arquivo de texto
         for linha in dados.readlines():
            print(linha.rstrip())
         
         
    def exportaDados(self):

        print("")

dados = GravaDados()
dados.salvaDados()
dados.leDados()
    