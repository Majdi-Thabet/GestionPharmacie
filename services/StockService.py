import models.Pharmacie

    
class StockService:
    c =[]
    def main():
        while True:
            print("1. INSERT")
            print("2. DISPLAY ")
            print("3. SEARCH")
            print("4. DELETE")
            print("5. UPDATE")
            print("0. EXIT")

            # Controle saisie avec Try Catch
            try:
                ch = int(input("Enter Your Choice: "))

                if ch == 0:
                    break  # Sortie de la boucle si l'utilisateur choisit 0

                # Ajoutez ici la logique pour chaque choix (1 à 5)
                if ch == 1:
                    # Logique pour l'option INSERT
                    print("Enter Empno: ", end="")
                    #lire l'entrée de l'utilisateur
                    eno = int(input())
                    print("Enter EmpName: ", end="")
                    ename = input()
                    print("Enter Salary: ", end ="")
                    salary = int(input())
                    CRUDDemo.c.append(Employee(eno, ename, salary))
                    
                    # Je veux afficher un msg après l'insertion
                    # print('--------------------------')

                elif ch == 2:
                    # Logique pour l'option DISPLAY
                    pass
                elif ch == 3:
                    # Logique pour l'option SEARCH
                    pass
                elif ch == 4:
                    # Logique pour l'option DELETE
                    pass
                elif ch == 5:
                    # Logique pour l'option UPDATE
                    pass
                else:
                    print("Invalid choice. Please enter a number between 0 and 5.")

            except ValueError:
                print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    CRUDDemo.main()


