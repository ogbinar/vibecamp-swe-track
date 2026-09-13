from dataclasses import dataclass


@dataclass(frozen=True)
class Post:
    author: str
    text: str


class SocialGraph:
    """Correct small-data behavior; persistence and optimization are learner work."""

    def __init__(self) -> None:
        self.profiles: dict[str, str] = {}
        self.follows: set[tuple[str, str]] = set()
        self.posts: list[Post] = []

    def add_profile(self, user_id: str, name: str) -> None:
        self.profiles[user_id] = name

    def follow(self, follower: str, followed: str) -> None:
        if follower not in self.profiles or followed not in self.profiles:
            raise KeyError("both profiles must exist")
        self.follows.add((follower, followed))

    def publish(self, author: str, text: str) -> None:
        if author not in self.profiles:
            raise KeyError("author profile must exist")
        self.posts.append(Post(author, text))

    def feed_for(self, user_id: str) -> list[Post]:
        visible = {followed for follower, followed in self.follows if follower == user_id}
        return [post for post in self.posts if post.author in visible]


class CountingProfiles:
    def __init__(self, names: dict[str, str]) -> None:
        self.names = names
        self.calls = 0

    def name_for(self, author: str) -> str:
        self.calls += 1
        return self.names[author]


def render_feed(posts: list[Post], profiles: CountingProfiles) -> list[dict[str, str]]:
    return [{"author": profiles.name_for(post.author), "text": post.text} for post in posts]
