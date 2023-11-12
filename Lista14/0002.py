class CarroSimplificado:

   def __init__(self, capacidade_tanque, qtd_atual_tanque, consumo_media_combustivel):
       self.__capacidade_tanque = capacidade_tanque
       self.__qtd_atual_tanque = qtd_atual_tanque
       self.__consumo_media_combustivel = consumo_media_combustivel

   def abastece(self, gasolina):
       if (gasolina < self.__qtd_atual_tanque < self.__capacidade_tanque):
           self.__qtd_atual_tanque += gasolina
           return True, self.__qtd_atual_tanque
       else:
           return False

   def informaGasolina (self):
       return self.__qtd_atual_tanque

   def consumeGasolina(self, km):
       if self.__qtd_atual_tanque > 0:
           consumo_gasolina = (float(km) / self.__consumo_media_combustivel)
           self.__qtd_atual_tanque -= consumo_gasolina

   def estaNoReserva(self):
       reserva = (self.__capacidade_tanque * 10 / 100)
       if self.__qtd_atual_tanque <= reserva:
           return True
       else:
           return False