# coding=utf-8

tr = {

    # CLIENTS TABLE HEADER
    'HEADER_IP_ADDRESS':            u'მისამართი',
    'HEADER_ALIAS':                 u'სახელი',
    'HEADER_SOCKET':                u'სოკეტი',
    'HEADER_OS':                    u'სისტემა',
    'HEADER_USER':                  u'მომხმარებელი',
    'HEADER_PRIVS':                 u'უფლებები',
    'HEADER_LOCK':                  u'ბლოკი',
    'HEADER_MIC':                   u'მიკროფონი',
    'HEADER_CAM':                   u'კამერა',
    'HEADER_ACTIVE_WINDOW_TITLE':   u'აქტიური ფანჯრის სათაური',
    # END CLIENTS TABLE HEADER

    # BOTTOM
    'BOTTOM_STATUS':                u'სტატუსი: ',
    'BOTTOM_IPV4':                  u'მისამართი: ',
    'BOTTOM_PORT':                  u'პორტი: ',
    'BOTTOM_SERVERS_TOTAL':         u'კლიენტების რაოდენობა: ',
    # END BOTTOM

    # MENU
    'MENU_SERVER':                  u'სერვერი',
    'MENU_SERVER_START':            u'ჩართვა',
    'MENU_SERVER_STOP':             u'გამორთვა',
    'MENU_SERVER_CONFIGURATION':    u'პარამეტრები',
    'MENU_CLIENT':                  u'კლიენტი',
    'MENU_CLIENT_UNLOCK':           u'განბლოკვა',
    'MENU_CLIENT_LOCK':             u'დაბლოკვა',
    'MENU_CLIENT_STOP':             u'გათიშვა',
    'MENU_CLIENT_SET_ALIAS':        u'სახელის შექმნა',
    'MENU_CLIENT_RUN_AS_ADMIN':     u'ადმინისტრატორით გაშვება',
    'MENU_PLUGIN':                  u'მოქმედება',
    'MENU_PLUGIN_SHELL':            u'ბრძანებები',
    'MENU_PLUGIN_EXPLORER':         u'ფაილების მენეჯერი',
    'MENU_PLUGIN_MICROPHONE':       u'მიკროფონი',
    'MENU_PLUGIN_PROCESSES':        u'პროცესები',
    'MENU_PLUGIN_KEYLOGGER':        u'კლავიატურის შპიონი',
    'MENU_PLUGIN_SCRIPTING':        u'პროგრამირება',
    'MENU_PLUGIN_DESKTOP':          u'ეკრანი',
    'MENU_PLUGIN_WEBCAM':           u'ვებ კამერა',
    # END MENU

    # STATUS
    'STATUS_ONLINE':                u'ჩართული',
    'STATUS_OFFLINE':               u'გამორთული',
    # END STATUS

    # MESSAGE BOX
    'MSGBOX_ERROR':                 u'შეცდომა',
    'MSGBOX_NO_CLIENT_SELECTED':    u'კლიენტი არჩეული არ არის',
    # END MESSAGE BOX

    # RIGHT CLICK MENU
    'RM_CLIENT_OPTIONS':            u'კლიენტის პარამეტრები',
    'RM_SET_ALIAS':                 u'სახელის შექმნა',
    'RM_RUN_AS_ADMIN':              u'ადმინისტრატორით გაშვება',
    'RM_SHELL':                     u'ბრძანებები',
    'RM_EXPLORER':                  u'ფაილების მენეჯერი',
    'RM_PROCESSES':                 u'პროცესები',
    'RM_MICROPHONE':                u'მიკროფონი',
    'RM_SCRIPTING':                 u'პროგრამირება',
    'RM_KEYLOGGER':                 u'კლავიატურის შპიონი',
    'RM_LOCK':                      u'დაბლოკვა',
    'RM_TERMINATE':                 u'გათიშვა',
    'RM_UNLOCK':                    u'განბლოკვა',
    'RM_DESKTOP':                   u'ეკრანი',
    'RM_CAMERA':                    u'ვებ კამერა',
    # END RIGHT CLICK MENU

    # UNLOCK CLIENT
    'UNLOCK_CLIENT':                u'კლიენტის განბლოკვა',
    'ENTER_PASSWORD':               u'პაროლი: ',
    # END UNLOCK CLIENT

    # CLIENT INFO
    'INFO_LOCKED':                  u'დაბლოკილი',
    'INFO_UNLOCKED':                u'განბლოკილი',
    'INFO_YES':                     u'კი',
    'INFO_NO':                      u'არა',
    'INFO_USER':                    u'მომხმარებელი',
    'INFO_ADMIN':                   u'ადმინისტრატორი',
    # END CLIENT INFO

    # TERMINATE CLIENT
    'TERMINATE_CONFIRM':            u'დადასტურება',
    'TERMINATE_TEXT':               u'დარწმუნებული ხართ გათიშოთ კლიენტი?',
    # END TERMINATE CLIENT

    # SET ALIAS
    'ALIAS_SET':                    u'კლიენტისთვის სახელის შექმნა',
    'ALIAS_NAME':                   u'სახელი: ',
    # END SET ALIAS

    # SETTINGS
    'TAB_CONNECTION_SETTINGS':      u'სერვერის პარამეტრები',
    'INTERFACE':                    u'ინტერფეისი',
    'SETTINGS_IP_ADDRESS':          u'მისამართი',
    'SETTINGS_PORT':                u'პორტი',
    'SETTINGS_TIMEOUT':             u'მოლოდინი',
    'SETTINGS_MAX_CONNECTIONS':     u'კლიენტების რაოდენობა',
    'SETTINGS_LANGUAGE':            u'ენა',
    'SETTINGS_SAVE':                u'შენახვა',
    'SETTINGS_MSG_INFO':            u'ინფორმაცია',
    'SETTINGS_MSG_TEXT':            u'ზოგიერთი ცვლილების შესატანად საჭიროა სერვერის გადატვირთვა',
    # END SETTINGS

    # SHELL
    'SHELL_CONNECTED_TO':           u'ბრძანებები - %s - სოკეტის #%s',
    # END SHELL

    # MAUDIO
    'MAUDIO_TITLE':                 u'მიკროფონი - %s - სოკეტის #%s',
    'MAUDIO_MSG_TITLE':             u'შეცდომა',
    'MAUDIO_MSG_TEXT':              u'მიკროფონი ვერ მოიძებნა',
    'MAUDIO_NO_SOUND':              u'სიჩუმეა',
    'MAUDIO_RECORDING':             u'იწერება',
    'MAUDIO_NOT_RECORDING':         u'არ იწერება',
    'MAUDIO_START':                 u'ჩართვა',
    'MAUDIO_RECORD':                u'ჩაწერა',
    'MAUDIO_STOP':                  u'გაჩერება',
    'MAUDIO_AUDIO_DEVICE':          u'მიკროფონი: ',
    'MAUDIO_RATE':                  u'ხარისხი',
    'MAUDIO_AUTOMATIC_RECORD':      u'ავტომატური ჩაწერის პარამეტრები',
    'MAUDIO_DETECT_SOUND':          u'ხმის დაფიქსირება \nდა ჩაწერა',
    # END MAUDIO
}
