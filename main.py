from cpf_cnpj import Documento

# cpf_um = Cpf("23028441810")
# print(cpf_um)
exemplo_cpf = 32007832062
exemplo_cnpj = 43918354000122
# cnpj = CNPJ()

# print(cnpj.validate(str(exemplo_cnpj)))


documento = Documento.cria_documento(str(exemplo_cpf))
print(documento)
