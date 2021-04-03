from models import Pessoas

# Inclui dados na tabela pessoas
def insere_pessoas():
    pessoa = Pessoas(nome='Galleani', idade=35)
    print(pessoa)
    pessoa.save()

# Consulta dados na table pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)

# Altera dados na table pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.idade = 21
    pessoa.save()

# Exclui dados na table pessoa
def exlui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    consulta_pessoas()
    exlui_pessoa()
    altera_pessoa()
    consulta_pessoas()