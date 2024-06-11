class Transaction:
    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.type = type

class PersonalFinance:
    def __init__(self):
        self.transactions = []

    def add_transaction(self):
        description = input("Masukan Keterangan Transaksi: ")
        amount = float(input("masukan jumlah transaksi: "))
        type = input("Pilih pemasukan/pengeluaran: ")
        if type not in ["pemasukan", "peneluaran"]:
            print("pilih pemasukan/pengeluaran.")
            return
        transaction = Transaction(description, amount, type)
        self.transactions.append(transaction)
        print(f"Transaksi '{description}' Sukses")

    def display_transactions(self):
        if not self.transactions:
            print("tidak ada transaksi")
            return
        print("\nSemua Transaksi:")
        for transaction in self.transactions:
            print(f"{transaction.description}: {'+' if transaction.type == 'pemasukan' else '-'}${transaction.amount}")

    def calculate_total_income(self):
        total_income = sum(t.amount for t in self.transactions if t.type == "pemasukan")
        print(f"Total pemasukan: ${total_income}")
        return total_income

    def calculate_total_expense(self):
        total_expense = sum(t.amount for t in self.transactions if t.type == "pengeluaran")
        print(f"Total pengeluaran: ${total_expense}")
        return total_expense

    def calculate_balance(self):
        total_income = self.calculate_total_income()
        total_expense = self.calculate_total_expense()
        balance = total_income - total_expense
        print(f"Saldo: ${balance}")
        return balance

def main():
    finance = PersonalFinance()

    while True:
        print("\nPersonal Finance Manager")
        print("1. Tambahkan Transaksi")
        print("2. Display Transaksi")
        print("3. Hitung Pemasukan")
        print("4. Hitung Pengeluaran")
        print("5. Saldo Akhir")
        print("6. Exit")

        choice = input("pilih menu (1-6): ")

        if choice == '1':
            finance.add_transaction()
        elif choice == '2':
            finance.display_transactions()
        elif choice == '3':
            finance.calculate_total_income()
        elif choice == '4':
            finance.calculate_total_expense()
        elif choice == '5':
            finance.calculate_balance()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("menu tidak tersedia")

if __name__ == "__main__":
    main()
