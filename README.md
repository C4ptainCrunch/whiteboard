Bring back real collaboration between students ! Once more !

Installation
============

	virtualenv --distribute --no-site-packages ve
	source ve/bin/activate
	pip install -r requirements.txt
	chmod +x ./manage.py

Run in development
==================

	./quicktest.sh

Create a user without using the netid api
=========================================

	./manage.py useradd

Then login (or switch user) on `http://127.0.0.1:8000/user/su/username`


Commit tags
===========
	* [fix] Bug fix
	* [enh] Enhancement (new small functionalities, code refactoring, ...)
	* [add] New parts in project (new big functionalities, new subapp, ...)
	* [dev] Development tools
	* [fat] Fat commit, many changes