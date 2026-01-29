from jesuit_coajudor_bio import BriefBiography

def select_person():
    while True:
        print("Which Dossier would you like to access?")
        for i, instance in enumerate(BriefBiography.instances):
            print(f"{i + 1}. {instance.__class__.__name__} - {instance.name}")
        print("**********************************************")

        try:
            person = int(input("Enter one of the numbers: ")) - 1
            if 0 <= person < len(BriefBiography.instances):
                return BriefBiography.instances[person]
            else:
                print("Invalid Choice")
                print("**********************************************")
                return None
        except ValueError:
            print("You can only enter numbers \n\n**********************************************")


def select_information(instance):
    while True:
        methods = [m for m in dir(instance) if callable(getattr(instance, m)) and not m.startswith("__")]

        print(f"Chose which data to display for {instance.name}:")
        for i, method in enumerate(methods):
            print(f"{i + 1}. {method}")
        print("**********************************************")

        try:
            choice = int(input("Enter one of the numbers: ")) -1
            if 0 <= choice < len(methods):
                method = getattr(instance, methods[choice])
                method()
            else:
                print("Invalid Choice")
            print("**********************************************")
        except ValueError:
            print("You can only enter numbers")
            print("**********************************************")
            select_information(instance)
        cont2 = input(f"Continue browsing {instance.name}? [y/n] ")
        if cont2.lower() == "n":
            break

def main():
    while True:
        print("**********************************************")
        print("Welcome to Jesuit World Order Dossier Program!")
        print("**********************************************")
        instance = select_person()
        if instance:
            select_information(instance)
        cont = input("Continue? (y/n): ")
        if cont.lower() == "n":
            break


if __name__ == "__main__":
    main()