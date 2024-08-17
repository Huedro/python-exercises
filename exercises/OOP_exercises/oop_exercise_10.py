# Write a Python program to create a class representing a bank
# Include methods for managing customer accounts and transactions


class BankAccount:
    def __init__(self, user, balance):
        self.user = user
        self.balance = balance

    def __str__(self):
        return str((self.user, self.balance))


class Bank:
    def __init__(self):
        self.customer_list = {}

    def __str__(self):
        return str(self.customer_list)

    def add_new_customer(self, id, user, balance):
        self.customer_list.update({id: BankAccount(user, balance)})
        # self.customer_list.append(BankAccount(id, user, balance))

    def make_transaction(self, sender_id, recipient_id, value):
        if sender_id in self.customer_list and recipient_id in self.customer_list:
            self.customer_list[sender_id].balance -= value
            self.customer_list[recipient_id].balance += value
            print("Transaction Done!")
            print(self.customer_list.get(sender_id))
            print(self.customer_list.get(recipient_id))

    def show_customer_list(self):
        for id in self.customer_list:
            print(id, ":", self.customer_list.get(id))

    def show_customer_detail(self, id):
        print(id, ":", self.customer_list.get(id))


bank1 = Bank()
bank1.add_new_customer(1, "Pedro Augusto", 200.00)
bank1.add_new_customer(2, "Lucas Augusto", 640.00)
bank1.add_new_customer(3, "Bernardo Reis", 2300.00)
bank1.add_new_customer(4, "Fabricio Ferretti", 30.00)
bank1.show_customer_list()

print()
bank1.show_customer_detail(3)

# bank1.make_transaction(1, 2, 50.00)
