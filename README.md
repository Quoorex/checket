# Checket

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields)](http://makeapullrequest.com)

**Checket** bulk checks domains for their availability.
This comes in handy when looking for the domain for your next project.

Checket makes use of WHOIS queries in the background.
This approach produces much more accurate results than other programs
which use third-party services or even DNS queries.

# Table of contents

- [Usage](#usage)
- [Installation](#installation)
- [License](#license)

# Usage

[(Back to top)](#table-of-contents)

There are three text files which are used for the program's input:

- [domains.txt](domains.txt)

  - `google.com`, `github.com`, ...
  - one domain per line

- [keywords.txt](keywords.txt)

  - `github`, `mynewdomainname`, ...
  - do not put a `.` at the end

- [tlds.txt](tlds.txt)

  - `com`, `net`, ...
  - do not put a `.` in front

The contents of the last two files are used to generate all possible combinations of domains and tlds.
For this to work, neither the contents of `keywords.txt` nor `tlds.txt` can be empty.

All that's left for you to do is to run the program:

```
python checket.py
```

## Additional Notes

WHOIS queries are rate limited,
but the limits are different for every top-level domain and their corresponding WHOIS servers.
While testing the program, I didn't encounter any rate limits,
but keep in mind that it can happen.

# Installation

[(Back to top)](#table-of-contents)

- Install [Python](https://python.org)
- Install Poetry

```
pip install poetry
```

- Navigate to the folder containing this repository's files
  - If you're unsure how to do this, look up `cd` and the name of your operating system online

- Set up the dependencies

```
poetry install
```

- Activate the virtual environment

```
poetry shell
```

Note that the program does not run if the virtual environment is not active.
In that case you just have to run the last command again.

# License

[(Back to top)](#table-of-contents)

Please have a look at the [LICENSE](LICENSE) for more details.
