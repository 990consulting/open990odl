# open990 -- Open IRS Form 990 Tools

`open990` is a free and open source command line tool for generating data extracts from the IRS Form 990 e-file dataset hosted on Amazon Web services. It is developed and maintained by [opendata.love](https://opendata.love), which specializes in IRS Form 990 analysis.

## Attribution

This package draws on an existing package, [`990_long`](https://github.com/CharityNavigator/990_long), published by [Charity Navigator](https://www.charitynavigator.org) under the [MIT License](https://opensource.org/licenses/MIT), the terms of which are available [here](https://opensource.org/licenses/MIT). The package consolidates individual XML-based 990 filings into a single Parquet file, then processes the filings into key value pairs that have been merged with the Nonprofit Open Data Collective's [990 concordance](https://github.com/Nonprofit-Open-Data-Collective/irs-efile-master-concordance-file).

## Author

[David Bruce Borenstein](https://github.com/borenstein) is the Director of Data Science at [opendata.love](https://opendata.love) and [990 Consulting, LLC](https://www.990consulting.com). Formerly of Charity Navigator, he created open-source software to turn IRS Form 990 into spreadsheets. He formed 990 Consulting and its sister site, opendata.love, to increase awareness and access to this remarkable dataset. Prior to Charity Navigator, he worked as a computational biologist at the Broad Institute MIT and Harvard. He holds a Ph.D. in Quantitative and Computational Biology from Princeton University.

## License

Copyright (c) 2017-2018 990 Consulting, LLC.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
