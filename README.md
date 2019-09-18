# perftracker-cp-crawler

perftracker-cp-crawler - a set of libraries and scripts to crawl Control Panels (like Wordpress), integrated with client library for the [perftracker](https://github.com/perfguru87/perftracker)

Features:
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
