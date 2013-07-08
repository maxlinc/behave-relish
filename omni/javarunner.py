import os
import subprocess

class JavaRunner(object):
  # def __init__(self, language, test_file):

  @staticmethod
  def run(code):
    p = subprocess.Popen(['groovy', 'features/steps/groovy_runner.groovy'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return p.communicate(code)[0]

  # def prepare(self):
    # virtualenv, pip, whatever