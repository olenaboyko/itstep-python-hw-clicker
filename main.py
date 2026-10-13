import tkinter as tk

BOMB_START = 100
SCORE_START = 0

root = tk.Tk()
root.title("Game")
root.geometry("600x600+500+400")
# root.iconbitmap("bomb.ico")

label = tk.Label(root, text='Press [enter] to start the game', font=('Comic Sans MS', 12))
label.pack()
fuse_label = tk.Label(root, text=f'Fuse: {str(BOMB_START)}', font=('Comic Sans MS', 14))
fuse_label.pack()
score_label = tk.Label(root, text=f'Score: {str(SCORE_START)}', font=('Comic Sans MS', 14))
score_label.pack()

img_1 = tk.PhotoImage(file="./img/bomb_normal.gif")
img_2 = tk.PhotoImage(file="./img/bomb_no.gif")
img_3 = tk.PhotoImage(file="./img/pow.gif")

bomb_label = tk.Label(image=img_1)
bomb_label.pack()

class Game:
  def __init__(self, bomb, score):
    self.__bomb = 0
    self.__score = 0
    self.__bomb_default = bomb
    self.__score_default = score

  def __clear(self):
    self.__bomb = self.__bomb_default
    self.__score = self.__score_default

  def start(self):
    if not self.is_alive():
      self.__clear()
      self.update_bomb(0)
      self.update_score(0)
      self.update_display()
      label.config(text='')

  def is_alive(self):
    if self.__bomb <= 0:
      self.__bomb = 0
      return False
    else:
      return True

  def update_bomb(self, add_count):
    if self.is_alive():
      self.__bomb += add_count
      self.update_display()
      bomb_label.after(400, lambda: self.update_bomb(-5))

  def update_score(self, add_count):
    if self.is_alive():
      self.__score += add_count
      self.update_display()
      score_label.after(3000, lambda: self.update_score(1))

  def click(self):
    if self.is_alive():
      self.__bomb += 1

  def update_display(self):
    if self.__bomb >= 60:
      bomb_label.config(image=img_1)
    elif 0 < self.__bomb < 60:
      bomb_label.config(image=img_2)
    else:
      bomb_label.config(image=img_3)

    if self.__bomb >= 0:
      fuse_label.config(text='Fuse: ' + str(self.__bomb))

    if self.__bomb <= 0:
      label.config(text='Bang! Bang! Bang!')
      fuse_label.config(text='Fuse: ' + str(0))

    if self.__score >= 0:
      score_label.config(text='Score: ' + str(self.__score))



my_game: Game | None = None

def start(event):
  global my_game
  if my_game is None:
    my_game = Game(BOMB_START, SCORE_START)

  if my_game is not None:
    my_game.start()

def click():
  global my_game
  if isinstance(my_game, Game):
    my_game.click()

click_button = tk.Button(root, text='Click me', bg='black', fg='white', width=15, font=('ComicSans MS', 14), command=click)
click_button.pack()
root.bind('<Return>', start)

def handle_s_press(event):
  click()

root.bind('<s>', handle_s_press)
root.bind('<S>', handle_s_press)

root.mainloop()
