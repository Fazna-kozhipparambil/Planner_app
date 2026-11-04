# Family Planner App

A Streamlit prototype for organizing a family's day: tasks, reminders, chores, meals and sleep routine, with simple parent/child logins.

> **Status:** early prototype. See [Known Issues](#known-issues) and [Roadmap](#roadmap).

## Features

- **Login with roles:** separate accounts for parents (admin) and children (user)
- **Daily tasks:** enter a comma-separated list of the day's tasks
- **Reminders and chores:** comma-separated lists for each
- **Daily food menu:** breakfast, lunch and dinner
- **Sleep routine:** pick a sleep time and a wake time
- **Task assignment:** assign each task to a family member from a dropdown
- **Summary table:** the day's entries are shown in a Pandas table

## Tech Stack

- **Python 3.11**
- **Streamlit**: web interface
- **Pandas**: tabular summary
- **google-auth / google-auth-oauthlib**: included for planned Google sign-in (not used yet)

## Getting Started

### Run locally
```bash
git clone https://github.com/Fazna-kozhipparambil/Planner_app.git
cd Planner_app
pip install -r requirements.txt
streamlit run project__1_py.py
```
The app opens at `http://localhost:8501`.

### Run in GitHub Codespaces
The repo includes a dev container. Open it in a Codespace and the app installs its dependencies and starts automatically on port 8501.

## Project Structure

```
├── project__1_py.py   # Streamlit app
├── requirements.txt   # Dependencies
└── .devcontainer/     # Codespaces / VS Code dev container config
```

## Known Issues

- Login accounts are hardcoded demo users in the source code. Do not reuse these passwords or treat this as real authentication.
- Roles (`admin` / `user`) are defined but not enforced yet. Every logged-in user sees the same page.
- Entered data is not saved. It disappears when the page reloads.
- The summary table is not finished and can fail when the lists have different lengths.

## Roadmap

- [ ] Replace hardcoded logins with secure authentication (Google sign-in)
- [ ] Enforce parent/child permissions
- [ ] Save data to a database (SQLite or Supabase)
- [ ] Shared family calendar view
- [ ] Mobile-friendly layout and app-store packaging

## Author

**Fazna Kozhipparambil**
[GitHub](https://github.com/Fazna-kozhipparambil) · [LinkedIn](https://www.linkedin.com/in/fazna-kp/)
