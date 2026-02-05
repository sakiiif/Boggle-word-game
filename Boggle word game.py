import tkinter as tk
from tkinter import messagebox
import random
import string
import time

ROWS = COLS = 4
FONT_TILE = ("Consolas", 20, "bold")
FONT_MISC = ("Consolas", 12)
SCORE_RULES = {3: 1, 4: 1, 5: 2, 6: 3, 7: 5}
TIMER_SECS = 180
DICT_FILE = "words.txt"

board = []
tiles = []
found = set()
path = []
legal = set()
score = 0
deadline = None
timer_job = None

root = tk.Tk()
root.title("Boggle Word Game")

timer_var = tk.StringVar(value="⏲︎ 03:00")
path_var = tk.StringVar()
score_var = tk.StringVar(value="Score: 0")

def random_board():
    return [[random.choice(string.ascii_uppercase) for _ in range(COLS)] for _ in range(ROWS)]

def score_word(w):
    n = len(w)
    if n >= 8:
        return 11
    return SCORE_RULES.get(n, 0)

def tile_click_handler(r, c):
    def handler(_):
        global path
        if path:
            pr, pc = path[-1]
            if abs(pr - r) > 1 or abs(pc - c) > 1 or (r, c) in path:
                return
        path.append((r, c))
        tiles[r][c]["bg"] = "#a0d8ff"
        path_var.set("".join(board[x][y] for x, y in path))
    return handler

def reset_path():
    global path
    for r, c in path:
        tiles[r][c]["bg"] = "#f0f0ff"
    path.clear()
    path_var.set("")

def submit_word():
    global score
    word = path_var.get().lower()
    if len(word) < 3:
        messagebox.showinfo("Oops", "Word too short!")
    elif word in found:
        messagebox.showinfo("Oops", "Already found!")
    elif legal and word not in legal:
        messagebox.showinfo("Oops", f"“{word.upper()}” not in dictionary!")
    else:
        pts = score_word(word)
        if pts == 0:
            messagebox.showinfo("Oops", "Word must be ≥3 letters.")
        else:
            found.add(word)
            listbox.insert(tk.END, f"{word.upper()}  (+{pts})")
            score += pts
            score_var.set(f"Score: {score}")
    reset_path()

def lock_board():
    for row in tiles:
        for lbl in row:
            lbl.unbind("<Button-1>")

def timer_tick():
    global timer_job
    remaining = int(deadline - time.time())
    if remaining < 0:
        timer_var.set("⏲︎ 00:00")
        lock_board()
        return
    m, s = divmod(remaining, 60)
    timer_var.set(f"⏲︎ {m:02d}:{s:02d}")
    timer_job = root.after(1000, timer_tick)

def start_round(first=False):
    global board, path, found, score, deadline, timer_job

    board = random_board()
    for r in range(ROWS):
        for c in range(COLS):
            tiles[r][c]["text"] = board[r][c]
            tiles[r][c]["bg"] = "#f0f0ff"

    found.clear()
    listbox.delete(0, tk.END)
    score = 0
    score_var.set("Score: 0")
    path.clear()
    path_var.set("")
    deadline = time.time() + TIMER_SECS

    if not first and timer_job is not None:
        root.after_cancel(timer_job)
    timer_tick()

try:
    with open(DICT_FILE, "r", encoding="utf-8") as f:
        legal = {w.strip().lower() for w in f if w.strip()}
except FileNotFoundError:
    messagebox.showerror("Dictionary missing", f"Cannot find {DICT_FILE}. Word check disabled.")
    legal = set()


top = tk.Frame(root)
top.pack(pady=5)

tk.Button(top, text="Start / Shuffle", font=FONT_MISC, command=lambda: start_round()) \
    .pack(side=tk.LEFT, padx=5)

tk.Label(top, textvariable=timer_var, font=FONT_MISC).pack(side=tk.LEFT, padx=10)

board_frame = tk.Frame(root)
board_frame.pack()

tiles = [[None] * COLS for _ in range(ROWS)]
for r in range(ROWS):
    for c in range(COLS):
        lbl = tk.Label(board_frame, width=3, height=1,
                       font=FONT_TILE, borderwidth=2, relief="ridge",
                       bg="#f0f0ff")
        lbl.grid(row=r, column=c, padx=1, pady=1, sticky="nsew")
        lbl.bind("<Button-1>", tile_click_handler(r, c))
        tiles[r][c] = lbl
    board_frame.grid_rowconfigure(r, weight=1)
    board_frame.grid_columnconfigure(r, weight=1)

mid = tk.Frame(root)
mid.pack(pady=4)

tk.Label(mid, text="Current path:", font=FONT_MISC).grid(row=0, column=0, sticky="w")
tk.Label(mid, textvariable=path_var, font=FONT_MISC, width=20, anchor="w").grid(row=0, column=1, sticky="w")
tk.Button(mid, text="Submit", font=FONT_MISC, command=submit_word).grid(row=0, column=2, padx=4)
tk.Button(mid, text="Reset Path", font=FONT_MISC, command=reset_path).grid(row=0, column=3)

listbox = tk.Listbox(root, width=20, height=6, font=FONT_MISC)
listbox.pack(pady=4)

tk.Label(root, textvariable=score_var, font=("Consolas", 16, "bold")).pack(pady=(0, 6))

start_round(first=True)
root.minsize(320, 400)
root.mainloop()
