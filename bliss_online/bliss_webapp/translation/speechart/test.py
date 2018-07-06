"""
TEST:

    Testing suite for WiktionaryParser and derived classes.
"""
'''
from speechart.blissweb import BlissWeb
from speechart.neural_net.neural_images import NeuralNodeImage, NeuralNetImage
from speechart.speecharts import SentenceChart
from speechart.morpheme_parser import *
'''
from speechart.wiktionary_parser import WiktionaryParser
import unittest
import excerpts

HTML = """<!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<meta charset="utf-8"/>
<title>rozdział - Wiktionary</title>
<script>document.documentElement.className = document.documentElement.className.replace( /(^|\s)client-nojs(\s|$)/, "$1client-js$2" );</script>
<script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"rozdział","wgTitle":"rozdział","wgCurRevisionId":45214878,"wgRevisionId":45214878,"wgArticleId":1774509,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Polish terms inherited from Proto-Slavic","Polish terms derived from Proto-Slavic","Polish terms with IPA pronunciation","Polish terms with audio links","Polish lemmas","Polish nouns","Polish masculine nouns"],"wgBreakFrames":false,"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgRelevantPageName":"rozdział","wgRelevantArticleId":1774509,"wgRequestId":"WzRhHwpAIC8AADk0W8sAAABU","wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgCategoryTreePageCategoryOptions":"{\"mode\":0,\"hideprefix\":20,\"showcount\":true,\"namespaces\":false}","wgWikiEditorEnabledModules":[],"wgBetaFeaturesFeatures":[],"wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en","usePageImages":true,"usePageDescriptions":true},"wgPreferredVariant":"en","wgMFExpandAllSectionsUserOption":true,"wgMFEnableFontChanger":true,"wgMFDisplayWikibaseDescriptions":{"search":true,"nearby":true,"watchlist":true,"tagline":false},"wgULSCurrentAutonym":"English","wgNoticeProject":"wiktionary","wgCentralNoticeCookiesToDelete":[],"wgCentralNoticeCategoriesUsingLegacy":["Fundraising","fundraising"],"wgScoreNoteLanguages":{"arabic":"العربية","catalan":"català","deutsch":"Deutsch","english":"English","espanol":"español","italiano":"italiano","nederlands":"Nederlands","norsk":"norsk","portugues":"português","suomi":"suomi","svenska":"svenska","vlaams":"West-Vlams"},"wgScoreDefaultNoteLanguage":"nederlands","wgCentralAuthMobileDomain":false,"wgCodeMirrorEnabled":true,"wgVisualEditorToolbarScrollOffset":0,"wgVisualEditorUnsupportedEditParams":["undo","undoafter","veswitched"],"wgEditSubmitButtonLabelPublish":true});mw.loader.state({"ext.globalCssJs.user.styles":"ready","ext.globalCssJs.site.styles":"ready","site.styles":"ready","noscript":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","ext.globalCssJs.site":"ready","user":"ready","user.options":"ready","user.tokens":"loading","ext.tmh.thumbnail.styles":"ready","mediawiki.legacy.shared":"ready","mediawiki.legacy.commonPrint":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","ext.wikimediaBadges":"ready","mediawiki.skinning.interface":"ready","skins.vector.styles":"ready"});mw.loader.implement("user.tokens@1dqfd7l",function($,jQuery,require,module){/*@nomin*/mw.user.tokens.set({"editToken":"+\\","patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
});mw.loader.load(["mw.MediaWikiPlayer.loader","mw.PopUpMediaTransform","mw.TMHGalleryHook.js","site","mediawiki.page.startup","mediawiki.user","mediawiki.hidpi","mediawiki.page.ready","mediawiki.toc","mediawiki.searchSuggest","ext.gadget.LegacyScripts","ext.gadget.JavascriptHeadings","ext.gadget.TargetedTranslations","ext.gadget.DocTabs","ext.gadget.BlockInfo","ext.gadget.RevdelInfo","ext.gadget.CodeLinks","ext.gadget.TranslationAdder","ext.gadget.RhymesAdder","ext.gadget.SpecialSearch","ext.gadget.zhDialMap","ext.centralauth.centralautologin","mmv.head","mmv.bootstrap.autostart","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.eventLogging.subscriber","ext.wikimediaEvents","ext.navigationTiming","ext.uls.eventlogger","ext.uls.init","ext.uls.compactlinks","ext.uls.interface","ext.3d","ext.centralNotice.geoIP","ext.centralNotice.startUp","skins.vector.js"]);});</script>
<link href="/w/load.php?debug=false&amp;lang=en&amp;modules=ext.tmh.thumbnail.styles%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cmediawiki.legacy.commonPrint%2Cshared%7Cmediawiki.skinning.interface%7Cskins.vector.styles&amp;only=styles&amp;skin=vector" rel="stylesheet"/>
<script async="" src="/w/load.php?debug=false&amp;lang=en&amp;modules=startup&amp;only=scripts&amp;skin=vector"></script>
<meta content="" name="ResourceLoaderDynamicStyles"/>
<link href="/w/load.php?debug=false&amp;lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=vector" rel="stylesheet"/>
<meta content="MediaWiki 1.32.0-wmf.8" name="generator"/>
<meta content="origin" name="referrer"/>
<meta content="origin-when-crossorigin" name="referrer"/>
<meta content="origin-when-cross-origin" name="referrer"/>
<link href="/w/index.php?title=rozdzia%C5%82&amp;action=edit" rel="alternate" title="Edit" type="application/x-wiki"/>
<link href="/w/index.php?title=rozdzia%C5%82&amp;action=edit" rel="edit" title="Edit"/>
<link href="/static/apple-touch/wiktionary/en.png" rel="apple-touch-icon"/>
<link href="/static/favicon/wiktionary/en.ico" rel="shortcut icon"/>
<link href="/w/opensearch_desc.php" rel="search" title="Wiktionary (en)" type="application/opensearchdescription+xml"/>
<link href="//en.wiktionary.org/w/api.php?action=rsd" rel="EditURI" type="application/rsd+xml"/>
<link href="//creativecommons.org/licenses/by-sa/3.0/" rel="license"/>
<link href="/w/index.php?title=Special:RecentChanges&amp;feed=atom" rel="alternate" title="Wiktionary Atom feed" type="application/atom+xml"/>
<link href="https://en.wiktionary.org/wiki/rozdzia%C5%82" rel="canonical"/>
<link href="//login.wikimedia.org" rel="dns-prefetch"/>
<link href="//meta.wikimedia.org" rel="dns-prefetch"/>
<!--[if lt IE 9]><script src="/w/load.php?debug=false&amp;lang=en&amp;modules=html5shiv&amp;only=scripts&amp;skin=vector&amp;sync=1"></script><![endif]-->
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-rozdział rootpage-rozdział skin-vector action-view"> <div class="noprint" id="mw-page-base"></div>
<div class="noprint" id="mw-head-base"></div>
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<div class="mw-body-content" id="siteNotice"><!-- CentralNotice --></div><div class="mw-indicators mw-body-content">
</div>
<h1 class="firstHeading" id="firstHeading" lang="en">rozdział</h1> <div class="mw-body-content" id="bodyContent">
<div class="noprint" id="siteSub">Definition from Wiktionary, the free dictionary</div> <div id="contentSub"></div>
<div id="jump-to-nav"></div> <a class="mw-jump-link" href="#mw-head">Jump to navigation</a>
<a class="mw-jump-link" href="#p-search">Jump to search</a>
<div class="mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><div class="toc" id="toc"><div class="toctitle" dir="ltr" lang="en"><h2>Contents</h2></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#Polish"><span class="tocnumber">1</span> <span class="toctext">Polish</span></a>
<ul>
<li class="toclevel-2 tocsection-2"><a href="#Etymology"><span class="tocnumber">1.1</span> <span class="toctext">Etymology</span></a></li>
<li class="toclevel-2 tocsection-3"><a href="#Pronunciation"><span class="tocnumber">1.2</span> <span class="toctext">Pronunciation</span></a></li>
<li class="toclevel-2 tocsection-4"><a href="#Noun"><span class="tocnumber">1.3</span> <span class="toctext">Noun</span></a>
<ul>
<li class="toclevel-3 tocsection-5"><a href="#Declension"><span class="tocnumber">1.3.1</span> <span class="toctext">Declension</span></a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
<h2><span class="mw-headline" id="Polish">Polish</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=rozdzia%C5%82&amp;action=edit&amp;section=1" title="Edit section: Polish">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<h3><span class="mw-headline" id="Etymology">Etymology</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=rozdzia%C5%82&amp;action=edit&amp;section=2" title="Edit section: Etymology">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<p>From <span class="etyl"><a class="extiw" href="https://en.wikipedia.org/wiki/Proto-Slavic" title="w:Proto-Slavic">Proto-Slavic</a></span> <i class="Latinx mention" lang="sla-pro"><a href="/wiki/Reconstruction:Proto-Slavic/d%C4%9Bliti" title="Reconstruction:Proto-Slavic/děliti">*děliti</a></i>.
</p>
<h3><span class="mw-headline" id="Pronunciation">Pronunciation</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=rozdzia%C5%82&amp;action=edit&amp;section=3" title="Edit section: Pronunciation">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<ul><li><a href="/wiki/Wiktionary:International_Phonetic_Alphabet" title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(<a href="/wiki/Appendix:Polish_pronunciation" title="Appendix:Polish pronunciation">key</a>)</sup>: <span class="IPA">/ˈrɔz̪d͡ʑaw/</span> or <span class="IPA">/ˈrɔʑd͡ʑaw/</span></li>
<li><table class="audiotable" style="vertical-align: bottom; display:inline-block; list-style:none;line-height: 1em; border-collapse:collapse;"><tbody><tr><td class="unicode audiolink" style="padding-right:5px; padding-left: 0;">Audio</td><td class="audiofile"><div class="mediaContainer" style="width:175px"><audio class="kskin" controls="" data-durationhint="1.2" data-mwprovider="wikimediacommons" data-mwtitle="Pl-rozdział.ogg" data-startoffset="0" id="mwe_player_0" preload="none" style="width:175px"><source data-bandwidth="99080" data-height="0" data-shorttitle="Ogg source" data-title="Original Ogg file (99 kbps)" data-width="0" src="//upload.wikimedia.org/wikipedia/commons/3/32/Pl-rozdzia%C5%82.ogg" type='audio/ogg; codecs="vorbis"'/><source data-bandwidth="139176" data-height="0" data-shorttitle="MP3" data-title="MP3" data-transcodekey="mp3" data-width="0" src="//upload.wikimedia.org/wikipedia/commons/transcoded/3/32/Pl-rozdzia%C5%82.ogg/Pl-rozdzia%C5%82.ogg.mp3" type="audio/mpeg"/></audio></div></td><td class="audiometa" style="font-size: 80%;">(<a href="/wiki/File:Pl-rozdzia%C5%82.ogg" title="File:Pl-rozdział.ogg">file</a>)</td></tr></tbody></table></li></ul>
<h3><span class="mw-headline" id="Noun">Noun</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=rozdzia%C5%82&amp;action=edit&amp;section=4" title="Edit section: Noun">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<p><strong class="Latn headword" lang="pl">rozdział</strong> <span class="gender"><abbr title="masculine gender">m</abbr> <abbr title="inanimate">inan</abbr></span>
</p>
<ol><li><a href="/wiki/chapter" title="chapter">chapter</a></li></ol>
<h4><span class="mw-headline" id="Declension">Declension</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=rozdzia%C5%82&amp;action=edit&amp;section=5" title="Edit section: Declension">edit</a><span class="mw-editsection-bracket">]</span></span></h4>
<div class="NavFrame inflection-table-noun" style="width: 29em">
<div class="NavHead">declension of <span class="Latn mention" lang="pl">rozdział</span></div>
<div class="NavContent">
<table class="wikitable inflection-table" style="width: 29em; margin: 0;">
<tbody><tr>
<th style="width: 8em;">
</th>
<th scope="col">singular
</th>
<th scope="col">plural
</th></tr>
<tr>
<th scope="row" title="mianownik (kto? co?)">nominative
</th>
<td><span class="Latn" lang="pl"><a class="mw-selflink selflink">rozdział</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82y&amp;action=edit&amp;redlink=1" title="rozdziały (page does not exist)">rozdziały</a></span>
</td></tr>
<tr>
<th scope="row" title="dopełniacz (kogo? czego?)">genitive
</th>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82u&amp;action=edit&amp;redlink=1" title="rozdziału (page does not exist)">rozdziału</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82%C3%B3w&amp;action=edit&amp;redlink=1" title="rozdziałów (page does not exist)">rozdziałów</a></span>
</td></tr>
<tr>
<th scope="row" title="celownik (komu? czemu?)">dative
</th>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82owi&amp;action=edit&amp;redlink=1" title="rozdziałowi (page does not exist)">rozdziałowi</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82om&amp;action=edit&amp;redlink=1" title="rozdziałom (page does not exist)">rozdziałom</a></span>
</td></tr>
<tr>
<th scope="row" title="biernik (kogo? co?)">accusative
</th>
<td><span class="Latn" lang="pl"><a class="mw-selflink selflink">rozdział</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82y&amp;action=edit&amp;redlink=1" title="rozdziały (page does not exist)">rozdziały</a></span>
</td></tr>
<tr>
<th scope="row" title="narzędnik (kim? czym?)">instrumental
</th>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82em&amp;action=edit&amp;redlink=1" title="rozdziałem (page does not exist)">rozdziałem</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82ami&amp;action=edit&amp;redlink=1" title="rozdziałami (page does not exist)">rozdziałami</a></span>
</td></tr>
<tr>
<th scope="row" title="miejscownik (o kim? o czym?)">locative
</th>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdziale&amp;action=edit&amp;redlink=1" title="rozdziale (page does not exist)">rozdziale</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82ach&amp;action=edit&amp;redlink=1" title="rozdziałach (page does not exist)">rozdziałach</a></span>
</td></tr>
<tr>
<th scope="row" title="wołacz (o!)">vocative
</th>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdziale&amp;action=edit&amp;redlink=1" title="rozdziale (page does not exist)">rozdziale</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82y&amp;action=edit&amp;redlink=1" title="rozdziały (page does not exist)">rozdziały</a></span>
</td></tr></tbody></table></div></div>
<!-- 
NewPP limit report
Parsed by mw1309
Cached time: 20180626091154
Cache expiry: 1900800
Dynamic content: false
CPU time usage: 0.144 seconds
Real time usage: 0.204 seconds
Preprocessor visited node count: 130/1000000
Preprocessor generated node count: 0/1500000
Post‐expand include size: 6438/2097152 bytes
Template argument size: 48/2097152 bytes
Highest expansion depth: 7/40
Expensive parser function count: 0/500
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
Number of Wikibase entities loaded: 0/400
Lua time usage: 0.091/10.000 seconds
Lua memory usage: 3.65 MB/50 MB
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  169.416      1 -total
 52.39%   88.752      1 Template:inh
 18.84%   31.918      1 Template:pl-noun
 12.80%   21.680      1 Template:IPA
 10.35%   17.539      1 Template:pl-decl-noun-masc-inani
  3.53%    5.984      1 Template:audio
  2.07%    3.505      1 Template:catlangname
  1.78%    3.018      1 Template:IPAchar
-->
</div>
<!-- Saved in parser cache with key enwiktionary:pcache:idhash:1774509-0!canonical and timestamp 20180626091154 and revision id 45214878
 -->
<noscript><img alt="" height="1" src="//en.wiktionary.org/wiki/Special:CentralAutoLogin/start?type=1x1" style="border: none; position: absolute;" title="" width="1"/></noscript></div> <div class="printfooter">
						Retrieved from "<a dir="ltr" href="https://en.wiktionary.org/w/index.php?title=rozdział&amp;oldid=45214878">https://en.wiktionary.org/w/index.php?title=rozdział&amp;oldid=45214878</a>"					</div>
<div class="catlinks" data-mw="interface" id="catlinks"><div class="mw-normal-catlinks" id="mw-normal-catlinks"><a href="/wiki/Special:Categories" title="Special:Categories">Categories</a>: <ul><li><a href="/wiki/Category:Polish_terms_inherited_from_Proto-Slavic" title="Category:Polish terms inherited from Proto-Slavic">Polish terms inherited from Proto-Slavic</a></li><li><a href="/wiki/Category:Polish_terms_derived_from_Proto-Slavic" title="Category:Polish terms derived from Proto-Slavic">Polish terms derived from Proto-Slavic</a></li><li><a href="/wiki/Category:Polish_terms_with_IPA_pronunciation" title="Category:Polish terms with IPA pronunciation">Polish terms with IPA pronunciation</a></li><li><a href="/wiki/Category:Polish_terms_with_audio_links" title="Category:Polish terms with audio links">Polish terms with audio links</a></li><li><a href="/wiki/Category:Polish_lemmas" title="Category:Polish lemmas">Polish lemmas</a></li><li><a href="/wiki/Category:Polish_nouns" title="Category:Polish nouns">Polish nouns</a></li><li><a href="/wiki/Category:Polish_masculine_nouns" title="Category:Polish masculine nouns">Polish masculine nouns</a></li></ul></div></div> <div class="visualClear"></div>
</div>
</div>
<div id="mw-navigation">
<h2>Navigation menu</h2>
<div id="mw-head">
<div aria-labelledby="p-personal-label" class="" id="p-personal" role="navigation">
<h3 id="p-personal-label">Personal tools</h3>
<ul>
<li id="pt-anonuserpage">Not logged in</li><li id="pt-anontalk"><a accesskey="n" href="/wiki/Special:MyTalk" title="Discussion about edits from this IP address [n]">Talk</a></li><li id="pt-anoncontribs"><a accesskey="y" href="/wiki/Special:MyContributions" title="A list of edits made from this IP address [y]">Contributions</a></li><li id="pt-createaccount"><a href="/w/index.php?title=Special:CreateAccount&amp;returnto=rozdzia%C5%82" title="You are encouraged to create an account and log in; however, it is not mandatory">Create account</a></li><li id="pt-login"><a accesskey="o" href="/w/index.php?title=Special:UserLogin&amp;returnto=rozdzia%C5%82" title="You are encouraged to log in; however, it is not mandatory [o]">Log in</a></li> </ul>
</div>
<div id="left-navigation">
<div aria-labelledby="p-namespaces-label" class="vectorTabs" id="p-namespaces" role="navigation">
<h3 id="p-namespaces-label">Namespaces</h3>
<ul>
<li class="selected" id="ca-nstab-main"><span><a accesskey="c" href="/wiki/rozdzia%C5%82" title="View the content page [c]">Entry</a></span></li><li class="new" id="ca-talk"><span><a accesskey="t" href="/w/index.php?title=Talk:rozdzia%C5%82&amp;action=edit&amp;redlink=1" rel="discussion" title="Discussion about the content page (page does not exist) [t]">Discussion</a></span></li> </ul>
</div>
<div aria-labelledby="p-variants-label" class="vectorMenu emptyPortlet" id="p-variants" role="navigation">
<input aria-labelledby="p-variants-label" class="vectorMenuCheckbox" type="checkbox"/>
<h3 id="p-variants-label">
<span>Variants</span>
</h3>
<div class="menu">
<ul>
</ul>
</div>
</div>
</div>
<div id="right-navigation">
<div aria-labelledby="p-views-label" class="vectorTabs" id="p-views" role="navigation">
<h3 id="p-views-label">Views</h3>
<ul>
<li class="collapsible selected" id="ca-view"><span><a href="/wiki/rozdzia%C5%82">Read</a></span></li><li class="collapsible" id="ca-edit"><span><a accesskey="e" href="/w/index.php?title=rozdzia%C5%82&amp;action=edit" title="Edit this page [e]">Edit</a></span></li><li class="collapsible" id="ca-history"><span><a accesskey="h" href="/w/index.php?title=rozdzia%C5%82&amp;action=history" title="Past revisions of this page [h]">History</a></span></li> </ul>
</div>
<div aria-labelledby="p-cactions-label" class="vectorMenu emptyPortlet" id="p-cactions" role="navigation">
<input aria-labelledby="p-cactions-label" class="vectorMenuCheckbox" type="checkbox"/>
<h3 id="p-cactions-label"><span>More</span></h3>
<div class="menu">
<ul>
</ul>
</div>
</div>
<div id="p-search" role="search">
<h3>
<label for="searchInput">Search</label>
</h3>
<form action="/w/index.php" id="searchform">
<div id="simpleSearch">
<input accesskey="f" id="searchInput" name="search" placeholder="Search Wiktionary" title="Search Wiktionary [f]" type="search"/><input name="title" type="hidden" value="Special:Search"/><input class="searchButton mw-fallbackSearchButton" id="mw-searchButton" name="fulltext" title="Search the pages for this text" type="submit" value="Search"/><input class="searchButton" id="searchButton" name="go" title="Go to a page with this exact name if it exists" type="submit" value="Go"/> </div>
</form>
</div>
</div>
</div>
<div id="mw-panel">
<div id="p-logo" role="banner"><a class="mw-wiki-logo" href="/wiki/Wiktionary:Main_Page" title="Visit the main page"></a></div>
<div aria-labelledby="p-navigation-label" class="portal" id="p-navigation" role="navigation">
<h3 id="p-navigation-label">Navigation</h3>
<div class="body">
<ul>
<li id="n-mainpage-text"><a href="/wiki/Wiktionary:Main_Page">Main Page</a></li><li id="n-portal"><a href="/wiki/Wiktionary:Community_portal" title="About the project, what you can do, where to find things">Community portal</a></li><li id="n-wiktprefs"><a href="/wiki/Wiktionary:Per-browser_preferences">Preferences</a></li><li id="n-requestedarticles"><a href="/wiki/Wiktionary:Requested_entries">Requested entries</a></li><li id="n-recentchanges"><a accesskey="r" href="/wiki/Special:RecentChanges" title="A list of recent changes in the wiki [r]">Recent changes</a></li><li id="n-randompage"><a accesskey="x" href="/wiki/Special:Random" title="Load a random page [x]">Random entry</a></li><li id="n-help"><a href="https://en.wiktionary.org/wiki/Help:Contents" title="The place to find out">Help</a></li><li id="n-Glossary"><a href="/wiki/Appendix:Glossary">Glossary</a></li><li id="n-sitesupport"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_en.wiktionary.org&amp;uselang=en" title="Support us">Donations</a></li><li id="n-contact"><a href="/wiki/Wiktionary:Contact_us">Contact us</a></li> </ul>
</div>
</div>
<div aria-labelledby="p-tb-label" class="portal" id="p-tb" role="navigation">
<h3 id="p-tb-label">Tools</h3>
<div class="body">
<ul>
<li id="t-whatlinkshere"><a accesskey="j" href="/wiki/Special:WhatLinksHere/rozdzia%C5%82" title="A list of all wiki pages that link here [j]">What links here</a></li><li id="t-recentchangeslinked"><a accesskey="k" href="/wiki/Special:RecentChangesLinked/rozdzia%C5%82" rel="nofollow" title="Recent changes in pages linked from this page [k]">Related changes</a></li><li id="t-upload"><a accesskey="u" href="//commons.wikimedia.org/wiki/Special:UploadWizard?uselang=en" title="Upload files [u]">Upload file</a></li><li id="t-specialpages"><a accesskey="q" href="/wiki/Special:SpecialPages" title="A list of all special pages [q]">Special pages</a></li><li id="t-permalink"><a href="/w/index.php?title=rozdzia%C5%82&amp;oldid=45214878" title="Permanent link to this revision of the page">Permanent link</a></li><li id="t-info"><a href="/w/index.php?title=rozdzia%C5%82&amp;action=info" title="More information about this page">Page information</a></li><li id="t-cite"><a href="/w/index.php?title=Special:CiteThisPage&amp;page=rozdzia%C5%82&amp;id=45214878" title="Information on how to cite this page">Cite this page</a></li> </ul>
</div>
</div>
<div aria-labelledby="p-lang-label" class="portal" id="p-lang" role="navigation">
<h3 id="p-lang-label">In other languages</h3>
<div class="body">
<ul>
<li class="interlanguage-link interwiki-cs"><a class="interlanguage-link-target" href="https://cs.wiktionary.org/wiki/rozdzia%C5%82" hreflang="cs" lang="cs" title="rozdział – Czech">Čeština</a></li><li class="interlanguage-link interwiki-el"><a class="interlanguage-link-target" href="https://el.wiktionary.org/wiki/rozdzia%C5%82" hreflang="el" lang="el" title="rozdział – Greek">Ελληνικά</a></li><li class="interlanguage-link interwiki-eo"><a class="interlanguage-link-target" href="https://eo.wiktionary.org/wiki/rozdzia%C5%82" hreflang="eo" lang="eo" title="rozdział – Esperanto">Esperanto</a></li><li class="interlanguage-link interwiki-io"><a class="interlanguage-link-target" href="https://io.wiktionary.org/wiki/rozdzia%C5%82" hreflang="io" lang="io" title="rozdział – Ido">Ido</a></li><li class="interlanguage-link interwiki-hu"><a class="interlanguage-link-target" href="https://hu.wiktionary.org/wiki/rozdzia%C5%82" hreflang="hu" lang="hu" title="rozdział – Hungarian">Magyar</a></li><li class="interlanguage-link interwiki-mg"><a class="interlanguage-link-target" href="https://mg.wiktionary.org/wiki/rozdzia%C5%82" hreflang="mg" lang="mg" title="rozdział – Malagasy">Malagasy</a></li><li class="interlanguage-link interwiki-nl"><a class="interlanguage-link-target" href="https://nl.wiktionary.org/wiki/rozdzia%C5%82" hreflang="nl" lang="nl" title="rozdział – Dutch">Nederlands</a></li><li class="interlanguage-link interwiki-pl"><a class="interlanguage-link-target" href="https://pl.wiktionary.org/wiki/rozdzia%C5%82" hreflang="pl" lang="pl" title="rozdział – Polish">Polski</a></li><li class="interlanguage-link interwiki-ru"><a class="interlanguage-link-target" href="https://ru.wiktionary.org/wiki/rozdzia%C5%82" hreflang="ru" lang="ru" title="rozdział – Russian">Русский</a></li><li class="interlanguage-link interwiki-sv"><a class="interlanguage-link-target" href="https://sv.wiktionary.org/wiki/rozdzia%C5%82" hreflang="sv" lang="sv" title="rozdział – Swedish">Svenska</a></li><li class="interlanguage-link interwiki-chr"><a class="interlanguage-link-target" href="https://chr.wiktionary.org/wiki/rozdzia%C5%82" hreflang="chr" lang="chr" title="rozdział – Cherokee">ᏣᎳᎩ</a></li> </ul>
</div>
</div>
<div aria-labelledby="p-coll-print_export-label" class="portal" id="p-coll-print_export" role="navigation">
<h3 id="p-coll-print_export-label">Print/export</h3>
<div class="body">
<ul>
<li id="coll-create_a_book"><a href="/w/index.php?title=Special:Book&amp;bookcmd=book_creator&amp;referer=rozdzia%C5%82">Create a book</a></li><li id="coll-download-as-rdf2latex"><a href="/w/index.php?title=Special:ElectronPdf&amp;page=rozdzia%C5%82&amp;action=show-download-screen">Download as PDF</a></li><li id="t-print"><a accesskey="p" href="/w/index.php?title=rozdzia%C5%82&amp;printable=yes" title="Printable version of this page [p]">Printable version</a></li> </ul>
</div>
</div>
</div>
</div>
<div id="footer" role="contentinfo">
<ul id="footer-info">
<li id="footer-info-lastmod"> This page was last edited on 25 May 2017, at 21:46.</li>
<li id="footer-info-copyright">Text is available under the <a href="//creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike License</a>; additional terms may apply.  By using this site, you agree to the <a href="//wikimediafoundation.org/wiki/Terms_of_Use">Terms of Use</a> and <a href="//wikimediafoundation.org/wiki/Privacy_policy">Privacy Policy.</a></li>
</ul>
<ul id="footer-places">
<li id="footer-places-privacy"><a class="extiw" href="https://wikimediafoundation.org/wiki/Privacy_policy" title="wmf:Privacy policy">Privacy policy</a></li>
<li id="footer-places-about"><a class="mw-redirect" href="/wiki/Wiktionary:About" title="Wiktionary:About">About Wiktionary</a></li>
<li id="footer-places-disclaimer"><a href="/wiki/Wiktionary:General_disclaimer" title="Wiktionary:General disclaimer">Disclaimers</a></li>
<li id="footer-places-developers"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute">Developers</a></li>
<li id="footer-places-cookiestatement"><a href="https://wikimediafoundation.org/wiki/Cookie_statement">Cookie statement</a></li>
<li id="footer-places-mobileview"><a class="noprint stopMobileRedirectToggle" href="//en.m.wiktionary.org/w/index.php?title=rozdzia%C5%82&amp;mobileaction=toggle_view_mobile">Mobile view</a></li>
</ul>
<ul class="noprint" id="footer-icons">
<li id="footer-copyrightico">
<a href="https://wikimediafoundation.org/"><img alt="Wikimedia Foundation" height="31" src="/static/images/wikimedia-button.png" srcset="/static/images/wikimedia-button-1.5x.png 1.5x, /static/images/wikimedia-button-2x.png 2x" width="88"/></a> </li>
<li id="footer-poweredbyico">
<a href="//www.mediawiki.org/"><img alt="Powered by MediaWiki" height="31" src="/static/images/poweredby_mediawiki_88x31.png" srcset="/static/images/poweredby_mediawiki_132x47.png 1.5x, /static/images/poweredby_mediawiki_176x62.png 2x" width="88"/></a> </li>
</ul>
<div style="clear: both;"></div>
</div>
<script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"limitreport":{"cputime":"0.144","walltime":"0.204","ppvisitednodes":{"value":130,"limit":1000000},"ppgeneratednodes":{"value":0,"limit":1500000},"postexpandincludesize":{"value":6438,"limit":2097152},"templateargumentsize":{"value":48,"limit":2097152},"expansiondepth":{"value":7,"limit":40},"expensivefunctioncount":{"value":0,"limit":500},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":0,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  169.416      1 -total"," 52.39%   88.752      1 Template:inh"," 18.84%   31.918      1 Template:pl-noun"," 12.80%   21.680      1 Template:IPA"," 10.35%   17.539      1 Template:pl-decl-noun-masc-inani","  3.53%    5.984      1 Template:audio","  2.07%    3.505      1 Template:catlangname","  1.78%    3.018      1 Template:IPAchar"]},"scribunto":{"limitreport-timeusage":{"value":"0.091","limit":"10.000"},"limitreport-memusage":{"value":3827826,"limit":52428800}},"cachereport":{"origin":"mw1309","timestamp":"20180626091154","ttl":1900800,"transientcontent":false}}});mw.config.set({"wgBackendResponseTime":84,"wgHostname":"mw1326"});});</script>
</body>
</html>
"""

HTML_CLEAN = """<h2><span class="mw-headline" id="Polish">Polish</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=rozdzia%C5%82&amp;action=edit&amp;section=1" title="Edit section: Polish">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<h3><span class="mw-headline" id="Etymology">Etymology</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=rozdzia%C5%82&amp;action=edit&amp;section=2" title="Edit section: Etymology">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<p>From <span class="etyl"><a class="extiw" href="https://en.wikipedia.org/wiki/Proto-Slavic" title="w:Proto-Slavic">Proto-Slavic</a></span> <i class="Latinx mention" lang="sla-pro"><a href="/wiki/Reconstruction:Proto-Slavic/d%C4%9Bliti" title="Reconstruction:Proto-Slavic/děliti">*děliti</a></i>.
</p>
<h3><span class="mw-headline" id="Pronunciation">Pronunciation</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=rozdzia%C5%82&amp;action=edit&amp;section=3" title="Edit section: Pronunciation">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<ul><li><a href="/wiki/Wiktionary:International_Phonetic_Alphabet" title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(<a href="/wiki/Appendix:Polish_pronunciation" title="Appendix:Polish pronunciation">key</a>)</sup>: <span class="IPA">/ˈrɔz̪d͡ʑaw/</span> or <span class="IPA">/ˈrɔʑd͡ʑaw/</span></li>
<li><table class="audiotable" style="vertical-align: bottom; display:inline-block; list-style:none;line-height: 1em; border-collapse:collapse;"><tbody><tr><td class="unicode audiolink" style="padding-right:5px; padding-left: 0;">Audio</td><td class="audiofile"><div class="mediaContainer" style="width:175px"><audio class="kskin" controls="" data-durationhint="1.2" data-mwprovider="wikimediacommons" data-mwtitle="Pl-rozdział.ogg" data-startoffset="0" id="mwe_player_0" preload="none" style="width:175px"><source data-bandwidth="99080" data-height="0" data-shorttitle="Ogg source" data-title="Original Ogg file (99 kbps)" data-width="0" src="//upload.wikimedia.org/wikipedia/commons/3/32/Pl-rozdzia%C5%82.ogg" type='audio/ogg; codecs="vorbis"'/><source data-bandwidth="139176" data-height="0" data-shorttitle="MP3" data-title="MP3" data-transcodekey="mp3" data-width="0" src="//upload.wikimedia.org/wikipedia/commons/transcoded/3/32/Pl-rozdzia%C5%82.ogg/Pl-rozdzia%C5%82.ogg.mp3" type="audio/mpeg"/></audio></div></td><td class="audiometa" style="font-size: 80%;">(<a href="/wiki/File:Pl-rozdzia%C5%82.ogg" title="File:Pl-rozdział.ogg">file</a>)</td></tr></tbody></table></li></ul>
<h3><span class="mw-headline" id="Noun">Noun</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=rozdzia%C5%82&amp;action=edit&amp;section=4" title="Edit section: Noun">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<p><strong class="Latn headword" lang="pl">rozdział</strong> <span class="gender"><abbr title="masculine gender">m</abbr> <abbr title="inanimate">inan</abbr></span>
</p>
<ol><li><a href="/wiki/chapter" title="chapter">chapter</a></li></ol>
<h4><span class="mw-headline" id="Declension">Declension</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=rozdzia%C5%82&amp;action=edit&amp;section=5" title="Edit section: Declension">edit</a><span class="mw-editsection-bracket">]</span></span></h4>
<div class="NavFrame inflection-table-noun" style="width: 29em">
<div class="NavHead">declension of <span class="Latn mention" lang="pl">rozdział</span></div>
<div class="NavContent">
<table class="wikitable inflection-table" style="width: 29em; margin: 0;">
<tbody><tr>
<th style="width: 8em;">
</th>
<th scope="col">singular
</th>
<th scope="col">plural
</th></tr>
<tr>
<th scope="row" title="mianownik (kto? co?)">nominative
</th>
<td><span class="Latn" lang="pl"><a class="mw-selflink selflink">rozdział</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82y&amp;action=edit&amp;redlink=1" title="rozdziały (page does not exist)">rozdziały</a></span>
</td></tr>
<tr>
<th scope="row" title="dopełniacz (kogo? czego?)">genitive
</th>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82u&amp;action=edit&amp;redlink=1" title="rozdziału (page does not exist)">rozdziału</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82%C3%B3w&amp;action=edit&amp;redlink=1" title="rozdziałów (page does not exist)">rozdziałów</a></span>
</td></tr>
<tr>
<th scope="row" title="celownik (komu? czemu?)">dative
</th>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82owi&amp;action=edit&amp;redlink=1" title="rozdziałowi (page does not exist)">rozdziałowi</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82om&amp;action=edit&amp;redlink=1" title="rozdziałom (page does not exist)">rozdziałom</a></span>
</td></tr>
<tr>
<th scope="row" title="biernik (kogo? co?)">accusative
</th>
<td><span class="Latn" lang="pl"><a class="mw-selflink selflink">rozdział</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82y&amp;action=edit&amp;redlink=1" title="rozdziały (page does not exist)">rozdziały</a></span>
</td></tr>
<tr>
<th scope="row" title="narzędnik (kim? czym?)">instrumental
</th>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82em&amp;action=edit&amp;redlink=1" title="rozdziałem (page does not exist)">rozdziałem</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82ami&amp;action=edit&amp;redlink=1" title="rozdziałami (page does not exist)">rozdziałami</a></span>
</td></tr>
<tr>
<th scope="row" title="miejscownik (o kim? o czym?)">locative
</th>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdziale&amp;action=edit&amp;redlink=1" title="rozdziale (page does not exist)">rozdziale</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82ach&amp;action=edit&amp;redlink=1" title="rozdziałach (page does not exist)">rozdziałach</a></span>
</td></tr>
<tr>
<th scope="row" title="wołacz (o!)">vocative
</th>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdziale&amp;action=edit&amp;redlink=1" title="rozdziale (page does not exist)">rozdziale</a></span>
</td>
<td><span class="Latn" lang="pl"><a class="new" href="/w/index.php?title=rozdzia%C5%82y&amp;action=edit&amp;redlink=1" title="rozdziały (page does not exist)">rozdziały</a></span>
</td></tr></tbody></table></div></div>
<!-- 
NewPP limit report
Parsed by mw1309
Cached time: 20180626091154
Cache expiry: 1900800
Dynamic content: false
CPU time usage: 0.144 seconds
Real time usage: 0.204 seconds
Preprocessor visited node count: 130/1000000
Preprocessor generated node count: 0/1500000
Post‐expand include size: 6438/2097152 bytes
Template argument size: 48/2097152 bytes
Highest expansion depth: 7/40
Expensive parser function count: 0/500
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
Number of Wikibase entities loaded: 0/400
Lua time usage: 0.091/10.000 seconds
Lua memory usage: 3.65 MB/50 MB
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  169.416      1 -total
 52.39%   88.752      1 Template:inh
 18.84%   31.918      1 Template:pl-noun
 12.80%   21.680      1 Template:IPA
 10.35%   17.539      1 Template:pl-decl-noun-masc-inani
  3.53%    5.984      1 Template:audio
  2.07%    3.505      1 Template:catlangname
  1.78%    3.018      1 Template:IPAchar
-->
</div>
<!-- Saved in parser cache with key enwiktionary:pcache:idhash:1774509-0!canonical and timestamp 20180626091154 and revision id 45214878
 -->
<noscript><img alt="" height="1" src="//en.wiktionary.org/wiki/Special:CentralAutoLogin/start?type=1x1" style="border: none; position: absolute;" title="" width="1"/></noscript></div> <div class="printfooter">
						Retrieved from "<a dir="ltr" href="https://en.wiktionary.org/w/index.php?title=rozdział&amp;oldid=45214878">https://en.wiktionary.org/w/index.php?title=rozdział&amp;oldid=45214878</a>"					</div>
<div class="catlinks" data-mw="interface" id="catlinks"><div class="mw-normal-catlinks" id="mw-normal-catlinks"><a href="/wiki/Special:Categories" title="Special:Categories">Categories</a>: <ul><li><a href="/wiki/Category:Polish_terms_inherited_from_Proto-Slavic" title="Category:Polish terms inherited from Proto-Slavic">Polish terms inherited from Proto-Slavic</a></li><li><a href="/wiki/Category:Polish_terms_derived_from_Proto-Slavic" title="Category:Polish terms derived from Proto-Slavic">Polish terms derived from Proto-Slavic</a></li><li><a href="/wiki/Category:Polish_terms_with_IPA_pronunciation" title="Category:Polish terms with IPA pronunciation">Polish terms with IPA pronunciation</a></li><li><a href="/wiki/Category:Polish_terms_with_audio_links" title="Category:Polish terms with audio links">Polish terms with audio links</a></li><li><a href="/wiki/Category:Polish_lemmas" title="Category:Polish lemmas">Polish lemmas</a></li><li><a href="/wiki/Category:Polish_nouns" title="Category:Polish nouns">Polish nouns</a></li><li><a href="/wiki/Category:Polish_masculine_nouns" title="Category:Polish masculine nouns">Polish masculine nouns</a></li></ul></div></div> <div class="visualClear"></div>
</div>
</div>
<div id="mw-navigation">
<h2>Navigation menu</h2>
<div id="mw-head">
<div aria-labelledby="p-personal-label" class="" id="p-personal" role="navigation">
<h3 id="p-personal-label">Personal tools</h3>
<ul>
<li id="pt-anonuserpage">Not logged in</li><li id="pt-anontalk"><a accesskey="n" href="/wiki/Special:MyTalk" title="Discussion about edits from this IP address [n]">Talk</a></li><li id="pt-anoncontribs"><a accesskey="y" href="/wiki/Special:MyContributions" title="A list of edits made from this IP address [y]">Contributions</a></li><li id="pt-createaccount"><a href="/w/index.php?title=Special:CreateAccount&amp;returnto=rozdzia%C5%82" title="You are encouraged to create an account and log in; however, it is not mandatory">Create account</a></li><li id="pt-login"><a accesskey="o" href="/w/index.php?title=Special:UserLogin&amp;returnto=rozdzia%C5%82" title="You are encouraged to log in; however, it is not mandatory [o]">Log in</a></li> </ul>
</div>
<div id="left-navigation">
<div aria-labelledby="p-namespaces-label" class="vectorTabs" id="p-namespaces" role="navigation">
<h3 id="p-namespaces-label">Namespaces</h3>
<ul>
<li class="selected" id="ca-nstab-main"><span><a accesskey="c" href="/wiki/rozdzia%C5%82" title="View the content page [c]">Entry</a></span></li><li class="new" id="ca-talk"><span><a accesskey="t" href="/w/index.php?title=Talk:rozdzia%C5%82&amp;action=edit&amp;redlink=1" rel="discussion" title="Discussion about the content page (page does not exist) [t]">Discussion</a></span></li> </ul>
</div>
<div aria-labelledby="p-variants-label" class="vectorMenu emptyPortlet" id="p-variants" role="navigation">
<input aria-labelledby="p-variants-label" class="vectorMenuCheckbox" type="checkbox"/>
<h3 id="p-variants-label">
<span>Variants</span>
</h3>
<div class="menu">
<ul>
</ul>
</div>
</div>
</div>
<div id="right-navigation">
<div aria-labelledby="p-views-label" class="vectorTabs" id="p-views" role="navigation">
<h3 id="p-views-label">Views</h3>
<ul>
<li class="collapsible selected" id="ca-view"><span><a href="/wiki/rozdzia%C5%82">Read</a></span></li><li class="collapsible" id="ca-edit"><span><a accesskey="e" href="/w/index.php?title=rozdzia%C5%82&amp;action=edit" title="Edit this page [e]">Edit</a></span></li><li class="collapsible" id="ca-history"><span><a accesskey="h" href="/w/index.php?title=rozdzia%C5%82&amp;action=history" title="Past revisions of this page [h]">History</a></span></li> </ul>
</div>
<div aria-labelledby="p-cactions-label" class="vectorMenu emptyPortlet" id="p-cactions" role="navigation">
<input aria-labelledby="p-cactions-label" class="vectorMenuCheckbox" type="checkbox"/>
<h3 id="p-cactions-label"><span>More</span></h3>
<div class="menu">
<ul>
</ul>
</div>
</div>
<div id="p-search" role="search">
<h3>
<label for="searchInput">Search</label>
</h3>
<form action="/w/index.php" id="searchform">
<div id="simpleSearch">
<input accesskey="f" id="searchInput" name="search" placeholder="Search Wiktionary" title="Search Wiktionary [f]" type="search"/><input name="title" type="hidden" value="Special:Search"/><input class="searchButton mw-fallbackSearchButton" id="mw-searchButton" name="fulltext" title="Search the pages for this text" type="submit" value="Search"/><input class="searchButton" id="searchButton" name="go" title="Go to a page with this exact name if it exists" type="submit" value="Go"/> </div>
</form>
</div>
</div>
</div>
<div id="mw-panel">
<div id="p-logo" role="banner"><a class="mw-wiki-logo" href="/wiki/Wiktionary:Main_Page" title="Visit the main page"></a></div>
<div aria-labelledby="p-navigation-label" class="portal" id="p-navigation" role="navigation">
<h3 id="p-navigation-label">Navigation</h3>
<div class="body">
<ul>
<li id="n-mainpage-text"><a href="/wiki/Wiktionary:Main_Page">Main Page</a></li><li id="n-portal"><a href="/wiki/Wiktionary:Community_portal" title="About the project, what you can do, where to find things">Community portal</a></li><li id="n-wiktprefs"><a href="/wiki/Wiktionary:Per-browser_preferences">Preferences</a></li><li id="n-requestedarticles"><a href="/wiki/Wiktionary:Requested_entries">Requested entries</a></li><li id="n-recentchanges"><a accesskey="r" href="/wiki/Special:RecentChanges" title="A list of recent changes in the wiki [r]">Recent changes</a></li><li id="n-randompage"><a accesskey="x" href="/wiki/Special:Random" title="Load a random page [x]">Random entry</a></li><li id="n-help"><a href="https://en.wiktionary.org/wiki/Help:Contents" title="The place to find out">Help</a></li><li id="n-Glossary"><a href="/wiki/Appendix:Glossary">Glossary</a></li><li id="n-sitesupport"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_en.wiktionary.org&amp;uselang=en" title="Support us">Donations</a></li><li id="n-contact"><a href="/wiki/Wiktionary:Contact_us">Contact us</a></li> </ul>
</div>
</div>
<div aria-labelledby="p-tb-label" class="portal" id="p-tb" role="navigation">
<h3 id="p-tb-label">Tools</h3>
<div class="body">
<ul>
<li id="t-whatlinkshere"><a accesskey="j" href="/wiki/Special:WhatLinksHere/rozdzia%C5%82" title="A list of all wiki pages that link here [j]">What links here</a></li><li id="t-recentchangeslinked"><a accesskey="k" href="/wiki/Special:RecentChangesLinked/rozdzia%C5%82" rel="nofollow" title="Recent changes in pages linked from this page [k]">Related changes</a></li><li id="t-upload"><a accesskey="u" href="//commons.wikimedia.org/wiki/Special:UploadWizard?uselang=en" title="Upload files [u]">Upload file</a></li><li id="t-specialpages"><a accesskey="q" href="/wiki/Special:SpecialPages" title="A list of all special pages [q]">Special pages</a></li><li id="t-permalink"><a href="/w/index.php?title=rozdzia%C5%82&amp;oldid=45214878" title="Permanent link to this revision of the page">Permanent link</a></li><li id="t-info"><a href="/w/index.php?title=rozdzia%C5%82&amp;action=info" title="More information about this page">Page information</a></li><li id="t-cite"><a href="/w/index.php?title=Special:CiteThisPage&amp;page=rozdzia%C5%82&amp;id=45214878" title="Information on how to cite this page">Cite this page</a></li> </ul>
</div>
</div>
<div aria-labelledby="p-lang-label" class="portal" id="p-lang" role="navigation">
<h3 id="p-lang-label">In other languages</h3>
<div class="body">
<ul>
<li class="interlanguage-link interwiki-cs"><a class="interlanguage-link-target" href="https://cs.wiktionary.org/wiki/rozdzia%C5%82" hreflang="cs" lang="cs" title="rozdział – Czech">Čeština</a></li><li class="interlanguage-link interwiki-el"><a class="interlanguage-link-target" href="https://el.wiktionary.org/wiki/rozdzia%C5%82" hreflang="el" lang="el" title="rozdział – Greek">Ελληνικά</a></li><li class="interlanguage-link interwiki-eo"><a class="interlanguage-link-target" href="https://eo.wiktionary.org/wiki/rozdzia%C5%82" hreflang="eo" lang="eo" title="rozdział – Esperanto">Esperanto</a></li><li class="interlanguage-link interwiki-io"><a class="interlanguage-link-target" href="https://io.wiktionary.org/wiki/rozdzia%C5%82" hreflang="io" lang="io" title="rozdział – Ido">Ido</a></li><li class="interlanguage-link interwiki-hu"><a class="interlanguage-link-target" href="https://hu.wiktionary.org/wiki/rozdzia%C5%82" hreflang="hu" lang="hu" title="rozdział – Hungarian">Magyar</a></li><li class="interlanguage-link interwiki-mg"><a class="interlanguage-link-target" href="https://mg.wiktionary.org/wiki/rozdzia%C5%82" hreflang="mg" lang="mg" title="rozdział – Malagasy">Malagasy</a></li><li class="interlanguage-link interwiki-nl"><a class="interlanguage-link-target" href="https://nl.wiktionary.org/wiki/rozdzia%C5%82" hreflang="nl" lang="nl" title="rozdział – Dutch">Nederlands</a></li><li class="interlanguage-link interwiki-pl"><a class="interlanguage-link-target" href="https://pl.wiktionary.org/wiki/rozdzia%C5%82" hreflang="pl" lang="pl" title="rozdział – Polish">Polski</a></li><li class="interlanguage-link interwiki-ru"><a class="interlanguage-link-target" href="https://ru.wiktionary.org/wiki/rozdzia%C5%82" hreflang="ru" lang="ru" title="rozdział – Russian">Русский</a></li><li class="interlanguage-link interwiki-sv"><a class="interlanguage-link-target" href="https://sv.wiktionary.org/wiki/rozdzia%C5%82" hreflang="sv" lang="sv" title="rozdział – Swedish">Svenska</a></li><li class="interlanguage-link interwiki-chr"><a class="interlanguage-link-target" href="https://chr.wiktionary.org/wiki/rozdzia%C5%82" hreflang="chr" lang="chr" title="rozdział – Cherokee">ᏣᎳᎩ</a></li> </ul>
</div>
</div>
<div aria-labelledby="p-coll-print_export-label" class="portal" id="p-coll-print_export" role="navigation">
<h3 id="p-coll-print_export-label">Print/export</h3>
<div class="body">
<ul>
<li id="coll-create_a_book"><a href="/w/index.php?title=Special:Book&amp;bookcmd=book_creator&amp;referer=rozdzia%C5%82">Create a book</a></li><li id="coll-download-as-rdf2latex"><a href="/w/index.php?title=Special:ElectronPdf&amp;page=rozdzia%C5%82&amp;action=show-download-screen">Download as PDF</a></li><li id="t-print"><a accesskey="p" href="/w/index.php?title=rozdzia%C5%82&amp;printable=yes" title="Printable version of this page [p]">Printable version</a></li> </ul>
</div>
</div>
</div>
</div>
<div id="footer" role="contentinfo">
<ul id="footer-info">
<li id="footer-info-lastmod"> This page was last edited on 25 May 2017, at 21:46.</li>
<li id="footer-info-copyright">Text is available under the <a href="//creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike License</a>; additional terms may apply.  By using this site, you agree to the <a href="//wikimediafoundation.org/wiki/Terms_of_Use">Terms of Use</a> and <a href="//wikimediafoundation.org/wiki/Privacy_policy">Privacy Policy.</a></li>
</ul>
<ul id="footer-places">
<li id="footer-places-privacy"><a class="extiw" href="https://wikimediafoundation.org/wiki/Privacy_policy" title="wmf:Privacy policy">Privacy policy</a></li>
<li id="footer-places-about"><a class="mw-redirect" href="/wiki/Wiktionary:About" title="Wiktionary:About">About Wiktionary</a></li>
<li id="footer-places-disclaimer"><a href="/wiki/Wiktionary:General_disclaimer" title="Wiktionary:General disclaimer">Disclaimers</a></li>
<li id="footer-places-developers"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute">Developers</a></li>
<li id="footer-places-cookiestatement"><a href="https://wikimediafoundation.org/wiki/Cookie_statement">Cookie statement</a></li>
<li id="footer-places-mobileview"><a class="noprint stopMobileRedirectToggle" href="//en.m.wiktionary.org/w/index.php?title=rozdzia%C5%82&amp;mobileaction=toggle_view_mobile">Mobile view</a></li>
</ul>
<ul class="noprint" id="footer-icons">
<li id="footer-copyrightico">
<a href="https://wikimediafoundation.org/"><img alt="Wikimedia Foundation" height="31" src="/static/images/wikimedia-button.png" srcset="/static/images/wikimedia-button-1.5x.png 1.5x, /static/images/wikimedia-button-2x.png 2x" width="88"/></a> </li>
<li id="footer-poweredbyico">
<a href="//www.mediawiki.org/"><img alt="Powered by MediaWiki" height="31" src="/static/images/poweredby_mediawiki_88x31.png" srcset="/static/images/poweredby_mediawiki_132x47.png 1.5x, /static/images/poweredby_mediawiki_176x62.png 2x" width="88"/></a> </li>
</ul>
<div style="clear: both;"></div>
</div>
<script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"limitreport":{"cputime":"0.144","walltime":"0.204","ppvisitednodes":{"value":130,"limit":1000000},"ppgeneratednodes":{"value":0,"limit":1500000},"postexpandincludesize":{"value":6438,"limit":2097152},"templateargumentsize":{"value":48,"limit":2097152},"expansiondepth":{"value":7,"limit":40},"expensivefunctioncount":{"value":0,"limit":500},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":0,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  169.416      1 -total"," 52.39%   88.752      1 Template:inh"," 18.84%   31.918      1 Template:pl-noun"," 12.80%   21.680      1 Template:IPA"," 10.35%   17.539      1 Template:pl-decl-noun-masc-inani","  3.53%    5.984      1 Template:audio","  2.07%    3.505      1 Template:catlangname","  1.78%    3.018      1 Template:IPAchar"]},"scribunto":{"limitreport-timeusage":{"value":"0.091","limit":"10.000"},"limitreport-memusage":{"value":3827826,"limit":52428800}},"cachereport":{"origin":"mw1309","timestamp":"20180626091154","ttl":1900800,"transientcontent":false}}});mw.config.set({"wgBackendResponseTime":84,"wgHostname":"mw1326"});});</script>
</body>
</html>
"""


class TestWiktionaryParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        unittest.TestCase.setUpClass()
        cls.maxDiff = None
        cls.wikt_parser = WiktionaryParser()

    '''
    def testWordTagDefinitions(self):
        czym_pg = self.wikt_parser.word_wikt_page("czym", "Polish")
        print(czym_pg.entry)
        self.assertEqual(czym_pg.entry["Polish"]["Pronoun"], {"head": "czym",
                                                              "definitions": ["instrumental of co",
                                                                              "locative of co"],
                                                              "lemmas": {"Polish": ["co"],
                                                                         "English": []}})


    def testSubtag(self):
        self.maxDiff = None
        wikt_pg = self.wikt_parser.word_wikt_page("rozdział", "Polish")
        #self.assertEqual(str(wikt_pg.page), HTML)
        self.assertEqual(str(wikt_pg.subtag(wikt_pg.page, {"h2"}, {"h2"}, "Polish")), HTML)
    '''

    def testTable(self):
        self.maxDiff = None
        wikt_pg = self.wikt_parser.word_wikt_page("warto", "Polish")
        self.assertEqual(wikt_pg.entry['Conjugation'], {"infinitive": None,
                                                       "present indicative": "warto",
                                                       "past indicative": "warto było",
                                                       "future tense": "warto będzie",
                                                       "conditional": ["warto by",
                                                                       "warto byłoby",
                                                                       "warto by było"]})
        wikt_pg = self.wikt_parser.word_wikt_page("płonąć", "Polish")



"""
class TestSpeechart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        unittest.TestCase.setUpClass()
        cls.maxDiff = None
        cls.words = dict()  # word-pronunciation dict in language & IPA
        cls.language = "English" #"Finnish"
        cls.parser = MorphemeParser(cls.language)
        cls.blissweb = BlissWeb(cls.language)
        cls.speechart = SentenceChart(cls.language)

        cls.nn1 = cls.blissweb.neural_net.create_node("minus,no,without")
        cls.nn2 = cls.blissweb.neural_net.create_node("and,also,plus,too")
        cls.nn3 = cls.blissweb.neural_net.create_node("life")
        cls.nn4 = cls.blissweb.neural_net.create_node("mind,intellect,reason")
        cls.nn5 = cls.blissweb.neural_net.create_node("body,trunk")
        cls.nn6 = cls.blissweb.neural_net.create_node("feeling,emotion,sensation")
        cls.nn7 = cls.blissweb.neural_net.create_node("love,affection")
        cls.nn8 = cls.blissweb.neural_net.create_node("person,human_being,individual,human")
        cls.nn9 = cls.blissweb.neural_net.create_node("existence,being_(1)")
        cls.nn10 = cls.blissweb.neural_net.create_node("soul")

        cls.nn1.set_outgoing([cls.nn3, cls.nn4])
        cls.nn2.set_outgoing([cls.nn3, cls.nn5])
        cls.nn3.set_outgoing([cls.nn4, cls.nn5])
        cls.nn6.extend_incoming([cls.nn4, cls.nn5])
        cls.nn6.extend_outgoing([cls.nn7])
        cls.nn8.extend_incoming([cls.nn3, cls.nn5])
        cls.nn9.extend_incoming([cls.nn3, cls.nn4])
        cls.nn10.extend_incoming([cls.nn6, cls.nn8, cls.nn3])

        cls.blissweb.neural_net.set_nodes([cls.nn1, cls.nn2, cls.nn3, cls.nn4, cls.nn5,
                                           cls.nn6, cls.nn7, cls.nn8, cls.nn9, cls.nn10])

        # cls.parser.common_phonemes(50)
    '''
    def test_table(self):
        self.parser.reset_language(language="Finnish")
        self.assertEqual(self.parser.word_declension(u"naapuri", language="Finnish"),
                         {u"singular": {u"nominative": [u"naapuri"],
                                        u"accusative > nom.": [u"naapuri"],
                                        u"accusative > gen.": [u"naapurin"],
                                        u"genitive": [u"naapurin"],
                                        u"partitive": [u"naapuria"],
                                        u"inessive": [u"naapurissa"],
                                        u"elative": [u"naapurista"],
                                        u"illative": [u"naapuriin"],
                                        u"adessive": [u"naapurilla"],
                                        u"ablative": [u"naapurilta"],
                                        u"allative": [u"naapurille"],
                                        u"essive": [u"naapurina"],
                                        u"translative": [u"naapuriksi"],
                                        u"instructive": [u"—"],
                                        u"abessive": [u"naapuritta"],
                                        u"comitative": [u"—"]},
                          u"plural": {u"nominative": [u"naapurit"],
                                      u"accusative > nom.": [u"naapurit"],
                                      u"accusative > gen.": [u"naapurit"],
                                      u"genitive": [u"naapurien",
                                                    u"naapureiden",
                                                    u"naapureitten"],
                                      u"partitive": [u"naapureita",
                                                     u"naapureja"],
                                      u"inessive": [u"naapureissa"],
                                      u"elative": [u"naapureista"],
                                      u"illative": [u"naapureihin"],
                                      u"adessive": [u"naapureilla"],
                                      u"ablative": [u"naapureilta"],
                                      u"allative": [u"naapureille"],
                                      u"essive": [u"naapureina"],
                                      u"translative": [u"naapureiksi"],
                                      u"instructive": [u"naapurein"],
                                      u"abessive": [u"naapureitta"],
                                      u"comitative": [u"naapureineen"]}})
        self.parser.word_declension("olla")

    def test_break_syllable(self):
        self.parser.reset_language("Polish")
        syllable = u"lat͡ɕ"
        ans = (u"l", u"a", u"t͡ɕ")
        self.assertEqual(self.parser.break_syllable(syllable), ans)

        self.parser.reset_language("Dutch")
        syllable = u"tjə"
        ans = (u"t", u"jə", u"")
        self.assertEqual(self.parser.break_syllable(syllable), ans)

    def test_break_syllables(self):
        self.parser.reset_language("Polish")
        ans = [(u"", u"ɔ", u""),
               (u"b", u"a", u""),
               (u"l", u"a", u"t͡ɕ")]
        ipa = u"ɔbalat͡ɕ"
        self.assertEqual(self.parser.break_syllables(ipa, use_syllables=False), ans)

        self.parser.reset_language("Dutch")
        ans = [(u"kl", u"ɛi", u"̯n"),
               (u"t", u"jə", u"")]
        ipa = u"klɛi̯ntjə"
        self.assertEqual(self.parser.break_syllables(ipa, use_syllables=False), ans)

    def test_extract_syllable(self):
        self.parser.reset_language("Polish")
        ans = (u"l", u"a", u"t͡ɕ")
        ipa = u"ɔbalat͡ɕ"
        num = 2
        self.assertEqual(self.parser.extract_syllable(ipa, num, use_syllables=False), ans)

        self.parser.reset_language("Dutch")
        ans = (u"kl", u"ɛi̯", u"n")
        ipa = u"klɛi̯ntjə"
        num = 0
        self.assertEqual(self.parser.extract_syllable(ipa, num, use_syllables=False), ans)

    def test_add_syllables(self):
        self.parser.reset_language("Polish")
        ans = u"ɔ.ba.lat͡ɕ"
        ipa = u"ɔbalat͡ɕ"
        self.assertEqual(self.ipa_word.add_syllables(ipa), ans)

        self.parser.reset_language("Dutch")
        ans = u"klɛi̯n.tjə"
        ipa = u"klɛi̯ntjə"
        self.assertEqual(self.ipa_word.add_syllables(ipa), ans)

    def test_next_phoneme(self):
        self.parser.reset_language("Polish")
        ans1 = u"ɔ" if self.language == "Polish" else u"k"
        ans2 = u"b" if self.language == "Polish" else u"l"
        ans3 = u"a" if self.language == "Polish" else u"ɛi"
        next_phoneme, next_ipa = self.parser.next_phoneme(self.ipa, use_syllables=False)
        self.assertEqual(next_phoneme, ans1)
        next_phoneme, next_ipa = self.parser.next_phoneme(next_ipa, use_syllables=False)
        self.assertEqual(next_phoneme, ans2)
        self.assertEqual(self.parser.next_phoneme(next_ipa, remove=False, use_syllables=False), ans3)

        self.parser.reset_language("Dutch")
        ans1 = u"k"
        ans2 = u"l"
        ans3 = u"ɛi"
        next_phoneme, next_ipa = self.parser.next_phoneme(self.ipa, use_syllables=False)
        self.assertEqual(next_phoneme, ans1)
        next_phoneme, next_ipa = self.parser.next_phoneme(next_ipa, use_syllables=False)
        self.assertEqual(next_phoneme, ans2)
        self.assertEqual(self.parser.next_phoneme(next_ipa, remove=False, use_syllables=False), ans3)

    def test_next_syllable(self):
        self.parser.reset_language("Polish")
        next_syllable, rest_ipa = self.parser.next_syllable(self.ipa)
        ans1 = u"ɔ"
        ans2 = u"ba"
        ans3 = u"lat͡ɕ"
        self.assertEqual(next_syllable, ans1)
        next_syllable, rest_ipa = self.parser.next_syllable(rest_ipa)
        self.assertEqual(next_syllable, ans2)
        self.assertEqual(self.parser.next_syllable(rest_ipa, remove=False), ans3)

        self.parser.reset_language("Dutch")
        next_syllable, rest_ipa = self.parser.next_syllable(self.ipa)
        ans1 = u"klɛi̯n"
        ans2 = u"tjə"
        ans3 = u""
        self.assertEqual(next_syllable, ans1)
        next_syllable, rest_ipa = self.parser.next_syllable(rest_ipa)
        self.assertEqual(next_syllable, ans2)
        self.assertEqual(self.parser.next_syllable(rest_ipa, remove=False), ans3)

    def test_split_syllables(self):
        self.parser.reset_language("Polish")
        ans = [u"ɔ", u"ba", u"lat͡ɕ"]
        ipa = u"ɔbalat͡ɕ"
        self.assertEqual(self.parser.split_syllables(ipa, use_syllables=False), ans)

        self.parser.reset_language("Dutch")
        ans = [u"klɛi̯n", u"tjə"]
        ipa = u"klɛi̯ntjə"
        self.assertEqual(self.parser.split_syllables(ipa, use_syllables=False), ans)

    def test_find_ipa_vowels(self):
        self.parser.reset_language("Polish")
        ans = u"ɔ", u"balat͡ɕ"
        ipa = u"ɔbalat͡ɕ"
        word = u"obalać"
        ipa_word = IPAWord(word, "Polish", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_vowels(ipa), ans)
 
        self.parser.reset_language("Dutch")
        ans = u"ɛi", u"̯ntjə"
        ipa = u"klɛi̯ntjə"
        word = u"kleintje"
        ipa_word = IPAWord(word, "Dutch", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_vowels(ipa), ans)

        self.parser.reset_language("Finnish")
        ans = u"ɑː", u"puri"
        word = u"naapuri"
        ipa = u"ˈnɑːpuri"
        ipa_word = IPAWord(word, "Finnish", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_vowels(ipa), ans)

    def test_find_ipa_consonants(self):
        self.parser.reset_language("Polish")
        ans = u"b", u"alat͡ɕ"
        ipa = u"ɔbalat͡ɕ"
        word = u"obalać"
        ipa_word = IPAWord(word, "Polish", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_consonants(ipa), ans)

        self.parser.reset_language("Dutch")
        ans = u"kl", u"ɛi̯ntjə"
        ipa = u"klɛi̯ntjə"
        word = u"kleintje"
        ipa_word = IPAWord(word, "Dutch", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_consonants(ipa), ans)

        self.parser.reset_language("Finnish")
        ans = u"ˈn", u"ɑːpuri"
        word = u"naapuri"
        ipa = u"ˈnɑːpuri"
        ipa_word = IPAWord(word, "Finnish", parser=self.parser)
        self.assertEqual(ipa_word.find_ipa_consonants(ipa), ans)
    '''

    def test_shortest_path(self):
        nn1, nn2, nn3, nn4, nn5 = self.blissweb.neural_net.nodes
        self.assertEqual(self.blissweb.shortest_path(nn1, nn2), None)
        self.assertEqual(self.blissweb.shortest_path(nn1, nn5), [nn1, nn3, nn5])

    def test_longest_path(self):
        nn1, nn2, nn3, nn4, nn5 = self.blissweb.neural_net.nodes
        self.assertEqual(self.blissweb.longest_path(nn1, nn4), [nn1, nn2, nn3, nn4])
        self.assertEqual(self.blissweb.longest_path(nn5, nn1), None)

    def test_cycles(self):
        nn1, nn2, nn3, nn4, nn5 = self.blissweb.neural_net.nodes
        nn4.set_outgoing([nn1])
        self.assertEqual(self.blissweb.find_cycle(nn1), [nn1, nn2, nn4, nn1])
        self.assertEqual(self.blissweb.find_cycle(nn5), None)

    def test_visualization(self):
        nn1, nn2, nn3, nn4, nn5, nn6, nn7, nn8, nn9, nn10 = self.blissweb.neural_net.nodes
        neural_img = NeuralNetImage(self.blissweb.neural_net.nodes, blissweb=self.blissweb)
        neural_img.draw_layers()
        neural_img.draw_web()
        self.blissweb.arrow_fan(self.blissweb.node_img(nn1), len(nn1.outgoing)).show()
        alice = excerpts.alice_in_wonderland[:5000]
        title = "Blissymbols in Alice in Wonderland"
        self.blissweb.add_bliss_sentences(alice)
        self.blissweb.chart(title)

    def test_speechart(self):
        alice = excerpts.alice_in_wonderland[:1000]
        title = "Alice in Wonderland"
        self.speechart.add_text(alice)
        self.speechart.chart(title)
        self.speechart.refresh_data()

    def test_tokenize_punct(self):
        self.assertEqual(self.speechart.tokenize_punct("Hello, this is my friend, Molly"),
                         [["Hello"], ["this", "is", "my", "friend"], ["Molly"]])
"""

if __name__ == '__main__':
    unittest.main()

