def newReclamation(inputReclametion, ombudsman):
  if len(inputReclametion) > 5:
    ombudsman.append(inputReclametion)
    print(f"Reclamação cadastrada com sucesso. COD[{len(ombudsman)}]")
    pass
  else:
    print('Reclamação Invalida abaixo de 5 caracteres!')

def list_complaints(ombudsman):
  print('Listando...')
  for i in range(len(ombudsman)):
      print(str(i + 1) + ') ' + (ombudsman[i]))
      
def update_complaints(id, ombudsman):
    if id <= 0 or id > len(ombudsman):
        print('Código inexistente!')
    else:
        edit_complaints = input("Edite a reclamação: ")
        ombudsman[id - 1] = edit_complaints
        print('Reclamação atualizada com sucesso.')

def detail_complaints(id, ombudsman):
  if id <= 0 or id > len(ombudsman):
    print('Código inexistente!')
  else:
    detailComplaint = ombudsman[id - 1]
    print(f'Detalhes: {detailComplaint}')

def delete_complaints(id, ombudsman):
  if id <= 0 or id > len(ombudsman):
    print('Código inexistente!')
  else:
    del ombudsman[id - 1]
    print(f'Reclamação com COD[{id}] removida com succeso!')