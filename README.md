URL shortener for Google App Engine

Simple GAE app that redirects custom key (or keyword) on custom 
domain to any url. Keys and URLs are stored in datastore and can be 
added and edited. Table and datastore management is accessible only 
to users from Google Apps domain, redirects are accessible to anyone.

Example:
Type http://go.tilenkranjc.com/gugl into your web browser and it will
redirect you to http://www.google.com. 

To-do:
1. Asynchronous editing of keys table
2. Nicer user interface
