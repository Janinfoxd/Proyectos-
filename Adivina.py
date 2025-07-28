import tkinter as tk
import random
from tkinter import messagebox

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("Adivina el Número")
        master.geometry("400x400")
        master.config(bg="#f0f0f0") # Un color de fondo suave

        self.secret_number = 0
        self.player_name = ""

        # --- Título ---
        self.lbl_title = tk.Label(master, text="¡Adivina el Número!", fg="#333333", bg="#f0f0f0",font=("Arial", 20, "bold"))
        self.lbl_title.pack(pady=10)

        self.lbl_description = tk.Label(master, text="La computadora pensará un número entre 1 y 10.\n¡Intenta adivinarlo!",
                                         fg="#555555", bg="#f0f0f0", font=("Arial", 10))
        self.lbl_description.pack(pady=5)

        # --- Recopilación de Nombre ---
        self.lbl_name = tk.Label(master, text="¿Cómo te llamas?", fg="#333333", bg="#f0f0f0", font=("Arial", 12))
        self.lbl_name.pack(pady=5)
        self.entry_name = tk.Entry(master, width=30, font=("Arial", 12))
        self.entry_name.pack(pady=5)
        self.entry_name.focus_set() # Pone el cursor en este campo al inicio

        self.btn_start = tk.Button(master, text="Empezar Juego", command=self.start_game,
                                   bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief=tk.RAISED)
        self.btn_start.pack(pady=10)

        # --- Sección del Juego (inicialmente oculta) ---
        self.game_frame = tk.Frame(master, bg="#f8f8f8")

        self.lbl_instruction = tk.Label(self.game_frame, text="Ingresa tu suposición (1-10):",
                                        fg="#333333", bg="#f0f0f0", font=("Arial", 12))
        self.lbl_instruction.pack(pady=5)

        self.entry_guess = tk.Entry(self.game_frame, width=10, font=("Arial", 14))
        self.entry_guess.pack(pady=5)

        self.btn_guess = tk.Button(self.game_frame, text="Adivinar", command=self.check_guess,
                                   bg="#2196F3", fg="white", font=("Arial", 12, "bold"), relief=tk.RAISED)
        self.btn_guess.pack(pady=10)

        self.lbl_feedback = tk.Label(self.game_frame, text="", fg="#333333", bg="#f0f0f0", font=("Arial", 12, "italic"))
        self.lbl_feedback.pack(pady=10)

        self.btn_play_again = tk.Button(self.game_frame, text="Jugar de Nuevo", command=self.reset_game,
                                         bg="#FF9800", fg="white", font=("Arial", 12, "bold"), relief=tk.RAISED)
        # Este botón estará oculto hasta que el juego termine
        self.btn_play_again.pack_forget()

    def start_game(self):
        """Inicializa el juego después de que el usuario ingresa su nombre."""
        self.player_name = self.entry_name.get().strip()
        if not self.player_name:
            messagebox.showwarning("Error", "Por favor, ingresa tu nombre para empezar.")
            return

        # Oculta la sección de nombre y muestra la del juego
        self.lbl_name.pack_forget()
        self.entry_name.pack_forget()
        self.btn_start.pack_forget()

        self.game_frame.pack(pady=20)
        self.reset_game() # Reinicia el juego para la primera partida
        messagebox.showinfo("¡Hola!", f"¡Mucho gusto, {self.player_name}! Vamos a jugar.")

    def reset_game(self):
        """Reinicia el estado del juego para una nueva partida."""
        self.secret_number = random.randint(1, 10)
        self.lbl_feedback.config(text="")
        self.entry_guess.delete(0, tk.END) # Limpia el campo de suposición
        self.btn_guess.config(state=tk.NORMAL) # Habilita el botón de adivinar
        self.btn_play_again.pack_forget() # Oculta el botón de jugar de nuevo
        self.entry_guess.focus_set() # Pone el cursor en el campo de suposición

    def check_guess(self):
        """Verifica la suposición del usuario."""
        try:
            guess = int(self.entry_guess.get())
            if not (1 <= guess <= 10):
                self.lbl_feedback.config(text="Por favor, ingresa un número entre 1 y 10.")
                return

            if guess == self.secret_number:
                self.lbl_feedback.config(text=f"¡Felicidades, {self.player_name}! ¡Has acertado! El número era {self.secret_number}.", fg="green")
                self.btn_guess.config(state=tk.DISABLED) # Deshabilita el botón de adivinar
                self.btn_play_again.pack(pady=10) # Muestra el botón de jugar de nuevo
            else:
                self.lbl_feedback.config(text=f"¡Incorrecto! El número era {self.secret_number}. Vuelve a intentarlo.", fg="red")
                # Aquí podrías dar pistas como "más alto" o "más bajo"
                if guess < self.secret_number:
                 self.lbl_feedback.config(text="¡Incorrecto! El número es más alto. Inténtalo de nuevo.", fg="orange")
                else:
                 self.lbl_feedback.config(text="¡Incorrecto! El número es más bajo. Inténtalo de nuevo.", fg="orange")
            
        except ValueError:
            self.lbl_feedback.config(text="Entrada inválida. Por favor, ingresa un número entero.", fg="purple")

# --- Ejecución del juego ---
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()





    
