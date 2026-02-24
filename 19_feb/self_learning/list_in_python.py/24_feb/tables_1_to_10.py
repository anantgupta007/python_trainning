# tables_1_to_10.py

def print_tables():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i, "x", j, "=", i * j)
        print()

print_tables()