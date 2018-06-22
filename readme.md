<h1>Blisscribe</h1>

Blisscribe is a translator designed for visual reading, allowing you to input text and receive a PDF with selected words replaced with Blissymbols.

After downloading Blisscribe, you can translate either from Python or a web interface.

<h3>Blisscribe in Python</h3>

To translate in Python, open the package in Python 2.7 and head to the  [blisscribe_py folder](https://github.com/coraharmonica/blisscribe/tree/master/main/bliss_web/bliss_app/bliss_webapp/blisscribe_py), located under main/bliss_web/bliss_webapp.  From here you can edit the demo.py file to run a demo.  The out folder also holds sample and output translations.

<h3>Blisscribe on the Web</h3>

To translate using the web interface, open the package in command line and cd to the [bliss_web folder](https://github.com/coraharmonica/blisscribe/tree/master/main/bliss_web) through the main folder.  Run the following prompt:

> source env/bin/activate

If successful, cd into bliss_app and run this prompt:

> manage.py makemigrations

If all files have been migrated then run the final prompt:

> manage.py runserver

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


![alice en p1 x=200 y=200](https://github.com/coraharmonica/blisscribe/blob/master/main/bliss_web/bliss_app/bliss_webapp/blisscribe_py/sample%20translations/alice%20en%20p1.png?raw=true)

***

![alice pl p1](https://github.com/coraharmonica/blisscribe/blob/master/main/bliss_web/bliss_app/bliss_webapp/blisscribe_py/sample%20translations/alice%20pl%20p1.png?raw=true)


Blisscribe also provides options for users to select which parts of speech to translate, including nouns, verbs, adjectives/adverbs, and/or all parts of speech.

![nouns](https://github.com/coraharmonica/blisscribe/blob/master/main/bliss_web/bliss_app/bliss_webapp/blisscribe_py/sample%20translations/quickbrownfox_nouns.png?raw=true)

***

![verbs](https://github.com/coraharmonica/blisscribe/blob/master/main/bliss_web/bliss_app/bliss_webapp/blisscribe_py/sample%20translations/quickbrownfox_verbs.png?raw=true)

***

![adjs/advs](https://github.com/coraharmonica/blisscribe/blob/master/main/bliss_web/bliss_app/bliss_webapp/blisscribe_py/sample%20translations/quickbrownfox_adjs.png?raw=true)

***

![other](https://github.com/coraharmonica/blisscribe/blob/master/main/bliss_web/bliss_app/bliss_webapp/blisscribe_py/sample%20translations/quickbrownfox_other.png?raw=true)


Blisscribe is currently maintained in Python 2.7, with (selective) 3.0 forward compatibility.
To learn more about Blisscribe, visit the website:  blisscribe.tumblr.com
You can also contact me through Blisscribe at blisscribe [at] gmail [dot] com.
