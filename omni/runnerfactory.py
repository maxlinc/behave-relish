from omni import rubyrunner
from omni import pythonrunner
from omni import noderunner

class RunnerFactory(object):
  @staticmethod
  def create(language):
    map = {
      'java': None,
      'cs': None,
      'node': noderunner.NodeRunner,
      'php': None,
      'python': pythonrunner.PythonRunner,
      'ruby': rubyrunner.RubyRunner,
      'go': None
    }
    return map[language]
