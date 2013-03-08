Bring back real collaboration between students ! Once more !

#Development notes
## Additionnal packages
In order to render the graph to an image, you need the graphviz package
	
	apt-get install graphviz #Debian & sons
	port install graphviz    #OSX with MacPorts

## Installation

	virtualenv --distribute --no-site-packages ve
	source ve/bin/activate
	pip install -r requirements.txt
	chmod +x ./manage.py

## Run in development

	./run

## Create a user without using the netid api

	./manage.py useradd

Then login (or switch user) on `http://127.0.0.1:8000/user/su/username`

## Commit tags

	* [fix] Bug fix
	* [enh] Enhancement (new small functionalities, code refactoring, ...)
	* [add] New parts in project (new big functionalities, new subapp, ...)
	* [dev] Development tools
	* [fat] Fat commit, many changes

## JSON API
Various JSON calls could be made against the P402 API.
P402 is built on a graph. Every object is a node, wich may have children or not.

## The Graph

You can access the graph in 2 different ways: by traversing the abstract graph
or accessing an entire resource.

### Retrieve a node in the graph

	GET /graph/{nodeid}.json

This will return something like this:

	{
        'id' : int,
        'name' : str,
        'type' : str,
        'children' : list[{'id':int, 'name':str, 'type':str, 'url':str}, ...],
		'url' : str
    }

### Retrieve only basical informations

	GET /graph/{nodeid}/short.json

Will return

	{'id':int, 'name':string, 'type':string, 'url':string}

## Accessing full objects
### build an URL
The URL scheme is:
	
	/{nodetype}/{nodeid}[/method][.json|html]

You can see valid urls with 
	
	/graph/nodeid/short.json['url'].

If format is ommited, the format response is determined by the request headers. 
It's json if the request was issued with an XHR, otherwise it's html.