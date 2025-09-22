import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

try:
    from tkcalendar import DateEntry
    TIENE_CALENDAR = True
except:
    TIENE_CALENDAR = False

class AgendaGirlFinal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Mi Agenda ✨')

        # Ventana grande automáticamente
        self.state('zoomed')  # Maximizada en Windows

        self.configure(bg='#ffe6f0')  # fondo rosa pastel

        self.eventos = []

        # Frames principales
        self.frame_lista = tk.Frame(self, bg='#fff0f5', padx=10, pady=10)
        self.frame_lista.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.frame_controles = tk.Frame(self, bg='#fff0f5', padx=10, pady=10)
        self.frame_controles.grid(row=0, column=1, sticky='ns', padx=10, pady=10)

        self._crear_treeview()
        self._crear_controles()

    def _crear_treeview(self):
        tk.Label(self.frame_lista, text='✨ Eventos Programados ✨', bg='#fff0f5', fg='#ff66b2',
                 font=('Comic Sans MS', 14, 'bold')).pack(anchor='w', pady=(0,10))

        cols = ('fecha', 'hora', 'desc')
        self.tree = ttk.Treeview(self.frame_lista, columns=cols, show='headings', height=18)
        self.tree.heading('fecha', text='Fecha')
        self.tree.heading('hora', text='Hora')
        self.tree.heading('desc', text='Descripción')
        self.tree.column('fecha', width=100, anchor='center')
        self.tree.column('hora', width=80, anchor='center')
        self.tree.column('desc', width=400, anchor='w')
        self.tree.pack(fill='both', expand=True)

        # Colores alternados para filas
        self.tree.tag_configure('odd', background='#ffe6f0')
        self.tree.tag_configure('even', background='#fff0f5')

        scrollbar = ttk.Scrollbar(self.frame_lista, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

    def _crear_controles(self):
        tk.Label(self.frame_controles, text='📝 Nuevo Evento', bg='#fff0f5', fg='#ff66b2',
                 font=('Comic Sans MS', 12, 'bold')).pack(anchor='w', pady=(0,10))

        tk.Label(self.frame_controles, text='Fecha (dd-mm-aaaa)', bg='#fff0f5', fg='#993366').pack(anchor='w')
        if TIENE_CALENDAR:
            self.entry_fecha = DateEntry(self.frame_controles, date_pattern='dd-mm-yyyy',
                                         background='#ffb3d9', foreground='black')
        else:
            self.entry_fecha = tk.Entry(self.frame_controles)
            self.entry_fecha.insert(0, datetime.now().strftime('%d-%m-%Y'))
        self.entry_fecha.pack(fill='x', pady=(0,5))

        tk.Label(self.frame_controles, text='Hora (HH:MM)', bg='#fff0f5', fg='#993366').pack(anchor='w')
        self.entry_hora = tk.Entry(self.frame_controles)
        self.entry_hora.insert(0, '09:00')
        self.entry_hora.pack(fill='x', pady=(0,5))

        tk.Label(self.frame_controles, text='Descripción', bg='#fff0f5', fg='#993366').pack(anchor='w')
        self.entry_desc = tk.Text(self.frame_controles, height=5, width=30, wrap='word')
        self.entry_desc.pack(pady=(0,5))

        tk.Button(self.frame_controles, text='Agregar Evento', bg='#ff66b2', fg='white', command=self.agregar_evento).pack(fill='x', pady=(0,5))
        tk.Button(self.frame_controles, text='Eliminar Evento', bg='#ff99cc', fg='white', command=self.eliminar_evento).pack(fill='x', pady=(0,5))
        tk.Button(self.frame_controles, text='Salir', bg='#cc6699', fg='white', command=self.destroy).pack(fill='x', pady=(20,0))

    def agregar_evento(self):
        fecha = self.entry_fecha.get().strip()
        hora = self.entry_hora.get().strip()
        desc = self.entry_desc.get('1.0','end').strip()

        if not fecha or not hora or not desc:
            messagebox.showwarning('Faltan datos', 'Completa todos los campos')
            return

        try:
            datetime.strptime(hora, '%H:%M')
        except:
            messagebox.showerror('Error hora', 'Formato de hora incorrecto')
            return

        try:
            datetime.strptime(fecha, '%d-%m-%Y')
        except:
            messagebox.showerror('Error fecha', 'Formato de fecha incorrecto')
            return

        self.eventos.insert(0, {'fecha': fecha, 'hora': hora, 'desc': desc})
        self._actualizar_treeview()
        self._limpiar_entradas()

    def eliminar_evento(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo('Atención', 'Selecciona un evento')
            return

        idx = int(self.tree.item(sel[0],'text'))
        if messagebox.askyesno('Confirmar', '¿Seguro que quieres eliminar este evento?'):
            try:
                del self.eventos[idx]
            except:
                pass
            self._actualizar_treeview()

    def _actualizar_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, ev in enumerate(self.eventos):
            tag = 'even' if i % 2 == 0 else 'odd'
            self.tree.insert('', 'end', text=str(i), values=(ev['fecha'], ev['hora'], ev['desc']), tags=(tag,))

    def _limpiar_entradas(self):
        if not TIENE_CALENDAR:
            self.entry_fecha.delete(0,'end')
            self.entry_fecha.insert(0, datetime.now().strftime('%d-%m-%Y'))
        self.entry_hora.delete(0,'end')
        self.entry_hora.insert(0,'09:00')
        self.entry_desc.delete('1.0','end')


if __name__=='__main__':
    app = AgendaGirlFinal()
    app.mainloop()
