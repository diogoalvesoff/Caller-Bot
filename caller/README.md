# Discord Caller Bot

A specialized Discord bot built with `discord.py` designed to manage role mentions securely. It allows authorized users (e.g., Hosters) to ping specific alert roles (like game modes or specific locations) via slash commands, without needing to grant them universal `@mention` permissions in the server.

## Features

* **Controlled Mentions:** Users can only ping pre-approved roles defined in the bot's internal dictionary.
* **Role-Based Access Control (RBAC):** Only users with specific roles (Hoster, Premium Hoster) can execute the commands.
* **Slash Commands:** Fully integrated with Discord's modern UI using `/ping <role>`.
* **Alias Mapping:** Supports quick aliases for faster typing (e.g., typing `/ping m` to ping the "Mines" role).
* **Global Error Handling:** Gracefully catches permission errors and missing roles, returning clean, ephemeral messages to the user without cluttering the chat.

## Prerequisites

* Python 3.8 or higher
* A valid Discord Bot Token

## Setup & Installation

1. **Create and activate a virtual environment:**
   * **Windows (PowerShell):** ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   * **Windows (CMD):** ```cmd
     python -m venv .venv
     .\.venv\Scripts\activate.bat
     ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt