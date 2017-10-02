# /usr/bin/env python
# -*- coding: UTF-8 -*-

from defaultargs.defaultargs import ArgumentParser, defaultargs, databaseargs


# ----------------------------------------------------------------------
def main():

  x = default_arguments().parse_args()
  print(x)

  y = database_arguments().parse_args()
  print(y)

  z = custom_arguments(ArgumentParser(usage="%%prog [options]")).parse_args()
  print(z)

# ----------------------------------------------------------------------
@defaultargs
def default_arguments():
  pass

# ----------------------------------------------------------------------
@databaseargs
def database_arguments():
  pass


# ----------------------------------------------------------------------
@databaseargs
def custom_arguments(parser):
  parser.add_argument(
      "--test", "-t",
            help="use the testing environment",
            action="store_true"
    )
  return parser


# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()