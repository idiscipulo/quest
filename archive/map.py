import imageio as iio

class Map:
    def __init__(self, path:str):
        img = iio.imread(path)
        img_width = len(img)
        img_height = len(img[0])

        self.tiles = [[0] * img_height for x in range(img_width)]
        
        for x in range(img_width):
            for y in range(img_height):
                if sum(img[x][y]) > 0:
                    self.tiles[x][y] = 1

    def __repr__(self):
        out = ""

        for row in self.tiles:
            for val in row:
                if val > 0:
                    out = f"{out}█"
                else:
                    out = f"{out} "
            out = f"{out}\n"

        return out

if __name__ == "__main__":
    map = Map("test_map.bmp")
    print(map)
