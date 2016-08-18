plugin_name = 'getPcInfo'

plugin_description = 'Get Info About Client PC'

plugin_source = '''

mprint = os.popen('systeminfo').read()

'''