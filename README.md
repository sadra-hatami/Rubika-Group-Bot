<div align="center">

# Rubika Group Bot
# 🤖

### A Persian Rubika Group Bot for Content Locks

A lightweight group-moderation bot built with Python and `rubka`, featuring admin-only lock commands, automatic deletion of blocked messages, and a live permission list for links, videos, photos, voice, GIFs, stickers, emojis, and text.

<br>

# 👨‍💻 **Sadra Hatami**

### *Developer • Software Engineer • Creator*

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Rubka](https://img.shields.io/badge/Rubka-Rubika%20Bot-8E44AD?style=for-the-badge)](https://pypi.org/)
[![AsyncIO](https://img.shields.io/badge/AsyncIO-Asynchronous-2C3E50?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/asyncio.html)
[![Moderation](https://img.shields.io/badge/Focus-Content%20Locks-4CAF50?style=for-the-badge)](#-group-locks)
[![Persian](https://img.shields.io/badge/Language-Persian-success?style=for-the-badge)](https://en.wikipedia.org/wiki/Persian_language)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
![GitHub](https://img.shields.io/badge/Open_Source-Project-black?style=for-the-badge&logo=github)

<br>

[🌐 GitHub Profile](https://github.com/sadra-hatami)
•
[📧 Email](mailto:sadra.hatami.1732@gmail.com)

</div>

---

# 📑 Table of Contents

- [About](#-about)
- [Related Repositories](#-related-repositories)
- [Why This Bot?](#-why-this-bot)
- [Key Features](#-key-features)
- [Group Locks](#-group-locks)
- [Permission List](#-permission-list)
- [Project Structure](#-project-structure)
- [Technologies](#️-technologies)
- [Installation](#-installation)
- [Configuration](#️-configuration)
- [Usage](#️-usage)
- [Command Examples](#-command-examples)
- [Target Audience](#-target-audience)
- [Roadmap](#️-roadmap)
- [FAQ](#-faq)
- [Security Notes](#-security-notes)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [License](#-license)
- [Copyright](#-copyright)
- [Support](#-support)

---

# 📖 About

**Rubika Group Bot** is a small Persian Rubika group bot developed with Python and the `rubka` library.

The admin can lock or unlock common content types with short Persian commands. When a lock is active, messages of that type sent by regular members receive a warning and are deleted. The configured admin is not blocked by the locks.

This repository is the lightweight lock bot. A much more complete version also exists, and there is a separate Telegram panel for controlling a Rubika user account.

> **Tagline:** *A Persian Rubika group bot that locks or unlocks links, videos, photos, voice, GIFs, stickers, emojis, and text, then auto-deletes blocked messages.*

---

# 🔗 Related Repositories

These three projects are related, but they solve different problems.

| Repository | Role |
|------------|------|
| **[Countries War Bot](https://github.com/sadra-hatami/Countries-War-Bot)** | Nation strategy game (this repo) |
| **[Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot)** | Lightweight group lock bot |
| **[Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot)** | Full group management, automation, and extra tools |
| **[Telegram Rubika Account Panel](https://github.com/sadra-hatami/Telegram-Rubika-Account-Panel)** | Telegram panel for a Rubika user account |

If you need only content locks, stay on this repository.  
If you need a much more advanced group bot, use [Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot).  
If you want a Telegram-based control panel for a Rubika user account, use [Telegram Rubika Account Panel](https://github.com/sadra-hatami/Telegram-Rubika-Account-Panel).

---

# 🚀 Why This Bot?

Not every group needs AI, games, and a database.

**Rubika Group Bot** stays small on purpose:

- One main Python file
- Clear Persian lock commands
- A separate lock for each common content type
- Immediate delete when a lock is on
- No extra services

It is the simple group tool. The advanced bot is the full platform.

---

# ✨ Key Features

## 👑 Administration

- One configured admin
- Admin-only lock changes
- Permission list for the current state
- Private helper command for reading a user ID

## 🛡️ Content Locks

- Links
- Videos
- Photos
- Voice messages
- GIFs
- Stickers
- Emojis
- Text

## 🗑️ Moderation

- Warning reply when a locked type is sent
- Automatic deletion of blocked messages
- Admin messages are not deleted by the locks

---

# 👑 Group Locks

Lock states are stored in memory.

- `True` — that content type is locked
- `False` — that content type is allowed

```text
لینک ممنوع
لینک آزاد

ویدیو ممنوع
ویدیو آزاد

عکس ممنوع
عکس آزاد

ویس ممنوع
ویس آزاد

گیف ممنوع
گیف آزاد

استیکر ممنوع
استیکر آزاد

ایموجی ممنوع
ایموجی آزاد

متن ممنوع
متن آزاد
```

If a non-admin tries to change a lock, the bot replies that they do not have permission.

These flags reset when the bot process stops. The advanced bot saves group settings in SQLite instead.

---

# 📋 Permission List

```text
لیست دسترسی ها
لیست دسترسی
```

The reply shows whether members may send each content type.

Private helper:

```text
/ad_admin_of_mike12
```

In a private chat, this command can return the sender's Rubika user ID. The lock features themselves still belong in a group.

---

# 📁 Project Structure

```text
Rubika-Group-Bot/
├── index.py
└── README.md
```

Run the bot from `index.py`. Keep the token and admin ID out of the public file.

---

# 🛠️ Technologies

- Python 3.8+
- `rubka`
- Async message handlers
- In-memory lock flags

---

# 🚀 Installation

```bash
git clone https://github.com/sadra-hatami/Rubika-Group-Bot.git
cd Rubika-Group-Bot
pip install rubka
```

```bash
python index.py
```

---

# ⚙️ Configuration

Use environment variables:

```python
import os
from rubka import Robot

bot = Robot(
    os.environ["RUBIKA_BOT_TOKEN"],
    show_progress=True,
    enable_offset=True,
)
admin_id = os.environ["RUBIKA_ADMIN_ID"]
```

```bash
export RUBIKA_BOT_TOKEN="YOUR_BOT_TOKEN"
export RUBIKA_ADMIN_ID="YOUR_ADMIN_ID"
python index.py
```

---

# ▶️ Usage

1. Start `index.py`.
2. Add the bot to a Rubika group.
3. Give it permission to delete messages.
4. Send lock commands as the admin.

The main features work in **groups**. A private chat with the bot is not enough for locks.

---

# 📚 Command Examples

```text
لیست دسترسی ها
لینک ممنوع
عکس آزاد
ویس ممنوع
```

---

# 🎯 Target Audience

- Rubika group admins who only need content locks
- Developers learning simple `rubka` handlers
- Anyone who wants a small Persian lock bot before moving to the advanced version

---

# 🗺️ Roadmap

Possible later improvements for this lightweight bot:

- Save lock states so they survive a restart
- Support more than one admin
- Per-group settings
- Cleaner handler structure

For AI, games, XP, reports, and saved group configuration, use the advanced repository instead of expanding this file too far.

---

# ❓ FAQ

### Do the locks stay on after restart?

No. This version keeps flags in memory only.

### Can regular members change the locks?

No. Only the configured admin ID can change settings.

### Is there a more advanced version?

Yes. [Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot) is the much larger group platform with moderation packs, automation, AI, games, XP, and SQLite.

### Is there a Telegram control version?

Yes. [Telegram Rubika Account Panel](https://github.com/sadra-hatami/Telegram-Rubika-Account-Panel) is a different project: a Telegram panel that controls a Rubika user account with `rubpy`. It is not this group lock bot.

### Why were some messages not deleted?

The bot must be running, must be a group admin, and must have delete permission.

---

# 🔐 Security Notes

- Never commit the bot token or admin ID.
- If a token was ever published, replace it.
- Add `.env` and `__pycache__/` to `.gitignore`.

---

# 🤝 Contributing

Contributions are welcome:

- Bug reports
- Extra lock types
- Saved settings
- Clearer command replies
- Pull requests

---

# 📬 Contact

**Developer:**

### Sadra Hatami

📧 [Email](mailto:sadra.hatami.1732@gmail.com)

🌐 [GitHub](https://github.com/sadra-hatami)

---

# 📄 License

This project is licensed under the **MIT License**.

---

# © Copyright

© 2026 **Sadra Hatami**

All rights reserved.

The source code, command texts, and project documentation are protected under applicable copyright laws.

---

# ⭐ Support

If this bot helped you manage a Rubika group, please consider giving it a ⭐ on GitHub.

---

<div align="center">

## Designed & Developed with ❤️ for the developer community of Iran and the world by **Sadra Hatami**

</div>
