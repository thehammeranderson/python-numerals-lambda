# Roman Numerals Converter

This is a python based Roman Numerals converter.  Given a Roman Numeral string (XIV) as a parameter, the converter will return the integer value.

Here are some of the main features:
* Roman Numeral format validation with tips on why it is wrong

## Getting Started

* Download and install Git
  * See https://git-scm.com/book/en/v2/Getting-Started-Installing-Git for more information
* Open a terminal/console and navigate to the directory you wish to clone the repository to
* At the command line type the following
```
git clone https://github.com/thehammeranderson/python-numerals-lambda.git
```

See deployment for notes on how to deploy the project on a live system.

### Prerequisites to build and run

* Python3 - see https://realpython.com/installing-python/ for download and install instructions

## Running the tests

If your environment is properly setup with Python, you can open up a shell/console/terminal window.  Change directory to the python-numerals-lambda folder.  If you are in the right folder, you will see a test.py file.  Now you can type the following from the command line and press <return> to run the Unit Tests:

```
python3 test_main.py
```

Optionally you may use pytest for better test output, run:
```
pip3 install -U pytest
pytest
```

### Break down of tests

Unit tests are in test.py.  Listed below are more details on the tests performed.

* TestValidation.test_invalid_numeral
    * test that invalid numeral characters are caught in the validation function
* TestValidation.test_invalid_sequence
    * test that invalid sequences of valid numeral characters are caught in the validation function
* TestValidation.test_single_numeral
    * test that the single character numerals return the proper value
* TestValidation.test_subtraction
    * test numeral subtraction scenarios
* TestValidation.test_addition
    * test numeral addition scenario

## Deployment

Prerequisites for deploying as a Lambda to AWS:
* NPM - see https://www.npmjs.com/get-npm
* AWS CDK
    * npm install -g aws-cdk
        * pip install --upgrade aws-cdk.cdk (run this if you get a language framework out of date error message)
    * see https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html for more information and troubleshooting
* pip3 install -r requirements.txt 

## Built With

* [NPM](https://www.python.org/) - Dependency Management
* [JUnit](https://junit.org/junit5/) - Used for unit testing
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html) - Used if deploying as a Lambda service

## Future improvements

* 
