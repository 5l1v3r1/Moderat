version_body = '''
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(6, 1, 7601, 17514),
    prodvers=(6, 1, 7601, 17514),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'{%CompanyName%}'),
        StringStruct(u'FileDescription', u'{%FileDescription%}'),
        StringStruct(u'FileVersion', u'{%FileVersion%}'),
        StringStruct(u'InternalName', u'{%InternalName%}'),
        StringStruct(u'LegalCopyright', u'{%LegalCopyright%}'),
        StringStruct(u'OriginalFilename', u'{%InternalName%}'),
        StringStruct(u'ProductName', u'{%ProductName%}'),
        StringStruct(u'ProductVersion', u'{%ProductVersion%}')])
      ]),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
'''
