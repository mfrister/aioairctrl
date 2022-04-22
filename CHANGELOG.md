# Changelog

## 0.4.1

* Add type annotations, verified by mypy in strict mode.
* Add linters black, flake8, isort and run them on GitHub Actions.

## 0.4.0

* Add an auto-reconnecting client mapping to Python data structures resulting in a much simpler, although incomplete API.

## 0.3.1

* Removed a monkey patch for aiocoap's `MessageManager._deduplicate_message`. The patch might conflict with other libraries using aiocoap and testing didn't result in any issues without the patch.

## 0.3.0

* Forked [betaboon's aioairctrl project](https://github.com/betaboon/aioairctrl).
* Renamed from aioairctrl to phipsair.
* Minor cleanups.
