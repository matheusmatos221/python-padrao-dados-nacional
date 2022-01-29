import requests
from acesso_cep import BuscaEndereco

cep = 13186235
obj_cep = BuscaEndereco(cep)

bairro, cidade, uf = obj_cep.acessa_via_cep()
print(f'{bairro}, {cidade}-{uf}')
