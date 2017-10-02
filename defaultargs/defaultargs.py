# -*- coding: UTF-8 -*-

from argparse import ArgumentParser


# -------------------------------------------------------------------------
def defaultargs(function):
    def parse_args(parser=None):
        if not parser:
            newParser = ArgumentParser(usage="%%prog [options]")
        else:
            newParser = parser

        newParser.add_argument(
            "--loglevel", "-l",
            help="[debug|info|warning|error|critical] default is info",
            choices=["debug", "info", "warning", "error", "critical"]
        )

        newParser.add_argument("--config", "-c",
                            help=("the full path to a"
                                  " custom configuration file")
                            )

        try:
            function(newParser)
        except TypeError:
            function()

        newParser.add_argument('args',
                            action="append",
                            nargs="*"
                            )
        return newParser
    return parse_args

# -------------------------------------------------------------------------
def databaseargs(function):
    @defaultargs
    def parse_args(parser=None):
        if not parser:
            newParser = ArgumentParser(usage="%%prog [options]")
        else:
            newParser = parser
        newParser.add_argument("--databases", "-d",
                            help=("<hostname> <database name> "
                                  "(and maybe use multiple times)"),
                            action="append",
                            metavar=("host", "database_name"),
                            nargs=2
                            )


        try:
            function(newParser)
        except TypeError:
            function()


        return newParser
    return parse_args
