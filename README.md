Bring back real collaboration between students ! Once more !

#Development notes
## Installation

	virtualenv --distribute --no-site-packages ve
	source ve/bin/activate
	pip install -r requirements.txt
	chmod +x ./manage.py

## Run in development

	./quicktest.sh

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
	
	GET /graph/{nodeid}

This will return something like this (Could have much more optional fields):
	
	{
        'id' : int, 
        'name' : str, 
        'type' : str, 
        'children' : list[{'id':int, 'name':str, 'type':str}, ...], 
        ... 
    }

### Retrieve only basical informations
	
	GET /graph/{nodeid}/short

Will return 
	
	{'id':int, 'name':string, 'type':string}