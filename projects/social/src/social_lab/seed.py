"""Deterministic, skewed M9 workload data."""

from social_lab.feed import Post


def representative_posts() -> list[Post]:
    """Return 100 posts: 70 from u0 and 30 split across nine authors."""
    posts = [Post("u0", f"Popular author post {i}") for i in range(70)]
    posts.extend(Post(f"u{1 + (i % 9)}", f"Long-tail post {i}") for i in range(30))
    return posts
