plugin_name = 'getInfoValues'

plugin_description = 'Get Info About Client Info.nfo file'

plugin_source = '''

mprint = open(os.path.join(os.path.dirname(sys.argv[0]), 'info.nfo'), 'r').read()

'''