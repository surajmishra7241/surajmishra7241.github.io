"""Generates the studio site (GitHub Pages): home, per-game landing, privacy, terms and support pages.

Run: python3 tools/build.py   (writes the HTML files next to this folder)
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
DEVELOPER = "Suraj Mishra"
EMAIL = "mail@shubhsandes.com"
UPDATED = "4 October 2026"
SITE = "https://surajmishra7241.github.io"

CSS = """
:root{--bg:#f7f8fb;--card:#fff;--ink:#1d2433;--muted:#5b6475;--line:#e3e6ee;--accent:#ff7a3d;--link:#1f6feb}
@media (prefers-color-scheme:dark){:root{--bg:#10131a;--card:#181c25;--ink:#e9ecf3;--muted:#9aa3b5;--line:#2a303d;--accent:#ff9a66;--link:#6ea8ff}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--link)}header,main,footer{max-width:820px;margin:0 auto;padding:0 20px}
header{padding-top:28px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}header .brand{font-weight:700;font-size:18px;color:var(--ink);text-decoration:none}
header nav{margin-left:auto;display:flex;gap:16px;flex-wrap:wrap}header nav a{text-decoration:none;color:var(--muted)}header nav a:hover{color:var(--ink)}
main{padding-top:12px;padding-bottom:40px}h1{font-size:30px;line-height:1.2;margin:24px 0 6px}h2{font-size:21px;margin:32px 0 8px}h3{font-size:17px;margin:20px 0 6px}
.lead{font-size:18px;color:var(--muted)}.meta{color:var(--muted);font-size:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px 22px;margin:16px 0}
table{width:100%;border-collapse:collapse;margin:10px 0;font-size:15px}th,td{text-align:left;vertical-align:top;padding:9px 10px;border-bottom:1px solid var(--line)}th{color:var(--muted);font-weight:600}
.games{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}.games .card h2{margin-top:0}
.pill{display:inline-block;padding:2px 10px;border-radius:99px;background:var(--accent);color:#fff;font-size:13px;font-weight:600}
footer{border-top:1px solid var(--line);padding:18px 20px 40px;color:var(--muted);font-size:14px}
"""


def page(path, title, body, game=None):
    nav = ""
    if game:
        g = game["slug"]
        nav = (f'<nav><a href="/{g}/">{escape(game["name"])}</a><a href="/{g}/privacy.html">Privacy</a>'
               f'<a href="/{g}/terms.html">Terms</a><a href="/{g}/support.html">Support</a></nav>')
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title><meta name="description" content="{escape(title)} by {DEVELOPER}">
<style>{CSS}</style></head><body>
<header><a class="brand" href="/">{DEVELOPER} Games</a>{nav}</header>
<main>{body}</main>
<footer>&copy; 2026 {DEVELOPER}. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></footer>
</body></html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


TUMBLEPALS = dict(
    slug="tumblepals", name="Tumble Pals",
    tagline="Tap one Pal, watch the chain! Cute domino puzzles for kids and grown-ups.",
    about="""<p>The Tumble Pals fell asleep all over Pebble Isles. Tap a Pal and it wakes up and tumbles &mdash; every friend it
bumps tumbles too, in a happy chain reaction that sends the whole gang home. Every level can be solved, with no lives,
no timers and free undo.</p>""",
    kids=True,
    products=[
        ("Remove Ads", "One-time purchase", "Removes the automatic ad breaks between levels, forever. Reward videos stay optional."),
        ("Pals Club", "Auto-renewing monthly subscription", "No ad breaks, unlimited hints, the Golden Pal and 100 bonus coins every day while active."),
        ("Pouch of Coins / Chest of Coins", "Consumable", "500 or 3,000 coins to spend on hints and Pals."),
    ],
)
SPINANDCARVE = dict(
    slug="spinandcarve", name="Spin & Carve",
    tagline="Woodturning 3D: shape real wood on a spinning lathe, then paint, polish and relax.",
    about="""<p>Turn a rough log into a masterpiece. Carve ash, cherry, oak, olive, walnut and teak on a vintage lathe in six
beautiful places, hit &ldquo;Perfect!&rdquo; cuts, then paint and polish your piece until it shines. Every finished piece
is saved to your gallery.</p>""",
    kids=False,
    products=[
        ("Remove Ads", "One-time purchase", "Removes the automatic ad breaks between levels, forever. Bonus videos stay optional."),
        ("Master's Toolkit", "One-time purchase", "Unlocks every chisel and handle right away."),
        ("Bag of Coins / Crate of Coins", "Consumable", "1,000 or 6,000 coins to spend in the workshop."),
    ],
)


def privacy(g):
    n = g["name"]
    kids = g["kids"]
    audience = (
        f"""<h2>Children</h2>
<p>{n} is made for everyone, including children. When the game starts it asks for the player's year of birth. The answer
<b>never leaves the device</b>; it only decides how the game behaves:</p>
<ul>
<li>Players under 13, or who have not told us their age, are in <b>child mode</b>: every ad request is marked
child-directed (COPPA) and under the age of consent, ads are not personalised, no advertising identifier is used, and ad
content is limited to the &ldquo;G&rdquo; (general audience) rating.</li>
<li>Purchases, links that leave the game and some settings are behind a grown-up check.</li>
<li>There is no chat, no user-generated content shared with others, and no social features.</li>
</ul>
<p>We do not knowingly collect personal information from children. If you believe a child has provided personal
information to us, contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> and we will delete it.</p>"""
        if kids else
        f"""<h2>Children</h2>
<p>{n} is intended for a general audience aged 13 and over and is not directed at children under 13. We do not knowingly
collect personal information from children. If you believe a child has provided personal information to us, contact us
at <a href="mailto:{EMAIL}">{EMAIL}</a> and we will delete it.</p>""")
    rating = "G (general audience)" if kids else "PG"
    body = f"""
<h1>{escape(n)} &mdash; Privacy Policy</h1>
<p class="meta">Last updated: {UPDATED}</p>
<p>This policy explains what information the game <b>{escape(n)}</b> (&ldquo;the game&rdquo;), published by {DEVELOPER}
(&ldquo;we&rdquo;, &ldquo;us&rdquo;), handles, why, and the choices you have. It applies to the game on iPhone, iPad and
Android.</p>

<div class="card"><b>In short:</b> we do not ask for your name, email, contacts, photos or precise location. Your progress is
stored on your device. Ads are provided by Google AdMob and are <b>not personalised</b>. Purchases are handled by Apple or
Google. The game does <b>not</b> track you across other companies' apps and websites and never shows Apple's tracking
permission prompt.</div>

<h2>Information stored on your device</h2>
<p>Game progress, coins, settings, purchases you own and (for age-appropriate behaviour) the year of birth you enter are
saved on your device only. Deleting the game deletes this data. You can also erase it at any time in
<b>Settings &rarr; Delete my data</b>.</p>

<h2>Advertising (Google AdMob)</h2>
<p>The game shows ads from Google AdMob: an occasional full-screen ad between levels and optional reward videos you choose
to watch. To deliver and measure ads and prevent fraud, Google may collect from your device: IP address (and the
approximate location derived from it), device and operating-system information, an app-specific identifier such as the
identifier for vendors (IDFV) on iOS or the app set ID on Android, and ad interactions (for example, whether an ad was shown
or tapped), and diagnostics. Google processes this under its own policy:
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its
services</a>.</p>
<ul>
<li>Ads in the game are <b>not personalised</b> (no interest-based advertising) and are limited to the {rating} content
rating.</li>
<li>The game never requests access to the iOS advertising identifier (IDFA) and does not track you.</li>
<li>In the European Economic Area, the United Kingdom and Switzerland, Google's consent form asks for your choices when
the game first starts; you can change them later in <b>Settings &rarr; Ad privacy choices</b>.</li>
<li>Buying <b>Remove Ads</b> turns off the automatic ad breaks.</li>
</ul>

<h2>In-app purchases</h2>
<p>Purchases are processed by the Apple App Store or Google Play. We never receive your payment card details. The store
tells the game which items your account owns so they can be delivered and restored (product, transaction identifiers and
dates). Subscriptions are managed and cancelled in your Apple ID or Google Play account settings.</p>

<h2>Information we do not collect</h2>
<p>We do not collect your name, email address, phone number, contacts, photos, precise location, health data or
browsing history, and we do not sell or share personal information for cross-context behavioural advertising. We do not
operate any server that receives your gameplay data.</p>

<h2>Contacting support</h2>
<p>If you email us, we receive your email address and whatever you write, and use it only to answer you. We delete
support emails when they are no longer needed.</p>

{audience}

<h2>Your rights</h2>
<p>Depending on where you live (for example under the GDPR, UK GDPR, CCPA/CPRA or India's DPDP Act) you may have the right
to access, correct or delete personal information, to object to or restrict processing, and to withdraw consent. Because
your game data stays on your device, you can delete it yourself with <b>Settings &rarr; Delete my data</b> or by deleting the
game. For anything else, email <a href="mailto:{EMAIL}">{EMAIL}</a>; we answer within 30 days. You may also complain to your
local data-protection authority.</p>

<h2>Security and retention</h2>
<p>Data on your device is kept until you delete it or the game. Network traffic from the game uses encrypted connections
(HTTPS).</p>

<h2>Changes</h2>
<p>If we change how the game handles information, we will update this page and the date above, and, for significant changes,
tell you in the game before the change applies.</p>

<h2>Contact</h2>
<p>{DEVELOPER} &mdash; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""
    page(f"{g['slug']}/privacy.html", f"{n} Privacy Policy", body, g)


def terms(g):
    n = g["name"]
    rows = "".join(f"<tr><td><b>{escape(a)}</b></td><td>{escape(b)}</td><td>{escape(c)}</td></tr>" for a, b, c in g["products"])
    sub = """
<h2>Subscriptions</h2>
<ul>
<li><b>Pals Club</b> is an auto-renewing subscription. The price and billing period are shown in the game before you
buy.</li>
<li>Payment is charged to your Apple ID (or Google Play) account when you confirm the purchase.</li>
<li>The subscription renews automatically unless it is cancelled at least 24 hours before the end of the current
period. Your account is charged for renewal within 24 hours before the end of the current period, at the same price
unless you were told otherwise in advance.</li>
<li>You can manage or cancel the subscription at any time in your device's <b>Settings &rarr; [your name] &rarr;
Subscriptions</b> (iOS) or in the Google Play app. Cancelling stops future renewals; you keep the benefits until the end
of the period you paid for.</li>
<li>If a free trial is offered, any unused part of it is forfeited when you buy a subscription.</li>
</ul>""" if g["kids"] else ""
    body = f"""
<h1>{escape(n)} &mdash; Terms of Use</h1>
<p class="meta">Last updated: {UPDATED}</p>
<p>These terms apply to the game <b>{escape(n)}</b> published by {DEVELOPER}. If you downloaded the game from the Apple App
Store, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User
License Agreement</a> also applies; if anything here conflicts with it, Apple's agreement wins for the App Store version.</p>

<h2>Licence</h2>
<p>We give you a personal, non-transferable, revocable licence to download and play the game for non-commercial purposes.
Do not copy, modify, reverse engineer, resell or exploit the game, or use cheats or automation.</p>

<h2>In-app purchases</h2>
<table><tr><th>Item</th><th>Type</th><th>What you get</th></tr>{rows}</table>
<ul>
<li>Prices are shown in your local currency in the game before you buy and may differ by country.</li>
<li>One-time purchases such as Remove Ads can be restored on another device signed in to the same Apple ID or Google
account with <b>Restore purchases</b> in the game.</li>
<li>Coins are a virtual item with no cash value, cannot be exchanged or refunded except as required by law, and are
lost if you delete your game data.</li>
<li>Refunds for App Store purchases are handled by Apple at
<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>; for Google Play, by Google.</li>
</ul>
{sub}

<h2>Ads</h2>
<p>The free version of the game shows ads. Reward videos are always optional.</p>

<h2>Availability and changes</h2>
<p>We may update the game, change or remove content and features, or stop offering it. We will not remove items you paid
for without a reasonable alternative unless required by law or the store.</p>

<h2>Disclaimer and liability</h2>
<p>The game is provided &ldquo;as is&rdquo;. To the extent the law allows, we are not liable for indirect or consequential
losses. Nothing in these terms limits rights you have under consumer-protection law.</p>

<h2>Privacy</h2>
<p>See the <a href="/{g['slug']}/privacy.html">{escape(n)} Privacy Policy</a>.</p>

<h2>Contact</h2>
<p>{DEVELOPER} &mdash; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""
    page(f"{g['slug']}/terms.html", f"{n} Terms of Use", body, g)


def support(g):
    n = g["name"]
    club = """
<h3>How do I cancel Pals Club?</h3>
<p>On iPhone or iPad open <b>Settings &rarr; [your name] &rarr; Subscriptions &rarr; Pals Club</b> and tap <b>Cancel
Subscription</b>. You keep Club benefits until the end of the period you paid for.</p>""" if g["kids"] else ""
    body = f"""
<h1>{escape(n)} Support</h1>
<p class="lead">Need help? Email <a href="mailto:{EMAIL}?subject={escape(n)}%20support">{EMAIL}</a>. We usually reply within
two working days. Please include your device model and what happened.</p>

<h2>Frequently asked questions</h2>
<h3>I bought Remove Ads (or another item) but it isn't showing.</h3>
<p>Open the shop or <b>Settings</b> in the game and tap <b>Restore purchases</b> while connected to the internet and signed
in to the same Apple ID (or Google account) you used to buy.</p>
<h3>I got a new phone. How do I get my purchases back?</h3>
<p>Install the game, sign in to the same Apple ID or Google account and tap <b>Restore purchases</b>. Progress and coins are
stored on the device and are not transferred.</p>
{club}
<h3>How do I get a refund?</h3>
<p>App Store purchases: request it at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>. Google Play:
follow Google's refund instructions in the Play Store app.</p>
<h3>How do I delete my data?</h3>
<p>In the game open <b>Settings &rarr; Delete my data</b>, or delete the game from your device. Details are in the
<a href="/{g['slug']}/privacy.html">Privacy Policy</a>.</p>
<h3>Can I change my ad privacy choices?</h3>
<p>Yes. In the EEA, UK and Switzerland, open <b>Settings &rarr; Ad privacy choices</b>.</p>
"""
    page(f"{g['slug']}/support.html", f"{n} Support", body, g)


def landing(g):
    n = g["name"]
    body = f"""
<h1>{escape(n)}</h1>
<p class="lead">{escape(g['tagline'])}</p>
{g['about']}
<p><span class="pill">Coming soon to the App Store</span></p>
<div class="card"><a href="/{g['slug']}/privacy.html">Privacy Policy</a> &middot; <a href="/{g['slug']}/terms.html">Terms of Use</a>
&middot; <a href="/{g['slug']}/support.html">Support</a></div>
"""
    page(f"{g['slug']}/index.html", f"{n} by {DEVELOPER}", body, g)


def home(games):
    cards = "".join(
        f"""<div class="card"><h2><a href="/{g['slug']}/">{escape(g['name'])}</a></h2><p>{escape(g['tagline'])}</p>
<p class="meta"><a href="/{g['slug']}/privacy.html">Privacy</a> &middot; <a href="/{g['slug']}/terms.html">Terms</a> &middot;
<a href="/{g['slug']}/support.html">Support</a></p></div>""" for g in games)
    body = f"""<h1>{DEVELOPER} Games</h1><p class="lead">Small, satisfying games for phones.</p>
<div class="games">{cards}</div>"""
    page("index.html", f"{DEVELOPER} Games", body)


NIGHTMARKET = dict(
    slug="nightmarkettycoon", name="Night Market Tycoon",
    tagline="Turn one glowing street stall into the busiest night-market food empire in Saffron Bay.",
    about="""<p>Cook street noodles, tomato soup, steamed dumplings and festival skewers, carry towering stacks to the
counter, collect the cash and build your tiny Ember Stall into a bustling lantern-lit restaurant. Hire crew, open new
rooms, upgrade your cookers and keep the queue happy. Play alone or with up to four friends on one device with
controllers.</p>
<p><b>No ads. No in-app purchases. No account.</b></p>""",
    kids=False, products=[],
)
NMT_UPDATED = "25 October 2026"


def nmt_privacy(g):
    n = g["name"]
    body = f"""
<h1>{escape(n)} &mdash; Privacy Policy</h1>
<p class="meta">Last updated: {NMT_UPDATED}</p>
<p>This policy explains how the game <b>{escape(n)}</b> (&ldquo;the game&rdquo;), published by {DEVELOPER}
(&ldquo;we&rdquo;, &ldquo;us&rdquo;), handles information. It applies to the game on iPhone, iPad and Mac.</p>

<div class="card"><b>In short: we collect no data.</b> The game has no ads, no in-app purchases, no accounts, no analytics and
no tracking. Your progress is stored on your device and, if you use iCloud, in your own iCloud account; achievements go
to Apple's Game Center. We never receive any of it.</div>

<h2>Information stored on your device</h2>
<p>Your restaurant progress, coins, chosen chef and settings (music, effects and ambience volume, haptics, reduced motion)
are saved in the game's own storage on your device. They are never sent to us. Deleting the game deletes this copy (your
iCloud copy, if any, stays in your iCloud until you reset the game or remove it in iCloud settings). If your device backs up apps (for example iCloud Backup), that backup is handled by Apple under Apple's privacy
policy; we cannot access it.</p>

<h2>iCloud and Game Center (Apple)</h2>
<p>If you are signed in to iCloud, a copy of your game save is kept in <b>your own iCloud account</b> (Apple's iCloud
key-value storage) so you can continue after reinstalling or on your other Apple devices. If you use Game Center, your
achievements and your best-day score are shared with Game Center. Both are Apple services, handled under
<a href="https://www.apple.com/legal/privacy/">Apple's Privacy Policy</a>; we cannot see or access this data. You can turn them
off in your device's Settings (iCloud, Game Center), and <b>Settings &rarr; Progress &rarr; Reset</b> in the game erases your
restaurant on all your devices.</p>

<h2>Information we do not collect</h2>
<p>We do not collect, receive or store any personal or usage information: no name, email address, phone number,
contacts, photos, location, identifiers, purchase history, diagnostics or gameplay data. The game contains no
advertising, analytics or tracking software, never asks for Apple's tracking permission, and we do not sell or share
any information.</p>

<h2>Controllers and local multiplayer</h2>
<p>Local co-op uses game controllers connected to your device. Controller input is used only to play and is not stored
or transmitted.</p>

<h2>Contacting support</h2>
<p>If you email us, we receive your email address and whatever you write, and use it only to answer you. We delete support
emails when they are no longer needed.</p>

<h2>Children</h2>
<p>The game is suitable for all ages and collects no information from anyone, including children.</p>

<h2>Your rights</h2>
<p>Because we hold no information about you, there is nothing for us to access, correct or delete. You can remove all game
data yourself by deleting the game. For any question, email <a href="mailto:{EMAIL}">{EMAIL}</a>; we answer within 30 days.</p>

<h2>Changes</h2>
<p>If a future version changes how information is handled, we will update this page and the date above before that version
is released.</p>

<h2>Contact</h2>
<p>{DEVELOPER} &mdash; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""
    page(f"{g['slug']}/privacy.html", f"{n} Privacy Policy", body, g)


def nmt_terms(g):
    n = g["name"]
    body = f"""
<h1>{escape(n)} &mdash; Terms of Use</h1>
<p class="meta">Last updated: {NMT_UPDATED}</p>
<p>These terms apply to the game <b>{escape(n)}</b> published by {DEVELOPER}. If you downloaded the game from the Apple App
Store, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User
License Agreement</a> also applies; if anything here conflicts with it, Apple's agreement wins for the App Store version.</p>
<h2>Licence</h2>
<p>We give you a personal, non-transferable, revocable licence to download and play the game for non-commercial purposes.
Do not copy, modify, reverse engineer, resell or exploit the game.</p>
<h2>Purchases</h2>
<p>The game contains no ads and no in-app purchases. Coins earned in the game are a virtual reward with no cash value.</p>
<h2>Availability and changes</h2>
<p>We may update the game or change its content. To the extent the law allows, the game is provided &ldquo;as is&rdquo; and we
are not liable for indirect or consequential losses. Nothing in these terms limits rights you have under consumer-protection
law.</p>
<h2>Credits</h2>
<p>The game uses third-party assets released under CC0 and the SIL Open Font License (Poly Haven, Kenney, BigSoundBank,
OpenGameArt, Google Fonts); full credits are in the game.</p>
<h2>Privacy</h2>
<p>See the <a href="/{g['slug']}/privacy.html">{escape(n)} Privacy Policy</a>.</p>
<h2>Contact</h2>
<p>{DEVELOPER} &mdash; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""
    page(f"{g['slug']}/terms.html", f"{n} Terms of Use", body, g)


def nmt_support(g):
    n = g["name"]
    body = f"""
<h1>{escape(n)} Support</h1>
<p class="lead">Need help? Email <a href="mailto:{EMAIL}?subject={escape(n)}%20support">{EMAIL}</a>. We usually reply within
two working days. Please include your device model and what happened.</p>
<h2>Frequently asked questions</h2>
<h3>How do I play?</h3>
<p>Drag anywhere on the screen to walk (or use a controller). Everything else happens when you walk up to it: stand at a
cooker to pick up food, at the counter to serve, near cash to collect it, and on a glowing pad to build. The brightest pad
is always the best next step.</p>
<h3>How do I play with friends?</h3>
<p>Connect up to four game controllers to your iPhone, iPad or Mac, then choose the number of chefs in <b>Settings &rarr;
Local chefs</b>.</p>
<h3>Is my progress saved?</h3>
<p>Yes, automatically. If you are signed in to iCloud, your restaurant is also kept in your iCloud, so after reinstalling
or on a new iPhone, iPad or Mac with the same Apple ID the game continues where you left off. <b>Settings &rarr; Progress</b>
shows where it is saved.</p>
<h3>My progress didn't come back after reinstalling.</h3>
<p>Check that you are signed in to iCloud with the same Apple ID and that iCloud is allowed for apps (Settings &rarr; [your
name] &rarr; iCloud). Open the game, wait a few seconds on the main menu, and it restores automatically. Still missing?
Email us with your device model.</p>
<h3>How do I start over?</h3>
<p>Tap <b>New game</b> on the main menu, or <b>Settings &rarr; Progress &rarr; Reset</b>. This erases your restaurant on all your
devices that share the same iCloud account.</p>
<h3>Achievements and leaderboard</h3>
<p>Sign in to Game Center in your device's Settings to earn achievements and post your best day's sales.</p>
<h3>Are there ads or purchases?</h3>
<p>No. The game has no ads and no in-app purchases.</p>
<h3>The game feels slow or my device is warm.</h3>
<p>The game adjusts its resolution automatically to keep running smoothly. Closing other apps and turning on
<b>Settings &rarr; Reduced motion</b> also helps.</p>
"""
    page(f"{g['slug']}/support.html", f"{n} Support", body, g)


games = [TUMBLEPALS, SPINANDCARVE]
for g in games:
    privacy(g); terms(g); support(g); landing(g)
nmt_privacy(NIGHTMARKET); nmt_terms(NIGHTMARKET); nmt_support(NIGHTMARKET); landing(NIGHTMARKET)
home(games + [NIGHTMARKET])
(ROOT / "app-ads.txt").write_text("google.com, pub-1369340241981817, DIRECT, f08c47fec0942fa0\n")
(ROOT / ".nojekyll").write_text("")
(ROOT / "404.html").write_text('<!doctype html><meta charset="utf-8"><title>Not found</title><p>Page not found. <a href="/">Home</a></p>\n')
print("built", sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*.html")))
