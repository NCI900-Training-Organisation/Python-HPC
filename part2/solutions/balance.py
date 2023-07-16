from threading import Thread
import time
import pretty_errors


class InsufficientFundsException(Exception):
    "Insufficient funds."
    pass

balance = 0.0

def deposit(amount, repeats):
    global balance
    for i in range(repeats):
        current = balance
        time.sleep(1/10000000.0)
        balance = current + amount
    return
   
    
def withdraw(amount, repeats):
    global balance
    for i in range(repeats):
        current = balance
        balance = current - amount
    return


if __name__ == "__main__":

    add_thread = Thread(target=deposit, args=(10,int(1e4)))
    sub_thread = Thread(target=withdraw, args=(10,int(1e4)))

    add_thread.start()
    sub_thread.start()
    
    add_thread.join()
    sub_thread.join()
    
    print(balance)