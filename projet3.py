from getpass import getpass
from utils.user_manager import*
from utils.hash_manager import generate_hash, store_key
from utils.encryptor import encrypt_data
from utils.decryptor import decrypt_cipher
from utils.file_manager import encrypt_file, decrypt_file, show_data_file

def affichage(titre, options):
    """Affiche un menu générique"""
    print(f"\n{' ' * 15}{'*' * 25} {title} {'*' * 27}")
    print("\n".join(f"\t{k}. {v}" for k, v in options.items()))
    return int(input("\nVotre choix : "))

def main():
    while True:
        choix = affichage("gestionnaire de mot de passe", {
            1: "Nouvel utilisateur",
            2: "Utilisateur existant",
            3: "Quitter"
        })

        if choix == 1:
            utilisateur, mot_de_passe = nouvel_utilisateur()
            stocker_cle(utilisateur, generate_hash(utilisateur, mot_de_passe))
            print("bien enregistré!")

        elif choix == 2:
            utilisateur, mot_de_passe = input("Nom : "), getpass("Mot de passe : ")
            if not check_user(utilisateur, mot_de_passe):
                print("Authentification échouée")
                continue

            while True:
                action = show_menu("MENU UTILISATEUR", {
                    1: "Crypter des mots de passe",
                    2: "Visualiser données",
                    3: "Décrypter mot de passe",
                    4: "Retour"
                })

                if action == 4: break
                
                decrypt_file(utilisateur, mot_de_passe)
                if action == 1:
                    encrypt_data(utilisateur, mot_de_passe)
                elif action == 2:
                    show_data_file(utlisateur)
                elif action == 3:
                    if pwd := decrypt_cipher(utilisateur, mot_de_pass):
                        print(f"{pwd} copié dans le presse-papiers!")
                encrypt_file(utilisateur, mot_de_pass)

        elif choix == 3:
            print("Au revoir!")
            break

if __name__ == '__main__':
    main()
