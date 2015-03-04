def read_configuration():
    """Reads the configuration for trump and the sources"""

    import os
    import ConfigParser
    
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    config_dir = os.path.join(cur_dir,"config")
    config_files = [(f,f[:-4]) for f in os.listdir(config_dir) if f[-4:] == ".cfg"]
    
    config = {}
    
    for fil,src in config_files:
        config[src] = {}
        cp = ConfigParser.ConfigParser()
        cp.read(os.path.join(config_dir,fil))
        for section in cp.sections():
            config[src][section] = dict(cp.items(section))
            section_args = list(config[src][section].keys())
            for arg in section_args:
                if arg != 'password':
                    lu = {'TRUE' : True, 'FALSE' : False}
                    if config[src][section][arg].upper() in lu.keys():
                        config[src][section][arg] = lu[config[src][section][arg].upper()]
                    elif config[src][section][arg].isdigit():
                        config[src][section][arg] = int(config[src][section][arg])
    
    trumpcfg = config['trump']
    del config['trump']
    return trumpcfg, config

if __name__ == '__main__':
    trumpcfg, config = read_configuration()