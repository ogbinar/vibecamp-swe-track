from social_lab.feed import CountingProfiles, Post, SocialGraph, render_feed


def test_small_feed_is_correct() -> None:
    profiles = CountingProfiles({"a": "Ada", "g": "Grace"})
    result = render_feed([Post("a", "Hello"), Post("g", "Compiler")], profiles)
    assert result == [
        {"author": "Ada", "text": "Hello"},
        {"author": "Grace", "text": "Compiler"},
    ]


def test_small_social_graph_filters_followed_authors() -> None:
    graph = SocialGraph()
    for user in ("reader", "ada", "grace"):
        graph.add_profile(user, user.title())
    graph.follow("reader", "ada")
    graph.publish("ada", "Visible")
    graph.publish("grace", "Hidden")
    assert graph.feed_for("reader") == [Post("ada", "Visible")]


def test_query_workload_has_stable_seeded_shape() -> None:
    profiles = CountingProfiles({f"u{i}": f"User {i}" for i in range(10)})
    posts = [Post("u0", str(i)) for i in range(100)]
    render_feed(posts, profiles)
    assert profiles.calls == 100
