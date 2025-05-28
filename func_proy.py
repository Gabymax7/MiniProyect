import os
from tkinter import messagebox

def sop_tec():
    enlace_soporte = "wa.me/5493735444916"
    try:
        import webbrowser
        webbrowser.open(enlace_soporte)
    except Exception as e:
        print(f"Error al abrir el enlace de soporte: {e}")

def docu():

    nombre_archivo = "Documentacion.txt"
    ruta_absoluta = os.path.abspath("Documentacion.txt")

    try:
        if os.path.exists(ruta_absoluta):
            if os.name == 'nt':
                os.startfile(ruta_absoluta)
            elif os.name == 'posix':
                import subprocess
                subprocess.call(['xdg-open', ruta_absoluta])
            else:
                print("Sistema operativo no soportado para abrir archivos.")
        else:
            print(f"El archivo {nombre_archivo} no existe en la ruta {ruta_absoluta}.") 
    except Exception as e:
        print(f"Error al abrir el archivo de documentación: {e}")

def tema_claro(root, barra_menu_obj, menu_apariencia_obj, submenutemas_obj, menu_configuracion_obj, menu_ayuda_obj):
    bg_color = "white"
    fg_color = "black"
    root.config(bg=bg_color) 
    barra_menu_obj.config(bg=bg_color, fg=fg_color)
    menu_apariencia_obj.config(bg=bg_color, fg=fg_color)
    submenutemas_obj.config(bg=bg_color, fg=fg_color)
    menu_configuracion_obj.config(bg=bg_color, fg=fg_color)
    menu_ayuda_obj.config(bg=bg_color, fg=fg_color)
    messagebox.showinfo("Tema", "Tema Claro aplicado.")

def tema_oscuro(root, barra_menu_obj, menu_apariencia_obj, submenutemas_obj, menu_configuracion_obj, menu_ayuda_obj):

    bg_color = "#333333"
    fg_color = "white"
    active_bg_color = "#555555"
    active_fg_color = "white"

    root.config(bg=bg_color)
     # Configurar los menús con sus colores de fondo, texto y activos
    barra_menu_obj.config(bg=bg_color, fg=fg_color,
                          activebackground=active_bg_color, activeforeground=active_fg_color)
    menu_apariencia_obj.config(bg=bg_color, fg=fg_color,
                                activebackground=active_bg_color, activeforeground=active_fg_color)
    submenutemas_obj.config(bg=bg_color, fg=fg_color,
                             activebackground=active_bg_color, activeforeground=active_fg_color)
    # Agrega aquí las configuraciones para menu_configuracion_obj y menu_ayuda_obj
    menu_configuracion_obj.config(bg=bg_color, fg=fg_color,
                                   activebackground=active_bg_color, activeforeground=active_fg_color)
    menu_ayuda_obj.config(bg=bg_color, fg=fg_color,
                           activebackground=active_bg_color, activeforeground=active_fg_color)

    messagebox.showinfo("Tema", "Tema Oscuro aplicado.")