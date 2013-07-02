import sys
import os
import tempfile
import subprocess
from behave import *
from omni import runnerfactory
from omni import katacontroller

@given('I have a password available')
def impl(context):
    assert True

@when('I execute the following code')
def impl(context):
  if os.environ.get('KATA_MODE') == 'true':
    if not hasattr(context, 'text'):
      context.text = katacontroller.KataController.createCode()
  assert hasattr(context, 'text') == True, 'No code'
  # import code
  # code.interact(local = locals())
  runnerfactory.RunnerFactory.create('python').run(context.text)

@then('It should succeed')
def impl(context):
  assert True

