


class Config:
    # get a token from @BotFather
    TG_BOT_TOKEN = "1640796806:AAEVKLVqOVK98wsnUT440SoEFXtsWtyjohQ"
    # The Telegram API things
    APP_ID = int("2180427")
    API_HASH = "b52730e42aabdb05615832d48c702ce6"
    # Get these values from my.telegram.org
    # array to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(
        int(x) for x in 
            "-1001435264443".split()
    )
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = int(50000000)
    TG_MAX_FILE_SIZE = int(2097152000)
    FREE_USER_MAX_FILE_SIZE = int(50000000)
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = "https://telegra.ph/file/8b973b270f4f380a427b1.png"
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = int(4096)
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = int(
        3600
    )
    #
    ARIA_TWO_STARTED_PORT = int(
        6800
    )
    EDIT_SLEEP_TIME_OUT = int(
        1
    )
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(
        600
    )
    MAX_TG_SPLIT_FILE_SIZE = int(
        1900000000
    )
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = "█"
    UN_FINISHED_PROGRESS_STR = "░"
    # add offensive API
    TG_OFFENSIVE_API = None
    # URL for the rclone configuration
    R_CLONE_CONF_URI = None
    # Destination folder for the rclone
    R_CLONE_DEST = "/PublicLeech"
    # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = False
    #
    LOG_FILE_ZZGEVC = "PublicLeech.log"
    #
    SP_LIT_ALGO_RITH_M = "hjs"
    #
    DIS_ABLE_ST_GFC_COMMAND_I = False
    # array to store the users who will have control (permissions)
    # in the bot

    )
