# django_transalate_example
In this article we are going to tell you about how to add internationalization and localization in Django project.
Internationalization

Refers to the process of designing programs for the potential use of any locale. This process is usually done by software developers. Internationalization includes marking text (such as UI elements and error messages) for future translation, abstracting the display of dates and times so that different local standards may be observed, providing support for differing time zones, and generally making sure that the code contains no assumptions about the location of its users. You’ll often see internationalization abbreviated I18N. (The 18 refers to the number of letters omitted between the initial I and the terminal N.)
Localization

Refers to the process of actually translating an internationalized program for use in a particular locale. This work is usually done by translators. You’ll sometimes see localization abbreviated as L10N.

Here are some other terms that will help us to handle a common language:

1. locale name

A locale name, either a language specification of the form ll or a combined language and country specification of the form ll_CC. Examples: it, de_AT, es, pt_BR. The language part is always in lower case and the country part in upper case. The separator is an underscore.

2. language code

Represents the name of a language. Browsers send the names of the languages they accept in the Accept-Language HTTP header using this format. Examples: it, de-at, es, pt-br. Language codes are generally represented in lower-case, but the HTTP Accept-Language header is case-insensitive. The separator is a dash.

3. message file

A message file is a plain-text file, representing a single language, that contains all available translation strings and how they should be represented in the given language. Message files have a .po file extension.

4. translation string

A literal that can be translated.

5. format file

A format file is a Python module that defines the data formats for a given locale.
Implementation steps
Configuring your Settings

Before we start translating the site, we need to tell Django to look for the user’s language preferences, which languages we support, what the default language is, and where it should look for the translation files we provide. All of this is done in our settings.py file.

from django.utils.translation import ugettext_lazy as _

# The LocaleMiddleware check's the incoming request for the 
# user's preferred language settings. Add the LocaleMiddleware
# after SessionMiddleware and CacheMiddleware, and before the 
# CommonMiddleware.

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # important
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

# Provide a lists of languages which your site supports.
LANGUAGES = [
    ('ar', _('Arabic')),
    ('en', _('English')),
]

# Set the default language for your site.
LANGUAGE_CODE = 'en-us'

# Tell Django where the project's translation files should be.
LOCALE_PATHS = [ os.path.join(BASE_DIR, 'locale') ]

Note that when LocaleMiddleware determines the language settings, a logged out user’s browser settings take priority, whereas a logged in user’s site language preferences take priority. For more information on how this works, see How Django Discover’s Language Preference.


Templates

At this point Django should be configured to determine the user’s language and look for translations. Let’s say we’re looking to translate a simple Log inpage with a template that looks like something like this:

<h1>Log in</h1><label>Username</label>
<input id='password' type='text'/><label>Password</label>
<input id='password' type='password'/>

Views

from django.shortcuts import render
# Create your views here.
from django.utils.translation import ugettext as _
from django.http import HttpResponse

def home(request):    
    output = _("Welcome to my site.")    
    return HttpResponse(output)

Django provides some template tags to translate your page. To give your template access to these tags, put {% load i18n %} at the top of the file. This needs to be added to every template that uses these tags, even if they extend a file that already has them.

There are two i18n template tags–trans and blocktrans–but I’ll just be discussing the trans tag in this tutorial. To translate a piece of text, we simple put that text inside quotes in the trans tag. Once we do this to all the text, our Login template will look like so:

# Loads the D
{% load i18n %}
<h1>{% trans 'Log in' %}</h1>
<label>{% trans 'Username' %}</label>
<input id='password' type='text'/>
<label>{% trans 'Password' %}</label>
<input id='password' type='password'/>

For information on the advanced features when translating templates, see the Internationalization: in template code article in the Django docs.
Making the Translation Files

Now that we’ve wrapped our text in `trans` tags, we’ll create the translation files. From the command-line in project directory, run the following command:

> python manage.py makemessages -l ar

This will find all the places in your project where translation might occur, and creates a .po file inside locale.

myproject/
    myproject/
    templates/
        login.html
    locale/
        ar/
            LOCALE_MESSAGES/
                django.mo

Take a look at the django.po

#: login.html:2
msgid "Log in"
msgstr ""#: login.html:4
msgid "Username"
msgstr ""#: login.html:7
msgid "Password"
msgstr ""

After you replace the msgstr with your translation, the file should look like this:

#: login.html:2
msgid "Log in"
msgstr "الدخول في"#: login.html:4
msgid "Username"
msgstr "اسم المستخد"#: login.html:7
msgid "Password"
msgstr "كلمه السر"
#: demotransalte/settings.py:112
msgid "Arabic"
msgstr "عربى"
#: demotransalte/settings.py:113
msgid "English"
msgstr "English"

#: home/views.py:7
msgid "Welcome to my site."
msgstr "مرحبا بكم في موقعي"

Note that if a msgstr is not provided for a language then the msgid will be used instead. Since we haven’t even provided a .mo file for english, the msgidwill be used instead.
Compile your Translations

The last thing we need to do in order for Django to translate your site, is compile the .po into .mo files. Once again open up the command-line in your directory, and run the following:

> python manage.py compilemessages

You should now see a .mo file alongside your .po file!

Add following snippets in the html or you can customise this as per your needs.

<form action="/i18n/setlang/" method="post">		
    {% csrf_token %}		
    <p>Select any language</p>		
    <input name="next" type="hidden" value="{% url 'demo' %}" />		<select name="language">		    
           {% for lang in LANGUAGES %}		    
              <option value="{{ lang.0 }}">{{ lang.1 }}</option>		   {% endfor %}		
        </select>		
    <input type="submit" value="Go" />	
</form>

Add following url into the urls.py

from django.conf.urls import url, include
url(r'^i18n/', include('django.conf.urls.i18n')),


Let do run and select your language and see the changes


project source code:

django_transaltion_test

mkvirtualenv test
clone the directory , 
https://github.com/Cadmus/django_transalate_example/tree/master
cd django_transalate
pip install -r requirements.txt
python manage.py runserver
