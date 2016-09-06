plugin_name = 'getPcInfo'

plugin_description = 'Get Info About Client PC'

r_source = '''

mprint = os.popen('systeminfo').read()

'''

l_source = ''