import random
import tkinter as tk
from tkinter import messagebox

# Liste de mots à deviner
mots = ["python", "programmation", "ordinateur", "intelligence", "apprentissage"]

def choisir_mot():
    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees):
    affichage = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            affichage += lettre
        else:
            affichage += "_"
    return affichage

# Images du pendu
images_pendu = [
"""

---------
""",
"""
        |
        |
        |
        |
        |
        |
---------
""",
"""
  -------
        |
        |
        |
        |
        |
        |
---------
""",
"""
  -------
    |   |
        |
        |
        |
        |
        |
---------
""",
"""
    -----
    |   |
    O   |
        |
        |
        |
        |
---------
""",
"""
    -----
    |   |
    O   |
    |   |
        |
        |
        |
---------
""",
"""
    -----
    |   |
    O   |
   /|   |
        |
        |
        |
---------
""",
"""
    -----
    |   |
    O   |
   /|\\  |
        |
        |
        |
---------
""",
"""
    -----
    |   |
    O   |
   /|\\  |
   /    |
        |
        |
---------
""",
"""
    -----
    |   |
    O   |
   /|\\  |
   / \\  |
        |
        |
---------
"""

]

class PenduApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu du Pendu")
        self.master.geometry("300x350")

        self.mot_a_deviner = choisir_mot()
        self.lettres_trouvees = []
        self.tentatives_restantes = 10
        self.image_pendu_index = 0

        self.label_image_pendu = tk.Label(master, text=images_pendu[self.image_pendu_index], justify='left')
        self.label_image_pendu.pack()

        self.label_mot = tk.Label(master, text=afficher_mot_cache(self.mot_a_deviner, self.lettres_trouvees))
        self.label_mot.pack()

        self.label_tentatives = tk.Label(master, text=f"Tentatives restantes : {self.tentatives_restantes}")
        self.label_tentatives.pack()

        self.entree = tk.Entry(master)
        self.entree.pack()
        self.entree.bind("<Return>", self.verifier_proposition)

        self.bouton_deviner = tk.Button(master, text="Deviner", command=self.verifier_proposition)
        self.bouton_deviner.pack()

    def verifier_proposition(self, event=None):
        proposition = self.entree.get().lower()
        self.entree.delete(0, tk.END)

        if len(proposition) == 1:  # Si la proposition est une lettre
            lettre = proposition
            if lettre in self.lettres_trouvees:
                messagebox.showinfo("Information", "Vous avez déjà deviné cette lettre. Essayez une autre lettre.")
            elif lettre in self.mot_a_deviner:
                self.lettres_trouvees.append(lettre)
                self.label_mot.config(text=afficher_mot_cache(self.mot_a_deviner, self.lettres_trouvees))
                if "_" not in afficher_mot_cache(self.mot_a_deviner, self.lettres_trouvees):
                    messagebox.showinfo("Félicitations", f"Vous avez deviné le mot : {self.mot_a_deviner}")
                    self.master.destroy()
            else:
                self.tentatives_restantes -= 1
                self.label_tentatives.config(text=f"Tentatives restantes : {self.tentatives_restantes}")
                if self.tentatives_restantes == 0:
                    messagebox.showinfo("Dommage", f"Vous avez perdu ! Le mot était : {self.mot_a_deviner}")
                    self.master.destroy()
                else:
                    self.image_pendu_index += 1
                    self.label_image_pendu.config(text=images_pendu[self.image_pendu_index])
        elif len(proposition) == len(self.mot_a_deviner):  # Si la proposition est le mot complet
            mot = proposition
            if mot == self.mot_a_deviner:
                messagebox.showinfo("Félicitations", f"Vous avez deviné le mot : {self.mot_a_deviner}")
                self.master.destroy()
            else:
                messagebox.showinfo("Dommage", "Ce n'est pas le bon mot.")
        else:
            messagebox.showinfo("Erreur", "La proposition doit être soit une lettre soit le mot complet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PenduApp(root)
    root.mainloop()
