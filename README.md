# perftracker-cp-crawler

perftracker-cp-crawler - a set of libraries and scripts to crawl web UI Control Panels (like Wordpress), integrated with the [perftracker](https://github.com/perfguru87/perftracker)

## Features

- selenium-based framework (on top of Chrome and Firefox browsers)
- python-based browser simulators
- page response time measurement
- individual HTTP request response time measurement
- export results to the perftracker server
- browser memory consumption tracking
- automatic login/logout with customizable:
  * login, password and submit buttons xpath/id/class names
  * automatic menu items recognition with customizsable:
  * menu item xpath
  * sub-menu item xpath
- page rendering phases recognition:
  * browser timing interface support
  * ajax request completion based on browser logs and pending HTTP requests
  * HTTP requests whitelisting to bypass websockets and long polls completion wait
- advanced reporting:
  * waterfall based requests view with information about requests size, compression, duration, status, etc
  * pages summary
  * HTML report with pages screenshot

## Installation

### MacOS

```
pip install -r requirements.txt
brew cask install chromedriver
chromedriver --version
brew cask install google-chrome
# install Google Chrome
```

### Linux

```
pip install -r requirements.txt
yum install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum install chromedriver
```

## Examples

Run selenium-based test on a real WordPress Admin panel:
```
python3 ./examples/pt-wp-crawler.py -m -U user -P user https://demo.wpjobboard.net/wp-login.php
```

## Contributing a patch

Make a change and test your code before commit:
```
python ./test.py
```
