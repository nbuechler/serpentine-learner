# serpentine-learner
I wanted to create a python machine learning tensorflow project, so I started learning based on the tutorials located here: https://www.tensorflow.org/

# Lessons Learned (2015)
* I did a few tutorials for the MNIST data from here: https://www.tensorflow.org/
* I discovered I am missing quite a bit of the theoretical underpinning.
* Therefore, I think I need to study on my own before continuing.
* Meanwhile, I think I could work on make an ML script run
with an API call. I could add flask, but I'm not sure if this is the best approach.

# Getting Started
* First, install virtualenv if not done so already -- https://virtualenv.pypa.io/en/latest/installation.html(https://virtualenv.pypa.io/en/latest/installation.html)
* Then, run this command:
<pre>
  <code>
    $ virtualenv venv
  </code>
</pre>
* Next, activate the virtual environment (make sure you get the'.'):
<pre>
  <code>
    $ . venv/bin/activate
  </code>
</pre>
* Last, install the requirements with pip:
<pre>
  <code>
    $ pip install -r requirements.txt
  </code>
</pre>
* For installing TensorFlow, follow this link:
https://www.tensorflow.org/versions/master/get_started/os_setup.html#pip_install

# Install Instructions
(I had some difficulties on Ubuntu 14.04)

* Install pip (or pip3 for python3) if it is not already installed:
<pre>
  <code>
    sudo apt-get install python-pip python-dev
  </code>
</pre>

* Make sure apt-get and gcc are up to date:
<pre>
  <code>
    sudo apt-get update
    sudo apt-get upgrade gcc
  </code>
</pre>

* Then, install the python development tools:
<pre>
  <code>
    python2.7-dev
    sudo apt-get install python2.7-dev
  </code>
</pre>

* Make sure to run this command without the sudo for TensorFlow:
<pre>
  <code>
    pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.6.0-cp27-none-linux_x86_64.whl
  </code>
</pre>

# License
GPLv3
