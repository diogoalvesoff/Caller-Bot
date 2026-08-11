import sqlite3
from shared.hardcore_globals import ROLE_IDS, CHANNEL_IDS, CHANNEL_NAMES
import re
import discord
from discord import app_commands

"""
#################################################################################################################################
#                                                              CONFIGS                                                          #
#################################################################################################################################
"""

PS_OPTIONS = {
    "ps" : "https://www.roblox.com/share?code=24f0174ac4601144ba68fa7999fbda3b&type=Server",
    "ps1" : "https://www.roblox.com/share?code=14bf45f0929a43478b4fd72f97970501&type=Server",
    "tps" : "https://www.roblox.com/share?code=6b969a5026042e4abc0e106a24f39999&type=Server"
}

COOLDOWN = 2.0
GAMBLING_PERMS_CHANNELS = [
    CHANNEL_IDS["GENERAL_CHANNEL"]
]
SHARED_CHANNEL_CHOICES = [
    app_commands.Choice(name=CHANNEL_NAMES["ANNNOUNCEMENTS_CHANNEL"], value="ANNNOUNCEMENTS_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["GIVEAWAYS_CHANNEL"], value="GIVEAWAYS_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["GENERAL_CHANNEL"], value="GENERAL_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["FLEXING_CHANNEL"], value="FLEXING_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["MEMES_CHANNEL"], value="MEMES_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["COUNTING_CHANNEL"], value="COUNTING_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["HOTEL_HELL_CHANNEL"], value="HOTEL_HELL_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["A_HARD_PLACE_CHANNEL"], value="A_HARD_PLACE_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["A_1000_CHANNEL"], value="A_1000_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["HOTEL_BADGES_CHANNEL"], value="HOTEL_BADGES_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["MINES_BADGES_CHANNEL"], value="MINES_BADGES_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["OUTDOORS_BADGES_CHANNEL"], value="OUTDOORS_BADGES_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["BACKDOORS_BADGES_CHANNEL"], value="BACKDOORS_BADGES_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["BATTLE_MODE_BADGES_CHANNEL"], value="BATTLE_MODE_BADGES_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["ITEM_BADGES_CHANNEL"], value="ITEM_BADGES_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["CRUCIFIX_BADGES_CHANNEL"], value="CRUCIFIX_BADGES_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["VISION_BADGES_CHANNEL"], value="VISION_BADGES_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["COLLAB_BADGES_CHANNEL"], value="COLLAB_BADGES_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["FANGAME_BADGES_CHANNEL"], value="FANGAME_BADGES_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["KNOB_GRIND_CHANNEL"], value="KNOB_GRIND_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["OTHERS_CHANNEL"], value="OTHERS_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["STAFF_CHANNEL"], value="STAFF_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["MODS_CHANNEL"], value="MODS_CHANNEL"),
    app_commands.Choice(name=CHANNEL_NAMES["ADMINS_CHANNEL"], value="ADMINS_CHANNEL"),
]

"""
#################################################################################################################################
#                                                           COMMAND PERMS                                                       #
#################################################################################################################################
"""

ROLES_WITH_PERMS_TO_USE__PING = [
    ROLE_IDS["HOSTER_ROLE_ID"],
    ROLE_IDS["PREMIUM_HOSTER_ROLE_ID"],
    ROLE_IDS["SANTA_CLAUS_ROLE_ID"],
    ROLE_IDS["LEAK_PING_MANAGER_ROLE_ID"],
    ROLE_IDS["SHOP_RESET_MANAGER_ROLE_ID"],
    ROLE_IDS["TOURNAMENT_MANAGER_ROLE_ID"],
    ROLE_IDS["CHALLENGE_MANAGER_ROLE_ID"]
]
ROLES_WITH_PERMS_TO_PING__BADGES = [
    ROLE_IDS["HOSTER_ROLE_ID"],
    ROLE_IDS["PREMIUM_HOSTER_ROLE_ID"]
]
ROLES_WITH_PERMS_TO_PING__SHOP_RESET = [
    ROLE_IDS["SHOP_RESET_MANAGER_ROLE_ID"]
]
ROLES_WITH_PERMS_TO_PING__GIVEAWAY = [
    ROLE_IDS["SANTA_CLAUS_ROLE_ID"],
    ROLE_IDS["PREMIUM_HOSTER_ROLE_ID"]
]
ROLES_WITH_PERMS_TO_PING__LEAK = [
    ROLE_IDS["LEAK_PING_MANAGER_ROLE_ID"]
]
ROLES_WITH_PERMS_TO_PING__TOURNAMENT = [
    ROLE_IDS["TOURNAMENT_MANAGER_ROLE_ID"]
]
ROLES_WITH_PERMS_TO_PING__CHALLENGE = [
    ROLE_IDS["CHALLENGE_MANAGER_ROLE_ID"]
]

ROLES_WITH_PERMS_TO_USE__ACTIVITY = [
    ROLE_IDS["STAFF_TEAM_ROLE_ID"]
]

ROLES_WITH_PERMS_TO__ASK_FOR_PERMS = [
    ROLE_IDS["ADMIN_ROLE_ID"],
    ROLE_IDS["HEAD_MOD_ROLE_ID"],
    ROLE_IDS["MOD_ROLE_ID"]
]
ROLES_WITH_PERMS_TO__USE_TALK = [
    ROLE_IDS["OWNER_ROLE_ID"]
]


"""
#################################################################################################################################
#                                                           COMMAND CONST                                                       #
#################################################################################################################################
"""

PING_CATEGORIES = [
    {
        "allowed_roles": ROLES_WITH_PERMS_TO_PING__BADGES,
        "options": ["hh", "ahp", "a", "r", "h", "m", "o", "b", "bm", "d", "gs", "c", "v", "th", "f", "kg"]
    },
    {
        "allowed_roles": ROLES_WITH_PERMS_TO_PING__SHOP_RESET,
        "options": ["sr"]
    },
    {
        "allowed_roles": ROLES_WITH_PERMS_TO_PING__GIVEAWAY,
        "options": ["g"]
    },
    {
        "allowed_roles": ROLES_WITH_PERMS_TO_PING__LEAK,
        "options": ["l"]
    },
    {
        "allowed_roles": ROLES_WITH_PERMS_TO_PING__TOURNAMENT,
        "options": ["t"]
    },
    {
        "allowed_roles": ROLES_WITH_PERMS_TO_PING__CHALLENGE,
        "options": ["challenge"]
    }
]


"""
#################################################################################################################################
#                                                           PERMS GAMBLE                                                        #
#################################################################################################################################
"""

_PERMS_GAMBLE_WORDS1 = ["perms", "permissions", "permes", "prems", "pers", "perm"]
_PERMS_GAMBLE_WORDS2 = ["make", "rn", "now", "right now", "please", "me", "i", "gimme", "gimmie", "give", "perms", "pass", "mod", "admin", "administrator", "moderator"]
PATTERN_W1 = re.compile(r'\b(?:' + '|'.join(map(re.escape, _PERMS_GAMBLE_WORDS1)) + r')\b', re.IGNORECASE)
PATTERN_W2 = re.compile(r'\b(?:' + '|'.join(map(re.escape, _PERMS_GAMBLE_WORDS2)) + r')\b', re.IGNORECASE)

"""
#################################################################################################################################
#                                                              BUTTONS                                                          #
#################################################################################################################################
"""

BUTTON_ACTIVITY_ACTIVE = {
    "label": "🔥Set active🔥",
    "style": discord.ButtonStyle.success,
    "cid": "btn_activity_active"
}
BUTTON_ACTIVITY_INACTIVE = {
    "label": "😴Set inactive😴",
    "style": discord.ButtonStyle.danger,
    "cid": "btn_activity_inactive"
}