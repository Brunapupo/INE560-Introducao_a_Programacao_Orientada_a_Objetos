m = [
   ['laranja', 'manga', 'uva'],
   ['banana', 'morango', 'pera'],
   ['tomate', 'uva', 'manga']
   ]
maior_len = -1000000
maiores_elementos = []
for linha in m:
   for elemento in linha:
       if len(elemento) >= maior_len:
           maior_len = len(elemento)
           maiores_elementos.append(elemento)


print(maiores_elementos)

