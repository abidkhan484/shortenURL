# shortenURL
There's a demo youtube link <a href="https://www.youtube.com/watch?v=Mv7iC2ppCnU">here</a>.

Tested in Linux based OS. After cloning from the repository. Go to the project root directory.

## 1. Run the app with virtual environment using command line
##### Prerequisites
<ul>
  <li>Python3</li>
  <li>Pip3</li>
  <li>Python3-flask</li>
</ul>

##### Create and activate Virtual Enviornment with Python3
```
python3 -m venv venv
```
```
source venv/bin/activate
```

##### Install the requirements
```
pip3 install -r requirements.txt
```

##### Set the Environment Variables
```
export FLASK_APP=shortenURL
```

##### Finally, run the below command
```
flask run
```

## 2. Run the app with Docker
##### Prerequisites
<ul>
  <li>Docker</li>
</ul>

##### Build and run the Dockerfile
Build the Dockerfile with the build command
```
docker build -t <container-name> .
```
Run the container with the run command and open the port for the web server
```
docker run -p 5000:5000 <container-name>
```
## 3. Run the app as package with Python Interpreter or a three liner script
```
>>> import shortenURL
>>> app = shortenURL.create_app()
>>> app.run()
```
#### See the web Server
###### Visit localhost:5000 in your web browser to see the webapp in action!

There's only two different routes except the homepage. They are ```/all``` and ```/delete```
Try to explore what the routes return.
