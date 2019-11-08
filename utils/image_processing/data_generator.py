# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DataGenerator
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

from .image_processor import ImageProcessor
from .runways_data_extractor import RunwaysDataExtractor


class DataGenerator:
    """ Class that generate data"""
    
    @staticmethod
    def generateData(path, icao, airportName):
        """
        generate data from given image

        :param path: Path to directory where image stored
        :param icao: icao code
        :param airportName: airport name

        :return: data about airport runways include image of the area
        :rtype: dictionary
        """
        img = ImageProcessor.processImg(path)
        rde = RunwaysDataExtractor(img,path,icao,airportName)
        data = rde.extractData()
        return data