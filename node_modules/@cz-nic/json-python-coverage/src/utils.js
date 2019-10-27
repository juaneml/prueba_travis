const fs = require('fs')
const yargs = require('yargs')

const { DEFAULT_REGEX, DEFAULT_FAIL_THRESHOLD } = require('./report_coverage')

function readFile(path, error_stream = process.stderr) {
    try {
        return JSON.parse(fs.readFileSync(path))
    } catch (err) {
        error_stream.write(`I/O Error: ${err}\n`)
        process.exit(1)
    }
}

function createArgv() {
    const argv = yargs
        .usage('Usage: $0 <json_filename> [options]')
        .command('$0 <json_filename>', '', yargs => {
            yargs.positional('json_filename', {
                describe: 'path to coverage-summary.json',
                type: 'string',
            })
        })
        .example(
            '$0 report.json -fail 90',
            'Parses JSON coverage from file, reports to readable python-coverage and checks coverage thresholds.'
        )
        .option('fail', {
            alias: 'f',
            describe:  'coverage fail threshold',
            default: DEFAULT_FAIL_THRESHOLD,
            type: 'number',
        })
        .option('regex', {
            alias: 'r',
            describe:  'path regex for reported files',
            default: DEFAULT_REGEX,
            type: 'string',
        })
        .help('h')
        .alias('h', 'help')
        .argv
    return argv
}

module.exports = { readFile, createArgv }
