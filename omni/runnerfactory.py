from omni import rubyrunner
from omni import pythonrunner

class RunnerFactory(object):
  @staticmethod
  def create(language):
    map = {
      'java': None,
      'cs': None,
      'node': None,
      'php': None,
      'python': pythonrunner.PythonRunner,
      'ruby': rubyrunner.RubyRunner,
      'go': None
    }
    return map[language]
