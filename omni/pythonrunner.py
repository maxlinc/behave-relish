import os
import subprocess

class PythonRunner(object):
  # def __init__(self, language, test_file):

  @staticmethod
  def run(script):
    p = subprocess.Popen(['python'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return p.communicate(script)[0]

  # def prepare(self):
    # virtualenv, pip, whatever