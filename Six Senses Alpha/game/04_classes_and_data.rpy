# ============================================================================
#                               DATA & LOGIC
# ============================================================================

init python:
    class Item: 
        def __init__(self, name, description, image):
            self.name = name
            self.description = description
            self.image = image

    class Suspect:
        def __init__(self, name, bio, image):
            self.name = name
            self.bio = bio
            self.image = image
            self.descriptions = []
            self.status = "Person of Interest"

    inventory_list = []
    journal_list = []
    selected_item = None
    selected_suspect = None

    def add_item(name, desc, img):
        if not any(x.name == name for x in inventory_list):
            inventory_list.append(Item(name, desc, img))

    def add_suspect(name, bio, img):
        if not any(x.name == name for x in journal_list):
            journal_list.append(Suspect(name, bio, img))

    def record_clue(name, clue_text):
        for person in journal_list:
            if person.name == name:
                if clue_text not in person.descriptions:
                    person.descriptions.append(clue_text)
                    renpy.show_screen("item_get_message", message="Journal Updated: " + name)
                return          

    def has_pat_clue(keyword):
            for person in journal_list:
                if "Pat" in person.name:
                    for clue in person.descriptions:
                        if keyword.lower() in clue.lower():
                            return True
            return False

    class SlidingPuzzle:
        def __init__(self, tiles_val):
            self.tiles = tiles_val
            self.blank_index = self.tiles.index(0)

        def switch(self, tile_index):
            if tile_index in [self.blank_index-1, self.blank_index+1, self.blank_index-3, self.blank_index+3]:
                if not (self.blank_index % 3 == 0 and tile_index == self.blank_index - 1) and \
                   not (self.blank_index % 3 == 2 and tile_index == self.blank_index + 1):
                    self.tiles[self.blank_index], self.tiles[tile_index] = self.tiles[tile_index], self.tiles[self.blank_index]
                    self.blank_index = tile_index
                    renpy.restart_interaction()

        def is_solved(self):
            return self.tiles == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def start_puzzle():
        import random
        initial_tiles = [1, 3, 0, 4, 5, 6, 7, 8, 2]
        random.shuffle(initial_tiles)
        return SlidingPuzzle(initial_tiles)

default my_puzzle = None
