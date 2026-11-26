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
<p><b>Free to play. Works offline. Local co-op. No account.</b></p>""",
    kids=False, products=[],
)
NMT_UPDATED = "25 October 2026"
NMT_PRIVACY_UPDATED = "14 November 2026"   # ads, purchases, age question, tracking prompt (version 1.2)


def nmt_privacy(g):
    n = g["name"]
    body = f"""
<h1>{escape(n)} &mdash; Privacy Policy</h1>
<p class="meta">Last updated: {NMT_PRIVACY_UPDATED}</p>
<p>This policy explains how the game <b>{escape(n)}</b> (&ldquo;the game&rdquo;), published by {DEVELOPER}
(&ldquo;we&rdquo;, &ldquo;us&rdquo;), handles information. It applies to the game on iPhone, iPad and Mac.</p>

<div class="card"><b>In short:</b> the game is free and shows ads on iPhone and iPad (optional reward videos, and an occasional
full-screen ad between restaurant days), served through Unity LevelPlay by ironSource Ads, Google AdMob and Unity Ads. There
are optional in-app purchases and no accounts. Your progress is stored on your device and, if you use iCloud, in your own
iCloud account; achievements go to Apple's Game Center. The game asks your age once: players under 13 get no analytics and
only child-directed ads. With your permission (asked first in the EEA, UK and Switzerland; on by default elsewhere and
switchable off in <b>Settings &rarr; Analytics</b>) we use <b>Google Analytics for Firebase</b> to see how the game is played
and measure our own advertising. Ads are <b>not personalised</b> unless you are 16 or older <b>and</b> allow tracking when
Apple's prompt asks. The Mac version has no ads.</div>

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

<h2>Your age</h2>
<p>When the game first starts it asks how old you are (under 13, 13 to 15, or 16 or older). The answer stays on your device
and decides:</p>
<ul>
<li><b>Under 13:</b> no analytics, never the tracking prompt, and every ad request is marked child-directed (COPPA), not
personalised and limited to the &ldquo;G&rdquo; (general audience) content rating.</li>
<li><b>13 to 15:</b> analytics as described below; ads are not personalised (marked under the age of consent) and rated G.</li>
<li><b>16 or older:</b> analytics as described below; ads are rated G and personalised only if you allow tracking.</li>
</ul>
<p>Nothing is measured and no ad is requested until you answer.</p>

<h2>Analytics (Google Analytics for Firebase)</h2>
<p>To understand how many people play, where new players get stuck and which of our ads on Google bring new players, the
game uses Google Analytics for Firebase, provided by Google. When analytics is allowed it receives:</p>
<ul>
<li>an app-instance identifier created by Firebase (not your name, email, Apple ID or the advertising identifier);</li>
<li>device and app information: device model, iOS version, app version, language, country/region (derived from your IP
address, which Google does not store as such), first-open and session times;</li>
<li>game events: tutorial steps completed, restaurant level reached, rooms, cookers, crew and upgrades bought, days
closed and their sales total, "new game" and iCloud restores, purchases (product and price), reward videos watched and the
estimated value of ads shown.</li>
</ul>
<p>We use this to improve the game and to measure our own advertising campaigns (for example, how many installs an ad
brought). Unless you allow tracking (below), it is not used for personalised advertising and is not combined with data from
other companies' apps or websites. Google processes this data under its own policy:
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from apps that use its
services</a>, and keeps detailed event data for 2 months (the Google Analytics default; reports use aggregated counts).</p>
<ul>
<li><b>EEA, UK and Switzerland:</b> nothing is collected until you choose <b>Allow</b> on the one-time privacy card.</li>
<li><b>Everywhere:</b> turn it off any time in <b>Settings &rarr; Analytics</b>. Analytics stops on that device.</li>
</ul>

<h2>Advertising</h2>
<p>On iPhone and iPad the game shows optional reward videos you choose to watch (for example, to double a day's takings) and,
from the fourth restaurant day, an occasional full-screen ad as you close a day's summary. Owner's Pass holders never see
the full-screen ads. All ads are limited to the &ldquo;G&rdquo; content rating.</p>
<p>Ads are served through <b>Unity LevelPlay</b>, an ad mediation service of Unity Technologies (ironSource), which picks
each ad from <b>ironSource Ads, Google AdMob and Unity Ads</b>. To deliver and measure ads and prevent fraud, these ad partners
may collect from your device: IP address (and the approximate location derived from it), device and operating-system
information, the identifier for vendors (IDFV), ad interactions (for example, whether an ad was shown or tapped) and
diagnostics. Each processes this under its own policy:
<a href="https://unity.com/legal/game-player-and-app-user-privacy-policy">Unity (LevelPlay, ironSource Ads, Unity Ads)</a> and
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its
services</a>. When analytics is on, the game also sends the estimated value of each ad shown (no personal data) to Google
Analytics for Firebase.</p>
<ul>
<li><b>Tracking.</b> If you said you are 16 or older, the game shows Apple's App Tracking Transparency prompt once, after
your first finished day. Only if you choose <b>Allow</b> do the ad partners receive your device's advertising identifier
(IDFA), may ads be personalised to your interests, and may Google Analytics share play statistics with Google's advertising
services to measure which of our ads brought you to the game. Either answer leaves the game the same; change it any time in
iOS <b>Settings &rarr; Privacy &amp; Security &rarr; Tracking</b>. Players under 16 are never asked.</li>
<li><b>EEA, UK and Switzerland:</b> Google's consent form asks for your ad choices before the first ad; change them later in
<b>Settings &rarr; Ad choices</b>.</li>
</ul>

<h2>In-app purchases</h2>
<p>Purchases (Owner's Pass, Chef Pack, coin packs) are processed by Apple. We never receive your payment details. The App
Store tells the game which items your Apple ID owns so they can be delivered and restored (product, transaction identifiers
and dates); this stays on your device and in your iCloud save.</p>

<h2>Information we do not collect</h2>
<p>We do not collect your name, email address, phone number, contacts, photos, precise location, health data or browsing
history, and we do not sell personal information. If you allow tracking, our ad partners may use your advertising identifier
for personalised ads, which some US state laws treat as &ldquo;sharing&rdquo; for cross-context behavioural advertising; you can
stop this at any time by turning tracking off in iOS Settings.</p>

<h2>Controllers and local multiplayer</h2>
<p>Local co-op uses game controllers connected to your device. Controller input is used only to play and is not stored
or transmitted.</p>

<h2>Contacting support</h2>
<p>If you email us, we receive your email address and whatever you write, and use it only to answer you. We delete support
emails when they are no longer needed.</p>

<h2>Children</h2>
<p>The game is suitable for all ages but is not directed at children under 13. Players who say they are under 13 get no
analytics, are never asked about tracking, and only see child-directed, non-personalised ads rated G. If you believe a child
has sent us personal information (for example by email), contact us and we will delete it.</p>

<h2>Your rights</h2>
<p>Depending on where you live (for example under the GDPR, UK GDPR, CCPA/CPRA or India's DPDP Act) you may have the right to
access, correct or delete personal information, to object to or restrict processing, and to withdraw consent. You can
withdraw analytics consent at any time in <b>Settings &rarr; Analytics</b>, change ad choices in <b>Settings &rarr; Ad
choices</b> (EEA, UK, Switzerland) or tracking in iOS Settings, reset your game in <b>Settings &rarr; Progress &rarr;
Reset</b>, or delete the game. Analytics data is not linked to your identity, so to ask Google to delete it, email us the
approximate date you played and your device model and we will request deletion of that app instance. Email
<a href="mailto:{EMAIL}">{EMAIL}</a>; we answer within 30 days. You may also complain to your local data-protection authority.</p>

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
<p>The game is free. It shows ads on iPhone and iPad and offers optional in-app purchases (Owner's Pass, Chef Pack and coin
packs), processed by Apple under the App Store's terms; Restore Purchases is in the Shop. Nothing for sale is needed to finish
the game. Coins have no cash value and cannot be exchanged for money.</p>
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
<p>The game is free. On iPhone and iPad it offers optional reward videos and shows an occasional ad as you close a day; the
Owner's Pass removes those ads and doubles your cash. Purchases are optional and Restore Purchases is in the Shop. Players
of the earlier paid version keep the Owner's Pass and Chef Pack for free.</p>
<h3>How do I turn analytics off?</h3>
<p>Open <b>Settings &rarr; Analytics</b> and switch it off. Details are in the <a href="/{g['slug']}/privacy.html">Privacy Policy</a>.</p>
<h3>The game feels slow or my device is warm.</h3>
<p>The game adjusts its resolution automatically to keep running smoothly. Closing other apps and turning on
<b>Settings &rarr; Reduced motion</b> also helps.</p>
"""
    page(f"{g['slug']}/support.html", f"{n} Support", body, g)


FAIRWAY = dict(
    slug="fairwayshowdown", name="Fairway Showdown",
    tagline="Head-to-head tour golf with one thumb. Beat named rivals, win championships, dress your golfer.",
    about="""<p>Read the wind, pick the club, set the spin and stop the needle in the gold. Play match play against named
rivals across four tours, fight through championships of 64 golfers, and try seven special events including The Bogey Run.
Four courses: parkland, desert, clifftop links and volcanic islands. Five golfers with their own strengths, and clubs,
balls, bags and clothes to earn by playing.</p>
<p><b>Free to play. No account. Plays offline.</b></p>""",
    kids=False, products=[],
)
FS_UPDATED = "3 November 2026"
FS_PRIVACY_UPDATED = "20 November 2026"   # 1.1: challenge links, settings/time, consent region, Google consent form, Ad Quality


def fs_privacy(g):
    n = escape(g["name"])
    body = f"""
<h1>{n} &mdash; Privacy Policy</h1>
<p class="meta">Last updated: {FS_PRIVACY_UPDATED}</p>
<p>This policy covers the game <b>{n}</b> (&ldquo;the game&rdquo;), published by {DEVELOPER} (&ldquo;we&rdquo;, &ldquo;us&rdquo;),
on iPhone (and on iPad, which runs iPhone apps).</p>

<div class="card"><b>In short:</b> the game is free with optional in-app purchases and shows ads (optional reward videos and
an occasional full-screen ad between rounds), served through Unity LevelPlay by ironSource Ads, Google AdMob and Unity Ads.
There are no accounts. Your progress stays on your device and in your own iCloud. With your permission (asked first in the
EEA, UK and Switzerland; on by default elsewhere) anonymous gameplay statistics go to <b>Google Analytics for Firebase</b>;
switch them off any time in <b>Settings &rarr; Share usage stats</b>. Ads are <b>personalised only</b> if usage stats are on
<b>and</b> you allow tracking when Apple's prompt asks (and, in the EEA, UK and Switzerland, Google's consent form allows it). A challenge link you choose to send carries your player name and
score; our server shows them on the challenge page and does not keep them.</div>

<h2>Information stored on your device and in iCloud</h2>
<p>Your progress (golfers, clubs, clothes, coins and gems, tour results, trophies, records), items you bought and your
settings are saved in the game's own storage on your device and, if you are signed in to iCloud, in <b>your own iCloud
account</b> so a new device or a reinstall carries on. We cannot see either copy. Deleting the game deletes the copy on the
device; the iCloud copy is handled by Apple under <a href="https://www.apple.com/legal/privacy/">Apple's Privacy Policy</a>.</p>

<h2>Analytics (Google Analytics for Firebase)</h2>
<p>To see how the game is played, improve it and measure our own advertising, the game uses Google Analytics for Firebase,
provided by Google. When usage stats are on it receives:</p>
<ul>
<li>an app-instance identifier created by Firebase and the identifier for vendors (IDFV), not your name, email or Apple ID;</li>
<li>device and app information: device model, iOS version, app version, language, country/region (derived from your IP
address, which Google does not store as such), first-open and session times;</li>
<li>game events: tutorial steps, rounds started and finished, screens opened, coins earned, trophies, shop visits,
purchases (product and price), reward videos watched and the estimated value of ads shown.</li>
</ul>
<p>Google processes this under its own policy:
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from apps that use its
services</a>, and keeps detailed event data for 2 months (the Google Analytics default; reports use aggregated counts).</p>
<ul>
<li><b>EEA, UK and Switzerland:</b> nothing is collected until you choose <b>Allow</b> on the one-time privacy card. The game
treats you as there if your device's region or time zone is in one of these countries, or once Google's consent check (made
with the ads, from your IP address) says its consent form applies to you; from then on stats stop until you choose.</li>
<li><b>Everywhere:</b> turn it off any time in <b>Settings &rarr; Share usage stats</b>. Stats then stop and ads are no longer
personalised.</li>
</ul>

<h2>Advertising</h2>
<p>The game shows optional reward videos you choose to watch (for example, to double a round's coins or retake a shot) and,
after your first rounds, an occasional full-screen ad as you leave a finished round. Remove Ads turns the full-screen ads
off for good. Google AdMob ads are limited to its &ldquo;PG&rdquo; content rating. The game is made for a general audience,
so ad requests are not marked as directed at children.</p>
<p>Ads are served through <b>Unity LevelPlay</b>, an ad mediation service of Unity Technologies (ironSource), which picks
each ad from <b>ironSource Ads, Google AdMob and Unity Ads</b>; LevelPlay includes Unity's Ad Quality component, which checks
the ads shown for quality and safety. To deliver and measure ads and prevent fraud, these ad partners
may collect from your device: IP address (and the approximate location derived from it), device and operating-system
information, the identifier for vendors (IDFV), ad interactions (for example, whether an ad was shown or tapped) and
diagnostics. Each processes this under its own policy:
<a href="https://unity.com/legal/game-player-and-app-user-privacy-policy">Unity (LevelPlay, ironSource Ads, Unity Ads)</a> and
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its
services</a>. When analytics is on, the game also sends the estimated value of each ad shown (no personal data) to Google
Analytics for Firebase.</p>
<ul>
<li><b>Tracking.</b> If usage stats are on, the game shows Apple's App Tracking Transparency prompt once. Only if you choose
<b>Allow</b> do the ad partners receive your device's advertising identifier (IDFA), may ads be personalised to your
interests, and may Google Analytics share statistics with Google's advertising services to measure which of our ads brought
you to the game. Either answer leaves the game the same; change it any time in iOS <b>Settings &rarr; Privacy &amp; Security
&rarr; Tracking</b>.</li>
<li><b>EEA, UK and Switzerland:</b> Google's consent form asks for your ad choices before the first ad; change them later in
<b>Settings &rarr; Ad privacy choices</b>. The ad partners read your answers there directly, and the game applies them to
Google Analytics too: if you decline personalised ads there, Google Analytics may not use your data for advertising.</li>
</ul>

<h2>In-app purchases</h2>
<p>Purchases (Full Tour, Golfer Pack, Remove Ads, coin packs) are processed by Apple. We never receive your payment details.
The App Store tells the game which items your Apple ID owns so they can be delivered and restored (product, transaction
identifiers and dates); this stays on your device and in your iCloud save.</p>

<h2>Apple services</h2>
<p>The game may ask Apple to show its standard &ldquo;rate this app&rdquo; prompt after you win a championship. That prompt
is run by Apple; we receive no information from it. Apple may give us anonymous, aggregated download and crash statistics
through App Store Connect if you have chosen to share them with developers in your device settings.</p>

<h2>Sharing a result</h2>
<p>If you tap <b>Share</b> after a match, the game opens your device's share sheet with a short text of your result and a
link to the game. Nothing is sent unless you choose where to send it.</p>

<h2>Challenging a friend</h2>
<p>If you tap <b>Challenge a friend</b> (or <b>Send one back</b>) on a result screen, the game builds a link and opens your
device's share sheet; nothing is sent unless you choose where to send it. The link itself contains the challenge: the kind of
round, a number that picks its holes and wind, the day or week for a Daily Challenge or Weekly Cup, your score, and the player
name you chose in the game (change it any time in <b>Profile &rarr; Change name</b>). Anyone who receives the link can read
these.</p>
<p>The link opens a page on our server (<b>evapi.shubhsandes.com</b>), which shows the challenge from the link and offers to
open or download the game. The server does not store the name, score or link. It keeps only a daily count of how many
challenge pages were opened, by kind of round, with nothing about who opened them. The connection passes through Cloudflare,
our hosting network, which handles your IP address to deliver the page under
<a href="https://www.cloudflare.com/privacypolicy/">Cloudflare's privacy policy</a>. When a friend's link opens the game, the
game reads the challenge from the link on your device.</p>

<h2>Game settings and time</h2>
<p>When it starts and when you return to it, the game asks the same server for its current settings (for example event and
ad pacing limits) and reads the server's clock so daily and weekly events change at the right time. This request carries no
identifier, name, score or other game data. If the server can't be reached, the game uses its built-in settings and plays
the same.</p>

<h2>Information we do not collect</h2>
<p>We do not collect your name (the player name in a challenge link is read from the link and not stored), email address,
phone number, contacts, photos, precise location, health data or browsing history, and we do not sell personal information. If you allow tracking, our ad partners may use your advertising identifier
for personalised ads, which some US state laws treat as &ldquo;sharing&rdquo; for cross-context behavioural advertising; you can
stop this at any time by turning tracking off in iOS Settings or usage stats off in the game.</p>

<h2>Children</h2>
<p>{n} is made for a general audience and is not directed at children under 13. We do not knowingly collect personal
information from children. If you believe a child has provided personal information to us, contact us at
<a href="mailto:{EMAIL}">{EMAIL}</a> and we will delete it.</p>

<h2>Your rights</h2>
<p>Depending on where you live (for example under the GDPR, UK GDPR, CCPA/CPRA or India's DPDP Act) you may have the right to
access, correct or delete personal information, to object to or restrict processing, and to withdraw consent. Switch usage
stats off in <b>Settings &rarr; Share usage stats</b>, change ad choices in <b>Settings &rarr; Ad privacy choices</b> (EEA, UK,
Switzerland) or tracking in iOS Settings, or delete the game. We don't know who you are: analytics data is tied to a random app-instance identifier, not to a name or
account. To ask Google to delete it, email us the approximate date you played and your device model and we will request
deletion of that app instance. Email <a href="mailto:{EMAIL}">{EMAIL}</a>; we answer within 30 days. You may also complain to your local
data-protection authority.</p>

<h2>Changes</h2>
<p>If a future version changes how information is handled, we will update this page and the date above before that version
is released.</p>

<h2>Contact</h2>
<p>{DEVELOPER} &mdash; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""
    page(f"{g['slug']}/privacy.html", f"{g['name']} Privacy Policy", body, g)


def fs_terms(g):
    n = escape(g["name"])
    body = f"""
<h1>{n} &mdash; Terms of Use</h1>
<p class="meta">Last updated: {FS_UPDATED}</p>
<p>These terms apply to the game <b>{n}</b> published by {DEVELOPER}. Apple's
<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License
Agreement</a> also applies; if anything here conflicts with it, Apple's agreement wins.</p>
<h2>Licence</h2>
<p>We give you a personal, non-transferable, revocable licence to play the game for non-commercial purposes. Do not copy,
modify, reverse engineer, resell or exploit the game.</p>
<h2>Price and purchases</h2>
<p>The game is free. It shows ads and offers optional in-app purchases (Full Tour, Golfer Pack, Remove Ads and coin packs),
processed by Apple under the App Store's terms; Restore Purchases is in the Shop and in Settings. Coins and gems have no cash
value and cannot be sold or exchanged for money.</p>
<h2>Names</h2>
<p>All golfers, rivals, tours, courses, events and equipment in the game are fictional. Any resemblance to real people,
tournaments or brands is coincidental.</p>
<h2>Availability and changes</h2>
<p>We may update the game or change its content. To the extent the law allows, the game is provided &ldquo;as is&rdquo; and we
are not liable for indirect or consequential losses. Nothing in these terms limits rights you have under consumer-protection
law.</p>
<h2>Credits</h2>
<p>The game uses third-party assets released under CC0 and the SIL Open Font License (Quaternius, ambientCG, Poly Haven,
Kenney, Google Fonts and others); full credits are in the game under Settings.</p>
<h2>Privacy</h2>
<p>See the <a href="/{g['slug']}/privacy.html">{n} Privacy Policy</a>.</p>
<h2>Contact</h2>
<p>{DEVELOPER} &mdash; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""
    page(f"{g['slug']}/terms.html", f"{g['name']} Terms of Use", body, g)


def fs_support(g):
    n = escape(g["name"])
    body = f"""
<h1>{n} Support</h1>
<p class="lead">Need help? Email <a href="mailto:{EMAIL}?subject=Fairway%20Showdown%20support">{EMAIL}</a>. We usually reply
within two working days. Please include your iPhone model and what happened.</p>
<h2>Frequently asked questions</h2>
<h3>How do I hit a shot?</h3>
<p>Drag to aim and set the distance (a faint blue line shows where the wind will take the ball), choose a club and spin,
then hold the swing button and let go with the needle in the gold zone. The white centre is a flush strike. On the green, the drifting marks show the
slope: aim above the hole on a break.</p>
<h3>Which golfer is mine?</h3>
<p>Yours is always marked in teal, with a YOU tag and a teal ring at its feet; your rival is always coral. The card at the top
of the screen says whose shot it is.</p>
<h3>How do I change my golfer's clothes?</h3>
<p>Open <b>Golfers</b>, pick a golfer you own and tap <b>Wardrobe</b>. Clothes are bought with coins or gems earned by playing
and change looks only, never stats.</p>
<h3>There is no sound.</h3>
<p>Turn up the volume with the side buttons while the game is open, and check <b>Settings &rarr; Music</b> and
<b>Sound effects</b> in the game. The game plays even with the ring switch on silent.</p>
<h3>Is my progress saved?</h3>
<p>Yes, automatically, on your iPhone and in your own iCloud account if you are signed in, so a reinstall or a new device
carries on.</p>
<h3>Are there ads or purchases?</h3>
<p>The game is free. It offers optional reward videos and shows an occasional ad between rounds; Remove Ads turns those
ads off. Purchases are optional and Restore Purchases is in the Shop and in Settings. Players of the earlier paid version
keep Remove Ads, Full Tour and the Golfer Pack for free.</p>
<h3>How do I get a refund?</h3>
<p>Request it from Apple at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<h3>Privacy</h3>
<p>With usage stats on, anonymous gameplay statistics go to Google Analytics for Firebase; switch them off in <b>Settings
&rarr; Share usage stats</b>. Ads come from Unity LevelPlay with ironSource Ads, Google AdMob and Unity Ads. See the
<a href="/{g['slug']}/privacy.html">Privacy Policy</a>.</p>
"""
    page(f"{g['slug']}/support.html", f"{g['name']} Support", body, g)


INKFLIGHT = dict(
    slug="inkflight", name="Inkflight",
    tagline="Arrow puzzles that restore beautiful engravings. Clear the arrows, reveal the art.",
    about="""<p>Every page of the Atlas hides an illustration under a tangle of ink arrows. Tap an arrow and it flies off the
page the way it points; every arrow you clear washes its part of the engraving into colour. Six collections and 180
hand-checked pages, from a fox and a lighthouse to Saturn and a palace gate, with four tools to help: Pencil, Eraser,
Lens and Quill.</p>
<p><b>Free to play. No account. Plays offline.</b> Optional Atlas Club membership: no ads, a new members' page every day
and a daily gift.</p>""",
    kids=False, products=[],
)
IF_UPDATED = "25 November 2026"


def if_privacy(g):
    n = escape(g["name"])
    body = f"""
<h1>{n} &mdash; Privacy Policy</h1>
<p class="meta">Last updated: {IF_UPDATED}</p>
<p>This policy covers the game <b>{n}</b> (&ldquo;the game&rdquo;), published by {DEVELOPER} (&ldquo;we&rdquo;, &ldquo;us&rdquo;),
on iPhone and iPad.</p>

<div class="card"><b>In short:</b> the game is free. It shows ads (optional reward videos, an occasional full-screen ad between
pages and a small banner while you play), served through Unity LevelPlay by ironSource Ads, Google AdMob and Unity Ads, and
offers optional in-app purchases and an optional <b>Atlas Club</b> subscription, all processed by Apple. There are no
accounts and no server of ours: your progress stays on your device and, if you leave iCloud save on, in your own iCloud. With usage stats on (the default; in the
EEA, UK and Switzerland they stay off unless you agree on Google's consent form) anonymous gameplay statistics go to <b>Google
Analytics for Firebase</b>; switch them off any time in <b>Settings &rarr; Share usage stats</b>. Ads are <b>personalised
only</b> if usage stats are on <b>and</b> you allow tracking when Apple's prompt asks (and, in the EEA, UK and Switzerland,
only if you agree on Google's consent form; while the game does not show that form there, ads there are never personalised).</div>

<h2>Information stored on your device and in your iCloud</h2>
<p>Your progress (pages finished, stars, coins, tools, pictures restored, daily gifts), items you bought, your membership
status and your settings are saved in the game's own storage on your device. With <b>Settings &rarr; iCloud save</b> on (the
default) a copy is also kept in your own iCloud account through Apple's iCloud key-value storage, so your progress comes
back if you reinstall the game or play on another iPhone or iPad signed in to the same Apple Account. Apple stores this copy
under its own privacy policy; we cannot see it. Turn iCloud save off in the game, or remove the game's iCloud data in iOS
<b>Settings &rarr; your name &rarr; iCloud</b>.</p>

<h2>Game Center</h2>
<p>If you are signed in to Apple's Game Center, the game sends your number of pages restored and stars to its leaderboards
and unlocks achievements. Apple runs Game Center and shows your Game Center nickname to other players as set in your Game
Center settings; we do not receive your Apple ID or contacts. You can sign out of Game Center in iOS Settings.</p>

<h2>Analytics (Google Analytics for Firebase)</h2>
<p>To see how the game is played, improve it and measure our own advertising, the game uses Google Analytics for Firebase,
provided by Google. When usage stats are on it receives:</p>
<ul>
<li>an app-instance identifier created by Firebase and the identifier for vendors (IDFV), not your name, email or Apple ID;</li>
<li>device and app information: device model, iOS version, app version, language, country/region (derived from your IP
address, which Google does not store as such), first-open and session times;</li>
<li>game events: pages started, won and lost, tools used, screens and offers viewed, purchases and subscriptions (product
and price), reward videos watched and the estimated value of ads shown.</li>
</ul>
<p>Google processes this under its own policy:
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from apps that use its
services</a>, and keeps detailed event data for 2 months (reports use aggregated counts).</p>
<ul>
<li><b>EEA, UK and Switzerland:</b> nothing is collected unless you agree on Google's consent form; while the game does
not show that form, nothing is collected there at all. The game treats you as there if your device's region is in one of
these countries or Google's consent check says its form applies to you.</li>
<li><b>Everywhere:</b> turn it off any time in <b>Settings &rarr; Share usage stats</b>. Stats then stop, ads are no longer
personalised and the game does not ask for tracking.</li>
</ul>

<h2>Advertising</h2>
<p>The game shows optional reward videos you choose to watch (for example, extra hearts, double coins, a free tool or free
coins), a full-screen ad now and then as you leave a finished page (never while you are solving one, never after a lost
page, and not on the first pages), and a small banner at the bottom of the puzzle screen on later pages. <b>No Ads</b>
turns the full-screen ads and the banner off for good; <b>Atlas Club</b> members see no ads at all. Google AdMob ads are
limited to its &ldquo;G&rdquo; content rating, and ad requests are not marked as directed at children.</p>
<p>Ads are served through <b>Unity LevelPlay</b>, an ad mediation service of Unity Technologies (ironSource), which picks
each ad from <b>ironSource Ads, Google AdMob and Unity Ads</b>; LevelPlay includes Unity's Ad Quality component, which checks
the ads shown for quality and safety. To deliver and measure ads and prevent fraud, these ad partners may collect from your
device: IP address (and the approximate location derived from it), device and operating-system information, the identifier
for vendors (IDFV), ad interactions (for example, whether an ad was shown or tapped) and diagnostics. Each processes this
under its own policy:
<a href="https://unity.com/legal/game-player-and-app-user-privacy-policy">Unity (LevelPlay, ironSource Ads, Unity Ads)</a> and
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its
services</a>. When usage stats are on, the game also sends the estimated value of each ad shown (no personal data) to Google
Analytics for Firebase.</p>
<ul>
<li><b>Tracking.</b> If usage stats are on, the game shows Apple's App Tracking Transparency prompt once, after your first
pages, with a short note first. Only if you choose <b>Allow</b> do the ad partners receive your device's advertising
identifier (IDFA), may ads be personalised to your interests, and may Google Analytics share statistics with Google's
advertising services to measure which of our ads brought you to the game. Either answer leaves the game the same; change it
any time in iOS <b>Settings &rarr; Privacy &amp; Security &rarr; Tracking</b>.</li>
<li><b>EEA, UK and Switzerland:</b> ads are not personalised unless you agree on Google's consent form. When the game shows
that form, it asks before the first ad and you can change your choices later in <b>Settings &rarr; Privacy Choices</b>; the
ad partners read your answers directly, and the game applies them to Google Analytics too. While it does not show the form,
only non-personalised ads are requested there.</li>
</ul>

<h2>Purchases and the Atlas Club subscription</h2>
<p>Purchases (bundles, coins, Safety Net, No Ads) and the <b>Atlas Club</b> subscription are processed by Apple. We never
receive your name, Apple ID or payment details. The App Store tells the game which items and which membership your Apple ID
owns, with product, transaction identifiers and dates, so they can be delivered, renewed and restored; this stays on your
device. You manage or cancel the subscription in your Apple Account settings.</p>

<h2>Apple services</h2>
<p>The game may ask Apple to show its standard &ldquo;rate this app&rdquo; prompt after a good win. That prompt is run by
Apple; we receive no information from it. Apple may give us anonymous, aggregated download, sales and crash statistics
through App Store Connect if you have chosen to share them with developers.</p>

<h2>Contacting us</h2>
<p>If you email support from <b>Settings &rarr; Contact Support</b>, the draft includes the game version, your current page,
your device model and iOS version so we can help. We receive your email address and anything you write only if you send
it, use it only to answer you and delete the thread within 12 months.</p>

<h2>Information we do not collect</h2>
<p>We do not collect your name, email address (unless you write to us), phone number, contacts, photos, precise location,
health data or browsing history, and we do not sell personal information. If you allow tracking, our ad partners may use
your advertising identifier for personalised ads, which some US state laws treat as &ldquo;sharing&rdquo; for cross-context
behavioural advertising; stop this any time by turning tracking off in iOS Settings or usage stats off in the game.</p>

<h2>Children</h2>
<p>{n} is made for a general audience and is not directed at children under 13. We do not knowingly collect personal
information from children. If you believe a child has provided personal information to us, contact us at
<a href="mailto:{EMAIL}">{EMAIL}</a> and we will delete it.</p>

<h2>Your rights</h2>
<p>Depending on where you live (for example under the GDPR, UK GDPR, CCPA/CPRA or India's DPDP Act) you may have the right to
access, correct or delete personal information, to object to or restrict processing, and to withdraw consent. Switch usage
stats off in <b>Settings &rarr; Share usage stats</b>, change ad choices in <b>Settings &rarr; Privacy Choices</b> (EEA, UK,
Switzerland) or tracking in iOS Settings, or delete the game. We don't know who you are: analytics data is tied to a random
app-instance identifier, not to a name or account. To ask Google to delete it, email us the approximate date you played and
your device model and we will request deletion of that app instance. Email <a href="mailto:{EMAIL}">{EMAIL}</a>; we answer
within 30 days. You may also complain to your local data-protection authority.</p>

<h2>Changes</h2>
<p>If a future version changes how information is handled, we will update this page and the date above before that version
is released.</p>

<h2>Contact</h2>
<p>{DEVELOPER} &mdash; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""
    page(f"{g['slug']}/privacy.html", f"{g['name']} Privacy Policy", body, g)


def if_terms(g):
    n = escape(g["name"])
    body = f"""
<h1>{n} &mdash; Terms of Use</h1>
<p class="meta">Last updated: {IF_UPDATED}</p>
<p>These terms apply to the game <b>{n}</b> published by {DEVELOPER}. Apple's
<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License
Agreement</a> (EULA) also applies; if anything here conflicts with it, Apple's agreement wins.</p>
<h2>Licence</h2>
<p>We give you a personal, non-transferable, revocable licence to play the game for non-commercial purposes. Do not copy,
modify, reverse engineer, resell or exploit the game.</p>
<h2>Price, ads and purchases</h2>
<p>The game is free and shows ads. It offers optional in-app purchases (bundles, coin packs, Safety Net, No Ads and the No
Ads Bundle), processed by Apple under the App Store's terms. No Ads removes the full-screen ads and the banner for good;
reward videos stay optional. Coins and tools have no cash value, cannot be sold or exchanged for money and do not expire.
Restore Purchases is in the Shop, in Settings and on the Atlas Club screen.</p>
<h2>Atlas Club subscription</h2>
<ul>
<li><b>What you get:</b> no ads of any kind, a new members' picture page every day, a daily gift (coins, a Lens and a
Pencil) and every video reward without watching a video, for as long as the membership is active.</li>
<li><b>Plans:</b> Atlas Club Monthly (1 month) and Atlas Club Yearly (1 year), at the price shown in the game and on the App
Store for your country. The Yearly plan may include a 7-day free trial for eligible new subscribers.</li>
<li><b>Billing and renewal:</b> payment is charged to your Apple Account when you confirm the purchase, or when a free trial
ends. The subscription renews automatically for the same period and price unless it is cancelled at least 24 hours before
the end of the current period; your account is charged for renewal within the 24 hours before the period ends.</li>
<li><b>Cancelling:</b> manage or cancel any time in your Apple Account settings (Settings &rarr; your name &rarr;
Subscriptions). Cancelling stops the next renewal; the membership stays active until the end of the period you paid for. If
you cancel during a free trial, you are not charged.</li>
<li><b>Refunds</b> are handled by Apple at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</li>
<li>If the benefits ever change, existing members keep at least the benefits above until their current period ends, and
we update this page first.</li>
</ul>
<h2>Availability and changes</h2>
<p>We may update the game or change its content. To the extent the law allows, the game is provided &ldquo;as is&rdquo; and we
are not liable for indirect or consequential losses. Nothing in these terms limits rights you have under consumer-protection
law.</p>
<h2>Credits</h2>
<p>Illustrations were made for the game with AI image tools and edited by us. Fonts: Space Grotesk and DM Sans (SIL Open Font
License).</p>
<h2>Privacy</h2>
<p>See the <a href="/{g['slug']}/privacy.html">{n} Privacy Policy</a>.</p>
<h2>Contact</h2>
<p>{DEVELOPER} &mdash; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""
    page(f"{g['slug']}/terms.html", f"{g['name']} Terms of Use", body, g)


def if_support(g):
    n = escape(g["name"])
    body = f"""
<h1>{n} Support</h1>
<p class="lead">Need help? Email <a href="mailto:{EMAIL}?subject=Inkflight%20support">{EMAIL}</a> or use <b>Settings &rarr;
Contact Support</b> in the game. We usually reply within two working days. Please include your iPhone model and what
happened.</p>
<h2>Frequently asked questions</h2>
<h3>How do I play?</h3>
<p>Tap an arrow and it flies off the page in the direction it points. An arrow can't pass through another one, so free its
way first. Three wrong taps and the page is lost. Clear every arrow to restore the picture underneath.</p>
<h3>What do the tools do?</h3>
<p><b>Pencil</b> shows an arrow that can leave now, <b>Eraser</b> removes one arrow, <b>Lens</b> lights up every free arrow
for a moment and <b>Quill</b> undoes your last move. Arrows with a gold dot are mirrors: tap the dot to turn them around.</p>
<h3>What is the Atlas Club?</h3>
<p>An optional monthly or yearly membership: no ads at all, a new members' page every day, a daily gift and instant video
rewards. The yearly plan may start with a 7-day free trial for new subscribers. Open it from the crown on the home screen,
the Shop or Settings.</p>
<h3>How do I cancel the Atlas Club?</h3>
<p>On your iPhone open <b>Settings &rarr; your name &rarr; Subscriptions &rarr; Inkflight</b>, or tap <b>Manage
subscription</b> on the Atlas Club screen. You keep the membership until the end of the period you paid for.</p>
<h3>I bought something but don't have it.</h3>
<p>Tap <b>Restore Purchases</b> in the Shop or in Settings, signed in with the same Apple Account. If it still doesn't
appear, email us the date of the purchase.</p>
<h3>Are there ads?</h3>
<p>The game is free with ads: optional reward videos, a full-screen ad now and then between pages and a banner on later
pages. <b>No Ads</b> turns off the full-screen ads and the banner for good; Atlas Club members see no ads at all.</p>
<h3>Is my progress saved?</h3>
<p>Yes, automatically, on your device and in your iCloud (Settings &rarr; iCloud save). Reinstall the game or open it on
another iPhone or iPad signed in to the same Apple Account and your pages, stars and coins come back. Purchases come back
with <b>Restore Purchases</b>.</p>
<h3>Are there leaderboards?</h3>
<p>Yes. Sign in to Game Center and tap <b>Settings &rarr; Game Center</b> for the leaderboards and 13 achievements.</p>
<h3>How do I get a refund?</h3>
<p>Request it from Apple at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<h3>Privacy</h3>
<p>See the <a href="/{g['slug']}/privacy.html">Privacy Policy</a>. Switch anonymous usage stats off in <b>Settings &rarr; Share
usage stats</b>.</p>
"""
    page(f"{g['slug']}/support.html", f"{g['name']} Support", body, g)


TUKTUK = dict(
    slug="tuktuk-tangle", name="TukTuk Tangle",
    tagline="Untangle the mela traffic jam: free the rides, fill them with riders, clear the lot.",
    about="""<p>The ride stand at Mela Mile is jammed. Tap a tuk-tuk, van or bus whose way out is clear and it drives to a
pickup bay, where riders in its colour hop aboard; full rides head home. Pick the right order so the bays never fill up.
100 hand-checked levels, from a small station square to giant picture-shaped lots, with friends who ride together, Hints,
Express Bays and route symbols for colour-blind play.</p>
<p><b>Free to play. No account. Plays offline.</b> Optional Mela Club membership: no ads between levels, a daily gift, and
Hints and Express Bays without videos.</p>""",
    kids=False, products=[],
)
TK_UPDATED = "27 November 2026"


def tk_privacy(g):
    n = escape(g["name"])
    body = f"""
<h1>{n} &mdash; Privacy Policy</h1>
<p class="meta">Last updated: {TK_UPDATED}</p>
<p>This policy covers the game <b>{n}</b> (&ldquo;the game&rdquo;), published by {DEVELOPER} (&ldquo;we&rdquo;, &ldquo;us&rdquo;),
on iPhone and iPad.</p>

<div class="card"><b>In short:</b> the game is free. It shows ads (optional reward videos, a full-screen ad now and then
between levels and a small banner on later levels), served through Unity LevelPlay by ironSource Ads and Unity Ads, and
offers optional in-app purchases and an optional <b>Mela Club</b> subscription, all processed by Apple. There are no accounts
and no server of ours: your progress stays on your device. With usage stats on (the default; in the EEA, UK and Switzerland
they stay off) gameplay statistics, not linked to your name or account, go to <b>Google Analytics for Firebase</b>; switch
them off any time in
<b>Settings &rarr; Usage stats</b>. Ads are <b>personalised only</b> if usage stats are on <b>and</b> you allow tracking when
Apple's prompt asks; in the EEA, UK and Switzerland ads are never personalised and the game does not ask.</div>

<h2>Information stored on your device</h2>
<p>Your progress (levels won, coins, Hints, Express Bays, daily gifts and missions), items you bought, your membership status,
when you last saw an ad (so the game can space ads out) and your settings are saved in the game's own storage on your device.
They are not sent to us. Deleting the game deletes them; Remove Ads and an active Mela Club come back with <b>Restore
Purchases</b>.</p>

<h2>Analytics (Google Analytics for Firebase)</h2>
<p>To see how the game is played, improve it and measure our own advertising, the game uses Google Analytics for Firebase,
provided by Google. When usage stats are on it receives:</p>
<ul>
<li>an app-instance identifier created by Firebase and the identifier for vendors (IDFV), not your name, email or Apple ID;</li>
<li>device and app information: device model, iOS version, app version, language, country/region (derived from your IP
address, which Google does not store as such), first-open and session times;</li>
<li>game events, for example: levels started, won and lost, Hints and Express Bays used, the home screen and Shop opened,
daily gifts and missions claimed, purchases and subscriptions (product and price), reward videos watched, ads shown and their
estimated value, and your answer to Apple's tracking prompt.</li>
</ul>
<p>Google processes this under its own policy:
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from apps that use its
services</a>, and keeps detailed event data for 2 months (reports use aggregated counts).</p>
<ul>
<li><b>EEA, UK and Switzerland:</b> nothing is collected unless you agree on Google's consent form; while the game does not
show that form, nothing is collected there at all. The game treats you as there if your device's region is set to one of
these countries.</li>
<li><b>Everywhere:</b> turn it off any time in <b>Settings &rarr; Usage stats</b>. Stats then stop, ads are no longer
personalised and the game does not ask for tracking.</li>
</ul>

<h2>Advertising</h2>
<p>The game shows optional reward videos you choose to watch (an Express Bay, a Hint, double coins after a win, free coins in
the Shop or a bigger daily gift), a full-screen ad now and then after you win a level (never while you are playing a level,
never after a lost level, not in the first ten levels or your first minutes of play, and at most one every 90 seconds), and a
small banner at the bottom of the play screen from level 20. <b>Remove Ads</b> turns the full-screen ads and the banner off for
good; <b>Mela Club</b> members see neither and get video rewards without watching a video. Ad requests are not marked as
directed at children.</p>
<p>Ads are served through <b>Unity LevelPlay</b>, an ad mediation service of Unity Technologies (ironSource), which picks
each ad from <b>ironSource Ads and Unity Ads</b>; LevelPlay includes Unity's Ad Quality component, which checks the ads shown
for quality and safety. To deliver and measure ads and prevent fraud, these ad partners may collect from your device: IP
address (and the approximate location derived from it), device and operating-system information, the identifier for vendors
(IDFV), ad interactions (for example, whether an ad was shown or tapped) and diagnostics. Unity processes this under its own
policy: <a href="https://unity.com/legal/game-player-and-app-user-privacy-policy">Unity Game Player and App User Privacy
Policy</a>. When usage stats are on, the game also sends the estimated value of each ad shown (no personal data) to Google
Analytics for Firebase.</p>
<ul>
<li><b>Tracking.</b> If usage stats are on, after your first few levels the game shows a short note and then Apple's App
Tracking Transparency prompt, once. Only if you choose <b>Allow</b> do the ad partners receive your device's advertising
identifier (IDFA), may ads be personalised to your interests, and may Google Analytics share statistics with Google's
advertising services to measure which of our ads brought you to the game. Either answer leaves the game the same, with the
same number of ads; change it any time in iOS <b>Settings &rarr; Privacy &amp; Security &rarr; Tracking</b>.</li>
<li><b>EEA, UK and Switzerland:</b> only non-personalised ads are requested and the game does not ask for tracking. The game
treats you as there if your device's region is set to one of these countries.</li>
<li><b>US privacy laws:</b> unless you allow tracking, the game tells the ad partners not to sell or share your
information.</li>
</ul>

<h2>Purchases and the Mela Club subscription</h2>
<p>Purchases (the Starter Pack, the Rush Hour Pack, coin packs and Remove Ads) and the <b>Mela Club</b> subscription are
processed by Apple. We never receive your name, Apple ID or payment details. The App Store tells the game which items and
which membership your Apple ID owns, with product and transaction identifiers and dates, so they can be delivered, renewed
and restored; this stays on your device. With usage stats on, a new purchase's product, price and transaction identifier also
go to Google Analytics for Firebase (see above). You manage or cancel the subscription in your Apple Account settings.</p>

<h2>Apple services</h2>
<p>The game may ask Apple to show its standard &ldquo;rate this app&rdquo; prompt after a couple of good wins. That prompt is
run by Apple; we receive no information from it. Apple may give us anonymous, aggregated download, sales and crash statistics
through App Store Connect if you have chosen to share them with developers.</p>

<h2>Contacting us</h2>
<p><b>Settings &rarr; Support</b> in the game opens our support page. If you email us, we receive your email address and
anything you write, use it only to answer you and delete the thread within 12 months.</p>

<h2>Information we do not collect</h2>
<p>We do not collect your name, email address (unless you write to us), phone number, contacts, photos, precise location,
health data or browsing history, and we do not sell personal information. If you allow tracking, our ad partners may use
your advertising identifier for personalised ads, which some US state laws treat as &ldquo;sharing&rdquo; for cross-context
behavioural advertising; stop this any time by turning tracking off in iOS Settings or usage stats off in the game.</p>

<h2>Children</h2>
<p>{n} is made for a general audience and is not directed at children under 13. We do not knowingly collect personal
information from children. If you believe a child has provided personal information to us, contact us at
<a href="mailto:{EMAIL}">{EMAIL}</a> and we will delete it.</p>

<h2>Your rights</h2>
<p>Depending on where you live (for example under the GDPR, UK GDPR, CCPA/CPRA or India's DPDP Act) you may have the right to
access, correct or delete personal information, to object to or restrict processing, and to withdraw consent. Switch usage
stats off in <b>Settings &rarr; Usage stats</b>, turn tracking off or reset your advertising identifier in iOS Settings, or
delete the game. We don't know who you are: the game has no account, and analytics data is tied to a random app-instance
identifier, not to a name or account. To ask Google to delete it, email us the approximate date you played and your device
model and we will request deletion of that app instance. For information the ad partners hold, use the choices in Unity's
policy linked above, or email <a href="mailto:{EMAIL}">{EMAIL}</a> and we will help; we answer within 30 days. You may also
complain to your local data-protection authority.</p>

<h2>Changes</h2>
<p>If a future version changes how information is handled, we will update this page and the date above before that version
is released.</p>

<h2>Contact</h2>
<p>{DEVELOPER} &mdash; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""
    page(f"{g['slug']}/privacy.html", f"{g['name']} Privacy Policy", body, g)


def tk_terms(g):
    n = escape(g["name"])
    body = f"""
<h1>{n} &mdash; Terms of Use</h1>
<p class="meta">Last updated: {TK_UPDATED}</p>
<p>These terms apply to the game <b>{n}</b> published by {DEVELOPER}. Apple's
<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License
Agreement</a> (EULA) also applies; if anything here conflicts with it, Apple's agreement wins.</p>
<h2>Licence</h2>
<p>We give you a personal, non-transferable, revocable licence to play the game for non-commercial purposes. Do not copy,
modify, reverse engineer, resell or exploit the game.</p>
<h2>Price, ads and purchases</h2>
<p>The game is free and shows ads. It offers optional in-app purchases (the Starter Pack, the Rush Hour Pack, coin packs and
Remove Ads), processed by Apple under the App Store's terms. Remove Ads removes the full-screen ads and the banner for good;
reward videos stay optional. Coins, Hints and Express Bays have no cash value, cannot be sold or exchanged for money and do
not expire. Restore Purchases is in the Shop and in Settings.</p>
<h2>Mela Club subscription</h2>
<ul>
<li><b>What you get:</b> no ads between levels and no banner, a daily gift (200 coins, 1 Hint and 1 Express Bay), Hints and
Express Bays without watching a video, and double coins from the daily gift calendar without a video, for as long as the membership is
active.</li>
<li><b>Plans:</b> Mela Club Weekly (1 week), Mela Club Monthly (1 month) and Mela Club Yearly (1 year), at the price shown in
the game and on the App Store for your country.</li>
<li><b>Billing and renewal:</b> payment is charged to your Apple Account when you confirm the purchase. The subscription
renews automatically for the same period and price unless it is cancelled at least 24 hours before the end of the current
period; your account is charged for renewal within the 24 hours before the period ends.</li>
<li><b>Cancelling:</b> manage or cancel any time in your Apple Account settings (Settings &rarr; your name &rarr;
Subscriptions). Cancelling stops the next renewal; the membership stays active until the end of the period you paid
for.</li>
<li><b>Refunds</b> are handled by Apple at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</li>
<li>If the benefits ever change, existing members keep at least the benefits above until their current period ends, and
we update this page first.</li>
</ul>
<h2>Availability and changes</h2>
<p>We may update the game or change its content. To the extent the law allows, the game is provided &ldquo;as is&rdquo; and we
are not liable for indirect or consequential losses. Nothing in these terms limits rights you have under consumer-protection
law.</p>
<h2>Credits</h2>
<p>The 3D models, music and sound effects were made by us for the game. The logo, app icon and interface icons were made with
AI image tools and edited by us. Fonts: Lilita One and Nunito (SIL Open Font License).</p>
<h2>Privacy</h2>
<p>See the <a href="/{g['slug']}/privacy.html">{n} Privacy Policy</a>.</p>
<h2>Contact</h2>
<p>{DEVELOPER} &mdash; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""
    page(f"{g['slug']}/terms.html", f"{g['name']} Terms of Use", body, g)


def tk_support(g):
    n = escape(g["name"])
    body = f"""
<h1>{n} Support</h1>
<p class="lead">Need help? Email <a href="mailto:{EMAIL}?subject=TukTuk%20Tangle%20support">{EMAIL}</a>. We usually reply
within two working days. Please include your iPhone or iPad model, the level number and what happened.</p>
<h2>Frequently asked questions</h2>
<h3>How do I play?</h3>
<p>Tap a ride whose way out is clear: it drives out of the lot to a free pickup bay, and riders in its colour climb aboard in
queue order. A full ride heads home. Friends wearing marigold garlands ride together and need two seats in the same ride. If
every bay is taken and the rider at the front can't board, the level is lost, so plan the order.</p>
<h3>What do Hints and Express Bays do?</h3>
<p>A <b>Hint</b> shows a ride that is safe to tap now. An <b>Express Bay</b> opens an extra pickup bay for the level. You start
with a few and get more from daily gifts and packs; when you run out, spend coins or watch a short video for one.</p>
<h3>I can't tell some colours apart.</h3>
<p>Turn on <b>Settings &rarr; Route symbols</b>: every colour gets its own symbol on the ride's roof and on the riders' caps.</p>
<h3>What is the Mela Club?</h3>
<p>An optional weekly, monthly or yearly membership: no ads between levels and no banner, a daily gift (200 coins, a Hint and an
Express Bay), Hints and Express Bays without videos, and double coins from the daily gift calendar without a video. Open it from the crown on the home
screen or from the Shop.</p>
<h3>How do I cancel the Mela Club?</h3>
<p>On your iPhone open <b>Settings &rarr; your name &rarr; Subscriptions &rarr; {n}</b>. You keep the membership until the end
of the period you paid for.</p>
<h3>I bought something but don't have it.</h3>
<p>Tap <b>Restore Purchases</b> in the Shop or in Settings, signed in with the same Apple Account. If it still doesn't
appear, email us the date of the purchase.</p>
<h3>Are there ads?</h3>
<p>The game is free with ads: optional reward videos, a full-screen ad now and then between levels from level 11 and a banner
from level 20. <b>Remove Ads</b> turns off the full-screen ads and the banner for good; Mela Club members don't see them
either.</p>
<h3>Is my progress saved?</h3>
<p>Yes, automatically, on your device. It is not stored online, so deleting the game deletes your progress. Remove Ads and an
active Mela Club come back with <b>Restore Purchases</b>.</p>
<h3>How do I get a refund?</h3>
<p>Request it from Apple at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<h3>How do I turn usage stats off?</h3>
<p>Open <b>Settings &rarr; Usage stats</b> in the game and switch it off. The game then sends no gameplay statistics to Google
Analytics for Firebase and ads are not personalised. In the EEA, UK and Switzerland usage stats are off already.</p>
<h3>Privacy</h3>
<p>See the <a href="/{g['slug']}/privacy.html">Privacy Policy</a>.</p>
"""
    page(f"{g['slug']}/support.html", f"{g['name']} Support", body, g)



games = [TUMBLEPALS, SPINANDCARVE]
for g in games:
    # Spin & Carve's pages are hand-maintained (privacy: age bands, Firebase, ATT, LevelPlay; terms + support updated
    # 20 Nov 2026 for 1.3.0): edit spinandcarve/*.html. Regenerating them here would roll them back to October's text.
    if g is SPINANDCARVE: continue
    privacy(g); terms(g); support(g); landing(g)
nmt_privacy(NIGHTMARKET); nmt_terms(NIGHTMARKET); nmt_support(NIGHTMARKET); landing(NIGHTMARKET)
fs_privacy(FAIRWAY); fs_terms(FAIRWAY); fs_support(FAIRWAY); landing(FAIRWAY)
if_privacy(INKFLIGHT); if_terms(INKFLIGHT); if_support(INKFLIGHT); landing(INKFLIGHT)
tk_privacy(TUKTUK); tk_terms(TUKTUK); tk_support(TUKTUK); landing(TUKTUK)
# index.html is hand-maintained (it also lists Ember Orchards, Party Royale, StoragePilot and NetScope); home() would drop them.
# home(games + [NIGHTMARKET, FAIRWAY])
# app-ads.txt: our AdMob line + the Unity LevelPlay / Unity Ads sellers (copy the list from Unity dashboard → Monetization → Settings → App-ads.txt)
(ROOT / "app-ads.txt").write_text((ROOT / "tools" / "app-ads.txt").read_text())
(ROOT / ".nojekyll").write_text("")
(ROOT / "404.html").write_text('<!doctype html><meta charset="utf-8"><title>Not found</title><p>Page not found. <a href="/">Home</a></p>\n')
print("built", sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*.html")))
