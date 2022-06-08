import requests

from acesso_cep import BuscaEndereco
cep = "27923160"
objeto_cep = BuscaEndereco(cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#rint(type(r.text))

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)
