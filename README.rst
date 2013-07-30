===============================
django-staticfiles-precompilers
===============================

Simply put, this overrides the ``static`` templatetag in ``django.contrib.staticfiles`` to allow it to transparently precompile the likes of scss, sass, less and so on.

So this::

  {% load staticfiles %}
  
  <link rel="stylesheet" href="{% static 'foo/bar.scss' %}" />

Gets rendered as this (assuming Django's ``STATIC_URL`` is ``/static/``)::

  <link rel="stylesheet" href="/static/foo/bar.css" />
  
  
Without this library you'd simply get this::

  <link rel="stylesheet" href="/static/foo/bar.scss" />
  

************
Installation
************

You can install it from PyPI::

  pip install django-staticfiles-precompilers
  
  
*****
Usage
*****

Simply add ``staticfiles_precompilers`` to ``INSTALLED_APPS`` in your Django settings. It **must come before django.contrib.staticfiles**, this is because it intercepts the search for the staticfiles template library and uses its own one instead.

Now you'll want to configure ``STATICFILES_PRECOMPILERS``, the default is currently this::

  STATICFILES_PRECOMPILERS = {
      '.scss': ('scss {infile} {outfile}', '{file_name}.css'),
      '.handlebars': ('handlebars {infile} -f {outfile}', '{file_name}.handlebars.js'),
  }

**This will likely change as I refine the API for defining precompilers**. The library won't check whether you have the necessary binaries to execute the compilation, in the example above we're depending on the scss and handlebars binaries.

The config for each precompiler currently takes the form of a tuple. The first value is the terminal command to execute, the second value lets you decide what form the output filename should take.  ``{file_name}`` is replaced with the path of the original file with the file extension removed.

And that's it for now. It plays nicely with ``./manage.py collectstatic`` and django-compressor. If you're using this with django-compressor you won't need to configure compressor's own precompilers, as this effectively removes the need for it.
  

************
How it works
************

When the ``static`` tag is rendered, we fetch the original file (assuming it exists) and see if its extension matches one of the keys in ``STATICFILES_PRECOMPILERS``. If it does we use the precompiler configuration to generate the compiled file and return the URL to that file instead of the original.
