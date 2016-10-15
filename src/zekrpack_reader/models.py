# coding: utf-8

"""
Created on 22 avr. 2010

@author: Assem Chelli
@contact: Assem.ch [at] gmail.com
@license: AGPL
"""

import os.path
import re
from zipfile import ZipFile


class Ta7rif(Exception):
    """Raise when there is an error in Quran text  """

    def __init__(self, type_=u"new", value=u"undefined", original=None, aya_gid=None, msg=""):
        self.type = type_
        self.aya_gid = aya_gid
        self.value = value
        self.original = original
        self.msg = msg

    def __str__(self):
        return "\nTa7rif in Holy Quran :\n\tType:" + str(self.type) + "\n\tvalue:" + str(
            self.value) + "\n\toriginalvalue:" + str(self.original) + "\n\taya_gid:" + str(self.aya_gid) + "\n\n" + str(
            self.msg)


class TranslationModel:
    def __init__(self, path="./example.zip"):
        if not os.path.exists(path):
            raise Exception("path does not exist!!")

        if os.path.isfile(path):
            self.path = self.open_zip(path)
        else:
            raise Exception("type of path is not defined : %s" % path)

    def open_zip(self, zip_path, temp="/tmp/alfanous/"):
        zip_file = ZipFile(zip_path)
        if not os.path.exists(temp):
            os.mkdir(temp)
        zip_file.extractall(temp)
        return temp

    def translation_properties(self):
        """ get the properties of the translation """
        tpfile = open(self.path + "translation.properties", "r")
        wordrx = re.compile("[^=\r\n#]+")
        d = {}
        for line in tpfile.readlines():
            res = wordrx.findall(line)
            if len(res) == 2:
                d[res[0]] = res[1]

        return d

    def translation_lines(self, props):
        """ return the lines list of translation """
        tfile = open(self.path + props["file"], "r")
        linerx = re.compile("[^" + props["lineDelimiter"] + "]+")
        return linerx.findall(tfile.read())

    def document_list(self):
        """ a generator of documents
        :raise: A ta7rif exception if the number of lines is not 6236
        """
        properties = self.translation_properties()
        lines = self.translation_lines(properties)
        if len(lines) != 6236:
            raise Ta7rif(type_="ayas number", value=unicode(len(lines)), original="6236",
                         msg="the number of lines is not 6236")
        for i in range(6236):
            doc = {"gid": i + 1, "id": properties["id"].decode(properties["encoding"]),
                   "text": lines[i].decode(properties["encoding"]), "type": u"translation",
                   "lang": properties["language"].decode(properties["encoding"]),
                   "country": properties["country"].decode(properties["encoding"]),
                   "author": properties["name"].decode(properties["encoding"]),
                   "copyright": properties["copyright"].decode(properties["encoding"]), "binary": None}
            yield doc
