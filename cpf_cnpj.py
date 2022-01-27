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
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]

        return (
            "{}.{}.{}-{}".format(
            fatia_um,
            fatia_dois,
            fatia_tres,
            fatia_quatro
            )
        )

    def format_cnpj(self):
        """  Example: INPUT -> 43918354000122 | OUTPUT -> 43.918.354/0001-22  """
        fatia_um = self.cnpj[:2]
        fatia_dois = self.cnpj[2:5]
        fatia_tres = self.cnpj[5:8]
        fatia_quatro = self.cnpj[8:12]
        fatia_cinco = self.cnpj[12:]

        return (
            "{}.{}.{}/{}-{}".format(
            fatia_um,
            fatia_dois,
            fatia_tres,
            fatia_quatro,
            fatia_cinco
            )
        )
