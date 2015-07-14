init python:
    from lib.Game import Game
    # Да, инициируем игру во время init. Чтобы она не участвовала в сохранениях.
    game = Game()
    renpy.store.say = game.say

label start:

    "ololol"
    $ renpy.call_screen("game_screen","someone", "something", interact=True)
    "someone" "something"
    "trollolol"

    return

label load(file):
    $ game.load(file)
    $ game.start()