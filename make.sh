#!/bin/sh
VER=`grep "__version__ = " perftracker_cp_crawler/__init__.py | cut -d "\"" -f 2`

echo "\n###### run the following commands manually ######\n"
echo "vim perftracker_cp_crawler/__init__.py  # update version"
echo "vim perftracker-cp-crawler.spec  # update version"
echo "git commit -m \"bump version to $VER\" perftracker_cp_crawler/__init__.py perftracker-cp-crawler.spec && git tag \"v$VER\" && git push origin --tags"
echo python3 setup.py sdist bdist_wheel
echo twine upload dist/perftracker-cp-crawler-$VER.tar.gz
echo git push
echo
