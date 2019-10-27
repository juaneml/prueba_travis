const stream = require('stream')
const { report_coverage, DEFAULT_REGEX, DEFAULT_FAIL_THRESHOLD } = require('../src/report_coverage')
const { readFile } = require('../src/utils')

describe('Coverage reporter', () => {
    let mock_stream

    beforeEach(() => {
        mock_stream = new stream.Writable()
        mock_stream.buffer = ''
        mock_stream._write = (chunk, encoding, done) => {
            mock_stream.buffer += chunk
            done()
        }
    })

    test('matches snapshot', () => {
        const test_report = require('./test_reports/basic.json')
        report_coverage(test_report, DEFAULT_REGEX, DEFAULT_FAIL_THRESHOLD, mock_stream)
        expect(mock_stream.buffer).toMatchSnapshot()
    })

    test('checks dividing by zero', () => {
        const test_report = require('./test_reports/zero.json')
        process.exit = jest.fn()
        process.stdout.write = jest.fn()
        report_coverage(test_report, DEFAULT_REGEX, DEFAULT_FAIL_THRESHOLD, process.stdout, mock_stream)

        // checks error
        expect(mock_stream.buffer).toMatchSnapshot()

        // checks program terminating
        expect(process.exit).toHaveBeenCalledWith(1)
    })

    test('checks i/o error', () => {
        process.exit = jest.fn()

        readFile('./in_the_middle_of_nowhere', mock_stream)

        // checks error
        expect(mock_stream.buffer).toContain('I/O Error:')

        // checks program terminating
        expect(process.exit).toHaveBeenCalledWith(1)
    })
})
