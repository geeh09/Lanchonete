class Usuario: #nome de class precisa ser com letras maiúscula

  """Documentação da classe no Python
     Funções do usuário padrão da Lanchonete
  """
  # mémoria tipada ex.cadeia
  # propriedades da classe (variaveis)
  # cadeia - string - str - "texto 1234" "1234"
  loginInf: str= "cliente"
  senhaInf:str = "1234"
  #array - matriz ou vetor nomeado
  dadosUsuario = {
    #  "chave"   :  "valor"
      "loginArm" : "cliente",
      "senhaArm" : "1234",
      "nomeUsuario" : "João do Santos",
  }

  #transforma em um manual para o cliente e é só no python
  # Método e função é a mesma coisa
  # Método Construtor: executado ao instanciar a classe
  # self refere-se à instância da classe
  # é o self é obrigatorio de a função/método está dentro de uma classe
  def __init__( self ):

    self.logar() # chamando o método logar da classe

    # 'print( "Executado automaticamente" )'

  def logar(self):    # se eu não colocar nada na função, ele não precisa de ':'
    self.loginInf = input("Informe o login: ")
    self.senhaInf = input("informe a senha: ")
    #comparação - condicionais - Se - If
    #senão - else - falso
    if self.loginInf == self.dadosUsuario["loginArm"]:
    # 'if self.loginInf == "cliente":' # quando é para chmara global precisa colocar o self
     self.mostraMen("Bem vindo ao sistema ")
     self.exibirInf()
    else:
      print("falha ao conectar, tente novamente")

  def sair(self):
    print("Logout do sistema")

  # se o def estiver fora da classe não precisa colocar o self
  def exibirInf(self):
    print("Mostra os dados do usuário são: \nNome: \nLogin: ")
  def mostraMen(self, mensagem):
    """ Exibe as mensagens enviadas pelo parâmetro.
    """
    print(f"------------------------- \n |   {mensagem}   \n -------------------------")

# Uma classe convencional precisa ser Instanciada para que seus objetos possam ser usados.
# Instanciar uma classe é colocar uma cópia ( instância ) em uma variável ( objeto )
# operação de atribuição =
#atendente = Usuario() # objeto da classe, transformei a classe em algo útil

# logar no sistema
# disparar o método

 #objeto é o que ue vou usar
#usando um dos métodos
#atendente.sair()