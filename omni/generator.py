import os

class Generator(object):
  def __init__(self, language, test_file):
    self.language = language
    self.test_file = test_file
    self.test_name = os.path.splitext(test_file)[0]
    self.solution_file = os.path.join('solutions', language, self.test_name + self.extension())

  def my_tags(self):
    if os.access(self.solution_file, os.R_OK):
      return '@' + self.language
    else:
      return '@wip, @' + self.language

  def solution(self):
    if not os.access(self.solution_file, os.R_OK):
      return ''
    solution = open(self.solution_file, 'r').read()
    return solution.strip()

  def language(self):
    return self.language

  def extension(self):
    extensions = {
      'java': '.java',
      'cs': '.cs',
      'node': '.js',
      'php': '.php',
      'python': '.py',
      'ruby': '.rb',
      'go': '.go'
    }
    return extensions[self.language]

  def solution_file(self):
    test = os.path.splitext(self.test_name)[0]
    solution_file = os.path.join('solutions', self.language, test + self.extension())