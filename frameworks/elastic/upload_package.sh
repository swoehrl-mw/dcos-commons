VERSION=2.4.0-6.4.2-mw1
S3_BUCKET=mw-universe S3_DIR_PATH=packages S3_DIR_NAME=$VERSION ./build.sh aws $VERSION
