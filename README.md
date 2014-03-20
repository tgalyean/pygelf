pygelf - Python library for sending Graylog2 events over the Gelf HTTP input
======

Install
```
git clone https://github.com/tgalyean/pygelf.git
easy_install pygelf
```

Configuration
In the directory your code will run in you will need to create a config.ini containing your graylog instance details.

The global parameter allows you to create one config file containing all environments (dev/test/prod) while maintaining a single config.ini.
```
[global]
env = test
```
For each environment define your graylog instance
```
[test]
hostname = testgraylog.mydomain.com
port = 12201

[dev] 
hostname = devgraylog.mydomain.com
port = 12201

[prod]
hostname = prodgraylog.mydomain.com
port = 12201
```


