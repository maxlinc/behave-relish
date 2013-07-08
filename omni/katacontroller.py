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
    code = open(tempfile.name, 'r').read()
    tempfile.close
    os.unlink(tempfile.name)
    return code

  @staticmethod
  def interactive():
    shell = 'groovysh'
    subprocess.call(args)
  # def prepare(self):
    # virtualenv, pip, whatever