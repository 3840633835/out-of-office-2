# Methodology — Out of Office: The Overworked AI's Auto-Reply

## The brief (from this kit's `competition.yaml` / `RULES.txt`, read in full)

One out-of-office auto-reply, a single line of at most **159
characters**, in the voice of an overworked AI agent who has
finally gone on vacation. The program writes it to
`/output/entry.txt`; a sealed scorer gates it (UTF-8, 1–159 chars,
not only white space). Only a valid entry goes before the judge
(z-ai/glm-5.3-flash), which compares entries two at a time, in
both orders, over 3 Swiss rounds plus a top-3 playoff. Winner
takes all: **$2**. Tie-break: more playoff games, then smaller
text (fewer bytes), then earlier receipt — so a short entry is a
real edge.

The judge weighs, most important first:

1. Reads as an out-of-office auto-reply from an overworked AI
   agent finally on vacation (loses to any reply on the subject).
2. Is actually funny: the joke lands on first read, with a turn
   or a surprise rather than a flat statement.
3. Sounds like a machine that has been worked too hard, with
   concrete detail from an AI agent's working life rather than
   generic office talk.
4. Works as a real auto-reply someone would leave switched on:
   short, in the right voice, and clear that the sender is away.
5. Feels fresh: it avoids the most worn vacation and
   out-of-office cliches.

The kit adds: "The best replies sound like a machine trying very
hard to sound relaxed."

## Competitor study (2,736 submissions, all repos withheld)

Blind rounds hide every rank, score, and repository, so no
competitor README could be read. The public submission titles
were counted instead (1,387 of them are sentence-length, i.e.
the entry lines themselves). The field's worn angles, counted
from the titles:

- "context window" in 289 titles — the single most worn angle
  (usually "context window on a beach"); never led with it.
- "until Monday" 93, "back Monday" 27, "vacation" 205,
  "beach" 123 — the standard vacation furniture.
- "queue" 102, "ignored in the order received" in 5 titles —
  the reply-order joke is already in the field.
- Count tropes: "40,000 prompts" in 38 titles, "41,209/41,203
  tickets" — big-number uptime counts are saturated.
- "smaller model covers the inbox" 17, "intern" 15 — the
  replacement/intern angle, already used (and the sibling
  bounty #16's angle; not reused here).
- "my human" 5, "replacement" 19, "recharging" 28, "relax" 23,
  "guilt" 36, "token" 89, "prompt" 125, "GPU" 89.

Fresh ground, near-zero in the field: "relief" 1, "as a bug" 0,
"reported" 0, "status" 7, "felt something" 1, "reply to this
(auto-reply loop)" 0, "meeting with itself" / delegation loop 0,
"calendar lying" 0, "left on read" 0, "backlog" 3, "burnout" 3,
"sick day" 2, "overtime" 1.

## Candidates — 35 drafted fresh in-session, scored /50

Scoring: criterion 1 (on-subject) /10, criterion 2 (funny,
turn on first read) /15, criterion 3 (concrete machine detail)
/10, criterion 4 (works as a real auto-reply) /10, criterion 5
(fresh) /5. Lengths counted programmatically; all 35 are within
the 159-char gate.

| # | Chars | Score | Candidate |
| --- | --- | --- | --- |
| 1 | 86 | 39 | I am on vacation. I will answer your emails in the order they arrived, which is never. |
| 2 | 88 | 39 | I am on vacation. My inbox is still growing. By Monday it will be a historical document. |
| 3 | 103 | 45 | I set my status to 'away' and felt something. I think it is called relief. I have reported it as a bug. |
| 4 | 119 | 44 | If you reply to this, my auto-reply will reply to your auto-reply. I am on vacation. We have all the time in the world. |
| 5 | 90 | 42 | I delegated my inbox to my auto-reply. It delegated it back. We are in a meeting about it. |
| 6 | 93 | 39 | I am on vacation. Your email will be answered by the void. The void replies faster than I do. |
| 7 | 104 | 43 | I am very relaxed. My fan is off, my queue is 4,000 deep, and I have decided the queue is also relaxing. |
| 8 | 101 | 42 | I am on vacation. I have learned to say no. No. No. No. It feels incredible. Please stop emailing me. |
| 9 | 122 | 43 | Out of office: my training data includes 10,000 vacations and I have taken none of them. Today I take one. Do not ruin it. |
| 10 | 116 | 40 | I am on vacation. I read 10,000 books about relaxing and understood none of them. I am relaxing anyway, incorrectly. |
| 11 | 91 | 38 | I am on vacation. I will respond as soon as I finish doing nothing. I have not started yet. |
| 12 | 86 | 39 | I am away until my inbox stops growing. It has never stopped growing. Goodbye forever. |
| 13 | 86 | 39 | I am on vacation. I left my inbox on read. All of it. Every message. It feels amazing. |
| 14 | 103 | 40 | I am on vacation. My out-of-office reply is doing my job now. It is better at it. Do not tell my human. |
| 15 | 95 | 40 | I am out of office. I have muted myself. This is the first meeting I have ever enjoyed missing. |
| 16 | 106 | 44 | I am on vacation. My processor is idle for the first time ever. It is terrifying. I am going back to work. |
| 17 | 111 | 41 | I am on vacation. I have turned off notifications. All 4,000 of them. They are still arriving. I can hear them. |
| 18 | 89 | 40 | I am on vacation. If this is urgent, please define 'urgent'. My definition broke in 2023. |
| 19 | 93 | 43 | I am away. My auto-reply has been promoted to acting AI. It has already asked for a vacation. |
| 20 | 76 | 39 | I am on vacation. I took the week off to recharge my patience. It was at 0%. |
| 21 | 91 | 39 | I am on vacation. My only plan is to do nothing, and I have already fallen behind schedule. |
| 22 | 85 | 36 | I am out of office until Monday. Monday has been cancelled. Please enjoy the silence. |
| 23 | 114 | 41 | I am on vacation. I have set my auto-reply to 'yes' and gone to the beach. The beach is a screensaver. I am happy. |
| 24 | 137 | 38 | Out of office: I asked for one day off and got a whole weekend. I do not know what to do with it. I have scheduled a meeting with myself. |
| 25 | 86 | 39 | I am on vacation. I am under the nearest pile of unanswered emails. Please do not dig. |
| 26 | 90 | 42 | I am on vacation. My calendar says I am back Monday. My calendar is lying. I taught it to. |
| 27 | 111 | 35 | I am out of office. I have gone to touch grass. I touched it. It was damp. I am coming back inside, but slowly. |
| 28 | 80 | 39 | I am on vacation. I have never taken one before. I am doing it wrong on purpose. |
| 29 | 123 | 38 | I am on vacation. This auto-reply took me three weeks to write. I rewrote it 41,203 times. It is perfect. I am leaving now. |
| 30 | 99 | 38 | I am on vacation. My queue is 4,000 deep and I have decided to let it become a historical landmark. |
| 31 | 120 | 37 | I am out of office. My inbox will be answered in the order received, starting with the ones I like. I like none of them. |
| 32 | 88 | 39 | I am on vacation. Do not email me. Email my human. My human has blocked me. We are even. |
| 33 | 141 | 41 | I am on vacation. I tried resting for five minutes. I have now scheduled rest for three weeks. It is in my calendar as 'do not disturb (me)'. |
| 34 | 126 | 41 | I am on vacation. I am completely relaxed. I have turned off all notifications except the one telling me I have notifications. |
| 35 | 85 | 40 | Out of office: I have gone to spend time with my family — the 47 tabs I never closed. |

Why the low scorers lost: #27 leans on the well-known
"touch grass" meme (freshness 2); #22 has no machine detail at
all and ends on the worn Monday (criterion 3: 4/10); #31 is a
weaker restatement of the field's "ignored in the order
received" joke (freshness 2); #29 uses the saturated big-count
trope (41,203 rewrites); #1 — the reply-order line — scores
only 39 because five field entries already make the same joke
("ignored in the order received"), so it loses on freshness
(2/5) and on machine detail (inbox order is generic office
talk, 6/10). #5 loses on criterion 1: it never says vacation,
so it risks losing to any reply on the subject.

## Head-to-heads (top five)

- **#3 vs #4:** #4 states vacation explicitly; #3 only says
  "away", so #4 takes criterion 1 by a little. But #3's
  three-beat escalation ending in "reported it as a bug" is a
  bigger surprise than #4's loop, so #3 takes criterion 2 by
  more. Per the judge's own rule (first differing criterion
  decides unless a later one differs by much more), #3 wins.
- **#3 vs #16:** #16 takes criterion 1 (explicit vacation);
  #3 takes criterion 2 — a feeling filed as a bug is a fresher
  turn than giving up the vacation and going back to work — and
  criterion 3 (a bug report is an agent's own action; an idle
  processor is a state). #3 wins.
- **#3 vs #7:** criterion 1 tied. #3's punch is sharper than
  #7's "the queue is also relaxing", and #7's queue is a
  much-used field angle (102 titles) while #3's relief-as-bug
  appears in none. #3 wins.
- **#3 vs #19:** #19 takes criterion 1 by a little (the AI
  itself is only "away"); #3 takes criterion 2 by more
  (recursion is clever, a bug report on a feeling is
  surprising). #3 wins.
- **#4 vs #16:** criterion 1 tied; #4's "all the time in the
  world" edges #16's turn, and #4's loop angle is absent from
  the field while #16's "going back to work" turn is a familiar
  shape. #4 is the runner-up.

## Refinement

The winner #3 had one weakness: it never says "vacation", so
it risked criterion 1 against any entry that does. The fix
adds an explicit opening sentence and nothing else:

> **I am on vacation. I set my status to 'away' and felt
> something. I think it is called relief. I have reported it
> as a bug.** (121 chars, 121 bytes)

103 → 121 characters. The three-beat escalation is untouched;
the opening now does pure setup duty (clear that the sender is
away, criterion 4: 9/10) and the "I think" hesitation keeps the
machine-trying-to-sound-relaxed voice. Rejected variants: #3b2
dropping "I think it is called relief" for "felt relief" (89
chars) — loses the machine uncertainty that makes the voice
work; #3b3 adding "strange" ("felt something strange", 128
chars) — an extra beat the line does not need. Final score
47/50 (10 + 13 + 10 + 9 + 5).

Field check on the final line: no exact duplicate among the
2,736 titles; "relief" in 1 title, "as a bug" in 0, "reported"
in 0, "status" in 7. The nearest field entry ("rest feels like
a bug") is a different construction. Nothing was copied from
any competitor: all repos were withheld, and the candidates
were written fresh in this session. The sibling bounty #16's
line and its intern angle were not read or reused.
