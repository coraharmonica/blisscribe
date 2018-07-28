<h1>Blisscribe</h1>

Blisscribe is a translator designed for visual reading, allowing you to input text and receive a PDF with selected words replaced with Blissymbols.


<h2>Setup</h2>

Ensure you're working in Python 2.7 or above.  You can setup Blisscribe either through command line or Python.


<h3>Command Line</h3>

Ensure you've installed virtualenv.  Open blisscribe in command line and cd to the [bliss_online folder](https://github.com/coraharmonica/blisscribe/tree/master/bliss_online), where the env folder is located.  Enter the command:

> source env/bin/activate

If successful, your command line prompt should now begin with (env).


<h3>Python</h3>

Blisscribe depends on the following libraries:

- nltk
- pattern3
- Pillow
- Django
- beautifulsoup4
- fpdf
- openpyxl
- scikit-learn
- requests

Ensure you have these all installed to your Python interpreter to run Blisscribe smoothly.


<h2>Translation</h2>

After setting up Blisscribe, you can translate either from command line, Python, or online.

<h3>Command Line</h3>

Open blisscribe on command line and enter this command:

> cd bliss_online/bliss_webapp/translation

Then enter:

> python blisscript.py

This will run a prompt asking which language and text you wish to translate.  To modify the script simply modify blisscript.py.

<h3>Python</h3>

To translate in Python, head to the [translation folder](https://github.com/coraharmonica/blisscribe/tree/master/bliss_online/bliss_webapp/translation), located under bliss_online/bliss_webapp.  From here you can edit the demo.py file to translate demo text or some of your own.  Any text you translate will appear as a PDF in the out folder.

<h3>Online</h3>

To translate online, open the package in command line and cd to the [bliss_online folder](https://github.com/coraharmonica/blisscribe/tree/master/bliss_online), where the env folder is located.  If you're not already in a virtualenv, run the following prompts:

> source env/bin/activate

> python manage.py makemigrations

> python manage.py migrate

If all files have been migrated then run the final prompt:

> python manage.py runserver

If the server connects properly you'll see a web address in command line.  Go to the address and visit the 'translate' section of the Blisscribe website to translate using the interface.

<h2>Features</h2>

Blisscribe currently supports the following languages:
- English
- Spanish
- German
- French
- Italian
- Dutch
- Polish
- Swedish
- Portuguese
- Danish


![alice en sample](https://github.com/coraharmonica/blisscribe/blob/master/bliss_online/bliss_webapp/translation/sample%20translations/alice%20en%20sample.png?raw=true)

***

![alice pl sample](https://github.com/coraharmonica/blisscribe/blob/master/bliss_online/bliss_webapp/translation/sample%20translations/alice%20pl%20sample.png?raw=true)


Blisscribe also provides options for users to select which parts of speech to translate, including nouns, verbs, adjectives/adverbs, and/or all parts of speech.

![nouns](https://github.com/coraharmonica/blisscribe/blob/master/bliss_online/bliss_webapp/translation/sample%20translations/quickbrownfox_nouns.png?raw=true)

***

![verbs](https://github.com/coraharmonica/blisscribe/blob/master/bliss_online/bliss_webapp/translation/sample%20translations/quickbrownfox_verbs.png?raw=true)

***

![adjs/advs](https://github.com/coraharmonica/blisscribe/blob/master/bliss_online/bliss_webapp/translation/sample%20translations/quickbrownfox_adjs.png?raw=true)

***

![other](https://github.com/coraharmonica/blisscribe/blob/master/bliss_online/bliss_webapp/translation/sample%20translations/quickbrownfox_other.png?raw=true)


Blisscribe is currently maintained in Python 3.6 (as of 06/22/2018), with backwards compatibility for Python 2.7 and above.
To learn more about Blisscribe, visit the website:  blisscribe.tumblr.com.  You can also contact me through Blisscribe at blisscribe [at] gmail [dot] com.
