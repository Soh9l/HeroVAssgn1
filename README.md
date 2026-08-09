# Flask Voting & User Management with Git Versioning Workflow


A lightweight RESTful web application built using Python and Flask that allows users to cast and tally votes dynamically while managing simple user profile records. Designed as a straightforward backend system to demonstrate HTTP routing, request handling, and in-memory state management.

---

## Installation and Setup Steps

Follow these step-by-step instructions to clone, configure, and run the application locally on your machine.

### Prerequisites
* Basic Python programming (functions, dictionaries, return statements)
* Installing and running Python files from the terminal
* Creating and managing Git branches
* Basic Git commands (clone, add, commit, push)
* What a GitHub repository is and how to create one

### Tools Required
* Python 3.x
* Flask
* Git
* GitHub account
* Code editor (VS Code recommended)

### API Endpoint Reference
| Endpoint | Method | Description | Example Response |
| :--- | :---: | :--- | :--- |
| `/` | `GET` | Returns a welcome message. | `"Welcome to the App Use the url to register your vote by entering the url as /vote/'type in your name'"` |
| `/health` | `GET` | Health check route to verify server status. | `"App is running"` |
| `/vote/<Name>` | `POST` | Casts a vote or increments count for a person. | `"Vote registered"` |
| `/results` | `GET` | Retrieves all current voting results. | `[{"person": "Alice", "Vote": 1}]` |
| `/add` | `POST` | Registers a new user profile. | `{"msg": "Profile Added"}` |
| `/get/<username>` | `GET` | Fetches password for a given user. | `{"Password": "123"}` |
| `/add/reset` | `DELETE` | Clears all registered votes. | `"Votes are all cleared"` |
| `/add/delete/<username>` | `DELETE` | Deletes a user profile by username. | `"User Alice deleted successfully"` |

### Git Workflow

1. main Branch: Stored production-ready code. Official releases (Version 1 and Version 2) were tagged and merged here.

2. dev Branch: Served as the active development integration branch. All code changes, endpoint refactoring, and bug fixes were committed to dev first.

3. Merging: Once features were tested on dev, a Pull Request was created to merge dev back into main.
