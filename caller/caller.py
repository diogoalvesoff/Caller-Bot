import os
import re
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import aiosqlite

from shared.hardcore_globals import GUILD_INFO, ROLE_IDS, ROLE_NAMES, CHANNEL_IDS
from caller.caller_contants import (
    PS_OPTIONS, COOLDOWN, GAMBLING_PERMS_CHANNELS, SHARED_CHANNEL_CHOICES,
    ROLES_WITH_PERMS_TO_USE__PING, ROLES_WITH_PERMS_TO_PING__BADGES, ROLES_WITH_PERMS_TO_PING__SHOP_RESET, ROLES_WITH_PERMS_TO_PING__GIVEAWAY, ROLES_WITH_PERMS_TO_PING__LEAK, ROLES_WITH_PERMS_TO_PING__TOURNAMENT, ROLES_WITH_PERMS_TO_USE__ACTIVITY, ROLES_WITH_PERMS_TO__USE_TALK, ROLES_WITH_PERMS_TO_PING__CHALLENGE, ROLES_WITH_PERMS_TO__ASK_FOR_PERMS,
    PING_CATEGORIES,
    PATTERN_W1, PATTERN_W2,
    BUTTON_ACTIVITY_ACTIVE, BUTTON_ACTIVITY_INACTIVE
)


load_dotenv()
TOKEN = os.getenv('TOKEN')

async def setup_db():
        async with aiosqlite.connect("activity.db") as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS inactives (
                    user_id INTEGER PRIMARY KEY,
                    reason TEXT
                )
            ''')
            await db.commit()


class Client (commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.reactions = True                                    # lets see reactions
        intents.guilds = True                                       # lets see specific guild info
        intents.members = True                                      # lets assign roles to users
        super().__init__(command_prefix="!", intents=intents)
        self.gamble_cooldown = commands.CooldownMapping.from_cooldown(1, COOLDOWN, commands.BucketType.user)

    async def on_ready(self):
        await setup_db()
        print(f'Logged on as {self.user}')
        try:
            synced = await self.tree.sync(guild=GUILD_INFO["GUILD"])
            print (f'Synced {len(synced)} commands to guild {GUILD_INFO["GUILD_ID"]}')
        except Exception as e:
            print (f'Error syncing commands: {e}')

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        bucket = self.gamble_cooldown.get_bucket(message)
        retry_after = bucket.update_rate_limit()
        if retry_after:
            print(f"Rate limit catch. {message.author.name} gotta wait more {retry_after:.2f}s")
            return
        
        await self.process_commands(message)

        content = message.content
        num_words = len(re.findall(r'\w+', content))
            
        if num_words == 0:
            return

        lower_content = content.lower()
        if lower_content in PS_OPTIONS.keys():
            await message.reply(PS_OPTIONS[lower_content])

        # After this, ignores dms
        if not message.guild:
            return

        # 3. Lógica principal
        perms_channel = message.author.guild.get_channel(CHANNEL_IDS["PERMS_CHANNEL"])
        if perms_channel:
            if message.channel.id in GAMBLING_PERMS_CHANNELS:
                user_roles = [role.id for role in message.author.roles]
                can_bypass_delete = any(role_id in ROLES_WITH_PERMS_TO__ASK_FOR_PERMS for role_id in user_roles)

                if num_words == 1:
                    # Regra: Se tem 1 palavra, tem de estar na words1
                    if PATTERN_W1.search(content):
                        print(f"{message.author.mention} asked for perms: {content}")
                        if not can_bypass_delete:
                            await message.delete()
                        await perms_channel.send(f"{message.author.mention} asked for perms!\nGambling ......\nNo")
                    
                elif num_words > 1:
                    # Regra: Se tem > 1 palavra, precisa de uma da words1 E uma da words2
                    if PATTERN_W1.search(content) and PATTERN_W2.search(content):
                        print(f"{message.author.mention} asked for perms: {content}")
                        if not can_bypass_delete:
                            await message.delete()
                        await perms_channel.send(f"{message.author.mention} asked for perms!\nGambling ......\nNo")

            if content.startswith("1/10"):
                if perms_channel:
                    await perms_channel.send(f"True")
                else:
                    print("E: No perms_channel")

        if message.mentions:
            if message.channel.id != CHANNEL_IDS.get("VOUCHES_CHANNEL"):
                resting_role = message.guild.get_role(ROLE_IDS.get("RESTING_ROLE_ID"))
                if not resting_role:
                    print("Err: No resting role")
                    return
                
                mentioned_inactives = []
                reasons = []
                async with aiosqlite.connect("activity.db") as db:
                    for user in message.mentions:
                        if isinstance(user, discord.Member) and resting_role in user.roles:
                            async with db.execute("SELECT reason FROM inactives WHERE user_id = ?", (user.id,)) as cursor:
                                row = await cursor.fetchone()
                                reason = row[0] if row else "No reason"
                                mentioned_inactives.append(user.display_name)
                                reasons.append(reason)
                if len(mentioned_inactives) == 1:
                    if reasons[0] == "No reason":
                        await message.reply(f"**Sorry, {mentioned_inactives[0]} is inactive 😴! **")
                    else:
                        await message.reply(f"**Sorry, {mentioned_inactives[0]} is inactive 😴! Reason: {reasons[0]}**")
                elif len(mentioned_inactives) > 1:
                    names = ", ".join(mentioned_inactives[:-1]) + f" and {mentioned_inactives[-1]}"
                    await message.reply(f"**Sorry, {names} are inactive 😴!**")

            if lower_content.startswith("hug "):
                user = message.mentions[0]
                print (f"{message.author.display_name} hugged {user.display_name}")
                await message.channel.send(f"🤗 {message.author.mention} hugged {user.mention}")
            if lower_content.startswith("handshake "):
                user = message.mentions[0]
                print (f"{message.author.display_name} shook hands with {user.display_name}")
                await message.channel.send(f"🤝 {message.author.mention} shook hands with {user.mention}")

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        print(f"E: '{ctx.command} failed: {error}")

client = Client()

@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.MissingAnyRole):
        await interaction.response.send_message("You don't have perms to execute me", ephemeral=True)
        return
    print(f"E: '{interaction.command.name}' failed: {error}")
    if not interaction.response.is_done():
        await interaction.response.send_message(f"I think smth went wrong... role <@&{ROLE_IDS.get('ADMIN_ROLE_ID')}>")


"""
#################################################################################################################################
#                                                               COMANDOS                                                        #
#################################################################################################################################

1. /ping
2. /activity

"""

"""
#################################################################################################################################
#                                                                PING                                                           #
#################################################################################################################################
"""

async def ping_autocomplete (interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    choices = []
    user_role_ids = [role.id for role in interaction.user.roles]
    for category in PING_CATEGORIES:
        if any(r_id in category["allowed_roles"] for r_id in user_role_ids):
            for opt in category["options"]:
                name = ROLE_NAMES.get(opt)
                if name and current.lower() in name.lower():
                    choices.append(app_commands.Choice(name=name, value=opt))

    return choices[:25]

@app_commands.checks.has_any_role(*ROLES_WITH_PERMS_TO_USE__PING)
@client.tree.command(name="ping", description="If you have perms, use me to ping certain roles", guild=GUILD_INFO["GUILD"])
@app_commands.autocomplete(role=ping_autocomplete)
async def ping(interaction: discord.Interaction, role: str):
    role_key = role.lower()
    target_role_id = ROLE_IDS.get(role_key)
    if not target_role_id:
        await interaction.response.send_message("That role doesn't exist", ephemeral=True)
        return

    user_role_ids = [r.id for r in interaction.user.roles]
    has_perms = False
    
    for category in PING_CATEGORIES:
        category_target_ids = [ROLE_IDS[opt] for opt in category["options"]]
        
        if target_role_id in category_target_ids:
            if any(r_id in category["allowed_roles"] for r_id in user_role_ids):
                has_perms = True
            break
    
    if not has_perms:
        await interaction.response.send_message("You don't have perms to ping that role", ephemeral=True)
        return

    if target_role_id:
        await interaction.response.send_message(
            f"<@&{target_role_id}>",
            allowed_mentions=discord.AllowedMentions(roles=True)
        )
        print(f"{interaction.user.name} used /ping")


"""
#################################################################################################################################
#                                                             ACTIVITY                                                          #
#################################################################################################################################
"""

class SetActivity(discord.ui.View):
    def __init__(self, reason: str):
        super().__init__(timeout=60)
        self.reason = reason.replace("@", "") if reason else "No reason"
        

    @discord.ui.button(label=BUTTON_ACTIVITY_ACTIVE["label"], style=BUTTON_ACTIVITY_ACTIVE["style"], custom_id=BUTTON_ACTIVITY_ACTIVE["cid"])
    async def btn_activity_active(self, interaction: discord.Interaction, button: discord.ui.Button):
        resting_role = interaction.guild.get_role(ROLE_IDS.get("RESTING_ROLE_ID"))
        if not resting_role:
            print("Err: No resting role")
            return
        if resting_role in interaction.user.roles:
            await interaction.user.remove_roles(resting_role)

        async with aiosqlite.connect("activity.db") as db:
            await db.execute("DELETE FROM inactives WHERE user_id = ?", (interaction.user.id,))
            await db.commit()

        for child in self.children:
            child.disabled = True

        await interaction.response.edit_message(
            content = f"✅ Done. You're active",
            view=self
        )

        staff_chat = interaction.guild.get_channel(CHANNEL_IDS.get("STAFF_CHANNEL"))
        if staff_chat:
            await staff_chat.send(f"{interaction.user.mention} is active")

    @discord.ui.button(label=BUTTON_ACTIVITY_INACTIVE["label"], style=BUTTON_ACTIVITY_INACTIVE["style"], custom_id=BUTTON_ACTIVITY_INACTIVE["cid"])
    async def btn_activity_inactive(self, interaction: discord.Interaction, button: discord.ui.Button):
        resting_role = interaction.guild.get_role(ROLE_IDS.get("RESTING_ROLE_ID"))
        if not resting_role:
            print("Err: No resting role")
            return
        if resting_role not in interaction.user.roles:
            await interaction.user.add_roles(resting_role)

        async with aiosqlite.connect("activity.db") as db:
            await db.execute("REPLACE INTO inactives (user_id, reason) VALUES (?, ?)", (interaction.user.id, self.reason))
            await db.commit()

        for child in self.children:
            child.disabled = True

        if self.reason == "No reason":
            await interaction.response.edit_message(
                content = f"✅ Done. You're inactive",
                view=self
            )
        else:
            await interaction.response.edit_message(
                content = f"✅ Done. You're inactive. Reason saved: {self.reason}",
                view=self
            )

        staff_chat = interaction.guild.get_channel(CHANNEL_IDS.get("STAFF_CHANNEL"))
        if not staff_chat:
            print ("Err - Could not find Staff Chat")
            return
        if self.reason == "No reason":
            await staff_chat.send(f"{interaction.user.mention} is inactive")
        else:
            await staff_chat.send(f"{interaction.user.mention} is inactive. Reason: {self.reason}")

@app_commands.checks.has_any_role(*ROLES_WITH_PERMS_TO_USE__ACTIVITY)
@client.tree.command(name="activity", description="If you are a staff member, use me to declare yourself active or inactive", guild=GUILD_INFO["GUILD"])
async def activity (interaction: discord.Interaction, reason: str = None):
    view = SetActivity(reason)
    await interaction.response.send_message(f"Press the button that best suits your purpose", view=view, ephemeral=True)

"""
@app_commands.checks.has_any_role(*ROLES_WITH_PERMS_TO__USE_TALK)
@client.tree.command(name="talk", description="talk", guild=GUILD_INFO["GUILD"])
@app_commands.choices(channel=SHARED_CHANNEL_CHOICES)
async def talk (interaction: discord.Interaction, message: str, channel: app_commands.Choice[str]):
    if not message:
        await interaction.response.send_message("✖️ Your message must not be empty ✖️", ephemeral=True)
        return
    if not channel:
        await interaction.response.send_message("✖️ You must choose a channel to send the message ✖️", ephemeral=True)
        return
    target_channel = interaction.guild.get_channel(CHANNEL_IDS[channel.value])
    if not target_channel:
        await interaction.response.send_message("✖️ That channel doesn't exist ✖️", ephemeral=True)
        return
    await target_channel.send(message)
    await interaction.response.send_message("✅ Message sent ✅", ephemeral=True)
"""

def main():
    if not TOKEN:
        print ("E: Token not found!")
        return
    print ("Starting!")
    client.run(TOKEN)

if __name__ == "__main__":
    main()

    ROLES_WITH_PERMS_TO__ASK_FOR_PERMS