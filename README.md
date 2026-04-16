# 🧩 Boggle Word Game (Python Tkinter)

A fully interactive **Boggle Word Game** built with Python and Tkinter, featuring real-time gameplay, adjacency-based word formation, and a responsive GUI.

This project demonstrates strong fundamentals in **event-driven programming, GUI design, and algorithmic problem solving**, making it a solid showcase for software engineering roles.

---

## 🚀 Overview

This application recreates the classic **Boggle experience** with a dynamically generated **4×4 letter grid**. Players form words by selecting adjacent tiles, while the system validates entries against a dictionary and updates scores in real time.

A built-in timer enforces a **3-minute gameplay window**, after which the board is locked and the round ends.

---

## ✨ Key Features

- 🎲 **Random Board Generation**  
  Generates a new 4×4 grid using uppercase English letters each round.

- 🔗 **Adjacency-Based Path Selection**  
  - Supports horizontal, vertical, and diagonal traversal  
  - Prevents reuse of the same tile in a single word  

- 📖 **Dictionary Validation**  
  - Loads words from an external `words.txt` file  
  - Gracefully handles missing dictionary scenarios  

- ⏱️ **Real-Time Countdown Timer (180s)**  
  - Live timer updates every second  
  - Automatically locks the board when time expires  

- 🧠 **Scoring System (Standard Boggle Rules)**  

  | Word Length | Points |
  |------------|--------|
  | 3–4        | 1      |
  | 5          | 2      |
  | 6          | 3      |
  | 7          | 5      |
  | ≥8         | 11     |

- 📋 **Live Word Tracking**
  - Prevents duplicate submissions  
  - Displays accepted words with earned points  

- 🖥️ **Interactive GUI**
  - Built using Tkinter  
  - Click-based tile selection with visual feedback  
  - Dynamic updates using `StringVar`  

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **GUI Framework:** Tkinter  

**Core Concepts:**
- Event-driven programming (`bind`, callbacks)
- Grid-based traversal logic
- State management using sets & lists
- Real-time UI updates with Tkinter variables

---

## 📂 Project Structure

```bash
Boggle%20%word%20%game/
│── Boggle%20%word%20%game.py        # Complete game logic + GUI
│── words.txt      # Dictionary file for validation
