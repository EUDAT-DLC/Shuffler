# Shuffler
A simple web service that shuffles words in a text.

# How to use

Clone this repository then start the service:

````
git clone https://github.com/EUDAT-DLC/Shuffler.git
cd Shuffler
python main.py
````

You can test that the service is up and running via your favourite browser. The URL is [http://localhost:5000](http://localhost:5000).

To use the web service, post a multipart encoded file to the same URL:

````
$ curl -X POST -F file=@test.txt http://localhost:5000
````
