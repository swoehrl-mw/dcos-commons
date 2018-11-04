#!/usr/bin/env bash

export TEMPLATE_ELASTIC_VERSION=$(jq -r '.extra_template_parameters."elastic-version"' package_options.json)
export TEMPLATE_ELASTIC_STATSD_VERSION=$(jq -r '.extra_template_parameters."elastic-statds-version"' package_options.json)
export TEMPLATE_SUPPORT_DIAGNOSTICS_VERSION=$(jq -r '.extra_template_parameters."support-diagnostics-version"' package_options.json)
export TEMPLATE_SEARCHGUARD_VERSION=$(jq -r '.extra_template_parameters."searchguard-version"' package_options.json)
