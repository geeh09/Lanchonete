import builtins 
import json # Javascript Object Notation
class Teste:

    def carregaArq(self):

        with builtins.open("C:\\Users\\geovana.scsantos1\\Downloads\\Python\\Lanchonete\\texto.txt","r") as dados :
            for linha in dados:
                print( linha.rstrip())
                # rstrip é para quebrar a linha sem o \
    def carregaJson(self):
         with open("C:\\Users\\geovana.scsantos1\\Downloads\\Python\\Lanchonete\\usuarios.json","r") as dados :
             # recuperando os dados do json
             dadosJson = json.load (dados) # metodo para carregar esse itens
             print(f"Usuário: {dadosJson[0]["loginArm"]}\nSenha {dadosJson[0]["senhaArm"]}")

             
             

teste = Teste()
teste.carregaJson()