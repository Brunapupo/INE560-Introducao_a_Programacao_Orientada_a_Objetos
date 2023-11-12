class ContaBancaria:

  def __init__(self, saldo, senha):
      self.__saldo = saldo
      self.__senha = senha

  def saque(self, senha, valor_saque):
      if senha == self.senha:
          if valor_saque <= self.__saldo:
              self.__saldo -= valor_saque
      return self.__saldo

  def deposito(self, senha, valor_deposito):
      if senha == self.senha:
          if valor_deposito > 0:
              self.__saldo += valor_deposito
      return self.__saldo

  def verificacao_saldo(self, senha):
      if senha == self.senha:
          return self.__saldo

  def eh_saldo_negativo(self, senha):
      if senha == self.senha:
          return self.__saldo < 0

  def troca_senha(self, senha, nova_senha):
      if senha == self.__senha:
          self.senha = nova_senha
          return True
      return False
