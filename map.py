# Description: The map class handles the drawing of the map.
import pygame as pg

_ = False
mini_map = [
    # 1 = wall _ = empty
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, _, 1, 1, _, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, 1, 1, _, _, _, 1, _, 1, _, _, 1],
    [1, _, _, _, _, 1, 1, _, _, _, 1, _, 1, _, _, 1],
    [1, _, _, _, _, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
        
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, col in enumerate(row):
                if col:
                    self.world_map[(i, j)] = col
                    
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2) for pos in self.world_map]