set HOME=C:\Users\Dubya
python setup.py build
python setup.py sdist upload -r pypi
python setup.py bdist_wheel upload -r pypi
