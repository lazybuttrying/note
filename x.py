from typing import List, Dict

def vcg_auction(bids: Dict[str, int]) -> Dict[str, int]:
    """
    Implements the VCG auction for a single-item setting.
    """
    if not bids:
        print("No bids received. Auction cannot proceed.")
        return {"winner": None, "payment": 0}
    
    # Print background to console
    print("\n=== VCG Auction Mechanism ===")
    print("The VCG (Vickrey-Clarke-Groves) mechanism ensures truthful bidding and efficiency.")
    print("In a single-item auction, the highest bidder wins but pays the second-highest bid.")
    print("The mechanism follows the formula: \n y_i = C - Σ_{j \neq i} u_j (excluding i's value from the sum).")
    print("A project is undertaken if y_i > 0, ensuring truth-telling as the dominant strategy.")
    
    # Log the original bids
    print("\nReceived bids:")
    for bidder, bid in bids.items():
        print(f"{bidder}: {bid}")
    
    # Sort bidders by bid value in descending order
    sorted_bidders = sorted(bids.items(), key=lambda x: x[1], reverse=True)
    print("\nSorted bidders (highest to lowest bid):")
    for bidder, bid in sorted_bidders:
        print(f"{bidder}: {bid}")
    
    # Winner is the highest bidder
    winner, highest_bid = sorted_bidders[0]
    print("\nWinner:", winner, "with bid:", highest_bid)
    
    # Price is the second-highest bid
    second_highest_bid = sorted_bidders[1][1] if len(sorted_bidders) > 1 else 0
    print("Payment required (second highest bid):", second_highest_bid)
    
    # Proof process
    print("\n=== Proof of VCG Mechanism ===")
    print("1. The mechanism ensures incentive compatibility: Each bidder maximizes utility by bidding truthfully.")
    print("2. The highest bidder wins the auction.")
    print("3. The winning bidder pays the opportunity cost imposed on other bidders, which is the second-highest bid.")
    print("4. This ensures that bidders are not incentivized to manipulate their bids.")
    
    print("\nTwo strategic choices exist, each with three possible cases:")
    print("\nCase 1: The bidder wins")
    print(f"   - {winner} bids truthfully: Pays the second-highest bid ({second_highest_bid}) and maximizes utility.")
    print(f"     - Utility calculation: u = {highest_bid} - {second_highest_bid}.")
    print(f"   - {winner} overbids: Still wins but pays the same amount ({second_highest_bid}), no incentive to overbid.")
    print(f"     - Since bid ({highest_bid}) > second-highest bid ({second_highest_bid}), payment remains the same.")
    print(f"   - {winner} underbids: May lose the auction, risking lower utility.")
    print(f"     - If bid < second-highest bid ({second_highest_bid}), the bidder loses and gets utility = 0.")
    
    print("\nCase 2: The bidder loses")
    for loser, bid in sorted_bidders[1:]:
        print(f"   - {loser} bids truthfully: Does not win and pays nothing.")
        print(f"     - Utility = 0 since no payment is made.")
        print(f"   - {loser} overbids: If it does not exceed {winner}'s bid ({highest_bid}), still loses and pays nothing.")
        print(f"     - If bid ({bid}) < highest bid ({highest_bid}), utility = 0.")
        print(f"   - {loser} underbids: Still loses and pays nothing.")
        print(f"     - If bid ({bid}) < highest bid ({highest_bid}), utility = 0.")
    
    print("\nConclusion: The optimal strategy is to bid truthfully, as any deviation results in the same or worse outcome.")
    print(f"\nFinal proof: {winner} wins by bidding {highest_bid}, but only pays {second_highest_bid}.")
    print("This ensures truthful bidding as overbidding does not reduce cost, and underbidding may lead to losing.")
    
    return {"winner": winner, "payment": second_highest_bid}

# Example usage
bids = {"Alice": 100, "Bob": 150, "Charlie": 130}
print("\n=== Auction Result ===")
print(vcg_auction(bids))

