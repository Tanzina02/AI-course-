# Subtraction Game with AI - Detailed Implementation Guide

This guide provides a full explanation of the Subtraction Game (Stones Game) implemented in Python using `tkinter`. It covers the **game rules, AI logic, GUI design, and step-by-step code breakdown** so anyone can run, understand, and extend the project.

---

## Table of Contents

1. [Game Overview](#game-overview)  
2. [Project Structure](#project-structure)  
3. [Game Rules](#game-rules)  
4. [Python Code Breakdown](#python-code-breakdown)  
   - [Main Variables and Board Setup](#main-variables-and-board-setup)  
   - [AI Implementation (Minimax)](#ai-implementation-minimax)  
   - [Player Moves](#player-moves)  
   - [GUI Updates](#gui-updates)  
5. [Game Flow](#game-flow)  
6. [Extending the Game](#extending-the-game)  

---

## Game Overview

The Subtraction Game is a **classic turn-based game** where players remove stones from a pile. It is implemented with an **AI opponent using the Minimax algorithm**, which ensures that the AI plays optimally and cannot be beaten unless the player makes perfect moves. The game is visually represented using `tkinter`, with stones displayed as colored circles on a canvas. Players can remove **1, 2, or 3 stones per turn**, and the player who removes the last stone wins.  

The AI uses **recursive evaluation** of all possible future moves to determine the optimal action. This project demonstrates key programming concepts such as **recursion, game state evaluation, GUI event handling, and real-time feedback**. The game is simple to run, easy to understand, and serves as a strong foundation for learning AI algorithms and Python GUI development.  

This guide will provide **line-by-line explanations** of the code, the AI logic, and how the GUI interacts with the game mechanics. It is designed for beginners and intermediate Python developers who want to understand both AI and GUI integration in Python.

---

## Project Structure

```

Two Player Subtraction/
├──two player subtraction.py      # Main Python game file containing all logic and GUI
├── README.md                # Basic instructions and game overview
├── DETAILED_GUIDE.md        # This detailed guide with code explanations
└── Screenshots/             # Optional folder for images showing the game interface
````

**Explanation**:  
- `two player subtraction.py` contains **all game logic and interface code**, including AI, player moves, and GUI updates.  
- `README.md` is for users who just want **quick instructions** to run the game.  
- `DETAILED_GUIDE.md` is for developers who want to **understand or modify the code**.  
- `screenshots/` can hold images to illustrate the interface, stone layout, and game results.  

This structure separates **user instructions** from **technical explanations**, making it professional and scalable for future modifications or extensions.

---

## Game Rules

1. There is a **pile of stones**, starting with 25 by default.  
2. Players take turns removing **1, 2, or 3 stones** per move.  
3. The player who removes the **last stone wins** the game.  
4. If a player tries to remove more stones than remain, the game **blocks the move** and displays a warning.  
5. The AI always **plays optimally** and will either win or force a draw.  
6. Each turn is clearly indicated by **visual updates** on the canvas and AI feedback label.  
7. The game ends immediately when stones reach **zero**, and a **popup announces the winner**.  
8. The game is single-player against AI, but the code can easily be modified for **two-player mode**.  
9. The game uses **colored circles to represent stones**, making it visually appealing and easy to track.  
10. Players interact using **buttons to remove stones**, and the AI moves automatically after each player turn.  

These rules ensure **fair play**, **easy understanding**, and a **clear challenge against AI**, making it suitable for both beginners and experienced players.

---

## Python Code Breakdown

### Main Variables and Board Setup

```python
stones = 25  # Total number of stones at the start
root = tk.Tk()  # Main Tkinter window
root.title("Subtraction Game")  # Window title
canvas = tk.Canvas(root, width=350, height=200, bg="#34495E")  # Stones visualization
buttons_frame = tk.Frame(root)  # Container for move buttons
ai_label = tk.Label(root, text="", font=("Helvetica", 16))  # Display AI move info
````

**Explanation**:

* `stones` keeps track of remaining stones. It is **global** because both AI and player functions modify it.
* `root` is the **main window** where all GUI elements appear.
* `canvas` draws **visual representation of stones**, updated every turn.
* `buttons_frame` contains **move buttons** for player interaction.
* `ai_label` provides **real-time AI feedback**, letting the player know which move AI chose.
* Colors, fonts, and sizes are **customized for clarity and aesthetics**.
* Canvas coordinates are calculated to **align stones in a grid-like pattern**.
* The setup ensures **separation of GUI elements** and game logic.
* This structure allows future **extensions** like move history, scores, or multi-player support.
* Using Tkinter widgets makes the game **platform-independent** for Windows, macOS, and Linux.

---

### AI Implementation (Minimax)

```python
def minimax(stones, is_maximizing):
    if stones == 0:
        return -1 if is_maximizing else 1
    scores = []
    for move in [1, 2, 3]:
        if stones - move >= 0:
            next_score = minimax(stones - move, not is_maximizing)
            scores.append(next_score)
    return max(scores) if is_maximizing else min(scores)
```

**Explanation**:

* **Minimax** recursively evaluates all possible moves to **predict the outcome**.
* `is_maximizing` indicates if the current turn is AI (True) or player (False).
* Base case: `stones == 0` → returns **1 or -1**, signaling who wins.
* For each valid move (1, 2, 3), the function **simulates the remaining stones**.
* Scores from recursive calls are stored in `scores` to **evaluate options**.
* AI picks `max(scores)` to maximize its chances of winning.
* Player moves are evaluated with `min(scores)` because the AI assumes the player plays optimally.
* This algorithm ensures the AI is **unbeatable**.
* Minimax demonstrates **recursion, backtracking, and decision trees**.
* Time complexity is **O(b^d)** (branching factor^depth), suitable for small games like this.

```python
def ai_move(stones):
    best_score = -math.inf
    best_move = 1
    for move in [1, 2, 3]:
        if stones - move >= 0:
            score = minimax(stones - move, False)
            if score > best_score:
                best_score = score
                best_move = move
    return best_move
```

* Selects the **optimal move** based on Minimax scores.
* Loops through all valid moves and chooses the **highest scoring move**.
* Updates GUI label to show AI's action, keeping the player informed.
* Handles ties automatically by picking the first highest score move.
* Allows the player to **anticipate AI strategy** visually.

---

### Player Moves

```python
def player_move(move):
    global stones
    if move > stones:
        messagebox.showwarning("Invalid Move", "Not enough stones!")
        return
    stones -= move
    update_stones_display()
    if stones == 0:
        messagebox.showinfo("Game Over", "You win! 🎉")
        root.destroy()
        return
    root.after(500, ai_turn)
```

**Explanation**:

* Validates the player's move to prevent **illegal actions**.
* Subtracts the selected number of stones from the pile.
* Calls `update_stones_display()` to **redraw the canvas** with remaining stones.
* Checks if **player wins** immediately after the move.
* `root.after(500, ai_turn)` introduces a **short delay** before AI moves.
* Provides **smooth user experience** with visible changes.
* Uses `messagebox` for clear feedback, informing the player of invalid moves or wins.
* This function demonstrates **event-driven programming** in Tkinter.
* Global `stones` ensures both AI and player functions access the current game state.
* The approach separates **game logic** from **GUI updates**, keeping code maintainable.

---

### GUI Updates

```python
def update_stones_display():
    canvas.delete("all")
    for i in range(stones):
        x = 20 + (i % 5) * 60
        y = 20 + (i // 5) * 60
        color = "#FF6F61" if i % 2 == 0 else "#6B5B95"
        canvas.create_oval(x, y, x + 50, y + 50, fill=color, outline="#333", width=2)
        canvas.create_text(x + 25, y + 25, text=str(stones - i), fill="white", font=("Helvetica", 14, "bold"))
```

**Explanation**:

* Clears the canvas to **redraw updated stone positions**.
* Uses a **grid layout**: 5 stones per row to keep the display organized.
* Alternating colors improve **visual clarity** for remaining stones.
* Numbers on stones indicate **how many stones remain**, giving immediate feedback.
* GUI updates happen **after every move**, keeping game state synchronized.
* The canvas is **interactive only visually**, actual moves are handled via buttons.
* Supports dynamic resizing and different numbers of stones.
* Easy to modify for **different colors or shapes**.
* Works seamlessly with AI moves to **show both player and AI stones**.
* Demonstrates practical **graphics handling in Tkinter**.

---

## Game Flow

1. Game starts with **25 stones displayed** on the canvas.
2. Player clicks a button to remove 1, 2, or 3 stones.
3. Stones update on canvas, and **AI label remains blank until AI moves**.
4. If stones reach 0 after the player’s turn, **player wins**, and a popup appears.
5. If not, `ai_turn()` is called after 500ms.
6. AI evaluates all possible moves using **Minimax** and selects the optimal move.
7. Stones decrease by AI's move amount and **update GUI**.
8. AI label shows how many stones were removed by the AI.
9. The game repeats **player → AI** until stones reach 0.
10. Final messagebox announces the winner, and the program exits gracefully.

---

## Extending the Game

1. **Change starting stones**: Modify `stones = 25` to any number.
2. **Two-player mode**: Disable AI and alternate between two human players.
3. **Difficulty levels**: Limit AI recursion depth to make it easier.
4. **Turn indicator**: Add a label showing “Player Turn” or “AI Turn”.
5. **Move history**: Store player and AI moves in a list for reference.
6. **Visual enhancements**: Different colors or animations for moves.
7. **Sound effects**: Play sounds for player moves or wins.
8. **Customizable AI**: Allow the AI to make random moves at easy levels.
9. **Leaderboard**: Track player wins/losses across sessions.
10. **Integration with GUI frameworks**: Could migrate to PyQt5 or Kivy for a modern interface.

---

This guide provides **all details needed** to run, understand, and modify the Subtraction Game.
By following this, anyone with Python experience can learn **AI algorithms, GUI handling, and event-driven programming** through a hands-on project.
