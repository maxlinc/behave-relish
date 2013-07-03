@given(u'I am setup to run example code for {lang}')
def step(context, lang):
  # pip, bundler, npm, whatever
  context.language = lang
