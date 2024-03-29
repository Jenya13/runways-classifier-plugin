# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AirportRunways
                                 A QGIS plugin
 This plugin classifying runways types based on their patterns
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-04-25
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Jenya Brodski
        email                : jekab596@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

class AirportRunways:
    """
    A class that used to store data of each airport (DTO)

    :ivar __icao: (International Civil Aviation Organization) Airport code or location indicator
    :type __icao: str
    :ivar __name: Airport name
    :type __name: str
    :ivar __runwaysNum: Number of runways in the specific airport
    :type __runwaysNum: int
    :ivar __runwaysData: List of data about each runway in the airport, contains, degrees length and
                        coordinates of the runway
    :type __runwaysData: list
    :ivar __location: Location of airport represented in EPSG:3857 Coordinates Reference System
    :type __location: list
    :ivar __model: Classification model of the runways
    :type __model: str
    :ivar __img: Digital map image of airport area
    :type __img: list

    """

    def __init__(self):
        """Constructor"""

        self.__icao = None
        self.__name = None
        self.__runwaysNum = None
        self.__runwaysData = None
        self.__location = None
        self.__model = None
        self.__img = None
        self.__model = None

    def setAirportName(self,name):
        """
        Set airport name

        :param name: Airport name
        :type name: str
        """
        self.__name = name

    def setIcaoCode(self,icao):
        """
        Set airport ICAO code

        :param icao: Civil aviation organization airport code
        :type icao: str
        """
        self.__icao = icao

    def setLocation(self, coords):
        """
        Set airport location

        :param coords: Airport coordinates in EPSG:3857 crs
        :type coords:  list
        """
        self.__location = coords

    def setRunwaysData(self, data):
        """
        Set airport runways data

        :param data: Data about airport runways, length, degrees and coordinates
        :type data: list
        """
        self.__runwaysData = data

    def setRunwaysNumber(self, num):
        """
        Set airport runways number

        :param num: Runways number
        :type num: int
        """
        self.__runwaysNum = num

    def setImg(self,img):
        """
        Set the image of airport area

        :param img: Digital image map of airport area
        :type img: numpy array
        """
        self.__img = img

    def setModel(self,model):
        """
        Add model's attribute to the dictionary

        :param data: A dictionary that store airport attributes
        :type data: dict
        :param model: Runways classification model
        :type model: str
        """
        
        self.__model = model

    def img2list(self):
        """
        Convert image representation in numpy array to list of lists

        :return: List of list with image pixels values
        :rtype: list
        """
        img = self.__img.tolist()
        return img

    def getClassificationData(self):
        data = {}
        data.update({"runways_num": self.__runwaysNum})
        data.update({"data": self.__runwaysData})
        return data

    def getData(self):
        """
        Preparing a dictionary from AirportRunways class attributes

        :return: Dictionary of AirportRunways class attributes
        :rtype: dict
        """
        data = {}
        data.update({"name": self.__name})
        data.update({"icao":self.__icao})
        data.update({"runways_num": self.__runwaysNum})
        data.update({"data": self.__runwaysData})
        data.update({"loc": self.__location})
        data.update({"model":self.__model})
        img = self.img2list()
        data.update({"image": img})

        return data

