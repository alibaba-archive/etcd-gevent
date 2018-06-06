#!/bin/bash
echo "[distutils]"                                  > ~/.pypirc
echo "index-servers ="                             >> ~/.pypirc
echo "    pypi"                                    >> ~/.pypirc
echo "[pypi]"                                      >> ~/.pypirc
echo "repository=https://upload.pypi.org/legacy/"  >> ~/.pypirc
echo "username=wenjun"                             >> ~/.pypirc
echo "password=$PWD"                               >> ~/.pypirc
python -m pip install twine
if [ "$TRAVIS_TAG" ]; then
  python -m twine upload -r pypi --skip-existing dist/*.tar.gz;
else
  echo "Not on a tag, won't deploy to pypi";
fi
