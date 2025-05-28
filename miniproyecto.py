import tkinter as tk
import func_proy as func_proy


ventana = tk.Tk()
ventana.title('Menú desplegable')
ventana.geometry('400x200')

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_apariencia = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label ='Apariencia', menu=menu_apariencia)

submenutemas = tk.Menu(menu_apariencia, tearoff=0)
menu_apariencia.add_cascade(label ='Temas', menu=submenutemas)

submenutemas.add_command(label = 'Tema Claro', command=lambda: func_proy.tema_claro(ventana, barra_menu, menu_apariencia, submenutemas, menu_configuracion, menu_ayuda))
submenutemas.add_command(label = 'Tema Oscuro', command=lambda: func_proy.tema_oscuro(ventana, barra_menu, menu_apariencia, submenutemas, menu_configuracion, menu_ayuda))

menu_configuracion = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label =
'Configuración', menu=menu_configuracion)
menu_configuracion.add_command(label = 'Preferencias')
menu_configuracion.add_command(label = 'Ajustes Avanzados')

menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label =
'Ayuda', menu=menu_ayuda)

menu_ayuda.add_command(label = 'Documentación', command=func_proy.docu)
menu_ayuda.add_command(label = 'Soporte Técnico', command=func_proy.sop_tec)

ventana.mainloop()