import random

def riddle_challenge():
    # Simulate a riddle challenge
    print("Answer this riddle to continue:")
    print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    user_answer = input("Your answer: ").lower()
    return user_answer == "an echo"

def visual_puzzle_challenge():
    # Simulate a visual puzzle challenge
    print("Solve this visual puzzle to continue:")
    print("   * * * ")
    print(" *       * ")
    print("   * * * ")
    user_answer = input("What is the shape in the middle? ").lower()
    return user_answer == "triangle"

def memory_challenge():
    # Simulate a memory challenge
    print("Engage in this memory challenge:")
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    random.shuffle(words)
    print("Remember the order of these words:", words)
    user_order = input("Enter the words in the correct order, separated by spaces: ").lower().split()
    return user_order == words

def play_puzzling_portals():
    # Simulate the "Realm of Puzzling Portals" game
    current_portal = 1
    final_portal = 6

    while current_portal < final_portal:
        roll = random.randint(1, 6)
        print(f"Player rolls a {roll}.")

        current_portal += roll
        current_portal = min(current_portal, final_portal)  # Ensure we don't go beyond the final portal

        print(f"Player moves to Portal {current_portal}.")

        # Choose a challenge based on portal difficulty
        if 1 <= current_portal <= 2:
            success = riddle_challenge()
        elif 3 <= current_portal <= 4:
            success = visual_puzzle_challenge()
        else:
            success = memory_challenge()

        if not success:
            print("Challenge failed. Player must roll again on the next turn.")

    print("Congratulations! Player reached the final destination portal and successfully completed the challenge.")

# Run the game
play_puzzling_portals()