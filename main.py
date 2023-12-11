from ombudsman import *

ombudsman = [ ]
option = 0

while option != 6:
    print('\n=========OUVIDORIA=========')
    print('1) Inserir nova reclamação.')
    print('2) Listar reclamações existentes.')
    print('3) Editar reclamação.')
    print('4) Mostrar detalhes de uma reclamação.')
    print('5) Deletar reclamação.')
    print('6) Sair') 

    option = int(input('Escolha uma opção: '))
    print('\n===================================')

    if option == 1:
      inputReclamation = input('Fale-nos sobre sua reclamação: ')
      newReclamation(inputReclamation, ombudsman)

    elif option == 2:
      list_complaints(ombudsman)

    elif option == 3:
      id = int(input("Digite o código da reclamação que deseja editar: "))
      id + 1
      update_complaints(id, ombudsman)

