# Get (next) Five Holidays
> CLI that returns the next five holidays for a given country code.

get-five-holidays is a simple CLI that returns the five upcoming holidays for a country. The CLI utilizes the https://github.com/nager/Nager.Date REST API (https://github.com/nager/Nager.Date) to retrieve the next five holidays. 

To limit the amount of requests sent to the API endpoint, the CLI maintains a file based cache and keeps query results for a day per country. Queries to countries not found in cache will be routed to the API.

## Getting started

```sh
git clone https://github.com/odehne/get-five-holidays.git
cd get-five-holidays
python get-five-holidays.py it
```
## Usage example

The CLI expects the <countryCode> as an argument. The country code is a two letter acronym that represents countries, like: de, gb, us, it ...

```sh
python get-five-holidays.py <countryCode>
```
<!-- _For more examples and usage, please refer to the [Wiki][wiki]._ -->

## Development setup

You can either compile the CLI through python as shown in the usage example above. Or you create an executable using https://pypi.org/project/pyinstaller/:

```sh
pyinstaller --noconfirm --onedir --console "path/to/get-five-holidays/get-five-holidays.py"  
```

## Reference

+ [naga.date](https://github.com/nager/Nager.Date) - [README.md](https://github.com/nager/Nager.Date/blob/master/README.md)
+ [pyinstaller](https://github.com/pyinstaller/pyinstaller) - [README.md](https://github.com/pyinstaller/pyinstaller#readme)

## Meta

Oliver Dehne – oliver@cope-dehne.de   


<!-- Markdown link & img dfn's
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki  -->
