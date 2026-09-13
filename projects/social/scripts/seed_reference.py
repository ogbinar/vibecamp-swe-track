"""Create deterministic lab-only rows without designing learner domain tables."""

from sqlalchemy import create_engine, text

from social_api.settings import Settings

REFERENCE = {"posts": 100, "high_fan_out_posts": 70, "other_authors": 9}


def seed() -> None:
    engine = create_engine(Settings(service_name="reference seed").database_url)
    with engine.begin() as connection:
        connection.execute(
            text(
                "CREATE TABLE IF NOT EXISTS lab_profiles "
                "(id integer PRIMARY KEY, name text NOT NULL)"
            )
        )
        connection.execute(
            text(
                "CREATE TABLE IF NOT EXISTS lab_posts "
                "(id integer PRIMARY KEY, author_id integer NOT NULL, body text NOT NULL)"
            )
        )
        connection.execute(text("TRUNCATE lab_posts, lab_profiles"))
        connection.execute(
            text(
                "INSERT INTO lab_profiles (id, name) "
                "SELECT value, 'User ' || value FROM generate_series(0, 9) AS value"
            )
        )
        connection.execute(
            text(
                "INSERT INTO lab_posts (id, author_id, body) "
                "SELECT value, CASE WHEN value < 70 THEN 0 "
                "ELSE 1 + ((value - 70) % 9) END, 'Post ' || value "
                "FROM generate_series(0, 99) AS value"
            )
        )
    print(REFERENCE)


if __name__ == "__main__":
    seed()
