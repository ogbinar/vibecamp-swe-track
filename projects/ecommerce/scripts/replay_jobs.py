"""Safe CLI contract for M7 replay; storage implementation remains learner work."""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--actor", required=True)
parser.add_argument("--reason", required=True)
parser.add_argument("--message-id", action="append", required=True)
parser.add_argument("--confirm", action="store_true")
args = parser.parse_args()

print(
    {
        "actor": args.actor,
        "reason": args.reason,
        "message_ids": args.message_id,
        "preview": not args.confirm,
    }
)
if args.confirm:
    raise SystemExit(
        "Durable replay is learner work; connect this CLI only after M7 storage tests pass"
    )
