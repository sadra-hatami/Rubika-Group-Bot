<div align="center">

# Rubika Group Bot
# 🤖

### A Complete Persian Rubika Group Platform

A full-featured Rubika group bot with **locks**, **filters**, **learning**, **speaker modes**, **AI replies**, **games**, **admin tools**, and **SQLite persistence**.

<br>

# 👨‍💻 **Sadra Hatami**

### *Developer • Software Engineer • Creator*

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Rubka](https://img.shields.io/badge/Rubka-Rubika%20Bot-8E44AD?style=for-the-badge)](https://pypi.org/)
[![AsyncIO](https://img.shields.io/badge/AsyncIO-Asynchronous-2C3E50?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/asyncio.html)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![aiohttp](https://img.shields.io/badge/aiohttp-HTTP%20Client-2C3E50?style=for-the-badge)](https://docs.aiohttp.org/)
[![Requests](https://img.shields.io/badge/Requests-HTTP%20Library-20232A?style=for-the-badge)](https://requests.readthedocs.io/)
[![HTTPX](https://img.shields.io/badge/HTTPX-HTTP%20Client-5A29E4?style=for-the-badge)](https://www.python-httpx.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Parsing-4CAF50?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)
[![AI](https://img.shields.io/badge/AI-Integrated-FF6F00?style=for-the-badge)](#-ai-system)
[![Automation](https://img.shields.io/badge/Automation-Enabled-0078D6?style=for-the-badge)](#️-automation)
[![Moderation](https://img.shields.io/badge/Moderation-Enabled-C0392B?style=for-the-badge)](#️-security--moderation)
[![Persian](https://img.shields.io/badge/Language-Persian-success?style=for-the-badge)](https://en.wikipedia.org/wiki/Persian_language)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
![Open Source](https://img.shields.io/badge/Open_Source-Project-black?style=for-the-badge&logo=github)

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
- [Group Management](#-group-management)
- [Security & Moderation](#️-security--moderation)
- [Learning & Speaker](#-learning--speaker)
- [AI System](#-ai-system)
- [Automation](#️-automation)
- [Games & Extra Tools](#-games--extra-tools)
- [Levels, XP & Badges](#-levels-xp--badges)
- [Operator Panel](#-operator-panel)
- [Database](#-database)
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

**Rubika Group Bot** is a complete Persian group platform for Rubika.

It is not a lock-only script. After the bot is added to a group and activated with `فعال`, administrators can run locks, filters, learning replies, speaker modes, games, optional AI answers, and saved settings from one process.

State lives in SQLite (`chats.db`) so group configuration can survive a restart.

> **Tagline:** *A complete Persian Rubika group platform with locks, learning, speaker modes, AI replies, games, and saved settings.*

---

# 🔗 Related Repositories

| Repository | Role |
|------------|------|
| **[Rubika Group Bot](https://github.com/sadra-hatami/Rubika-Group-Bot)** | Complete group platform (this repo) |
| **[Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot)** | Newest, larger group codebase |
| **[Countries War Bot](https://github.com/sadra-hatami/Countries-War-Bot)** | Nation strategy game |
| **[Telegram Rubika Account Panel](https://github.com/sadra-hatami/Telegram-Rubika-Account-Panel)** | Telegram panel for a Rubika user account |

---

# 🚀 Why This Bot?

A group needs more than one lock switch.

This project keeps the usual community tools together:

- Lock and filter families
- Special and exempt members
- Learning and speaker replies
- Games and extra commands
- Optional AI with a `+` prefix
- An operator panel in private chat
- SQLite persistence

---

# ✨ Key Features

- Group activation and live status
- Owner, assistant admins, special users, exempt users
- Content locks, ban locks, and warn locks
- Anti-link, anti-ad, anti-curse, anti-emoji, anti-edit, anti-mention
- Learning (`یادگیری - پرسش - پاسخ`)
- Speaker modes and a built-in calculator
- Custom commands and auto responders
- XP, levels, badges, and a leaderboard
- Welcome, goodbye, reminders, and auto-delete
- Polls, events, giveaways, notes
- Private `/start` onboarding and operator panel
- Persistent SQLite storage

---

# 👑 Group Management

```text
فعال
ربات روشن
ربات خاموش
وضعیت گروه
قوانین
تنظیم قوانین
```

`فعال` registers the group owner. After that, systems can be turned on per chat.

---

# 🛡️ Security & Moderation

| System | Role |
|--------|------|
| Content locks | Block a message type |
| Ban / warn locks | Stronger lock actions |
| Anti-Link | Controls links |
| Anti-Advertisement | Controls ads |
| Anti-Curse | Filters blocked language |
| Anti-Emoji / Anti-Edit / Anti-Mention | Extra filters |
| Auto-delete | Removes matched messages after a delay |

The bot must be a group admin with delete permission.

---

# 🧠 Learning & Speaker

```text
یادگیری - سلام - خوبی
حذف یادگیری - سلام
لیست یادگیری‌ها
```

Speaker modes can stay polite, personal, or default. Learned replies are stored per group.

---

# 🤖 AI System

```text
+پایتون چیست؟
```

Works in private chat and, when enabled, in groups. If the external API is missing, the rest of the bot still runs.

---

# ⚙️ Automation

Welcome and goodbye texts, reminders, timers, custom commands, and auto responders can be limited to the groups where they are enabled.

---

# 🎮 Games & Extra Tools

```text
بازی ریاضی
فال حافظ
دیالوگ
انگیزشی
اخبار
بیو
وضعیتم
```

These are group and utility commands, not a separate game server.

---

# 🏆 Levels, XP & Badges

Members can receive XP in the group. Levels and badges are stored in SQLite.

```text
لیست برترینها
```

---

# 🛠️ Operator Panel

In private chat, the configured operator can open a panel for stats and broadcast tools.

```text
/panel
پنل
```

Do not publish the operator ID inside the source file.

---

# 💾 Database

`chats.db` holds:

- Levels and badges
- Custom commands and learning
- Warnings and locks
- Welcome, goodbye, reminders
- Notes, events, giveaways, polls

Do not commit this file.

---

# 📁 Project Structure

```text
Rubika-Group-Bot/
├── index.py
├── chats.db      # created at runtime
└── README.md
```

---

# 🛠️ Technologies

- Python 3.8+
- `rubka`
- asyncio
- SQLite
- aiohttp, requests, httpx
- BeautifulSoup
- jdatetime

---

# 🚀 Installation

```bash
git clone https://github.com/sadra-hatami/Rubika-Group-Bot.git
cd Rubika-Group-Bot
pip install rubka aiohttp requests httpx beautifulsoup4 jdatetime
```

```bash
python index.py
```

---

# ⚙️ Configuration

```text
RUBIKA_BOT_TOKEN
RUBIKA_ADMIN_ID
AI_API_URL
```

`.gitignore`:

```text
.env
chats.db
__pycache__/
```

---

# ▶️ Usage

1. Move secrets out of the source file.
2. Start `index.py`.
3. Add the bot to a Rubika group.
4. Grant administrator permission.
5. Send `فعال`.
6. Use `وضعیت گروه` and `راهنما` inside the group.

---

# 📚 Command Examples

```text
فعال
راهنما
وضعیت گروه
ربات روشن
ضد لینک روشن
لینک قفل
یادگیری - سلام - خوبی
+پایتون چیست؟
بازی ریاضی
فال حافظ
لیست برترینها
```

---

# 🎓 Target Audience

- Rubika group owners
- Communities that need locks plus learning and games
- Developers studying a large `rubka` group bot

---

# 🗺️ Roadmap

- Move secrets to environment variables
- Split handlers into packages
- Clearer command documentation

The newest group codebase is in [Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot).

---

# ❓ FAQ

### Is this only a lock bot?

No. Locks are one family of tools. Learning, speaker, games, AI, XP, and the operator panel are part of the same bot.

### Where is the newer group platform?

[Rubika Advanced Group Bot](https://github.com/sadra-hatami/Rubika-Advanced-Group-Bot)

### Do settings survive a restart?

Yes, when SQLite is working.

---

# 🔐 Security Notes

- Never commit the bot token, admin chat ID, or channel usernames.
- If those values were pasted into the source file, replace them before a public push.
- Keep `chats.db` private.

---

# 🤝 Contributing

Cleanup, documentation, and safer configuration are welcome.

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

---

# ⭐ Support

If this platform helped you run a Rubika group, please consider giving it a ⭐ on GitHub.

---

<div align="center">

## Designed & Developed with ❤️ for the developer community of Iran and the world by **Sadra Hatami**

</div>
