import customtkinter as ctk
import pymem, pymem.process
import os, sys

PROCESS = "SonicMania.exe"
OFFSET = 0x469AD4


def resource_path(path):
    try:
        return os.path.join(sys._MEIPASS, path)
    except:
        return path


def set_rings():
    try:
        pm = pymem.Pymem(PROCESS)
        base = pymem.process.module_from_name(pm.process_handle, PROCESS).lpBaseOfDll
        pm.write_int(base + OFFSET, int(rings_var.get()))
    except:
        pass


def toggle_theme():
    global dark
    dark = not dark
    ctk.set_appearance_mode("Dark" if dark else "Light")
    theme_btn.configure(text="Bright Mode" if dark else "Dark Mode")


def slider_update(v):
    rings_var.set(int(v))


# ===== UI =====
dark = False
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("360x280")
app.title("Sonic Mania - Rings Giver")
app.resizable(False, False)

if os.path.exists("Sonic.ico"):
    app.iconbitmap(resource_path("Sonic.ico"))

ctk.CTkLabel(
    app,
    text="Number of Rings",
    font=("Segoe UI", 18, "bold")
).pack(pady=15)

rings_var = ctk.IntVar(value=99)

ctk.CTkEntry(
    app,
    width=120,
    height=40,
    corner_radius=20,
    justify="center",
    textvariable=rings_var,
    font=("Segoe UI", 14)
).pack(pady=5)

ctk.CTkSlider(
    app,
    from_=0,
    to=999,
    width=260,
    command=slider_update
).pack(pady=15)

ctk.CTkButton(
    app,
    text="Apply",
    width=180,
    height=42,
    corner_radius=22,
    font=("Segoe UI", 14, "bold"),
    command=set_rings
).pack(pady=10)

theme_btn = ctk.CTkButton(
    app,
    text="Dark Mode",
    width=150,
    height=32,
    corner_radius=18,
    command=toggle_theme
)
theme_btn.pack(pady=10)

app.mainloop()
