from distutils.core import setup
import challonge


setup(name = "pychallonge",
      author = "Russ Amos",
      url = "http://github.com/russ-/pychallonge",
      version = challonge.__version__,
      packages = [
          'challonge',
      ],
      requires = [
          'python-dateutil<2.0',
      ]
)
