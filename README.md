# Zen Wisdom Generator

A minimalist, floating desktop widget built with Python and Flet. This application provides instant, relaxing life advice at the click of a button, designed to sit quietly on your desktop without breaking your focus.

## Features

* **Minimalist UI:** Uncluttered, distraction-free interface with a calming dark mode aesthetic.
* **Smooth Animations:** Utilizes Flet's `AnimatedSwitcher` to create relaxing, 800ms cross-fade transitions between quotes and loading states.
* **Floating Widget Behavior:** Configured to stay "Always on Top" of other windows, acting as a permanent digital desk toy.
* **Keyless API Integration:** Powered by the open [AdviceSlip JSON API](https://api.adviceslip.com/), requiring zero authentication or API keys.
* **Bulletproof Controls:** Features custom, emoji-based interactive containers to ensure 100% compatibility with strict Python linters and Flet updates.

## Privacy & Data Security

* **Zero Tracking:** The app does not collect, store, or transmit any personal data or local files. 
* **Anonymous Requests:** The only information sent over the network is a generic HTTP GET request to fetch a random piece of advice.
* **Safe to Share:** Relying entirely on public endpoints without embedded credentials, you can safely share this source code or host it publicly without any risk.

## Prerequisites

Ensure you have **Python 3.8+** installed on your system. 

You will need the Flet UI framework and the `requests` library to handle HTTP networking:

```bash
pip install flet requests
