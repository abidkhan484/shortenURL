# shortenURL
There's a demo youtube link <a href="https://www.youtube.com/watch?v=Mv7iC2ppCnU">here</a>.

Tested in Linux based OS. After pulling from the repository. Go to the project root directory.

## Run the app using command line
### Prerequisites
<ul>
  <li>Python3</li>
  <li>Pip3</li>
  <li>python3-flask</li>
</ul>

### Create and activate Virtual Enviornment with Python3
```
$ python3 -m venv venv
```
```
$ source venv/bin/activate
```

### Install the requirements
```
$ pip3 install -r requirements.txt
```

### Set these Environment Variables
```
$ export FLASK_APP=shortenURL
```
```
$ export FLASK_ENV=development
```

### Finally, run the below command
```
$ flask run
```

## Dockerize the App
### Prerequisites
<ul>
  <li>Docker</li>
</ul>

### Build and run the Dockerfile
Build the Dockerfile with the build command
```
docker build -t <container-name> .
```
Run the container with the run command and open the port for the web server
```
docker run -p 5000:5000 <container-name>
```
There's only two different routes except the homepage. they are /all and /delete
Try to explore what the routes return.
