plugin_name = 'getWebcamName'

plugin_description = 'Get Name of Webcamera'

plugin_source = '''

try:
    import vidcap
    cam = vidcap.new_Dev(0, 0)
    mprint = str(cam.getdisplayname())
    del cam
except:
    mprint = 'NoDevice'

'''