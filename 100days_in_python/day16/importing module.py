from prettytable import PrettyTable
#object=vlass()
table = PrettyTable()
#calling an method
table.add_column("pockemon", ["pikachu", "squirtle", "charmender"])
table.add_column("type", ["electric", "water", "fire"])
#changing the attributr / variable
table.align="l"
print(table)
