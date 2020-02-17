# shortenURL
There's a demo youtube link <a href="https://www.youtube.com/watch?v=Mv7iC2ppCnU">here</a>.

<div>Tested in Linux based OS. After pulling from the repository. Go to the project root directory.</div>

### Prerequisites
<ul>
  <li>Python3</li>
  <li>Pip3</li>
  <li>python3-flask</li>
</ul>

### Create and activate Virtual Enviornment with Python3
<div><code>$ python3 -m venv venv</code></div>
<div><code>$ source venv/bin/activate</code></div>

### Install the requirements
<div><code>$ pip3 install -r requirements.txt</code></div>

### Set these Environment Variables
<div><code>$ export FLASK_APP=shortenURL</code></div>
<div><code>$ export FLASK_ENV=development</code></div>

### Finally, run the below command
<div><code>$ flask run</code><div>
  </br></br>
<div>There's only two different routes except the homepage. they are /all and /delete
Try to explore what the routes return.</div>
