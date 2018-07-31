VERSION=2.4.0-6.3.1-mw2
S3_BUCKET=sebastianw-dcos-dev S3_DIR_PATH=packages S3_DIR_NAME=$VERSION ./build.sh aws $VERSION
