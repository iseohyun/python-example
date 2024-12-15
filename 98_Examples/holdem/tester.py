import random
from rank import get_rank
from winner import get_winner

values = "AKQJT98765432"
shapes = "schd"

ranks = [
    "R. Flush",
    "S. Flush",
    "Four of Card",
    "Full House",
    "Flush",
    "Straight",
    "Triple",
    "Two pair",
    "One pair",
    "High card",
]

all_cards = [value + shape for value in values for shape in shapes]


def get_random_card():
    """랜덤 카드 생성 (예: Ah, Ks 등)"""
    # 1. [A ~ 2] 중에서 무작위로 선택
    value = random.choice(values)

    # 2. [schd] 중에서 무작위로 선택
    shape = random.choice(shapes)

    return value + shape


def gen_random_cards():
    cards = []
    while len(cards) < 7:
        card = get_random_card()
        if card not in cards:  # 중복 카드 방지
            cards.append(card)
    return cards


def gen_random_hand():
    hand = []
    while len(hand) < 2:
        card = get_random_card()
        if card not in hand:  # 중복 카드 방지
            hand.append(card)
    return hand


def add_random_player(players=[]):
    hand = []
    while len(hand) < 2:
        card = get_random_card()
        if (card not in hand) and all(
            card not in player for player in players
        ):  # 중복 카드 방지
            hand.append(card)
    return hand


def run_random(players):
    """Community Card를 반환합니다."""
    board = []
    while len(board) < 5:
        card = get_random_card()
        if all(card not in player for player in players):
            board.append(card)
    return board


def test_get_rank_multiple(times, loop=1_000_000):
    for j in range(times):
        num_of_rank = [0 for _ in range(10)]
        for i in range(loop):
            cards = gen_random_cards()
            rank = get_rank(cards)
            num_of_rank[rank[0]] += 1
        print(num_of_rank)


calc_data = [
    32,
    290,
    1600,
    26300,
    30300,
    45500,
    48000,
    235000,
    438000,
    175000,
]  # for 1_000_000


def test_get_rank():
    cards = gen_random_cards()
    # cards = ["Kh", "Ah", "6h", "Qh", "Th", "Jh", "2h"]  # ['R. Flush', {'AKQJT'}]
    # cards = ["3h", "Ah", "6h", "5h", "4h", "3h", "2h"] # ['S. Flush', {'65432'}]
    # cards = ["3h", "Ah", "6s", "5h", "4h", "3h", "2h"] # ['S. Flush', {'5432A'}]
    # cards = ["3h", "Kh", "Ks", "Kd", "Kc", "Qh", "2h"] # ['Four of Card', {'KKKK'}]
    # cards = ["3h", "Qd", "Js", "Jd", "Jc", "Qh", "3h"] # ['Full House', 'JJJQQ']
    # cards = ["3h", "Ah", "6s", "5h", "9h", "Kh", "2h"] # ['Flush', {'AK953'}]
    # cards = ["3s", "Ah", "6s", "5d", "4d", "3h", "2h"] # ['Straight', '65432']
    # cards = ["3s", "Ah", "9s", "5d", "4d", "3h", "2h"] # ['Straight', '5432A']
    # cards = ["3h", "Qd", "Js", "Jd", "Jc", "8h", "Ah"] # ['Triple', 'JJJAQ']
    # cards = ["3h", "Qd", "Js", "Jd", "Ac", "8h", "Ah"] # ['Two pair', 'AAJJQ']
    # cards = ["3h", "Qd", "Js", "Jd", "Ac", "8h", "9h"] # ['One pair', 'JJAQ9']
    # cards = ["3h", "Qd", "Js", "6d", "Ac", "8h", "9h"] # ['High card', 'AQJ98']
    rank = get_rank(cards)
    print(ranks[rank[0]], ":", rank[1])


def test_get_winner(num_of_player=2):
    players = []
    for i in range(num_of_player):
        players.append(add_random_player(players))
    print("players :", players)
    
    board = run_random(players)
    print("board :", board)

    winner = get_winner(players, board)
    print(winner)


### Test 1
# test_get_rank()

### test 2
# test_get_rank_multiple(1)

### test 3
# test_get_winner()

