#!/usr/bin/env python
import os
import re
import yaml

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    # import unicodedata
    # value = unicode(value)
    # value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = str(value)
    # value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    # value = unicode(re.sub('[-\s]+', '-', value))
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    value = re.sub('[-\s]+', '_', value)
    return value

class StatusReport(object):
    def __init__(self, output, yaml):
        self.output = output
        self.yaml = yaml

    def report(self):
        output = self.output
        self.write_header()
        for group in self.yaml['feature_groups']:
            for feature in group['features']:
                self.write_feature(group['name'], feature)
        output.flush()
        output.close()

    def write_header(self):
        output = self.output
        print >>output, 'Product | Feature | fog | php-opencloud | jclouds | pyrax | pkgcloud | openstack.net | gorax | gophercloud'
        print >>output, '--------|---------|-----|---------------|---------|-------|----------|---------------|-------|------------'

    def write_feature(self, feature_group, feature):
        output = self.output
        output.write(feature_group + '|')
        output.write(feature + '|')
        status = {
            'fog': self.determine_status(feature_group, feature, 'ruby'),
            'php': self.determine_status(feature_group, feature, 'php'),
            'jclouds': self.determine_status(feature_group, feature, 'java'),
            'pyrax': self.determine_status(feature_group, feature, 'python'),
            'pkgcloud': self.determine_status(feature_group, feature, 'node'),
            'net': self.determine_status(feature_group, feature, 'cs'),
            'gorax': self.determine_status(feature_group, feature, 'go'),
            'gophercloud': 'supported?'
        }
        output.write(status['fog'] + '|')
        output.write(status['php'] + '|')
        output.write(status['jclouds'] + '|')
        output.write(status['pyrax'] + '|')
        output.write(status['pkgcloud'] + '|')
        output.write(status['net'] + '|')
        output.write(status['gorax'] + '|')
        output.write(status['gophercloud'] + "\n")

    def determine_status(self, feature_group, feature, lang):
        test_file = os.path.join(slugify(feature_group), slugify(feature) + '.feature')
        from omni import generator
        solution_file = generator.Generator(lang, test_file).solution_file
        if os.path.isfile(solution_file):
            return 'test exists'
        else:
            return ''

feature_data = open('features.yaml', 'r').read()
features = yaml.load(feature_data)
output_file = 'features/readme.md'
if not os.path.exists(os.path.dirname(output_file)):
  os.makedirs(os.path.dirname(output_file))
output = open(output_file, 'w')
report = StatusReport(output, features)
report.report()
print output_file + " generated!"
