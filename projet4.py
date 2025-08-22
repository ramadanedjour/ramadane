import json
import random
def charger_questions(fichier="questions.json"):
    
  [
    {
        "question": "Quelle est la capitale du tchad?",
        "options": ["n'djamena", "amdjarass", "moundou", "abeche"],
        "reponse": "n'djamena"
    },
    {
        "question": "Combien de oceans y a-t-il?",
        "options": ["0", "1", "2", "3"],
        "reponse": "3"
    }
    with open(fichier) as f:
        return json.load(f)

def jouer(questions):
    score = 0
    random.shuffle(questions)
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        random.shuffle(q['options'])
        
        for j, option in enumerate(q['options'], 1):
            print(f"{j}. {option}")
        
        while True:
            try:
                reponse = int(input("Votre réponse (numéro) : "))
                if 1 <= reponse <= len(q['options']):
                    break
                print(f"Veuillez entrer un nombre entre 1 et {len(q['options']}")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
        
        if q['options'][reponse-1] == q['reponse']:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Faux! La réponse était : {q['reponse']}")
    
    print(f"\nScore final : {score}/{len(questions)}")
    return score

def main():
    questions = charger_questions()
    print("\n=== QUIZ ===")
    print(f"Il y a {len(questions)} questions. Bonne chance!\n")
    
    jouer(questions)
    
    while input("\nVoulez-vous rejouer? (o/n) "):
        jouer(questions)
    
    print("\nMerci d'avoir joué!")

if name == "__main__":
    main()

]
