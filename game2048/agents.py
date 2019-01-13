import numpy as np
from keras.models import load_model
# model1 = load_model('E:/PyCharm 2018.2.4/2048_game/game2048/model_64_256_fifth.h5')
# model2 = load_model('E:/PyCharm 2018.2.4/2048_game/game2048/model_0_512_2.h5')

model = load_model('E:/PyCharm 2018.2.4/2048_game/game2048/model_0_512_2.h5')

class Agent:
    '''Agent Base.'''

    def __init__(self, game, display=None):
        self.game = game
        self.display = display

    def play(self, max_iter=np.inf, verbose=False):
        n_iter = 0
        while (n_iter < max_iter) and (not self.game.end):
            direction = self.step()
            self.game.move(direction)
            n_iter += 1
            if verbose:
                print("Iter: {}".format(n_iter))
                print("======Direction: {}======".format(
                    ["left", "down", "right", "up"][direction]))
                if self.display is not None:
                    self.display.display(self.game)

    def step(self):
        direction = int(input("0: left, 1: down, 2: right, 3: up = ")) % 4
        return direction


class RandomAgent(Agent):

    def step(self):
        direction = np.random.randint(0, 4)
        return direction


# 定义自己的agent
class MyOwnAgent(Agent):

    def __init__(self, game, display=None):
        super().__init__(game, display)
        self.board = self.game.board
        self.model = model

    def predict(self):
        return self.model.predict_on_batch(np.log2(self.game.board_log)[np.newaxis, :, :, np.newaxis])  # 棋盘取对数后进行预测

    def step(self):
        direction = self.predict().argmax()
        return direction


class ExpectiMaxAgent(Agent):

    def __init__(self, game, display=None):
        if game.size != 4:
            raise ValueError(
                "`%s` can only work with game of `size` 4." % self.__class__.__name__)
        super().__init__(game, display)
        from .expectimax import board_to_move
        self.search_func = board_to_move

    def step(self):
        direction = self.search_func(self.game.board)
        return direction
