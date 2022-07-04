import pygame
import random


class Board:    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]        
        self.left = 35
        self.top = 35
        self.cell_size = 60        
        self.empty_cells = []
        for j in range(height):
            for i in range(width):
                self.empty_cells.append((i, j))        
        self.crosses = True

    def render(self, screen, msg=''):        
        if msg:
            font = pygame.font.Font(None, 50)
            text = font.render(f"Game Over. {msg} =)", True, (210, 5, 5))
            text_x = 700 // 2 - text.get_width() // 2
            text_y = 670 - text.get_height() // 2
            screen.blit(text, (text_x, text_y))

        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.line(screen, pygame.Color("green"),
                                     (self.left + x * self.cell_size + 3,
                                      self.top + y * self.cell_size + 3),
                                     (self.left + x * self.cell_size - 3 + self.cell_size,
                                      self.top + y * self.cell_size - 3 + self.cell_size), 2)
                    pygame.draw.line(screen, pygame.Color("green"),
                                     (self.left + x * self.cell_size + 3,
                                      self.top + y * self.cell_size + self.cell_size - 3),
                                     (self.left + x * self.cell_size - 3 + self.cell_size,
                                      self.top + y * self.cell_size + 3), 2)
                if self.board[y][x] == 2:
                    pygame.draw.ellipse(screen, pygame.Color("black"), (
                        (self.left + x * self.cell_size + 3, self.top + y * self.cell_size + 3),
                        (self.cell_size - 6, self.cell_size - 6)), 2)
                pygame.draw.rect(screen, pygame.Color("black"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)
    
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    
    def on_click(self, cell):
        if self.crosses:
            if self.board[cell[1]][cell[0]] == 0:
                self.board[cell[1]][cell[0]] = 1
                self.crosses = not self.crosses
    
    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        if (cell_x, cell_y) in self.empty_cells:
            del self.empty_cells[self.empty_cells.index((cell_x, cell_y))]
        return cell_x, cell_y
    
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)
    
    def step_ii(self):
        if not self.crosses:
            cell_x, cell_y = random.choice(self.empty_cells)
            del self.empty_cells[self.empty_cells.index((cell_x, cell_y))]
            self.board[cell_y][cell_x] = 2
            self.crosses = not self.crosses
    
    def check_win(self):        
        for variant in [self.board, zip(*self.board), self.all_diag()]:
            d = [''.join([str(i) for i in j]) for j in variant]
            if any('11111' in i for i in d):
                print('AI Win')               
                return 1
            if any('22222' in i for i in d):
                print('Human Win')                
                return 2
            if all('0' not in i for i in d):
                print('no one won')
                return 3
        return 0

    def all_diag(self):
        l = len(self.board)
        b = l * 2 - 1
        ALL_DIAG = [[] for _ in range(b * 2)]
        for i in range(l):
            for j in range(l):
                ALL_DIAG[i + j].append(self.board[j][i])
                ALL_DIAG[i + j + b].append(self.board[~j][i])
        return ALL_DIAG


def result_game(screen, board):
    msg = ''
    res = board.check_win()
    global game_over
    if res == 1: 
        msg = 'AI Win'        
        game_over = True
    elif res == 2:        
        msg = 'Human Win'
        game_over = True
    elif res == 3:        
        msg = 'no one won'
        game_over = True
    screen.fill((255, 255, 255))
    board.render(screen, msg)
    pygame.display.flip()    

# def result_game_over():    
#     if  game_over == True: 
#         return True
#     return False


def main():
    pygame.init()
    size = 670, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Reverse tic-tac-toe')
    board = Board(10, 10)
    running = True
    global game_over
    game_over = False
    screen.fill((255, 255, 255))
    board.render(screen, '')
    pygame.display.flip()
    while running:
        msg = ''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and game_over == False:                
                board.get_click(event.pos)
                result_game(screen, board)
                # result_game_over()                
                board.step_ii()
                result_game(screen, board)
                # result_game_over()
    pygame.quit()


if __name__ == '__main__':
    main()