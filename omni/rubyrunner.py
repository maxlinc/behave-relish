import os
import subprocess

class RubyRunner(object):
  # def __init__(self, language, test_file):

  @staticmethod
  def run(code):
    p = subprocess.Popen(['ruby'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return p.communicate(code)[0]

  # def prepare(self):
    # virtualenv, pip, whatever