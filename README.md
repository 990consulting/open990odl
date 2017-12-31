# open990
Open IRS Form 990 Tools -- opendata.love

`open990` is a free and open source command line tool for generating data extracts from the IRS Form 990 e-file dataset hosted on Amazon Web services.

## Attribution

### Charity Navigator

This package draws on existing packages that were published by [Charity Navigator](https://www.charitynavigator.org) under the [MIT License](https://opensource.org/licenses/MIT), the terms of which are available [here](https://opensource.org/licenses/MIT).

* [`990_long`](https://github.com/CharityNavigator/990_long): consolidates individual XML-based 990 filings into a single Parquet file, then processes the filings into key value pairs that have been merged with the Nonprofit Open Data Collective's [990 concordance](https://github.com/Nonprofit-Open-Data-Collective/irs-efile-master-concordance-file).

* [`990_metadata`](https://github.com/CharityNavigator/990_metadata): crawls XML-based 990 filings and counts Xpath usage by version.

### Nonprofit Open Data Collective

This project also makes use of the [community concordance](https://github.com/Nonprofit-Open-Data-Collective/irs-efile-master-concordance-file), a draft of mappings from Xpaths to variables. The concordance was created by volunteers at the 2017 [Nonprofit Datathon](https://www.aspeninstitute.org/blog-posts/aspen-institutes-program-philanthropy-social-innovation-psi-hosts-nonprofit-datathon/) and Validatathon, which both took place at the Aspen Institute in 2017. The concordance was developed by multiple parties, and contributions have continued to be published without a copyright.

## Author

[David Bruce Borenstein](https://github.com/borenstein) is the Director of Data Science at [opendata.love](https://opendata.love) and [990 Consulting, LLC](https://www.990consulting.com). Formerly of Charity Navigator, he created open-source software to turn IRS Form 990 into spreadsheets. He formed 990 Consulting and its sister site, opendata.love, to increase awareness and access to this remarkable dataset. Prior to Charity Navigator, he worked as a computational biologist at the Broad Institute MIT and Harvard. He holds a Ph.D. in Quantitative and Computational Biology from Princeton University.

## License

Copyright (c) 2017-2018 990 Consulting, LLC.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
