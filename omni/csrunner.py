import os
import subprocess
import tempfile

class CSRunner(object):
  # def __init__(self, language, test_file):

  @staticmethod
  def run(code):
	source = tempfile.NamedTemporaryFile(suffix=".cs", delete=False)
	source.write(code)
	source.flush()
	subprocess.call(['gmcs', source.name])
	program = source.name.replace('.cs', '.exe')
	p = subprocess.Popen(['mono', program], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	result = p.communicate(code)[0]
	source.close()
	os.unlink(program)
	os.unlink(source.name)
	return result

  # def prepare(self):
    # virtualenv, pip, whatever