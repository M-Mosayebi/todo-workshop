# Changelog

All notable changes to this project are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/) and
commit messages follow [Conventional Commits](https://www.conventionalcommits.org/).

## [0.1.0] - 2026-10-31

### Added
- `complete_task(index)` to mark a task as done (#1)
- `delete_task(index)` to remove a task from the list (#2)

### Changed
- Fixed indentation of `complete_task` to follow PEP 8 (#1)

### Known issues
- No input validation: `complete_task(0)` marks the last task, and
  out-of-range indexes raise `IndexError`.
- No automated tests yet.
