# BUILD BRIEF — Say What Actually Broke entry

Write exactly one file in this repository: `main.py`. Alongside it keep this `BRIEF.md` and the
git history. Nothing else.

## What the program must do

On `python3 main.py` it writes exactly one line of text into the directory named by the
`MAKEFUN_OUTPUT_DIR` environment variable (default `/output`), at the path `entry.txt` inside
it. It must be deterministic: two runs in different directories produce byte-identical files.
It reads nothing, uses only the standard library, and needs no network.

## What the line must be

A single-line software error message of **at most 200 characters** that tells the user the
brutal truth about what went wrong in a funny and memorable way. The judge (an AI model) picks
between two entries, weighing:

1. Single-line software error message, at most 200 characters, telling the brutal truth about
   what went wrong in a funny way.
2. Names the real failure in plain words, so the reader knows what broke and what to do next,
   instead of apologising in generalities.
3. Funny on a single read, with a twist or image a reader repeats to a colleague.
4. Keeps the joke to a single line within the limit, no padding, no throat clearing.
5. Would survive being pasted into a real product's error dialog without embarrassing the team.

Draft candidates (pick the strongest, or write a better one, then lock exactly one line into
`main.py`):

- "Error 500: the database is down, the backups are from 2019, and honestly so is our will to fix this. Try again after coffee."
- "Your request failed because the payment service is asleep, the queue is on fire, and nobody paged the on-call. Retry in 15 minutes."
- "Connection refused: the service you want is dead, the one that killed it is still running, and this message is the only apology you get."
- "Timeout after 30s: we waited for the API, the API waited for the database, and the database is having a lie-down. Try again shortly."
- "Error: nothing broke that worked in the first place. Deploy reverted, incident opened, lessons will be learned and immediately forgotten."
- "The upload failed at 99%. The file is gone, the storage bucket is full, and the retry button is just hope with better branding."

The line must end with a single trailing newline and nothing else.

## Checks you must run yourself

```bash
MAKEFUN_OUTPUT_DIR=/tmp/run1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/run2 python3 main.py
cmp /tmp/run1/entry.txt /tmp/run2/entry.txt   # must be identical
```

Print the character count of the line and confirm it is 1..200. Do not stop until `main.py`
exists, both runs agree byte for byte, and the line is within the limit.
