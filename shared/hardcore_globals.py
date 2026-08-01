import discord

_GUILD_ID_VAL = 1479320102745800838

GUILD_INFO = {
    "GUILD_ID" : _GUILD_ID_VAL,
    "GUILD" : discord.Object(id=_GUILD_ID_VAL)
}

"""
#################################################################################################################################
#                                                                ROLES                                                          #
#################################################################################################################################
"""
ROLE_IDS = {
    "OWNER_ROLE_ID" : 1479320318043623454,
    "ADMIN_ROLE_ID" : 1483236165019631799,
    "HEAD_MOD_ROLE_ID" : 1479922530621063218,
    "MOD_ROLE_ID" : 1479921630758178980,
    "SECURITY_MANAGER_ROLE_ID" : 1486549522803982396,
    "LEADERBOARDS_MANAGER_ROLE_ID" : 1512900802358939879,
    "HOSTER_ROLE_ID" : 1480252394481910012,
    "PREMIUM_HOSTER_ROLE_ID" : 1497426112471367751,
    "SANTA_CLAUS_ROLE_ID" : 1508246646671016026,
    "LEAK_PING_MANAGER_ROLE_ID" : 1479949973947682826,
    "SHOP_RESET_MANAGER_ROLE_ID" : 1479949902657093842,
    "TOURNAMENT_MANAGER_ROLE_ID" : 1480030870822977638,
    "CHALLENGE_MANAGER_ROLE_ID" : 1480773783974449295,
    "STAFF_TEAM_ROLE_ID" : 1479986763534700807,
    "RESTING_ROLE_ID" : 1512632251517763604,
    "hotel hell": 1480063127864475832, "hotelhell": 1480063127864475832, "hh": 1480063127864475832,
    "a hard place": 1480065104958455970, "ahardplace": 1480065104958455970, "ahp": 1480065104958455970,
    "a-1000": 1480065693973221489, "a1000": 1480065693973221489, "a 1000": 1480065693973221489, "a": 1480065693973221489,
    "rooms": 1480067095583789347, "r": 1480067095583789347,
    "hotel": 1480066879832850506, "h": 1480066879832850506,
    "mines": 1480066992806428734, "m": 1480066992806428734,
    "outdoors": 1480067153603596318, "o": 1480067153603596318,
    "backdoors": 1480067070245732352, "b": 1480067070245732352,
    "battle mode": 1480076512962281633, "battlemode": 1480076512962281633, "bm": 1480076512962281633,
    "donut": 1487301312998801408, "d": 1487301312998801408,
    "gween soda": 1487301509665394779, "gweensoda": 1487301509665394779, "gs": 1487301509665394779,
    "crucifix": 1480069665593102356, "c": 1480069665593102356,
    "visions": 1487304057193496656, "v": 1487304057193496656,
    "tower heroes": 1480240740834607124, "towerheroes": 1480240740834607124, "th": 1480240740834607124,
    "fangame": 1515544047152926760, "f": 1515544047152926760,
    "knob grind": 1480403815898284124, "knobgrind": 1480403815898284124, "kg": 1480403815898284124,
    "giveaway": 1480105656316072120, "g": 1480105656316072120,
    "leak": 1479922262407909660, "l": 1479922262407909660,
    "shop reset": 1479922359870947559, "shopreset": 1479922359870947559, "sr": 1479922359870947559,
    "tournament": 1480030682804650005, "t": 1480030682804650005,
    "challenge": 1480774570792321064,
}

ROLE_NAMES = {
    "hotel hell": "👹 | HH ᵖⁱⁿᵍ", "hotelhell": "👹 | HH ᵖⁱⁿᵍ", "hh": "👹 | HH ᵖⁱⁿᵍ",
    "a hard place": "🪨 | AHP ᵖⁱⁿᵍ", "ahardplace": "🪨 | AHP ᵖⁱⁿᵍ", "ahp": "🪨 | AHP ᵖⁱⁿᵍ",
    "a-1000": "🛑 | A-1000 ᵖⁱⁿᵍ", "a1000": "🛑 | A-1000 ᵖⁱⁿᵍ", "a 1000": "🛑 | A-1000 ᵖⁱⁿᵍ", "a": "🛑 | A-1000 ᵖⁱⁿᵍ",
    "rooms": "🔦 | Rooms ᵖⁱⁿᵍ", "r": "🔦 | Rooms ᵖⁱⁿᵍ",
    "hotel": "🚪 | Hotel ᵖⁱⁿᵍ", "h": "🚪 | Hotel ᵖⁱⁿᵍ",
    "mines": "⛏️ | Mines ᵖⁱⁿᵍ", "m": "⛏️ | Mines ᵖⁱⁿᵍ",
    "outdoors": "🌲 | Outdoors ᵖⁱⁿᵍ", "o": "🌲 | Outdoors ᵖⁱⁿᵍ",
    "backdoors": "🕰️ | Backdoors ᵖⁱⁿᵍ", "b": "🕰️ | Backdoors ᵖⁱⁿᵍ",
    "battle mode": "💣 | Battle Mode ᵖⁱⁿᵍ", "battlemode": "💣 | Battle Mode ᵖⁱⁿᵍ", "bm": "💣 | Battle Mode ᵖⁱⁿᵍ",
    "donut": "🍩 | Donut ᵖⁱⁿᵍ", "d": "🍩 | Donut ᵖⁱⁿᵍ",
    "gween soda": "🍹 | Gween Soda ᵖⁱⁿᵍ", "gweensoda": "🍹 | Gween Soda ᵖⁱⁿᵍ", "gs": "🍹 | Gween Soda ᵖⁱⁿᵍ",
    "crucifix": "✝️ | Crucifix ᵖⁱⁿᵍ", "c": "✝️ | Crucifix ᵖⁱⁿᵍ",
    "visions": "👁️ | Visions ᵖⁱⁿᵍ", "v": "👁️ | Visions ᵖⁱⁿᵍ",
    "tower heroes": "🗼 | Tower heroes ᵖⁱⁿᵍ", "towerheroes": "🗼 | Tower heroes ᵖⁱⁿᵍ", "th": "🗼 | Tower heroes ᵖⁱⁿᵍ",
    "fangame": "🎮 | Fangame ᵖⁱⁿᵍ", "f": "🎮 | Fangame ᵖⁱⁿᵍ",
    "knob grind": "🪙 | Knob grind ᵖⁱⁿᵍ", "knobgrind": "🪙 | Knob grind ᵖⁱⁿᵍ", "kg": "🪙 | Knob grind ᵖⁱⁿᵍ",
    "giveaway": "🎉 | Giveaway ᵖⁱⁿᵍ", "g": "🎉 | Giveaway ᵖⁱⁿᵍ",
    "leak": "👀 | Leak ᵖⁱⁿᵍ", "l": "👀 | Leak ᵖⁱⁿᵍ",
    "shop reset": "🛒 | Shop reset ᵖⁱⁿᵍ", "shopreset": "🛒 | Shop reset ᵖⁱⁿᵍ", "sr": "🛒 | Shop reset ᵖⁱⁿᵍ",
    "tournament": "⚔️ | Tournament ᵖⁱⁿᵍ", "t": "⚔️ | Tournament ᵖⁱⁿᵍ",
    "challenge": "🎯 | Challenge ᵖⁱⁿᵍ"
}

"""
#################################################################################################################################
#                                                             CHANNELS                                                          #
#################################################################################################################################
"""

CHANNEL_IDS = {
    "ANNNOUNCEMENTS_CHANNEL": 1479898314416591014,
    "GIVEAWAYS_CHANNEL": 1479906724805873814,
    "BATTLE_CHANNEL" : 1512906241041764364,
    "VOUCHES_CHANNEL": 1482214901513453629,
    "vip": 1511375916247420977,
    "GENERAL_CHANNEL": 1509981090134233088,
    "PERMS_CHANNEL": 1510644799311450152,
    "FLEXING_CHANNEL": 1479895864913821837,
    "MEMES_CHANNEL": 1497420183235592243,
    "COUNTING_CHANNEL": 1479897597962489957,
    "BOT_COMMANDS_CHANNEL": 1533106374844612759, 
    "HOTEL_HELL_CHANNEL": 1486613677049384960,
    "A_HARD_PLACE_CHANNEL": 1486613408634900600,
    "A_1000_CHANNEL": 1486613863062310913,
    "HOTEL_BADGES_CHANNEL": 1486751309049757706,
    "MINES_BADGES_CHANNEL": 1486751376313815122,
    "OUTDOORS_BADGES_CHANNEL": 1486613914559971348,
    "BACKDOORS_BADGES_CHANNEL": 1486748541765554306,
    "BATTLE_MODE_BADGES_CHANNEL": 1486613976648384545,
    "ITEM_BADGES_CHANNEL": 1486614118059343974,
    "CRUCIFIX_BADGES_CHANNEL": 1486614205342683156,
    "VISION_BADGES_CHANNEL": 1489014761759965375,
    "COLLAB_BADGES_CHANNEL": 1486614265870815252,
    "FANGAME_BADGES_CHANNEL": 1515371258114609244,
    "KNOB_GRIND_CHANNEL": 1501982243873095700,
    "OTHERS_CHANNEL": 1486614305309982781,
    "STAFF_CHANNEL" : 1479987103436771462,
    "MODS_CHANNEL": 1483912829630414989,
    "ADMINS_CHANNEL": 1483190291383980062
}

CHANNEL_NAMES = {
    "ANNNOUNCEMENTS_CHANNEL": "📢・announcements",
    "GIVEAWAYS_CHANNEL": "🎊・giveaways",
    "BATTLE_CHANNEL" : "⚔️・battle",
    "VOUCHES_CHANNEL": "✅・vouches",
    "vip": "💎・vip",
    "GENERAL_CHANNEL": "💭・general",
    "PERMS_CHANNEL": "🍀・perms-gamble",
    "FLEXING_CHANNEL": "📸・flexing",
    "MEMES_CHANNEL": "😂・memeesssssssss",
    "COUNTING_CHANNEL": "🔢・counting-till-archives",
    "BOT_COMMANDS_CHANNEL": "🤖・bot-commands",
    "HOTEL_HELL_CHANNEL": "👹・hotel-hell",
    "A_HARD_PLACE_CHANNEL": "🪨・a-hard-place",
    "A_1000_CHANNEL": "🛑・a-1000",
    "HOTEL_BADGES_CHANNEL": "🚪・hotel-badges",
    "MINES_BADGES_CHANNEL": "⛏️・mines-badges",
    "OUTDOORS_BADGES_CHANNEL": "🌲・outdoor-badges",
    "BACKDOORS_BADGES_CHANNEL": "🕰️・backdoor-badges",
    "BATTLE_MODE_BADGES_CHANNEL": "💣・battle-mode-badges",
    "ITEM_BADGES_CHANNEL": "🍩・item-badges",
    "CRUCIFIX_BADGES_CHANNEL": "✝️・crucifix-badges",
    "VISION_BADGES_CHANNEL": "👁️・vision-badges",
    "COLLAB_BADGES_CHANNEL": "🗼・collab-badges",
    "FANGAME_BADGES_CHANNEL": "🎮・fangame-badges",
    "KNOB_GRIND_CHANNEL": "🪙・knob-grind",
    "OTHERS_CHANNEL": "🔍・others",
    "STAFF_CHANNEL" : "💬・staffs-chat",
    "MODS_CHANNEL": "🕴🏼・mods-chat",
    "ADMINS_CHANNEL": "🛡️・admins-chat"
}