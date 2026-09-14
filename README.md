<div align="center">

# Rubika Group Bot

# 🤖

### A Persian Rubika Group Bot for Content Locks

A focused Rubika group bot built with Python, featuring admin-only lock commands, automatic deletion of blocked messages, and a live permission list for links, videos, photos, voice, GIFs, stickers, emojis, and text.

# 👨‍💻 Sadra Hatami

### Developer • Software Engineer • Creator

[🌐 GitHub](https://github.com/sadra-hatami) • [📧 Email](mailto:sadra.hatami.1732@gmail.com)

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Rubka](https://img.shields.io/badge/Rubka-Rubika%20Bot-8E44AD?style=for-the-badge)](https://pypi.org/)
[![AsyncIO](https://img.shields.io/badge/AsyncIO-Asynchronous-2C3E50?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/asyncio.html)
[![Moderation](https://img.shields.io/badge/Focus-Content%20Locks-4CAF50?style=for-the-badge)](#-group-locks)
[![Persian](https://img.shields.io/badge/Language-Persian-success?style=for-the-badge)](https://en.wikipedia.org/wiki/Persian_language)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

</div>

---

# 📑 Table of Contents

* [📖 About](#-about)
* [🚀 Why Rubika Group Bot?](#-why-rubika-group-bot)
* [✨ Key Features](#-key-features)
* [👑 Group Locks](#-group-locks)
* [📋 Permission List](#-permission-list)
* [🛠️ Technologies](#️-technologies)
* [🚀 Installation](#-installation)
* [⚙️ Configuration](#️-configuration)
* [▶️ Usage](#️-usage)
* [📚 Command Examples](#-command-examples)
* [🎯 Target Audience](#-target-audience)
* [🗺️ Roadmap](#️-roadmap)
* [❓ FAQ](#-faq)
* [🔐 Security Notes](#-security-notes)
* [🤝 Contributing](#-contributing)
* [📬 Contact](#-contact)
* [📄 License](#-license)

---

# 📖 About

**Rubika Group Bot** is a Persian Rubika group bot developed with Python and the `rubka` library.

The admin can lock or unlock common content types with short Persian commands. When a lock is active, messages of that type sent by regular members receive a warning and are deleted. The configured admin is not blocked by the locks.

This repository is the lightweight lock bot. For the larger platform with AI, games, XP, and database-backed settings, see [Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot).

> **Tagline:** *A Persian Rubika group bot for locking and unlocking common content types with Persian admin commands.*

---

# 🚀 Why Rubika Group Bot?

Many groups only need content locks, not a full management platform.

**Rubika Group Bot** keeps that path short:

* One Python file
* Clear Persian commands
* A separate lock for each common content type
* Immediate delete when a lock is on
* No extra services and no database

The project is designed for Persian-speaking Rubika groups that want a small, readable moderation bot.

---

# ✨ Key Features

## 👑 Administration

* One configured admin
* Admin-only lock changes
* Permission list for the current state
* Private command to read a user ID

## 🛡️ Content Locks

* Links
* Videos
* Photos
* Voice messages
* GIFs
* Stickers
* Emojis
* Text

## 🗑️ Moderation

* Warning reply when a locked type is sent
* Automatic deletion of blocked messages
* Admin messages are not deleted by the locks

---

# 👑 Group Locks

Lock states are stored in the `data_bot` dictionary.

* `True` — that content type is locked
* `False` — that content type is allowed

Supported commands:

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

These flags live in memory. They reset when the bot process stops.

---

# 📋 Permission List

The admin can ask for the current state:

```text
لیست دسترسی ها
لیست دسترسی
```

The reply shows whether members may send each content type.

A private helper command is also available:

```text
/ad_admin_of_mike12
```

In a private chat, this command returns the sender's Rubika user ID.

---

# 🛠️ Technologies

* Python 3.8+
* `rubka`
* Async message handlers
* In-memory lock flags

---

# 🚀 Installation

```bash
git clone https://github.com/sadra-hatami/Rubika-Group-Bot.git
cd Rubika-Group-Bot
pip install rubka
```

---

# ⚙️ Configuration

Do not put the real token inside the repository.

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

Then run:

```bash
export RUBIKA_BOT_TOKEN="YOUR_BOT_TOKEN"
export RUBIKA_ADMIN_ID="YOUR_ADMIN_ID"
python Mike12_Grup.py
```

---

# ▶️ Usage

1. Start the bot.
2. Add it to a Rubika group.
3. Give it permission to delete messages.
4. Send lock commands as the admin.

```bash
python Mike12_Grup.py
```

The main features work in **groups**. The private chat is only used for the user-ID helper command.

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

* Rubika group admins
* Developers learning bot handlers and filters
* Anyone who needs a small Persian lock bot

---

# 🗺️ Roadmap

Possible later improvements:

* Save lock states so they survive a restart
* Support more than one admin
* Per-group settings instead of one global dictionary
* Cleaner handler structure
* Optional log messages for deleted content

---

# ❓ FAQ

### Do the locks stay on after restart?

No. The current version keeps flags in memory only.

### Can regular members change the locks?

No. Only the configured admin ID can change settings.

### Is this the same as Rubika Advanced Group Bot?

No. This repository is the smaller lock bot. The advanced project has management, automation, AI, games, and SQLite settings.

### Why were some messages not deleted?

The bot must be running, must be a group admin, and must have delete permission.

---

# 🔐 Security Notes

* Keep the bot token private.
* If a token was ever pasted into a chat or public file, create a new token and stop using the old one.
* Do not commit `.env` files.
* Add `.env`, secrets, and `__pycache__/` to `.gitignore`.
* Remove any non-Python text accidentally appended after `bot.run()`.

---

# 🤝 Contributing

Contributions are welcome.

You can:

* Report bugs
* Suggest extra lock types
* Help store settings on disk
* Improve command replies
* Submit Pull Requests

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
