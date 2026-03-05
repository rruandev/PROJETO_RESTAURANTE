

class Avaliacao:
    

    def __init__(self, cliente, nota):
        
        self._cliente = cliente
        self._nota = nota

    @property
    def cliente(self):
        return self._cliente

    @property
    def nota(self):
        return self._nota

    def __str__(self):
        return f'{self._cliente} → nota {self._nota}'



class ItemCardapio:
    

    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    def __str__(self):
        return f'{self._nome} - R$ {self._preco:.2f}'


class Prato(ItemCardapio):
    

    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return f'  {self._nome} - R$ {self._preco:.2f}  [{self._descricao}]'


class Bebida(ItemCardapio):
    

    def __init__(self, nome, preco, alcoolica=False):
        super().__init__(nome, preco)
        self._alcoolica = alcoolica

    def __str__(self):
        tipo = ' alcoólica' if self._alcoolica else ' não alcoólica'
        return f'{tipo}  {self._nome} - R$ {self._preco:.2f}'



class Restaurante:
    

    
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False          
        self._avaliacoes = []        
        self._cardapio = []          

       
        Restaurante.restaurantes.append(self)

   

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def ativo(self):
        return self._ativo

    @property
    def media_avaliacoes(self):
       
        if not self._avaliacoes:
            return '-'
        total = sum(a.nota for a in self._avaliacoes)
        return round(total / len(self._avaliacoes), 1)

   

    def alternar_estado(self):
        
        self._ativo = not self._ativo

    def adicionar_avaliacao(self, avaliacao):
        
        self._avaliacoes.append(avaliacao)

    def adicionar_item_cardapio(self, item):
        
        self._cardapio.append(item)

    def exibir_cardapio(self):
       
        if not self._cardapio:
            print('  (cardápio vazio)')
            return
        for item in self._cardapio:
            print(f'  {item}')

    def __str__(self):
        status = ' Ativado' if self._ativo else ' Desativado'
        return (f'{self._nome:20} | {self._categoria:15} '
                f'| {status:14} | Média: {self.media_avaliacoes}')




def exibir_cabecalho():
    print('\n' + '='*50)
    print('         SISTEMA DE RESTAURANTES  ')
    print('='*50)


def exibir_menu():
    print('\n--- MENU PRINCIPAL ---')
    print('1_ Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Alternar estado do restaurante')
    print('4 - Adicionar avaliação')
    print('5 - Adicionar item ao cardápio')
    print('6 - Exibir cardápio de um restaurante')
    print('7 - Sair')
    print('----------------------')


def escolher_restaurante():
    """Mostra a lista numerada e pede que o usuário escolha um."""
    if not Restaurante.restaurantes:
        print('Nenhum restaurante cadastrado ainda.')
        return None

    print('\nRestaurantes disponíveis:')
    for i, r in enumerate(Restaurante.restaurantes, start=1):
        print(f'  {i} - {r.nome}')

    try:
        escolha = int(input('Digite o número do restaurante: '))
        if 1 <= escolha <= len(Restaurante.restaurantes):
            return Restaurante.restaurantes[escolha - 1]
        else:
            print('Número inválido.')
            return None
    except ValueError:
        print('Por favor, digite apenas números.')
        return None



def cadastrar_restaurante():
    print('\n--- Cadastrar Restaurante ---')
    nome = input('Nome do restaurante: ').strip()
    categoria = input('Categoria (ex: Italiana, Japonesa): ').strip()

    if nome and categoria:
        Restaurante(nome, categoria)
        print(f' "{nome}" cadastrado com sucesso (status: Desativado).')
    else:
        print('Nome e categoria não podem ser vazios.')




def listar_restaurantes():
    print('\n--- Lista de Restaurantes ---')
    if not Restaurante.restaurantes:
        print('Nenhum restaurante cadastrado ainda.')
        return

    print(f'{"Nome":20} | {"Categoria":15} | {"Status":14} | Média')
    print('-'*65)
    for r in Restaurante.restaurantes:
        print(r)



def alternar_estado():
    print('\n--- Alternar Estado ---')
    restaurante = escolher_restaurante()
    if restaurante:
        restaurante.alternar_estado()
        novo_estado = ' Ativado' if restaurante.ativo else ' Desativado'
        print(f'"{restaurante.nome}" agora está: {novo_estado}')




def adicionar_avaliacao():
    print('\n--- Adicionar Avaliação ---')
    restaurante = escolher_restaurante()
    if not restaurante:
        return

    cliente = input('Nome do cliente: ').strip()
    try:
        nota = float(input('Nota (0 a 10): '))
        if 0 <= nota <= 10:
            avaliacao = Avaliacao(cliente, nota)
            restaurante.adicionar_avaliacao(avaliacao)
            print(f' Avaliação de {cliente} adicionada!')
        else:
            print('A nota deve ser entre 0 e 10.')
    except ValueError:
        print('Nota inválida.')


 
def adicionar_item_cardapio():
    print('\n--- Adicionar Item ao Cardápio ---')
    restaurante = escolher_restaurante()
    if not restaurante:
        return

    print('Tipo do item:')
    print('  1 - Prato')
    print('  2 - Bebida')
    tipo = input('Escolha (1 ou 2): ').strip()

    nome = input('Nome do item: ').strip()
    try:
        preco = float(input('Preço (ex: 29.90): '))
    except ValueError:
        print('Preço inválido.')
        return

    if tipo == '1':
        descricao = input('Descrição / ingredientes: ').strip()
        item = Prato(nome, preco, descricao)
    elif tipo == '2':
        alcoolica_str = input('É alcoólica? (s/n): ').strip().lower()
        alcoolica = alcoolica_str == 's'
        item = Bebida(nome, preco, alcoolica)
    else:
        print('Tipo inválido.')
        return

    restaurante.adicionar_item_cardapio(item)
    print(f' "{nome}" adicionado ao cardápio de {restaurante.nome}!')



def exibir_cardapio():
    print('\n--- Cardápio ---')
    restaurante = escolher_restaurante()
    if restaurante:
        print(f'\nCardápio de: {restaurante.nome}')
        print('-'*40)
        restaurante.exibir_cardapio()



def main():
    exibir_cabecalho()

    opcoes = {
        '1': cadastrar_restaurante,
        '2': listar_restaurantes,
        '3': alternar_estado,
        '4': adicionar_avaliacao,
        '5': adicionar_item_cardapio,
        '6': exibir_cardapio,
    }

    while True:           
        exibir_menu()
        escolha = input('Escolha uma opção: ').strip()

        if escolha == '7':
            print('\nAté logo! ')
            break         

        funcao = opcoes.get(escolha)
        if funcao:
            funcao()     
        else:
            print('Opção inválida. Tente novamente.')



if __name__ == '__main__':
    main()