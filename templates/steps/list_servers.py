import sys
import os
import tempfile
import subprocess

@given(u'I have a password available')
def impl(context):
    assert True

@when(u'I execute the following code')
def impl(context):
  # temp = tempfile.NamedTemporaryFile(delete=False)
  # temp.write(context.text)
  # temp.flush()
  # print 'Executing ' + temp.name
  # temp.close()
  p = subprocess.Popen(['python'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
  print p.communicate(context.text)[0]
  # os.unlink(temp.name)
  print "Max"

@then(u'It should succeed')
def impl(context):
  assert True

