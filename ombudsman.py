def newReclamation(inputReclametion, ombudsman, author):
  inputAuthor = input('Autor: ')
  if len(inputReclametion) > 5 or len(inputAuthor) > 5:
    ombudsman.append(inputReclametion)
    if len(inputAuthor) > 3:
      author.append(inputAuthor)
      print(f"Reclamação cadastrada com sucesso. COD[{len(ombudsman)}]")
    else:
      print('Autor inválido (menos de 5 caracteres)!')
  else:
    print('Reclamação Invalida abaixo de 5 caracteres!')

def list_complaints(ombudsman, author):
  if len(ombudsman) > 0:
    print('Listando...')
    for i in range(len(ombudsman)):
      print(str(i + 1) + ') ' + (ombudsman[i]))
      print('Autor: ' + (author[i]))
      print('==============================')
  else:
    print('Sem reclamações!')

def update_complaints(id, ombudsman, author):
    if id <= 0 or id > len(ombudsman):
        print('Código inexistente!')
    else:
        edit_complaints = input("Edite a reclamação: ")
        ombudsman[id - 1] = edit_complaints
        yesOrNo = input('Você quer mudar o autor? (SIM (Y) NÃO (N): ')
        if yesOrNo.lower() == 'y':
          update_author = input('Atualize o autor: ')
          author[id - 1] = update_author
        print('Reclamação atualizada com sucesso.')

def detail_complaints(id, ombudsman, author):
    if id <= 0 or id > len(ombudsman):
        print('Código inexistente!')
    else:
        detailComplaint = ombudsman[id - 1]
        author_detail = author[id - 1]
        print(f'Detalhes: {detailComplaint}, Autor: {author_detail}')


def delete_complaints(id, ombudsman, author):
  if id <= 0 or id > len(ombudsman):
    print('Código inexistente!')
  else:
    del author[id - 1]
    del ombudsman[id - 1]
    print(f'Reclamação com COD[{id}] removida com succeso!')