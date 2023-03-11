# ch-urls.py
Check urls (status code, content length, content type, redirect)

## Usage: 
```
./ch-urls.py urls.txt
```
## Install:
```
git clone https://github.com/Weep2609/ch-urls.git
```
## Example:
```
$ ./bat_brute.py host.txt
https://help-test.kommunikations-dienste.de     [307]   [0]     [text/html; charset=UTF-8]      --> https://help-test.kommunikations-dienste.de/de/
http://www.mynfon.net   [301]   [162]   [text/html]     --> https://mynfon.net/
http://corporate.nfon.com       [301]   [161]   [text/html]     --> https://corporate.nfon.com/en/
http://mynfon.net       [301]   [162]   [text/html]     --> https://mynfon.net/
http://web-nwlp-4.nfon.com      [301]   [236]   [text/html; charset=iso-8859-1] --> https://web-nwlp-4.nfon.com/en/
http://help-test.kommunikations-dienste.de      [301]   [252]   [text/html; charset=iso-8859-1] --> https://help-test.kommunikations-dienste.de/de/
https://speedtest.cloud-cfg.com [200]   [377]   [text/html]
http://status.nfon.com  [301]   [167]   [text/html]     --> https://status.nfon.com/
http://speedtest.cloud-cfg.com  [301]   [240]   [text/html; charset=iso-8859-1] --> https://speedtest.cloud-cfg.com/
http://web-nwlp-13.nfon.com     [301]   [237]   [text/html; charset=iso-8859-1] --> https://web-nwlp-13.nfon.com/en/
https://www.mynfon.net  [301]   [162]   [text/html]     --> https://mynfon.net/
http://web-production.nfon.com  [301]   [229]   [text/html; charset=iso-8859-1] --> https://www.nfon.com/en/
```
