# serpentine-learner
python machine learning tensorflow project

# Future Steps

So, I did a few tutorials for the MNIST data, but I found out that I am missing
quite a bit of the theoretical underpinning. Therefore, I think I need to study on my
own before continuing. Meanwhile, I think I could work on make an ML script run
with an API call. I could add flask, but I'm not sure if this is the best approach. 

# Steps


.. first, install virtualenv if not done so already -- https://virtualenv.pypa.io/en/latest/installation.html

.. then, run this command: $ virtualenv venv

.. next, activate virtualenv with this command (make sure you get the'.'): $ . venv/bin/activate

..For installing TensorFlow, follow this:

    https://www.tensorflow.org/versions/master/get_started/os_setup.html#pip_install

# (I had some difficulties on Ubuntu 14.04)
1. Install pip (or pip3 for python3) if it is not already installed:

sudo apt-get install python-pip python-dev

2. make sure apt-get and gcc are up to date:

sudo apt-get update
sudo apt-get upgrade gcc

3. then install the:

python2.7-dev

sudo apt-get install python2.7-dev

4. Make sure to run this command without the sudo for TensorFlow: pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.6.0-cp27-none-linux_x86_64.whl
