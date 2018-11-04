VERSION=$(jq -r '.version' package_options.json)
S3_BUCKET=mw-universe S3_DIR_PATH=packages S3_DIR_NAME=$VERSION ./build.sh aws $VERSION
