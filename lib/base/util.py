# -*- coding: utf-8 -*-
import os, sys, json, datetime
import configparser


class Util:
    @staticmethod
    def getConfig(file, section, key):
        config = configparser.ConfigParser()
        config.read(file)
        return config.get(section, key)
