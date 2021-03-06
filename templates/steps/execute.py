import sys
import os
import tempfile
import subprocess
from behave import *
from omni import runnerfactory
from omni import generator
from omni import katacontroller

@given('I have a password available')
def impl(context):
    assert True

@when('I execute the following code')
def impl(context):
  if os.environ.get('KATA_MODE') == 'true':
    if not hasattr(context, 'text'):
      test_name = context.feature.filename.split("features/",1)[1]
      test_name = test_name.replace('_' + context.language, '')
      g = generator.Generator(context.language, test_name)
      g.kata()
  if os.environ.get('KATA_MODE') == 'shell':
    p = subprocess.Popen(['groovysh'], stdout=subprocess.PIPE)
    p.wait()
    context.output = p.stdout.read()
  else:
    assert hasattr(context, 'text') == True, 'No code'
    context.output = runnerfactory.RunnerFactory.create(context.language).run(context.text)
  print context.output
  print context.output

@then('It should succeed')
def impl(context):
  assert True
