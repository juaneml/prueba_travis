const path  = require('path')

const DEFAULT_REGEX = '', DEFAULT_FAIL_THRESHOLD = 0

function report_coverage(json_file, regex_pattern = DEFAULT_REGEX, fail_threshold = DEFAULT_FAIL_THRESHOLD,
    report_stream = process.stdout, error_stream = process.stderr
) {
    report_stream.write(`${'Name'.padEnd(55)} ${'Stmts'.padStart(6)} ${'Miss'.padStart(6)} `)
    report_stream.write(`${'Branch'.padStart(6)} ${'BrPart'.padStart(6)} ${'Cover'.padStart(6)}\n`)
    report_stream.write('\n'.padStart(91, '-'))

    const regex = new RegExp(regex_pattern)
    let statements_total = 0, statements_covered = 0, branches_total = 0, branches_covered = 0

    for (const report_property in json_file) {
        if (report_property === 'total')
            continue
        const js_path = path.relative('.', report_property)
        if (!regex.test(report_property))
            continue

        const json_data = json_file[report_property]

        report_stream.write(js_path.padEnd(55))
        report_stream.write(json_data.statements.total.toString().padStart(7))
        report_stream.write((json_data.statements.total - json_data.statements.covered).toString().padStart(7))
        report_stream.write(json_data.branches.total.toString().padStart(7))
        report_stream.write((json_data.branches.total - json_data.branches.skipped).toString().padStart(7))
        report_stream.write(`${Math.round(((json_data.statements.covered + json_data.branches.covered)
            / (json_data.statements.total + json_data.branches.total)) * 100)}%`.padStart(7))
        report_stream.write('\n')

        statements_total += json_data.statements.total
        statements_covered += json_data.statements.covered
        branches_total += json_data.branches.total
        branches_covered += json_data.branches.covered
    }

    if (statements_total + branches_total === 0) {
        error_stream.write('There are no matching files or all matching files are empty.\n')
        process.exit(1)
    }
    const total_coverage = Math.round((statements_covered + branches_covered)
        / (statements_total + branches_total) * 100)

    report_stream.write('\n'.padStart(91, '-'))
    report_stream.write('TOTAL'.padEnd(55))
    report_stream.write(statements_total.toString().padStart(7))
    report_stream.write((statements_total - statements_covered).toString().padStart(7))
    report_stream.write(branches_total.toString().padStart(7))
    report_stream.write((branches_total - branches_covered).toString().padStart(7))
    report_stream.write(`${total_coverage}%`.padStart(7))
    report_stream.write('\n')

    if (total_coverage < fail_threshold)
        process.exit(1)
}

module.exports = { report_coverage, DEFAULT_REGEX, DEFAULT_FAIL_THRESHOLD }
