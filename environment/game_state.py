class GameState:

    def __init__(
        self,
        player_hp,
        player_max_hp,
        player_block,
        energy,
        gold,
        deck_size,
        discard_size,
        hand_size,
        enemy_hp,
        enemy_block,
        enemy_intent
        hand_size
        deck_size
        discard_size
    ):

        self.player_hp = player_hp
        self.player_max_hp = player_max_hp
        self.energy = energy
        self.gold = gold
        self.player_block = 0
        
        self.deck_size = deck_size
        self.discard_size = discard_size
        self.hand_size = hand_size

        self.enemy_hp = enemy_hp
        self.enemy_block = enemy_block
        self.enemy_intent = enemy_intent


    def to_vector(self):

        return [
            self.player_hp,
            self.player_max_hp,
            self.energy,
            self.gold,
            self.deck_size,
            self.discard_size,
            self.hand_size,
            self.enemy_hp,
            self.enemy_block,
            self.enemy_intent
        ]