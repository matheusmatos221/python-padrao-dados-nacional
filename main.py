from cpf_cnpj import CpfCnpj

# cpf_um = Cpf("23028441810")
# print(cpf_um)

exemplo_cnpj = 43918354000122
# cnpj = CNPJ()

# print(cnpj.validate(str(exemplo_cnpj)))


documento = CpfCnpj(exemplo_cnpj, 'cnpj')
print(documento)
