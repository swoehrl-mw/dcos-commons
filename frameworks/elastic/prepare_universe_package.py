#!/usr/bin/env python3

import json
import sys
import os
from datetime import datetime

_jre_url = 'https://downloads.mesosphere.com/java/server-jre-8u172-linux-x64.tar.gz'
_libmesos_bundle_url = 'https://downloads.mesosphere.com/libmesos-bundle/libmesos-bundle-1.11.0.tar.gz'

_config_json_filename = 'config.json'
_marathon_json_filename = 'marathon.json.mustache'
_package_json_filename = 'package.json'
_resource_json_filename = 'resource.json'
_expected_package_filenames = [
    _config_json_filename,
    _marathon_json_filename,
    _package_json_filename,
    _resource_json_filename
]

class PackageBuilder(object):
    def __init__(self, package_name, package_version, upgrades_from, downgrades_to, artifact_url, extra_template_parameters, shasums):
        now = datetime.now()
        self._template_mapping = {
            'package-name': package_name,
            'package-version': package_version,
            'upgrades-from': upgrades_from, #json.dumps(upgrades_from),
            'downgrades-to': downgrades_to, #json.dumps(downgrades_to),
            'artifact-dir': artifact_url,
            'jre-url': _jre_url,
            'libmesos-bundle-url': _libmesos_bundle_url,
            "package-build-time-epoch-ms": str(int(now.timestamp()*1000)),
            "package-build-time-str": now.isoformat()
        }
        for path, shasum in shasums.items():
            self._template_mapping["sha256:"+path] = shasum
        for key, val in extra_template_parameters.items():
            self._template_mapping[key] = val


    def _apply_template_to_file(self, input_file_name, output_file_name):
        with open(input_file_name) as input_file:
            content = input_file.read()
        for key, val in self._template_mapping.items():
            content = content.replace('{{%s}}' % key, val)
        with open(output_file_name, "w") as output_file:
            output_file.write(content)


    def create_package(self, package_dir, target_dir):
        os.mkdir(target_dir)
        for filename in _expected_package_filenames:
            self._apply_template_to_file(os.path.join(package_dir, filename), os.path.join(target_dir, filename))


def _parse_shasums(data):
    shasums = dict()
    for line in data.split("\n"):
        if len(line) == 0:
            continue
        shasum, path = line.split()
        shasums[path.rsplit("/", 1)[1]] = shasum
    return shasums

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: %s <config.json> <shasums-file> <package-dir> <path-to-repo-dir>" % sys.argv[0])
        sys.exit(1)
    with open(sys.argv[1]) as config_file:
        config = json.load(config_file)
    with open(sys.argv[2]) as shasums_file:
        shasums = shasums_file.read()
        shasums = _parse_shasums(shasums)
    builder = PackageBuilder(config["name"], config["version"], config["upgrades_from"], config["downgrades_to"], config["artifact_url"]+"/"+config["version"], config.get("extra_template_parameters", dict()), shasums)
    builder.create_package(sys.argv[3], sys.argv[4])
