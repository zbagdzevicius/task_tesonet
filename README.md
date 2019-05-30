# Word Search

Implement a CLI tool that finds top 5 matched words from a given text file.
Implement the American Soundex algorithm to match the words:
[Soundex - Wikipedia][wiki].

Sample file wiki_lt.txt:

    Lithuania (UK and US: Listeni/ˌlɪθuːˈeɪniə/,[11][12][13] Lithuanian: Lietuva
    [ljɪɛtʊˈvɐ]), officially the Republic of Lithuania (Lithuanian: Lietuvos
    Respublika), is a country in Northern Europe.[14] One of the three Baltic
    states, it is situated along the southeastern shore of the Baltic Sea, to the
    east of Sweden and Denmark. It is bordered by Latvia to the north, Belarus to
    the east and south, Poland to the south, and Kaliningrad Oblast (a Russian
    exclave) to the southwest. Lithuania has an estimated population of 2.9 million
    people as of 2015, and its capital and largest city is Vilnius. Lithuanians are
    a Baltic people. The official language, Lithuanian, along with Latvian, is one
    of only two living languages in the Baltic branch of the Indo-European language
    family.

Sample usage:

    $ ./find.py wiki_lt.txt lituania

Sample output:

    Lithuania
    Lithuanian
    Lietuva
    Listeni
    living

The exact results might be different because of different scoring, matching,
sorting algorithms, etc.

## Requirements

* Use Python 3.
* Use Version Control System (preferably `git`).
    * If you put the repository online (GitHub, GitLab, etc.), keep it private.
* It is highly encouraged to maintain a well formed version control history:
    * commit messages should be consistent and relevant to changes
      (see: [How to Write a Git Commit Message][commit_msg]);
    * commits should be atomic (see: [Atomic Commits][commit_atomic]).
* Every project should have a README.
    * A structured text format is preferred: Markdown, ReStructuredText, etc.
    * README should have a general description of a project, a list of package
      library, tools, requirements and instructions how to setup and run the 
      project. In general, README should eliminate the need to read the source 
      code in order to deploy or test it.
* Source code should be well formatted and consistent. There should be no dead
  code (code that is not used anywhere) and no commented code.
* The code should be commented where necessary. Formal documenting format
  is preferred. E.g. [Google Style Python Docstrings][google_docstrings].

## Optional, but Highly Advisable

* Handle errors, validate user input.
* Allow for the given text file might be larger than the RAM availabe,
  e.g. 4+ GB, etc.
* Parallelize code for faster performance.
* Cover the code with automated tests. Unit, functional, integration, etc.
  tests are all encouraged.

## Resources

* [PEP8](http://pep8.org/).
* [PEP257](https://www.python.org/dev/peps/pep-0257/).
* [pylint](https://www.pylint.org/),
  [flake8](http://flake8.pycqa.org/en/latest/) or any other tool to lint the code.
* Type hints: [PEP484](https://www.python.org/dev/peps/pep-0484/),
  [mypy](http://www.mypy-lang.org/).
* [py.test](https://docs.pytest.org/en/latest/).

[wiki]: <https://en.wikipedia.org/wiki/Soundex>
[commit_msg]: <http://chris.beams.io/posts/git-commit/>
[commit_atomic]: <http://www.freshconsulting.com/atomic-commits/>
[google_docstrings]: <http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>