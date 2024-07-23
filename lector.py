import tkinter as tk
from tkinter import messagebox
from pyttsx3 import init as engine_init
from threading import Thread

# Inicializar el motor de pyttsx3
engine = engine_init()
stop_flag = False

def read_text():
    """
    Función para leer el texto ingresado en el cuadro de texto usando pyttsx3.
    """
    global stop_flag
    text = text_box.get("1.0", tk.END).strip()  
    if text:  
        try:
            set_text_box_state(tk.DISABLED)  # Deshabilitar el cuadro de texto durante la lectura
            engine.say(text) 
            engine.runAndWait()  # Espera hasta que termine la lectura
        except Exception as e:
            if not stop_flag:
                messagebox.showerror("Error", f"Ocurrió un error al intentar leer el texto: {e}")
        finally:
            if not stop_flag:
                messagebox.showinfo("Información", "Se completó la lectura.")
                set_text_box_state(tk.NORMAL)  # Habilitar nuevamente el cuadro de texto al finalizar la lectura
                read_button.config(state=tk.NORMAL)  # Habilitar el botón de "Leer Texto"
    else:
        if not stop_flag:
            messagebox.showwarning("Advertencia", "El cuadro de texto está vacío. Por favor ingresa algún texto.")
        read_button.config(state=tk.NORMAL)  # Habilitar el botón de "Leer Texto" si el campo está vacío

    stop_flag = False

def set_text_box_state(state):
    """
    Función para cambiar el estado del cuadro de texto.
    """
    text_box.config(state=state)

def read_text_thread():
    """
    Ejecuta la función read_text en un hilo separado para evitar que la GUI se congele.
    """
    global stop_flag
    stop_flag = False
    read_button.config(state=tk.DISABLED)  # Deshabilitar el botón de "Leer Texto"
    thread = Thread(target=read_text)
    thread.start()

def stop_engine():
    """
    Detiene el motor de pyttsx3.
    """
    global stop_flag
    stop_flag = True
    engine.stop()

def on_closing():
    """
    Maneja el evento de cierre de la aplicación.
    """
    # Detener el motor de pyttsx3
    stop_engine()
    # Destruir la ventana
    root.destroy()

def update_rate(value):
    """
    Actualiza la velocidad de la voz según el valor del Scale.
    """
    rate = int(value) * 75 + 25
    engine.setProperty('rate', rate)

def configure_voice(rate=300, volume=1.0):
    """
    Configura las propiedades de la voz del motor pyttsx3.
    :param rate: Velocidad de la voz.
    :param volume: Volumen de la voz.
    """
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.connect('started-utterance', lambda name: None)
    engine.connect('finished-utterance', lambda name: on_end())

def on_end():
    """
    Función que se llama cuando se completa la lectura en voz alta.
    """
    set_text_box_state(tk.NORMAL)  # Habilitar el cuadro de texto al finalizar la lectura
    read_button.config(state=tk.NORMAL)  # Habilitar el botón de "Leer Texto"

root = tk.Tk()
root.title("Lector de Texto")

# Crear el cuadro de texto
text_box = tk.Text(root, wrap='word', width=100, height=20)
text_box.pack(padx=10, pady=10)

# Crear un botón para leer el texto
read_button = tk.Button(root, text="Leer Texto", command=read_text_thread)
read_button.pack(pady=10)

# Crear un Scale para ajustar la velocidad de la voz
rate_scale = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL, label="Velocidad de Voz", command=update_rate)
rate_scale.set(3)  # Valor inicial
rate_scale.pack(pady=10)

# Configurar la voz al inicio
configure_voice()

# Manejar el evento de cierre de la ventana
root.protocol("WM_DELETE_WINDOW", on_closing)

# Ejecutar la aplicación
root.mainloop()
