import numpy as np
from PIL import Image
from .repo import TILE_SIZE

# A world that is played by many players through ActiveWorld
# The grid of each World is the same, but the Entities within it vary for each ActiveWorld
# Each player has their own ActiveWorld, meaning everyone plays their own copy of the same "base" World.
class World:
    def __init__(self, dimensions, tile_repo):
        self.dimensions = dimensions

        # Non-dynamic blocks (walls, etc)
        self.grid = np.random.randint(1, size=dimensions, high=3) # TODO
        
        self.repo = tile_repo

        self.prerender_world()
        
    # Cache the 'grid' (non-dynamic blocks) as an image
    # This renders the *entire* world into a single image and keeps it for later use.
    def prerender_world(self):
        size = (self.dimensions[0] * TILE_SIZE, self.dimensions[1] * TILE_SIZE)
        image = Image.new("RGB", size)

        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                # get the block type and image for that block type
                block_type = BlockType(self.grid[x,y])
                block_img = self.repo.block(block_type)

                # paste onto the image
                coords = (x * TILE_SIZE, y * TILE_SIZE)
                image.paste(block_img, coords)

        self.image = image

        pass