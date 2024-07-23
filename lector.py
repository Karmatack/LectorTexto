import tkinter as tk
from tkinter import messagebox
from pyttsx3 import init as engine_init
from threading import Thread

# Inicializar el motor de pyttsx3
engine = engine_init()
stop_flag = False

def read_text():
    global stop_flag
    text = text_box.get("1.0", tk.END).strip()  
    if text:  
        try:
            set_text_box_state(tk.DISABLED)
            engine.say(text) 
            engine.runAndWait()
        except Exception as e:
            if not stop_flag:
                messagebox.showerror("Error", f"Ocurrió un error al intentar leer el texto: {e}")
        finally:
            if not stop_flag:
                messagebox.showinfo("Información", "Se completó la lectura.")
                set_text_box_state(tk.NORMAL)
                read_button.config(state=tk.NORMAL)
    else:
        if not stop_flag:
            messagebox.showwarning("Advertencia", "El cuadro de texto está vacío. Por favor ingresa algún texto.")
        read_button.config(state=tk.NORMAL)

    stop_flag = False

def set_text_box_state(state):

    text_box.config(state=state)

def read_text_thread():

    global stop_flag
    stop_flag = False
    read_button.config(state=tk.DISABLED)
    thread = Thread(target=read_text)
    thread.start()

def stop_engine():

    global stop_flag
    stop_flag = True
    engine.stop()

def on_closing():
    
    stop_engine()
    root.destroy()

def update_rate(value):

    rate = int(value) * 75 + 25
    engine.setProperty('rate', rate)

def configure_voice(rate=300, volume=1.0):

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.connect('started-utterance', lambda name: None)
    engine.connect('finished-utterance', lambda name: on_end())

def on_end():

    set_text_box_state(tk.NORMAL)  # Habilitar el cuadro de texto al finalizar la lectura
    read_button.config(state=tk.NORMAL)  # Habilitar el botón de "Leer Texto"

root = tk.Tk()
root.title("Lector de Texto")

text_box = tk.Text(root, wrap='word', width=100, height=20)
text_box.pack(padx=10, pady=10)

read_button = tk.Button(root, text="Leer Texto", command=read_text_thread)
read_button.pack(pady=10)


rate_scale = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL, label="Velocidad de Voz", command=update_rate)
rate_scale.set(3)
rate_scale.pack(pady=10)

configure_voice()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
