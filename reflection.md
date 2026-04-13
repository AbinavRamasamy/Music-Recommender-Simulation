# Reflection: Profile Pair Comparisons

## High-Energy Pop vs. Chill Lofi

These two profiles are near-opposites: Pop targets high energy (0.9) with no acoustic preference, while Lofi targets low energy (0.3) with acoustic preferred. The outputs had almost zero overlap. This makes sense — energy and acoustic preference together push the scoring in opposite directions, so songs that score well for one profile actively score poorly for the other.

## Deep Intense Rock vs. High-Energy Pop

Both are high-energy and non-acoustic, but genre and mood differ (rock/intense vs. pop/happy). The top results shared similar energy ranges but split on genre — rock songs ranked near the top for the Rock profile but fell mid-list for Pop. This shows genre's +2.0 weight acting as a hard separator even when all other features align closely.

## All Midpoints vs. Chill Lofi

All Midpoints uses energy 0.5 and no acoustic preference; Chill Lofi uses energy 0.3 and acoustic preferred. The Lofi profile returned a tight, consistent set of lofi/acoustic songs. All Midpoints returned a more scattered list — songs from different genres and moods appeared simply because no signal was strong enough to filter them out. The comparison highlights how a profile with no strong preferences produces recommendations that feel generic.

## Unknown Genre vs. High-Energy Pop

Both use mood "happy" and similar energy (~0.7–0.9), but Unknown Genre uses "bossa nova" which doesn't exist in the catalog. The two profiles returned nearly identical results — the genre bonus never fired for Unknown Genre, so mood and energy took over. This is the clearest failure mode: a user with a very specific genre preference gets treated the same as someone with no genre preference at all.

## Max Energy Non-Acoustic vs. Deep Intense Rock

Both are non-acoustic and high-energy, but Max Energy Non-Acoustic targets the ambient genre. Ambient songs are low-energy by nature, so the genre bonus (+2.0) and energy score pulled in opposite directions — ambient songs matched genre but were penalized for low energy. Rock songs had no genre bonus but scored well on energy. The results ended up mixing both, showing the tension between categorical and continuous features in the scoring formula.
