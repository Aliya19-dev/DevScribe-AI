from dataclasses import dataclass
from datetime import datetime


@dataclass
class PullRequest:
    pr_id: int
    title: str
    author: str
    repository: str
    changed_files: dict
    created_at: str


def create_sample_pr():
    return PullRequest(
        pr_id=142,
        title="Add Redis caching to AuthenticationService",
        author="developer",
        repository="example/backend",
        changed_files={
            "auth_service.py": """
class AuthenticationService:

    def login(self, username, password):
        user = self.repository.find_user(username)

        if user and self.verify_password(password, user.password):
            return self.create_session(user)

        return None

    def get_user_profile(self, user_id):
        return self.repository.find_user(user_id)
""",

            "redis_cache.py": """
class RedisCache:

    def get(self, key):
        return redis_client.get(key)

    def set(self, key, value, ttl=300):
        redis_client.setex(key, ttl, value)
""",

            "tests/test_auth.py": """
def test_login():
    service = AuthenticationService()
    result = service.login("alice", "password")
    assert result is not None
""",

            "package-lock.json": """
{
    "name": "example",
    "lockfileVersion": 3
}
"""
        },
        created_at=datetime.utcnow().isoformat()
    )


if __name__ == "__main__":
    pr = create_sample_pr()

    print("=" * 60)
    print("DEVSCRIBE AI — GITHUB PR SIMULATOR")
    print("=" * 60)

    print(f"PR #{pr.pr_id}")
    print(f"Title: {pr.title}")
    print(f"Author: {pr.author}")
    print(f"Repository: {pr.repository}")

    print("\nChanged files:")

    for filename in pr.changed_files:
        print(f"  - {filename}")
