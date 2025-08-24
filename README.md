# FAKE_NEWS_GENARATOR
A fun Python project that generates random fake news headlines with categories, emojis, and live ticker mode. Headlines can also be saved to a file.
# 📰 Fake News Channel Generator

A fun Python project that generates random fake news headlines with categories, emojis, and a live ticker mode. Headlines are saved to `fake_news.txt` with timestamps — like your own funny newspaper!

---

## ✨ Features
- 🎭 Choose from categories: **Sports, Bollywood, Politics, Animals**
- 🎲 Random **subjects, actions, places** → hilarious combinations
- 📺 **Live ticker mode** (auto-generates every few seconds)
- ⏳ Set an optional **headline limit** (or run endlessly)
- 📝 Headlines are **saved to a text file** with session headers and timestamps

---

## 🚀 Quickstart

```bash
# Clone the repo (replace YOUR_USERNAME)
git clone https://github.com/YOUR_USERNAME/fake-news-generator.git
cd fake-news-generator

# Run
python fake_news.py
```

---a

## 🔧 Usage

When you run the script, you'll be asked:
- **Category**: `sports`, `bollywood`, `politics`, `animals` (or press Enter for random)
- **Number of headlines**: `0` means unlimited (until Ctrl+C)
- **Interval (seconds)**: time between headlines

**Example output**
```
[22:15:03] BREAKING NEWS: Virat Kohli eats inside parliament! 😂
[22:15:06] BREAKING NEWS: A Lazy Panda dances with at Red Fort! 📰
```

The file `fake_news.txt` will keep appending your headlines, with a header for each run.

---

## 📌 Suggested Repo Topics
`python` · `random` · `fun-project` · `fake-news` · `generator` · `beginner-friendly`

---

## 🗺️ Roadmap Ideas
- Sound effect text cues (e.g., *DUN DUN DUN!*)
- Simple GUI using Tkinter or PyQt
- Export to CSV/JSON
- Option to create memes/images with the headline text

---

## 📝 License
MIT (recommended). Create a file `LICENSE` and paste the MIT License text if you want it to be open-source.
