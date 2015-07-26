# cookiecutter-django

There are many like it, but this one is mine.

## Why?

I want a templated Django setup that conforms to my idiosyncracies.

Naturally, everything I exclude from this is a pointless opinionated extra, and everything I include is of vital importance
(and for the avoidance of doubt, that's pure flippancy).

## Features

* Django 1.8
* My preferred "Django project as a subdirectory of the repository root" layout
* 100% test coverage
* Tox configuration
* Dependencies in `requirements.txt`
* Test dependencies in `requirements-test.txt`
* `Procfile` for Heroku
* [`django12factor`](https://django12factor.readthedocs.org/) to get configuration from the environment
* ...and not much else!

## Usage

```
$ cookiecutter https://github.com/doismellburning/cookiecutter-django.git
```

See the [cookiecutter docs](https://cookiecutter.readthedocs.org/en/latest/) for more information.
