#!/usr/bin/env bash
set -e


if [ $# -lt 1 ]; then
    echo "Usage: prepare_universe.sh <target_dir>"
    exit 1
fi

TARGET_DIR=$1
FRAMEWORK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT_DIR=$(dirname $(dirname $FRAMEWORK_DIR))

sha256sum  $REPO_ROOT_DIR/sdk/cli/dcos-service-cli* > shasums

./prepare_universe_package.py package_options.json shasums universe $TARGET_DIR
