from library import Library

lib= Library()

while (True):
      print('\n\nChoose what you want to deal with:')
      print('c    :     Clients')
      print('o    :     Orders')
      print('b    :     Books')
      print('\n\n press q to quit\n')
      sel = input()
      if sel == 'q':
            break
      elif sel == 'c':
            while (True):
                  print('\n\nChoose what you want to do:\n')
                  print('a    :     add client')
                  print('c    :     check client info')
                  print('m    :     modify client')
                  print('r    :     remove client')
                  print('q    :     return to main page')
                  sel = input('\n')
                  if sel == 'q':
                        break
                  cpf = input('Client cpf:')
                  if sel == 'a':
                        name = input('Client name:')
                        email = input('Client email:')
                        lib.add_client(cpf, name, email)
                        print('Client added.')
                  elif sel == 'c':
                        lib.check_client(cpf)
                  elif sel == 'm':
                        attr = input('What information do you want to modify (name or email):')
                        value = input('New information value:')
                        lib.modify_client(cpf, attr, value)
                  elif sel == 'r':
                        lib.remove_client(cpf)
                        print('Client removed.')
                  else:
                        print('Unrecognized action')

      else: print('Unrecognized action')
