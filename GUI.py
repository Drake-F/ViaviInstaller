import tkinter as tk
from tkinter import ttk
from installSoftware import pyInstall, zebraInstall, viperInstall, mstInstall, ms_cipInstall

class ViaviToolkit:
    def __init__(self, root):
        self.root = root
        self.root.title("Viavi Toolkit")
        self.root.geometry("460x460")
        self.root.minsize(460, 460)

        self._configure_style()
        self._build_layout()

    def _configure_style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.Tc1Error:
            pass

        style.configure("Treeview", rowheight=25)
        style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))

    def _build_layout(self):
        outer = ttk.Frame(self.root, padding=12)
        outer.pack(fill="both", expand=True)

        outer.columnconfigure(0, weight=1, uniform="columns")
        outer.columnconfigure(1, weight=1, uniform="columns")
        for i in range(10):
            outer.rowconfigure(i, weight=1)

        self._build_install(outer)

    def _build_install(self, outer):
        softwareOptions = ["Python", "Viper Monitor", "Zebra Designer", "MST", "MS-CIP"]
        ttk.Label(outer, text="Choose Software to Install:").grid(
            row=0, column=0, sticky="w", padx=(0,8), pady=5
        )
        for i in range(len(softwareOptions)):
            ttk.Label(outer, text=softwareOptions[i]).grid(
                row=i+1, column=0, padx=(0,8), pady=5, sticky="w"
            )
        
        self.py_install = tk.BooleanVar(value=False)
        self.viper_install = tk.BooleanVar(value=False)
        self.zebra_install = tk.BooleanVar(value=False)
        self.MST_install = tk.BooleanVar(value=False)
        self.MS_CIP_install = tk.BooleanVar(value=False)
        variables = [self.py_install, self.viper_install, self.zebra_install,
                     self.MST_install, self.MS_CIP_install]

        for i in range(len(softwareOptions)):
            ttk.Checkbutton(outer, variable=variables[i]).grid(
                row=i+1, column=1, padx=(0,8), pady=5, sticky="w"
            )

        ttk.Button(
            outer, text="Install", command=self._install_software
        ).grid(row=6, column=0, padx=(0,8), pady=5, sticky="w")
        
    def _install_software(self):
        if self.py_install.get():
            pyInstall()
        if self.viper_install.get():
            viperInstall()
        if self.zebra_install.get():
            zebraInstall()
        if self.MST_install.get():
            mstInstall()
        if self.MS_CIP_install.get():
            ms_cipInstall()

        self.py_install.set(False)
        self.viper_install.set(False)
        self.zebra_install.set(False)
        self.MST_install.set(False)
        self.MS_CIP_install.set(False)

root = tk.Tk()
app = ViaviToolkit(root)
root.mainloop()