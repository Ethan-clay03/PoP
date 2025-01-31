import os
from PIL import Image, ImageSequence

# Conway’s Game of Life
class GameOfLife:
    
    #Construct class
    def __init__(self, frames, x, y):
        self.data = [[[False for _ in range(x)] for _ in range(y)] for _ in range(frames)]

    #
    def get_previous_cell(self, current_frame, x, y):
        if 0 <= x < len(self.data[0]) and 0 <= y < len(self.data[0][0]):
            return self.data[current_frame][x][y]
        return False
    
    #
    def get_prev_neighbours(self, frame, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        live_neighbors = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.data[frame]) and 0 <= ny < len(self.data[frame][0]):
                if self.get_previous_cell(frame, nx, ny):
                    live_neighbors += 1
        return live_neighbors

    def underpopulation(self, frame, x, y):
        return self.get_previous_cell(frame, x, y) and self.get_prev_neighbours(frame, x, y) < 2

    def overpopulation(self, frame, x, y):
        return self.get_previous_cell(frame, x, y) and self.get_prev_neighbours(frame, x, y) > 3

    def reproduction(self, frame, x, y):
        return not self.get_previous_cell(frame, x, y) and self.get_prev_neighbours(frame, x, y) == 3

    def stasis(self, frame, x, y):
        return self.get_previous_cell(frame, x, y) and (self.get_prev_neighbours(frame, x, y) == 2 or self.get_prev_neighbours(frame, x, y) == 3)

    def evolve(self):
        all_frames = [self.data[0]] 

        for frame in range(1, len(self.data)):
            next_frame = [[False for _ in range(len(self.data[0][0]))] for _ in range(len(self.data[0]))]

            for x in range(len(self.data[0])):
                #Run through the rules in order, update cells to be living or dead
                for y in range(len(self.data[0][0])):
                    if self.underpopulation(frame - 1, x, y) or self.overpopulation(frame - 1, x, y):
                        next_frame[x][y] = False
                    elif self.reproduction(frame - 1, x, y):
                        next_frame[x][y] = True
                    elif self.stasis(frame - 1, x, y):
                        next_frame[x][y] = True
                    else:
                        next_frame[x][y] = False

            self.data[frame] = next_frame
            # Add Frame to stack
            all_frames.append(next_frame)

        return all_frames

    def set_start_grid(self, file_name, size_x, size_y):
        line_number = 1
        with open(file_name, 'r') as file:
            for line in file:
                try:
                    x, y = map(int, line.split())
                    if 0 <= x < size_x and 0 <= y < size_y:
                        self.data[0][x][y] = True
                except ValueError:
                    line = line.strip()
                    if not line:
                        print(f"Invalid line (number {line_number}) Reason: Blank Row")
                    else:
                        print(f"Invalid line (number {line_number}) Reason: Not Two Integers, line values entered - {line}")
                line_number += 1

    def generate_gif(self, filename, frame_duration):
        frames = self.evolve() 
        rows, cols = len(self.data[0]), len(self.data[0][0])
        images = []

        for frame in frames:
            img = Image.new('RGB', (cols, rows))
            for i, row in enumerate(frame):
                for j, col in enumerate(row):
                    img.putpixel((j, i), (255, 255, 255) if col else 0)
            images.append(img)

        # Save the images as a GIF.
        images[0].save(f"{filename}.gif", format="GIF", append_images=images[1:], save_all=True, duration=frame_duration, loop=0)


if __name__ == '__main__':
    f, x, y = 100, 100, 100
    game = GameOfLife(f, x, y)
    game.set_start_grid('initial_grid.txt', x, y)
    #Change second value below to speed up / slow down gif. Lower number = quicker
    game.generate_gif('game_of_life', 200)
