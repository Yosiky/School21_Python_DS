import sys

def func_call_center():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
        'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    # participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
    #         'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return list(set(clients) - set(recipients))

def func_potential_clients():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
        'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
            'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    # recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return list(set(participants) - set(clients))

def func_loyalty_program():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
        'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
            'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return list((set(clients) | set(recipients)) - set(participants))

if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            match sys.argv[1]:
                case 'call_center':
                    print(func_call_center())
                case 'potential_clients':
                    print(func_potential_clients())
                case 'loyalty_program':
                    print(func_loyalty_program())
                case _:
                    raise Exception("No valid argument")
        else:
            print('No valid input value')
    except Exception as answer:
        print(answer)
        
