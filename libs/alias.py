import ConfigParser
import os

class Alias:

    alias_db = 'alias.ini'

    if not os.path.exists(alias_db):
        open(alias_db, 'w').close()

    alias = ConfigParser.ConfigParser()

    def set_alias(self, ip, os, alias):

        print 'aq'

        self.alias.read(self.alias_db)
        if not self.alias.has_section(ip):
            self.alias.add_section(ip)
        self.alias.set(ip, os, alias)

        with open(self.alias_db, 'w') as alias_db:
            self.alias.write(alias_db)

        print 'done'

    def get_alias(self, ip, os):
        self.alias.read(self.alias_db)
        try:
            alias = self.alias.get(ip, os)
            return alias
        except:
            return ''

