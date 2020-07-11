import tkinter as tk

def encrypt(text):
    encrypted_text = ""
    for letter in text:
        letter_num = ord(letter) - 96
        encrypted_text += chr(ord(letter) + 2)

    output.delete('1.0', tk.END)
    output.insert(1.0, encrypted_text)



def decrypt(text):
    decrypted_text = ""
    for letter in text:
        letter_num = ord(letter) - 96
        decrypted_text += chr(ord(letter) - 2)

    output.delete('1.0', tk.END)
    output.insert(1.0, decrypted_text)


if __name__ == "__main__":
    root = tk.Tk()

    canvas = tk.Canvas(root, height=595, width=600)
    canvas.pack()

    background_img = tk.PhotoImage(file="encryption-OG.png")
    background_label = tk.Label(root, image=background_img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    ##Encryption
    enframe = tk.Frame(root, bd=5, bg="black")
    enframe.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.15, anchor='n')

    entryen = tk.Entry(enframe, font=('Times New Roman', 25))
    entryen.place(relwidth=0.65, relheight=0.5)

    buttonen = tk.Button(enframe, text="Encrypt", font=('Times New Roman bold', 25), bg="green",
                         command=lambda: encrypt(entryen.get()))
    buttonen.place(relx=0.7, relwidth=0.3, relheight=0.5)
    # Decryption
    deframe = tk.Frame(root, bd=5, bg="black")
    deframe.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.15, anchor='n')

    entryde = tk.Entry(deframe, font=('Times New Roman', 25))
    entryde.place(relwidth=0.65, relheight=0.5)

    buttonde = tk.Button(deframe, text="Decrypt", font=('Times New Roman bold', 25), bg="green",
                         command=lambda: decrypt(entryde.get()))
    buttonde.place(relx=0.7, relwidth=0.3, relheight=0.5)

    # Output
    botframe = tk.Frame(root, bg='#004d00', bd=10)
    botframe.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n')

    output = tk.Text(botframe, font=('Times New Roman', 25), bd=4)
    output.place(relwidth=1, relheight=1)
    root.mainloop()
