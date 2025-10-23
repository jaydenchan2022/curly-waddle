##### Benjamin Luo and Jayden Chan #####
from random import randint

def bananabid(my_player_number: int, my_bananas: int, monkey_position: int, opponent_bananas: int, past_bid_list: list, turn_number: int):
    if turn_number==1:
        return randint(1,17)+randint(1,17)+randint(1,17)
    elif monkey_position==2*(my_player_number*2-3):
        return my_bananas
    elif monkey_position==-2*(my_player_number*2-3):
        return min(my_bananas-4,opponent_bananas+1)
    elif my_bananas<=5:
        return 1
    else:
        lastBid=past_bid_list[turn_number-2][2-my_player_number]
        if lastBid>26 and lastBid<58:
            return min(my_bananas-abs(monkey_position-3*(my_player_number*2-3))+1,lastBid+randint(2,12))
        elif lastBid<=26:
            return min(my_bananas-abs(monkey_position-3*(my_player_number*2-3))+1,2*lastBid+randint(1,6))
        elif lastBid>=58:
            return min(my_bananas-abs(monkey_position-3*(my_player_number*2-3))+1,int(lastBid/2)+randint(2,12))
