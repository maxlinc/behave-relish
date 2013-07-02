import os
import subprocess

class KataController(object):
  # def __init__(self, language, test_file):

  @staticmethod
  def createCode():
    args = os.environ["EDITOR"].split()
    import tempfile
    tempfile = tempfile.NamedTemporaryFile(suffix=".tmp")
    args.append(tempfile.name)
    subprocess.call(args)

  # def prepare(self):
    # virtualenv, pip, whatever