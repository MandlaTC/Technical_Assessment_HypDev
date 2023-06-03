# Technical_Assessment_HypDev

# Magic Squares 
This Magic Square function is a simple Python function that generates a magic square of a specified size. A magic square is a square grid filled with distinct positive integers, where the sums of the numbers in each row, each column, and diagonals are equal.

# Demo App
Chess Game visualiser. This app stores .pgn files of chess grandmasters in dropbox using the Dropbox API and allows you to see their latest games visualised with SVGs amd the chess library.

## TODO 
- Allow searching of games 
- Stylising the site 
- Run games through chess engine for analysis
- Deletion of .pgn files 

Installation

To install and run the Chess App locally, follow these steps:

- Clone the repository from GitHub:

```shell

$ git clone https://github.com/your-username/chess-app.git
```

- Navigate to the project directory:



```shell

$ cd chess-app
```

- Set up a virtual environment (optional but recommended):

```shell

$ python3 -m venv venv
$ source venv/bin/activate
```
- Install the required dependencies:
```shell
$ pip install -r requirements.txt
```
- Set up a Dropbox app and obtain an access token:
- - Create a new app on the Dropbox App Console.
- -  Generate an access token for your app.

- Configure the app:
```
DROPBOX_KEY="******"
UPLOAD_FOLDER = './temp'
DELETE_FOLDER = '/temp'
ALLOWED_EXTENSIONS = {'pgn'}
```

Start the application:

```shell

$ flask run
```
    Open your web browser and visit http://localhost:5000 to access the Chess App.

### Technologues Used 
The Chess App is built using the following technologies:

    Python: The programming language used to develop the application.
    Flask: A lightweight web framework used to create the web interface.
    chess: A Python chess library that provides the core chess functionality.
    Dropbox API: Used to store and retrieve games in .pgn format securely.

### License

This Chess App is released under the MIT License.

### Acknowledgements 

The Chess App was inspired by the love for chess and the desire to create an accessible and enjoyable way to play and record games. Special thanks to the developers of Flask, chess library, and the Dropbox API for their excellent tools and documentation.


## Tell us what you consider important in software development.


Write three or four paragraphs about how you would develop a good web API. Talk about the process you would follow from idea to release, the tools you would use, and the problems you would need to solve. You could talk about scalability, authorization, design, discoverability, and/or anything you think is important.

First and foremost I would look at what the use case of this API is and start settining out a list of required functionality of the API. It is very easy to loose track of what it is you have set out to build without documenting it early in the 
development process. Documenting your functional requirements also prevents scope creep which can hinder your ability to deliver results in a timeous fashion. 

Secondly I would then start to design the system. You would need to take into account cost of deployment, systems you will integrate with, and the skillset of the dev team to decided on technologies and different design paradigms. 

Finally I would start to build out the system, writing tests as you move to ensure that all parts of the API are functioning as expected. This will then be followed by integration tests, a period of time as a beta before releasing to production. 

Most importantly, through out this whole process it is imperative to document your API. It improves the overall useability of the API as well as makes it easy for team members to pick up tasks on what you're developing. 