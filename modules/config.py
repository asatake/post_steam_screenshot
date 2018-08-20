#!/bin/python
# coding: utf-8

import configparser
import os


class Config:
    def read_config(config_path):
        confp = configparser.ConfigParser()
        if os.path.exists(config_path):
            confp.read(config_path)
        else:
            confp["PATH"] = {"path": ""}
            confp["Twitter"] = {
                "key": "",
                "key_secret": "",
                "token": "",
                "token_secret": ""
            }
            confp["Mastodon"] = {
                "client": "",
                "client_secret": "",
                "token": ""
            }
            with open(config_path, "w") as cf:
                confp.write(cf)

        return confp

    def parse_config():
        return

    def write_config(path):
        return
