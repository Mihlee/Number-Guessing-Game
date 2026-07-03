# Number-Guessing-Game
# 🎮 Epic Guessing Arcade

**Epic Guessing Arcade** is a feature-rich, terminal-based number guessing game built with Python. Moving beyond standard linear high/low games, this arcade edition introduces an economic layer, strategic item scaling, and progressive difficulty risk management loops.

---

## 🕹️ Core Game Features

* **💰 Integrated Gold Economy:** Players start with 30 Gold and earn passive payout yields for active tracking metrics, alongside massive baseline victory prize drops.
* **🛒 Interactive Item Shop:** Players can enter the shop at any point during their run to purchase game-altering power-ups:
  * 🧪 **Scanner Hint (15 Gold):** Tracks proximity variances to generate structural number zone boundaries.
  * ❤️ **Extra Life (25 Gold):** Restores missing attempts to lengthen standard running sequences.
  * 🛡️ **Guess Shield (20 Gold):** Negates the life penalty of the user's immediate next incorrect guess.
* **⚙️ Dynamic Difficulty Tiers:**
  * 🟢 **Easy:** Range 1-50 | 10 Lives | 1x Gold Payouts
  * 🟡 **Medium:** Range 1-100 | 7 Lives | 2x Gold Payouts
  * 🔴 **Hard:** Range 1-200 | 4 Lives | 4x Gold Payouts
* **🔄 Infinite Progression Mode:** Guessing correctly doesn't force a system reset. Players can carry over their accumulated gold and scores across continuous progressive rounds to maximize historical leaderboards.

---

## 📂 Project Structure

```text
└── Epic-Guessing-Arcade/
    ├── arcade_game.py    # Main game engine loop, logic operations, shop states
    └── README.md         # Project breakdown documentation
