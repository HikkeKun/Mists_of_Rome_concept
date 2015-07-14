#coding: utf-8
__author__ = 'Hikke Kun'

from location import Location

class Location_Manager:
    """
    Менеджер локаций игры.
    """

    # Список всех возможных локаций
    locations = []

    def __init__(self):
        pass

    def add_location(self, location):
        """ Добавление новой локации

        :param location:
        :return:
        """
        self.locations.append(location)
        return

    def get_location(self, name):
        """Возвращает локацию с заданным именем

        :param name:
        :rtype: Location
        :return:
        """
        for location in self.locations:
            if name == location.name:
                return location