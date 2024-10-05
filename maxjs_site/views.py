from django.http import HttpResponse
from django.conf import settings

def index(request):
    return HttpResponse("""  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="We create Minecraft addons and skins. Check out our latest collections!">
    <meta name="keywords" content="Minecraft, addons, skins, modding">
    <title>home - mczoo & co | Minecraft Addons & Skins</title>
    <link rel="stylesheet" href="static/main.css">
    <script src="static/script.js"></script>

    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4360870132554397"
     crossorigin="anonymous"></script>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VDP6YV9882"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-VDP6YV9882');
    </script>
</head>
<body>
    <div id="topbar">
        <a href="index.html" class="topbar active">home</a>
        <a href="about" class="topbar">about</a>
        <a href="skins" class="topbar">skins</a>
        <a href="addons" class="topbar">addons</a>
        <a href="legal" class="topbar">legal stuff</a>
    </div>
    <div id="cookie-consent-banner" style="display: none; position: fixed; bottom: 0; width: 100%; background: #333; color: #fff; padding: 10px; text-align: center;">
        <p>This website uses cookies to ensure you get the best experience on our website. <a href="/legal.html" style="color: #f1d600;">click here to view our privacy policy</a>.</p>
        <button id="accept-cookies" style="background: #f1d600; color: #000; border: none; padding: 5px 10px; cursor: pointer;">Got it!</button>
    </div>
    <div class="info">
        <h1>welcome to mczoo & co</h1>
        <h2>We are a minecraft addon and skin creation site.</h2>
        <h2>We want to create minecraft related things for you.</h2>
        <br>
        <h2>Minecraft News</h2>
        <br>
        <h3>microsoft hates modding!</h3>
        <p>minecraft has a file which modloaders edit to mod the game, update 1.21.1.3 made that file completely unpredictable so most developers gave up on trying and just joined the minecraft partner program. They would do this for java edition, but that would give them a terrible reputation. Why not develop your own client? The server APIs are open source.</p>
        <br>
        <h3>microsoft released bedrock protocols</h3>
        <p>mojang released the minecraft bedrock protocol docs, probably to stop retaliation against the removal of modloaders.</p>
    </div>
</body>
</html>
    """
    )
def about(request):
    return HttpResponse("""

""")