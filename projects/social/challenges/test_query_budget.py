from social_lab.feed import CountingProfiles, render_feed
from social_lab.seed import representative_posts


def test_feed_profile_reads_do_not_grow_per_post() -> None:
    profiles = CountingProfiles({f"u{i}": f"User {i}" for i in range(10)})
    posts = representative_posts()
    assert len(render_feed(posts, profiles)) == 100
    assert profiles.calls <= 2
