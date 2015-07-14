#coding: utf-8
__author__ = 'Hikke Kun'

import renpy.exports as renpy

from location_manager import Location_Manager

class Game:
    """
    Base game class. Defines all game logic
    """

    location_manager = Location_Manager()

    #Закончилась ли игра
    ended = False
    #Текущая локация
    current_location = None

    _start_location = None

    def __init__(self):
        pass

    def start(self):
        """
        :return: None

        Starts the game. New or loaded.
        """
        #self.current_location = self.location_manager.get_location(self.start_location)
        #while not self.ended:
        #    self.current_location.stay()
        #pass
        renpy.call_screen("game_screen")

    def save(self, file='last.sav'):
        """
        :param file: файл в который вести сохнанение
        :return: True on success. False otherwise.

        Save this game
        """
        pass

    def load(self, file):
        """ Загрузка данных сохранения в этот объект игры

        :param file: файл сохранения
        :rtype Bool:
        :return: объект типа Game
        """
        pass

    @property
    def start_location(self):
        """

        :return: Start location name
        """
        return self._start_location

    @start_location.setter
    def start_location(self, value):
        self._start_location = value

    def say(self, who, what, interact=True):
        renpy.call_screen("game_screen", who, what, interact)