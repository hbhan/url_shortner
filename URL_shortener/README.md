An URL Shortener App
====================

Background
----------

* Uses a framework (knowledge of sockets)
* Process post requests.


Modules
-------

* url_shortener.py: This is the flask application.

1) First we create the a Flask application and import the methods we are going to use:

        - request:

        - render_template:

        - url_for:

        - redirect:


2) Created a hash table (dictionary) where we are going to keep all the urls


3) For our Flask application we have 4 methods:

    - homepage: where we call our index.html

    - display_new_url: where we hash our url, save into our dictionary and render the information in the webpage.

    - redirector: simply finds the right url by the key and redirect it.

    - error404: redirects in case the page does not exists.



* hash_function.py:  Here is where the hashing happens.

1) Uses MD5 hashing and we encode into 64bits.
2) Randomize our URL with a pseudo random function.
3) Sanitize the result to extract "=" and "/".


Running
-------

1) Run python url_shortener.py
2) Open your Browser at localhost:5000
3) Create your link!

