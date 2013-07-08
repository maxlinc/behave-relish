from omni import rubyrunner
from omni import pythonrunner
from omni import noderunner
from omni import javarunner
from omni import phprunner
from omni import gorunner
from omni import csrunner

class RunnerFactory(object):
  @staticmethod
  def create(language):
    map = {
      'java': javarunner.JavaRunner,
      'cs': csrunner.CSRunner,
      'node': noderunner.NodeRunner,
      'php': phprunner.PhpRunner,
      'python': pythonrunner.PythonRunner,
      'ruby': rubyrunner.RubyRunner,
      'go': gorunner.GoRunner
    }
    return map[language]
