from src.bookstore import Bookstore

store = Bookstore()

while (True):
    print('\n\nChoose what you want to deal with:')
    print('b    :     Books')
    print('c    :     Clients')
    print('o    :     Orders')
    print('\n\n press q to quit\n')
    sel = input()
    if sel == 'q':
        break

    elif sel == 'b':
        while (True):
            print('\n\nChoose what you want to do:\n')
            print('a    :     add book')
            print('c    :     check books by author')
            print('m    :     modify book')
            print('r    :     remove book')
            print('q    :     return to main page')
            sel = input('\n')
            if sel == 'q':
                break
            if sel == 'a':
                title = input('Book title:')
                author_name = input('Author name:')
                genre = input('Genre:')
                edition = input('Edition:')
                publisher = input('Publisher:')
                sell_price = input('Sell price:')
                buy_price = input('Buy price:')
                store.add_book(title, author_name, genre, edition,
                               publisher, sell_price, buy_price)
                print('Book added.')
            elif sel == 'c':
                author_name = input('Author name:')
                store.check_author_books(author_name)
            elif sel == 'm':
                title = input('Book title:')
                attr = input('What information do you want to modify:')
                value = input('New information value:')
                store.modify_book(title, attr, value)
            elif sel == 'r':
                title = input('Book title:')
                store.remove_book(title)
                print('Book removed.')
            else:
                print('Unrecognized action')

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
                store.add_client(cpf, name, email)
                print('Client added.')
            elif sel == 'c':
                store.check_client(cpf)
            elif sel == 'm':
                attr = input(
                    'What information do you want to modify (name or email):')
                value = input('New information value:')
                store.modify_client(cpf, attr, value)
            elif sel == 'r':
                store.remove_client(cpf)
                print('Client removed.')
            else:
                print('Unrecognized action')

    elif sel == 'o':
        while (True):
            print('\n\nChoose what you want to do:\n')
            print('a    :     add order')
            print('c    :     check order info')
            print('m    :     modify order')
            print('r    :     remove order')
            print('q    :     return to main page')
            sel = input('\n')
            if sel == 'q':
                break
            client_name = input('Client name:')
            if sel == 'a':
                qtd = input('Quantity:')
                price = input('Price:')
                store.add_order(client_name, qtd, price)
                print('Order added.')
            elif sel == 'c':
                store.check_order(client_name)
            elif sel == 'm':
                attr = input('What information do you want to modify:')
                value = input('New information value:')
                store.modify_order(client_name, attr, value)
            elif sel == 'r':
                store.remove_order(client_name)
                print('Order removed.')
            else:
                print('Unrecognized action')

    else:
        print('Unrecognized action')
