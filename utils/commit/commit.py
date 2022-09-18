from dataclasses import dataclass


@dataclass
class Commit:
    repository_name: str = None
    branch_info: str = None
    commiter: str = None
    commit_message: str = None
