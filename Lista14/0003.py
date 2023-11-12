class Pessoa:

    def __init__(self, nome='', rg='', idade=0):
        self.nome = nome
        self.rg = rg
        self.idade = idade

    def obterNome(self):
        return self.nome

    def obterIdade(self):
        return self.idade

    def atualizarIdade(self, novaIdade):
        if novaIdade > 0:
            self.idade = novaIdade

    def obterRG(self):
        return self.rg


class CadastroPessoa:

    def __init__(self):
        self.cadastro_pessoas = {}

    def adicionaPessoa(self, nome, rg, idade):
        if rg not in self.cadastro_pessoas:
            pessoa = Pessoa(nome, rg, idade)
            self.cadastro_pessoas[rg] = pessoa

    def listaPessoas(self):
        return self.cadastro_pessoas.values()

    def nomeIdade(self, rg):
        if rg in self.cadastro_pessoas:
            pessoa = self.cadastro_pessoas[rg]
            return pessoa.obterNome(), pessoa.obterIdade()

    def removeCadastro(self, rg):
        if rg in self.cadastro_pessoas:
            del self.cadastro_pessoas[rg]
            return True
        else:
            return False

    def maiorIdade(self):
        pessoa_maior_idade = None
        maior_idade = 0
        for pessoa in self.cadastro_pessoas.values():
            if pessoa.obterIdade() > maior_idade:
                maior_idade = pessoa.obterIdade()
                pessoa_maior_idade = pessoa
        return pessoa_maior_idade


if __name__ == '__main__':
    cadastro = CadastroPessoa()
    cadastro.adicionaPessoa("Carlos", "45415515", 88)
    cadastro.adicionaPessoa("Bruna", "44235901826", 14)

    print(cadastro.removeCadastro('44235901826'))

    print(cadastro.nomeIdade('45415515'))

    for pessoa in cadastro.listaPessoas():
        print(f"{pessoa.obterRG()}, {pessoa.obterNome()}, {pessoa.obterIdade()}")

    pessoa_mais_velha = cadastro.maiorIdade()
    if pessoa_mais_velha:
        print(f"Pessoa mais velha: {pessoa_mais_velha.obterNome()}, Idade: {pessoa_mais_velha.obterIdade()}")
