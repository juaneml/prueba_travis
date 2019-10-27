#! /usr/bin/env node

const { report_coverage } = require('./report_coverage')
const { createArgv, readFile } = require('./utils')

const argv = createArgv()
const json_file = readFile(argv.json_filename)
report_coverage(json_file, argv.regex, argv.fail)
