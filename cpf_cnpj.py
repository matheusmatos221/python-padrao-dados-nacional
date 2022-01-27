from validate_docbr import CPF, CNPJ


class CpfCnpj:
    def __init__(self, documento, tipo_documento: str):
        self.tipo_documento = tipo_documento.lower()
        documento = str(documento)

        if tipo_documento == "cpf":
            if self.cpf_e_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF Inválido!")
        elif tipo_documento == "cnpj":
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Inválido!")
        else:
            raise ValueError("Tipo de documento inválido!")

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.format_cpf()
        elif self.tipo_documento == "cnpj":
            return self.format_cnpj()

    def cpf_e_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def cnpj_e_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)