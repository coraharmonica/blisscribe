<h1>Blisscribe</h1>

Blisscribe is a translator designed for visual reading, allowing you to input text and receive a PDF with selected words replaced with Blissymbols.


<h2>Setup</h2>

Ensure you're working in Python 3.6 or above.  You can setup Blisscribe either locally or with a virtualenv.

Blisscribe depends on the following libraries:

- Django
- Pillow
- nltk
- beautifulsoup4
- fpdf
- openpyxl
- requests
- sklearn
- lxml**

** The lxml binding can be downloaded [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) and then installed with pip, like so:

> pip install C:\Users\me\lxml‑4.2.3‑cp37‑cp37m‑win_amd64.whl

Ensure you have these all installed either to your local Python interpreter or to a virtualenv.
You will need a virtualenv to use the Blisscribe web interface.


<h3>Virtualenv</h3>

Ensure you've installed virtualenv.  Open command prompt and cd to the [bliss_online folder](https://github.com/coraharmonica/blisscribe/tree/master/bliss_online), where the env folder is located.

If you are a Windows user, enter the following prompts to activate a virtualenv:

> py -m virtualenv env

> cd env/Scripts

> activate.bat

Otherwise, enter this (works for OS X):

> source env/bin/activate

If successful, your command prompt should now begin with (env).

Install any missing packages to your virtualenv.  You'll likely need all the dependencies listed above under Setup.



<h2>Translation</h2>

After setting up Blisscribe, you can translate either from command line, Python, or online.

<h3>Command Line</h3>

Open blisscribe-master in command line and enter the prompt:

> cd bliss_online/bliss_webapp/translation

Then run blisscript.py with your version of Python:

> python blisscript.py

This will run a prompt asking which language and text you wish to translate.  To change the script simply modify blisscript.py.

<h3>Python</h3>

To translate in Python, head to the [translation folder](https://github.com/coraharmonica/blisscribe/tree/master/bliss_online/bliss_webapp/translation), located under bliss_online/bliss_webapp.  From here you can edit the demo.py file to translate demo text or some of your own.  Any text you translate will appear as a PDF in the out folder.

<h3>Online</h3>

To translate online, open the package in command line and cd to the [bliss_online folder](https://github.com/coraharmonica/blisscribe/tree/master/bliss_online), where the env folder is located.  If you're not already in a virtualenv, follow the steps above (under Setup>Virtualenv) to activate one.

Then run manage.py's makemigrations and migrate with Python:

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


Blisscribe is currently maintained in Python 3.6 (as of 06/22/2018).
To learn more about Blisscribe, visit the website:  blisscribe.tumblr.com.  You can also contact me through Blisscribe at blisscribe [at] gmail [dot] com.
