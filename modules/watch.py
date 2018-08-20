#!/bin/python
# coding: utf-8

from watchdog.events import FileSystemEventHandler
import os


class ChangeHandler(FileSystemEventHandler):
    def init(self, image_path):
        self.image_path = image_path

    def on_created(self, event):
        if event.is_directory:
            return
        if os.path.splitext(event.src_path)[-1].lower()\
           in [".jpg", ".png", ".gif"]:
            print("has been created {0}".format(event.src_path))
