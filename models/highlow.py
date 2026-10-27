import random

def draw_cards():
    suits = ("spades", "hearts", "diamonds", "clubs")
    deck = [
        {"suit": suit, "rank": rank}
        for suit in suits
        for rank in range(1, 14)
    ]
    return random.sample(deck, 2)

def judge(base_rank, result_rank, choice):
    if base_rank == result_rank:
        return "draw"

    if choice == "High":
        if result_rank > base_rank:
            return "win"
        else:
            return "lose"
    
    if choice == "Low":
        if result_rank < base_rank:
            return "win"
        else:
            return "lose"

    return "invalid"