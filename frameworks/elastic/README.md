# DC/OS Elastic Service Documentation

User documentation may be found at the [DC/OS Docs site](https://docs.mesosphere.com/services/elastic/).


## How to create a new release
1. Update versions in package_options.json
2. Build new binary release and upload package binaries to aws using `./upload_package.sh`
3. Prepare new Universe release by running `./prepare_universe.sh <local-universe-dir>` (e.g. `./prepare_universe.sh ~/projects/dcos/mw-universe/packages/E/elastic/2`, choose the lowest number not yet used).
4. Build and deploy a new local universe
