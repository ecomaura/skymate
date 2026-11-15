import re
NAV=[('index','Home'),('services','Services'),('about','About'),('contact','Contact')]
def ph(img,size,desc,cls=''):
    return f'<figure class="ph {cls}" data-img="{img}"><span><b>Image: {img}</b>{desc}<br><small>{size}</small></span></figure>'
def page(name,title,desc,body):
    nav=''.join(f'<li><a href="{n}.html"{" class=on aria-current=page" if n==name else ""}>{l}</a></li>' for n,l in NAV)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="icon" href="assets/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="style.css"></head><body>
<header><div class="w nav"><a class="brand" href="index.html"><img src="assets/icon.png" alt="">Sky<b>Mate</b> Digital</a>
<nav aria-label="Main"><button id="mt" aria-label="Menu" aria-expanded="false">☰</button><ul>{nav}<li><a class="btn" href="contact.html">Get a free audit</a></li></ul></nav></div></header>
<main>{body}</main>
<footer><div class="w"><div><img src="assets/logo.png" alt="SkyMate Digital logo"></div>
<div><h3>Explore</h3><a href="index.html">Home</a><a href="services.html">Services</a><a href="about.html">About</a><a href="contact.html">Contact</a></div>
<div><h3>Talk to us</h3><a href="https://wa.me/91XXXXXXXXXX">WhatsApp: +91 XXXXX XXXXX</a><a href="mailto:hello@yourdomain.com">hello@yourdomain.com</a></div></div>
<p class="copy">SkyMate™ Digital. Elevate Brand. Engage Audience. Drive Growth.</p></footer>
<a class="wab" href="https://wa.me/91XXXXXXXXXX?text=Hi%20SkyMate%20Digital" aria-label="Chat on WhatsApp">Chat on WhatsApp</a>
<script src="script.js"></script></body></html>'''
CTA='''<section class="sec"><div class="w"><div class="cband"><h2>Ready to lift off? Start with a free audit.</h2><a class="btn g" href="contact.html">Book my free audit</a></div></div></section>'''
rocket='''<svg class="fly" viewBox="0 0 560 460" aria-hidden="true"><path class="trail" pathLength="1" d="M10 440C120 430 250 330 330 220S470 60 540 20" fill="none" stroke="#F5A01A" stroke-width="7" stroke-linecap="round"/>
<g><animateMotion dur="2.8s" begin="0.4s" fill="freeze" rotate="auto" calcMode="spline" keyTimes="0;1" keySplines=".2 .6 .3 1" path="M10 440C120 430 250 330 330 220S470 60 540 20"/>
<path d="M-8 -9L18 -5L18 5L-8 9Z" fill="#5BA832"/><path d="M14 -13Q50 -10 62 0Q50 10 14 13Z" fill="#0B1B3F"/><circle cx="46" cy="0" r="4" fill="#fff"/><path d="M14 -13L22 -20L26 -12Z M14 13L22 20L26 12Z" fill="#1565D8"/></g></svg>'''
home=f'''<section class="hero"><div class="w"><div><h1>Get found. Get chosen. Get growing.</h1>
<p class="lead">SkyMate Digital sets up and runs the Google, Meta and WhatsApp presence that brings local customers to your door.</p>
<div class="cta"><a class="btn" href="contact.html">Get a free audit</a><a class="btn o" href="services.html">See our services</a></div></div>
<div class="stage">{ph("hero-team.jpg","1200 × 1000 px, landscape","Friendly photo of a small business owner at their shop or office checking Google Maps or social stats on a phone")}{rocket}</div></div></section>
<section class="sec"><div class="w"><h2>Three promises, one team</h2>
<div class="pill"><div class="pc" style="--c:var(--blue)"><h3>Elevate your brand</h3><p>A clear identity, a complete Google Business Profile and a website people trust at first glance.</p><a href="services.html#brand">Branding and design</a></div>
<div class="pc" style="--c:var(--green)"><h3>Engage your audience</h3><p>Instagram, Facebook, YouTube and WhatsApp that keep customers talking to you, not past you.</p><a href="services.html#social">Social and video</a></div>
<div class="pc" style="--c:var(--orange)"><h3>Drive growth</h3><p>Google Ads, Meta Ads and lead generation tracked from the first click to the sale.</p><a href="services.html#leads">Performance marketing</a></div></div></div></section>
<section class="sec alt"><div class="w goal"><div><h2>What do you want more of?</h2><p class="lead">Pick a goal and see where we would start.</p>
<div class="chips" role="group" aria-label="Goals">{''.join(f'<button class="chip" data-g="{k}" aria-pressed="false">{t}</button>' for k,t in [('maps','Get found on Google Maps'),('leads','More leads and enquiries'),('social','Grow on Instagram and Facebook'),('site','A website or brand'),('chat','Chat with customers on WhatsApp'),('trust','Reviews and trust')])}</div></div>
<div id="res" aria-live="polite"><h3>Your starting plan appears here</h3><p class="lead">Choose a goal on the left.</p></div></div></section>
<section class="sec"><div class="w"><h2>Start with the five basics</h2><p class="lead">Every local business needs these set up properly before any ad money is spent.</p>
<div class="setup">
<div class="sc">{ph("setup-gbp.jpg","600 × 600 px, square","Phone showing a Google Business Profile with photos and reviews")}<div><h3>Google Business Profile</h3><p>Verified, complete and ready to rank.</p></div></div>
<div class="sc">{ph("setup-maps.jpg","600 × 600 px, square","Google Maps pin on a street with a shop front")}<div><h3>Google Maps listing</h3><p>Show up when people search nearby.</p></div></div>
<div class="sc">{ph("setup-instagram.jpg","600 × 600 px, square","Instagram profile grid on a phone with branded posts")}<div><h3>Instagram Business Account</h3><p>Profile, highlights and a posting plan.</p></div></div>
<div class="sc">{ph("setup-facebook.jpg","600 × 600 px, square","Facebook business page on a laptop or phone")}<div><h3>Facebook Business Page</h3><p>Set up for reach, messages and ads.</p></div></div>
<div class="sc">{ph("setup-whatsapp.jpg","600 × 600 px, square","WhatsApp Business chat with catalogue and quick replies")}<div><h3>WhatsApp Business set-up</h3><p>Catalogue, greeting and quick replies.</p></div></div></div></div></section>
<section class="sec alt"><div class="w">{ph("band-dashboard.jpg","1600 × 600 px, wide","Wide shot of a growth dashboard or team reviewing campaign results","band")}
<h2 style="margin-top:56px">How we work</h2><div class="steps">
<div class="st"><h3>Audit</h3><p>We check your profiles, listings, site and ads.</p></div><div class="st"><h3>Set up</h3><p>We fix the basics and build what is missing.</p></div>
<div class="st"><h3>Launch</h3><p>Content and campaigns go live with tracking.</p></div><div class="st"><h3>Improve</h3><p>We review results and tune every month.</p></div></div></div></section>{CTA}'''
svc=[('gbp','local','Google Business Profile and Google Maps optimization',['Profile setup, verification and clean-up','Categories, services, photos and posts','Local ranking improvements on Google Maps'],'var(--blue)'),
('seo','search','SEO and Search Engine Marketing (SEM)',['Keyword research and on-page SEO','Local SEO for your service areas','Google Search ad campaigns'],'var(--blue)'),
('social','social','Facebook and Instagram marketing',['Business account and page set-up','Content calendar, posts and reels','Community replies and growth'],'var(--green)'),
('ads','search','Meta Ads and Google Ads',['Campaign structure and audiences','Ad creatives and copy','Budget control and weekly optimization'],'var(--orange)'),
('web','build','Website development',['Mobile-first, fast multi-page sites','Enquiry forms and click-to-call','Built to be found on Google'],'var(--blue)'),
('wa','social','WhatsApp Business marketing',['Business set-up, catalogue and quick replies','Broadcast campaigns','Click-to-WhatsApp ads'],'var(--green)'),
('brand','build','Branding and graphic design',['Logo and brand kit','Social media creatives','Print and promotional designs'],'var(--blue)'),
('leads','search','Lead generation and performance marketing',['Landing pages and lead forms','Conversion and call tracking','Cost-per-lead reporting'],'var(--orange)'),
('video','social','YouTube and video marketing',['Channel set-up and optimization','Short and long video planning','Video ads and thumbnails'],'var(--green)'),
('orm','local','Business listings and online reputation management',['Consistent listings across directories','Review requests and replies','Alerts for new reviews and mentions'],'var(--orange)')]
cards=''.join(f'<details id="{i}" data-c="{c}" style="--c:{col}"><summary>{t}</summary><ul>{"".join(f"<li>{x}</li>" for x in l)}</ul></details>' for i,c,t,l,col in svc)
services=f'''<section class="ph-head"><div class="w two"><div><h1>Everything your business needs online</h1><p class="lead">Ten services, one team. Use the filters to find what fits, then open a card for details.</p></div>
{ph("services-hero.jpg","1200 × 900 px, landscape","Creative team planning campaigns on a whiteboard or screens")}</div></section>
<section class="sec"><div class="w"><div class="fl" role="group" aria-label="Filter services">{''.join(f'<button class="chip" data-f="{k}" aria-pressed="{"true" if k=="all" else "false"}">{t}</button>' for k,t in [('all','All'),('local','Local and Maps'),('search','Search and ads'),('social','Social and chat'),('build','Website and brand')])}</div>
<div class="cards">{cards}</div></div></section>
<section class="sec alt"><div class="w two"><div><h2>Not sure where to start?</h2><p class="lead">We begin with a free audit of your Google profile, social pages and website, then suggest the few things that matter most.</p><p style="margin-top:24px"><a class="btn" href="contact.html">Get a free audit</a></p></div>{ph("services-audit.jpg","1200 × 900 px, landscape","Consultant showing a client a report on a tablet")}</div></section>'''
about=f'''<section class="ph-head"><div class="w two"><div><h1>A digital partner that grows with you</h1><p class="lead">SkyMate Digital helps businesses elevate their brand, engage their audience and drive growth, with simple plans and honest reporting.</p></div>
{ph("about-team.jpg","1200 × 900 px, landscape","Team photo of the SkyMate Digital founders or staff")}</div></section>
<section class="sec"><div class="w"><h2>What we stand for</h2><div class="vals">
<div><h3>Clarity</h3><p>You always know what we are doing, why, and what it costs.</p></div><div><h3>Measurable results</h3><p>Calls, chats and leads are tracked, not guessed.</p></div><div><h3>Long-term thinking</h3><p>We build assets you keep: profiles, content, listings and websites.</p></div></div></div></section>
<section class="sec alt"><div class="w two">{ph("about-office.jpg","1200 × 900 px, landscape","Office or workspace, or the team in a client meeting")}<div><h2>Our story</h2><p class="lead">Add two or three sentences here about who founded SkyMate Digital, why, and the kinds of businesses you serve.</p><p style="margin-top:24px"><a class="btn" href="contact.html">Work with us</a></p></div></div></section>{CTA}'''
contact=f'''<section class="ph-head"><div class="w"><h1>Let’s talk about your growth</h1><p class="lead">Tell us about your business. Your message opens in WhatsApp so you can send it straight to us.</p></div></section>
<section class="sec"><div class="w two" style="align-items:start"><form id="cf"><label>Your name<input name="nm" required></label><label>Phone<input name="ph" type="tel" required></label><label>Business name<input name="biz"></label>
<label>What do you need?<select name="svc">{''.join(f"<option>{x[2].split(' (')[0]}</option>" for x in svc)}</select></label><label>Message<textarea name="msg" rows="4"></textarea></label>
<button class="btn g" type="submit">Send on WhatsApp</button><p id="ok" aria-live="polite"></p></form>
<div><ul class="ci"><li><b>WhatsApp</b>+91 XXXXX XXXXX</li><li><b>Email</b>hello@yourdomain.com</li><li><b>Hours</b>Mon to Sat, 10am to 7pm</li></ul>{ph("contact-map.jpg","1000 × 700 px, landscape","Map or photo of your office location")}</div></div></section>'''
P={'index':('SkyMate Digital | Google, Meta and WhatsApp marketing','Elevate brand. Engage audience. Drive growth. Google Business Profile, SEO, Meta Ads, websites and more.',home),
'services':('Services | SkyMate Digital','Google Business Profile, SEO, Meta and Google Ads, websites, WhatsApp, branding, video and reputation management.',services),
'about':('About | SkyMate Digital','Meet SkyMate Digital, a digital marketing partner for growing businesses.',about),
'contact':('Contact | SkyMate Digital','Get a free audit of your Google profile, social pages and website.',contact)}
for n,(t,d,b) in P.items(): open(n+'.html','w').write(page(n,t,d,b))
imgs=re.findall(r'<b>Image: (.*?)</b>(.*?)<br><small>(.*?)</small>',''.join(open(n+'.html').read() for n in P))
seen=set();out='# Images needed\n\nDrop files into `assets/images/` using these exact names. They replace the placeholders automatically.\n\n| File | Size | What to show |\n|---|---|---|\n'
for f,d,s in imgs:
    if f not in seen: seen.add(f);out+=f'| {f} | {s} | {d} |\n'
open('IMAGES.md','w').write(out);print(out)
