#coding: utf-8
__author__ = 'Hikke Kun'
import renpy.exports as renpy

class Location:
    """
    Локация
    """

    name = u'Название локации'
    _onEnter = None
    _onExit = None
    _stay = None

    #Вошли ли мы уже в локацию.
    entered = False

    def __init__(self, name, onEnter=None, onExit=None, stay=None):
        """

        :param name: Location name
        :return:
        """
        self.name = name

    def on_enter(self):
        """ При заходе в локацию

        :return:
        """
        self.entered = True
        if self._onEnter is not None:
            renpy.call(self._onEnter)

    def on_exit(self):
        """ При выходе из локации.

        :return:
        """
        if self._onExit is not None:
            renpy.call(self._onExit)
        self.entered = False

    def stay(self):
        """ При нахождении в локации.

        :return:
        """
        if self._stay is not None:
            renpy.call(self._stay)