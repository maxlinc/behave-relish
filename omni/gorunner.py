import os
import subprocess
import tempfile

class GoRunner(object):
  # def __init__(self, language, test_file):

  @staticmethod
  def run(code):
	source = tempfile.NamedTemporaryFile(suffix=".go", delete=False)
	source.write(code)
	source.flush()
	p = subprocess.Popen(['go', 'run', source.name], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	result = p.communicate(code)[0]
	source.close()
	os.unlink(source.name)
	return result

  # def prepare(self):
    # virtualenv, pip, whatever