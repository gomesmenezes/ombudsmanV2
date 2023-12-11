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

    try:
      option = int(input('Escolha uma opção: '))
    except ValueError:
      print('Por favor, insira um número inteiro válido.')
      continue

    print('\n===================================')

    if option == 1:
      inputReclamation = input('Fale-nos sobre sua reclamação: ')
      newReclamation(inputReclamation, ombudsman)

    elif option == 2:
      if len(ombudsman) > 0:
        list_complaints(ombudsman)
      else:
        print('Sem reclamações!')

    elif option == 3:
      id = int(input("Digite o código da reclamação que deseja editar: "))
      update_complaints(id, ombudsman)

    elif option == 4:
      id = int(input("Digite o código da reclamação para mostrar os detalhes: "))
      detail_complaints(id, ombudsman)

    elif option == 5:
      id = int(input("Digite o código da reclamação para deletar: "))
      delete_complaints(id, ombudsman)
