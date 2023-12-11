def newReclamation(inputReclametion, ombudsman):
  if len(inputReclametion) > 10:
    ombudsman.append(inputReclametion)
    print(f"Reclamação cadastrada com sucesso. COD[{len(ombudsman)}]")
    pass
  else:
    print('Reclamação Invalida abaixo de 10 caracteres!')

def list_complaints(ombudsman):
  for i in range(len(ombudsman)):
      print(str(i + 1) + ') ' + (ombudsman[i]))
      
def update_complaints(id, ombudsman):
  if id < len(ombudsman):
    edit_complaints = input("Edite a reclamação: ") 
    ombudsman[id] = edit_complaints
    print('Reclamação atualizada com sucesso.')
  else:
    print('Código inexistente!')