# WikiMathExtractor

WikiMathExtractor is a Python script to extract and clean text and mathematical formulas from a [Wikipedia database backup dump](https://dumps.wikimedia.org/), e.g. https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2 for English.
WikiMathExtractor is based on the original [WikiExtractor](https://github.com/attardi/wikiextractor) project.

This repository introduces an additional feature that allows the extraction of math elements (<math> tags) in addition to the standard text extraction functionality.

## Installation

The script can be invoked directly:

    python -m wikimathextractor.WikiMathExtractor <Wikipedia dump file>

## Usage

### WikiMathextractor
The script is invoked with a Wikipedia dump file as an argument:

    python -m wikimathextractor.WikiMathExtractor <Wikipedia dump file> [options]

The options are the same with those in wikiextractor.

## License
The code is made available under the [GNU Affero General Public License v3.0](LICENSE).
