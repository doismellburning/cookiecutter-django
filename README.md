# cookiecutter-django

There are many like it, but this one is mine.

## Why?

I want a templated Django setup that conforms to my idiosyncracies.

Naturally, everything I exclude from this is a pointless opinionated extra, and everything I include is of vital importance
(and for the avoidance of doubt, that's pure flippancy).

## Features

* Modern Django (Unless I missed a requires.io PR)
* My preferred "Django project as a subdirectory of the repository root" layout
* 100% test coverage
* Tox configuration
* Dependencies in `requirements.txt`
* Test dependencies in `requirements-test.txt`
* `Procfile` for Heroku
* [`django12factor`](https://django12factor.readthedocs.org/) to get configuration from the environment
* [`WhiteNoise`](http://whitenoise.evans.io/en/latest/) for serving static files
* ...and not much else!

## Usage

```
$ cookiecutter https://github.com/doismellburning/cookiecutter-django.git
```

See the [cookiecutter docs](https://cookiecutter.readthedocs.org/en/latest/) for more information.
