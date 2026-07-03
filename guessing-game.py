import random
import time

def print_divider():
    print("=" * 50)

def show_shop(gold, lives, shield_active):
    print("\n🛒 --- ARCADE ITEM SHOP ---")
    print(f"💰 Your Wallet: {gold} Gold")
    print(f"1. 🧪 Higher/Lower Hint Scan [Cost: 15 Gold]")
    print(f"2. ❤️ Extra Life (+1 Attempt)   [Cost: 25 Gold]")
    print(f"3. 🛡️ Guess Shield (No penalty) [Cost: 20 Gold] {'(ACTIVE)' if shield_active else ''}")
    print("4. ❌ Exit Shop")
    print_divider()

def play_arcade_game():
    print_divider()
    print("🎮 WELCOME TO THE EPIC NUMBER GUESSING ARCADE! 🎮")
    print_divider()
    
    # Selection of Difficulty
    print("Choose your level:")
    print("1. 🟢 Easy   (Range 1-50,  10 Lives, 1x Gold)")
    print("2. 🟡 Medium (Range 1-100,  7 Lives, 2x Gold)")
    print("3. 🔴 Hard   (Range 1-200,  4 Lives, 4x Gold)")
    
    choice = input("Select difficulty (1-3): ").strip()
    
    if choice == "1":
        max_num, max_lives, gold_multiplier = 50, 10, 1
    elif choice == "3":
        max_num, max_lives, gold_multiplier = 200, 4, 4
    else:  # Default to Medium
        max_num, max_lives, gold_multiplier = 100, 7, 2

    secret_number = random.randint(1, max_num)
    lives = max_lives
    gold = 30  # Starting cash to play with the shop!
    score = 0
    shield_active = False
    
    print(f"\n🚀 System initialized! Number locked between 1 and {max_num}.")
    print(f"❤️ You have {lives} lives. 💰 Starting allowance: {gold} Gold.")
    
    while lives > 0:
        print_divider()
        print(f"❤️ Lives: {lives} | 💰 Gold: {gold} | ⭐ Score: {score}")
        print("Options: Enter a number to guess, or type 'shop' to buy power-ups.")
        
        action = input("👉 Your action: ").strip().lower()
        
        # SHOP INTERACTIVE TRIGGER
        if action == "shop":
            while True:
                show_shop(gold, lives, shield_active)
                shop_choice = input("What would you like to buy? (1-4): ").strip()
                
                if shop_choice == "1":
                    if gold >= 15:
                        gold -= 15
                        # Give a structural hint calculation
                        diff = abs(secret_number - random.randint(1, max_num))
                        print(f"\n📡 SCANNER: The secret number is within {diff + 10} numbers of a random point!")
                    else:
                        print("\n❌ Not enough gold!")
                elif shop_choice == "2":
                    if gold >= 25:
                        gold -= 25
                        lives += 1
                        print(f"\n❤️ Purchased! Lives increased to {lives}.")
                    else:
                        print("\n❌ Not enough gold!")
                elif shop_choice == "3":
                    if shield_active:
                        print("\n🛡️ You already have a shield equipped!")
                    elif gold >= 20:
                        gold -= 20
                        shield_active = True
                        print("\n🛡️ Shield equipped! Your next wrong guess won't cost a life.")
                    else:
                        print("\n❌ Not enough gold!")
                elif shop_choice == "4" or shop_choice == "":
                    break
            continue

        # PROCESS STANDARD GUESS LAYOUTS
        try:
            guess = int(action)
            
            if guess < 1 or guess > max_num:
                print(f"⚠️ Out of bounds! Stay between 1 and {max_num}.")
                continue
                
            if guess == secret_number:
                reward = (lives * 15) * gold_multiplier
                score += (lives * 100)
                print(f"\n🎉 BOOM! You guessed it! The number was {secret_number}!")
                print(f"💰 You earned a victory bonus of {reward} Gold!")
                gold += reward
                
                # Check for continuous progression play
                continue_play = input("\n🔄 Keep your stash and advance to a new number? (yes/no): ").lower()
                if continue_play in ["yes", "y"]:
                    secret_number = random.randint(1, max_num)
                    lives = max_lives
                    print(f"\n🎲 New number locked! Lives reset to {lives}. Let's roll!")
                    continue
                else:
                    print(f"\n🏆 Final Run Complete! Ultimate Score: {score} | Banked Gold: {gold}")
                    break
            
            # Handling a wrong guess
            if shield_active:
                print("\n🛡️ SHIELD POPPED! Wrong guess, but your shield absorbed the damage. No life lost!")
                shield_active = False
            else:
                lives -= 1
                print("\n💥 Direct Hit! You lost a life.")
                
            if lives == 0:
                print(f"\n💀 GAME OVER! You ran out of lives. The secret number was: {secret_number}")
                break
                
            if guess < secret_number:
                print("📈 System Reading: TOO LOW!")
                gold += (2 * gold_multiplier) # Console pity gold rewards
            else:
                print("📉 System Reading: TOO HIGH!")
                gold += (2 * gold_multiplier)

        except ValueError:
            print("❌ Error: Type a valid number or 'shop'!")

    print("\n👋 Thanks for playing the Arcade Edition!")

if __name__ == "__main__":
    play_arcade_game()