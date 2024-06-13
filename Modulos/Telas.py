#importando a classe Time do próprio Python
import time
import os 

class Telas:
    
    def entradaSistema(self):
        print( f"+-------------------------------------------------------+" )
        print( f"|                                                       |" )
        print( f"|                ** Seja Bem Vindo ao Sistema **        |" )
        print( f"|                                                       |" )
        print( f"+-------------------------------------------------------+" )

        self.esperaLimpa()
    
    def esperaLimpa(self, tempo = 3):
         time.sleep(tempo)
       
        # esperar X segundos

        #limpar a tela
         self.limpaConsole()
    
    def saidaSistema(self):
        print( f"+-------------------------------------------------------+" )
        print( f"|                                                       |" )
        print( f"|                ** Obrigado por usar o Sistema **      |" )
        print( f"|                                                       |" )
        print( f"+-------------------------------------------------------+" )
    
    # mensagem é um parâmetro   
    def mensagensSistema(self, mensagem):
        print( f"+-------------------------------------------------------+" )
        print( f"|                                                       |" )
        print( f"        ** {mensagem} **      " )
        print( f"|                                                       |" )
        print( f"+-------------------------------------------------------+" )
 
    def limpaConsole(self):
        if os.name == "nt": # quer dizer que é windows nt - Linux posix
            os.system("cls") # os é para acessar o sistema operacional
        else:
            os.system("clear")

        # if os.name == "nt":
        #     os.system("cls")
        # elif os.name == "darwin":
        #     os.system("clear")
        # else:
        #     os.system("clear")
        
        # tipoSistema = os.name
        # switch(tipoSistema): # switch = escolha
        #     case "nt":
        #         os.system("cls")
        #         breck:
    


#Objeto       
#'tela' = Telas()'

# Objeto chamando o método
# 'tela.entradaSistema()'

#'tela.saidaSistema()'
