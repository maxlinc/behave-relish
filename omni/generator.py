import os

class Generator(object):
  def __init__(self, language, test_file):
    self.language = language
    self.test_file = test_file
    self.test_name = os.path.splitext(test_file)[0]
    self.solution_file = os.path.join('solutions', language, self.test_name + self.extension())

  def my_tags(self):
    if os.access(self.solution_file, os.R_OK):
      return ['@' + self.language]
    else:
      return ['@wip', '@' + self.language]

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

  def expected(self):
    return """
Name: 512MB Standard Instance
  ID: 2
  RAM: 512
  Disk: 20
  VCPUs: 1

Name: 1GB Standard Instance
  ID: 3
  RAM: 1024
  Disk: 40
  VCPUs: 1

Name: 2GB Standard Instance
  ID: 4
  RAM: 2048
  Disk: 80
  VCPUs: 2

Name: 4GB Standard Instance
  ID: 5
  RAM: 4096
  Disk: 160
  VCPUs: 2

Name: 8GB Standard Instance
  ID: 6
  RAM: 8192
  Disk: 320
  VCPUs: 4

Name: 15GB Standard Instance
  ID: 7
  RAM: 15360
  Disk: 620
  VCPUs: 6

Name: 30GB Standard Instance
  ID: 8
  RAM: 30720
  Disk: 1200
  VCPUs: 8
"""