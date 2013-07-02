#!/usr/bin/env python
from omni import generator
import pystache
import glob
import os

languages = ['java', 'cs', 'node', 'php', 'python', 'ruby', 'go']
tests = glob.glob('templates/*/*.feature.mustache')
for language in languages:
  for test in tests:
    test_name = test.replace('templates/', '').replace('.mustache', '')
    g = generator.Generator(language, test_name)
    template = open(test, 'r').read()
    renderer = pystache.Renderer(escape = lambda u: u)
    generated_test = renderer.render(template, g)
    # test_path = test.replace('templates/', '').replace('.mustache', '')
    output_file = os.path.join('features', language, test_name)
    if not os.path.exists(os.path.dirname(output_file)):
      os.makedirs(os.path.dirname(output_file))
    output = open(output_file, 'w')
    output.write(generated_test)
    output.flush
    output.close
    print output_file + " generated!"

