import configparser
import os
try:
    cfgs = ["/etc/pardus/greeter.conf"]
    if os.path.isdir("/etc/pardus/greeter.conf.d"):
        for cdir in os.listdir("/etc/pardus/greeter.conf.d/"):
            cfgs.append("/etc/pardus/greeter.conf.d/"+cdir)

    config = configparser.RawConfigParser()
    config.read(cfgs)
except:
    print("Failed to read config. Using defaults")
    config = []

print({section: dict(config[section]) for section in config.sections()})

def get(variable, default=None, section="pardus"):
    if section not in config:
        return default
    if variable not in config[section]:
        return default
    ret = config[section][variable]
    return str(ret)