# 🏓 The Pong Game

A faithful, object-oriented recreation of the classic arcade game **Pong**, built entirely in Python using the `turtle` graphics module.

> ⚠️ **Work in Progress** — This project is currently under active development. Core components are in place, but the game is not yet fully playable.

---

## 📖 About

This project is a Python-based reimplementation of the iconic Pong arcade game (1972). It follows an object-oriented design, with each game element — the ball, the paddles — defined as its own class. The game runs in a black 800×600 window using Python's built-in `turtle` module, requiring zero external dependencies.

---

## 📁 Project Structure

```
The_Pong_Game/
├── main.py       # Entry point — sets up the screen, initialises game objects, runs the game loop
├── paddle.py     # Paddle class — handles paddle creation and movement
└── ball.py       # Ball class — handles ball creation and movement
```

---

## ✅ What's Done

- Game window setup (800×600, black background)
- `Paddle` class with up/down movement controls
- Two-player paddle controls:
  - **Right paddle** — `↑` / `↓` arrow keys
  - **Left paddle** — `W` / `S` keys
- `Ball` class with basic movement logic
- Main game loop with `turtle` screen updates

---

## 🚧 What's Still In Progress

- [ ] Ball collision detection with top/bottom walls
- [ ] Ball collision detection with paddles
- [ ] Ball bouncing/direction reversal logic
- [ ] Scoring system
- [ ] Score display on screen
- [ ] Ball reset after a point is scored
- [ ] Win condition / game over screen
- [ ] Ball speed increase over time

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no external libraries needed — `turtle` is part of the standard library)

### Run the Game

```bash
git clone https://github.com/Prithviraj-chw/The_Pong_Game.git
cd The_Pong_Game
python main.py
```

---

## 🎮 Controls

| Player       | Move Up | Move Down |
|--------------|---------|-----------|
| Right Paddle | `↑`     | `↓`       |
| Left Paddle  | `W`     | `S`       |

---

## 🛠️ Built With

- **Python 3**
- **turtle** — Python's standard graphics library

---

## 👤 Author

**Prithviraj** — [@Prithviraj-chw](https://github.com/Prithviraj-chw)
