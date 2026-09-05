# Chess Error Adaptation — Source Register Pass 1

Status: `LIVE_REGISTER`
Date: 2026-09-05

Language is recorded for retrieval/context. **Language is not an independence family.**

| ID | Source | Lang | Type | Research use | Independence / lineage note | Use ceiling |
|---|---|---|---|---|---|---|
| S01 | McIlroy-Young et al., *Aligning Superhuman AI with Human Behavior: Chess as a Model System* / Maia | EN | peer-reviewed ML + OSS | skill-conditioned human move distributions | Maia lineage | human likelihood by skill; not error cause/pedagogy |
| S02 | Tang et al., *Maia-2: A Unified Model for Human-AI Alignment in Chess*, NeurIPS 2024 | EN | peer-reviewed ML + OSS | unified skill-aware move/outcome model | Maia lineage, later generation | skill-conditioned modeling and trajectories; not learning efficacy |
| S03 | Monroe et al., *Chessformer: A Unified Architecture for Chess Modeling* / Maia-3, ICLR 2026 | EN | peer-reviewed ML + OSS | latest rating-conditioned human move instrument | Maia/Chessformer lineage | executable human prior; not Stockfish evaluation or diagnosis |
| S04 | McIlroy-Young et al., *Learning Models of Individual Behavior in Chess*, KDD 2022 | EN | peer-reviewed ML + OSS | player-specific residual beyond cohort | Maia-individual lineage | individual behavior/style; not optimal intervention |
| S05 | *Blunder prediction in chess*, Applied Intelligence 2026 | EN | peer-reviewed ML/data | personalized blunder profile, Elo bins, immediate/non-immediate definition | independent modeling paper using Lichess/human-board embeddings; cites Maia | blunder probability/type under its operational definition |
| S06 | Saariluoma, *Error in chess: the apperception-restructuring view*, Psychological Research 1992 | EN | protocol experiments | cognitive error mechanisms beyond working-memory overload | classic chess cognition | mechanism theory from task protocols; not population prevalence |
| S07 | *Intuition in chess: a study with world-class players*, Psychological Research 2023 | EN | empirical psychology | Elo vs evaluation accuracy / complexity interaction | expertise cognition | evaluation accuracy relation; elite-heavy scope |
| S08 | van Harreveld et al., *The effects of time pressure on chess skill*, Psychological Research 2007 | EN | empirical psychology | skill × time-control boundary | time-pressure expertise family | context effect; not personalized taxonomy |
| S09 | *Intuition and deliberation in elite expertise*, Cognitive Research 2026 | EN | empirical archival | move time, time pressure, blunder propensity in elite play | related time-pressure family | elite context; informs temporal conditioning |
| S10 | Cüvitoğlu, *Interpretable machine learning analysis of nonlinear error amplification under time pressure and positional ambiguity in elite blitz chess*, Scientific Reports 2026 | EN | peer-reviewed ML/behavior | interaction of time pressure × ambiguity | separate recent empirical family | seven elite players/blitz; narrow population |
| S11 | Lesche & Hagemann, *Errors in Chess Impair Subsequent Performance of Novices, But Not Experts*, 2026 preprint | EN | large-scale preprint | post-error slowing/accuracy and skill moderation | separate post-error family | not yet peer-reviewed in Pass 1 |
| S12 | Voronkov & Persits, *Типичные ошибки* (Typical Errors), 1974 | RU | trainer book / taxonomy | tactical, positional, endgame, psychological error families; level-sensitive teaching examples | Soviet/Russian coaching lineage | taxonomy candidate only; selected/modified pedagogical examples |
| S13 | Popov, *Шахматы: работа над ошибками* (Chess: Work on Errors), 2010 | RU | trainer book | recurring characteristic errors and remediation candidates | Russian coaching lineage | pedagogy/taxonomy hypothesis; no frequency-by-Elo promotion |
| S14 | Didierjean, Ferrari & Marmèche, *L'expertise cognitive au jeu d'échecs : quoi de neuf depuis De Groot (1946)?*, 2004 | FR | review | novice/expert cognition synthesis | largely shared foundational international literature | synthesis/lineage; not independent replication by language |
| S15 | 许松芽, 连榕, *新手到专家:职业专长发展的必由之路*, 2002 | ZH | expertise review | novice→expert factors: motivation, practice, perception, knowledge | general expertise, chess as foundational domain | not chess-error-by-rating evidence |
| S16 | Current Spanish level-specific coaching articles/videos surfaced in Pass 1 | ES | coaching/community | candidate labels for planning/calculation/tactical habits | doctrine/community family | hypothesis discovery only |
| S17 | CSSLab `maia2-skill-adaptation` | EN | OSS/research code | 172 measurable chess concepts; skill adaptation / knowledge externalization experiments | Maia-2 mechanistic lineage | candidate concept instrumentation; not direct human error taxonomy |
| S18 | CSSLab `maia-chess`, `maia2`, `maia3`, `maia-individual` | EN | OSS/instruments | executable models, datasets/pipelines, inference interfaces | shared Maia family | implementation/reproduction resources |
| S19 | Yardenms `ChessBlunderPrediction` | EN | OSS associated with blunder-prediction work | code/notebooks for blunder prediction | blunder prediction lineage | requires code-level validation before reuse |

## URLs / locators

- Maia project: https://www.maiachess.com/
- Maia 2 paper: https://proceedings.neurips.cc/paper_files/paper/2024/hash/250190819ff1dda47cd23cecc0c5a69b-Abstract-Conference.html
- Maia 2 repo: https://github.com/CSSLab/maia2
- Maia 3 repo: https://github.com/CSSLab/maia3
- Maia individual repo: https://github.com/CSSLab/maia-individual
- Maia 2 skill-adaptation repo: https://github.com/CSSLab/maia2-skill-adaptation
- Applied Intelligence blunder prediction: https://link.springer.com/article/10.1007/s10489-026-07131-2
- Saariluoma error paper: https://pubmed.ncbi.nlm.nih.gov/1603886/
- Intuition/world-class paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC10497664/
- Time-pressure paper: https://pubmed.ncbi.nlm.nih.gov/17186308/
- 2026 elite intuition/deliberation: https://link.springer.com/article/10.1186/s41235-026-00727-9
- 2026 time pressure × ambiguity: https://www.nature.com/articles/s41598-026-59689-z
- 2026 post-error preprint: https://sciety.org/articles/activity/10.31234/osf.io/cdk59_v1
- Russian *Типичные ошибки*: https://www.nehudlit.ru/books/bibliotechka-shakhmatista-tipichnye-oshibki.html
- French expertise review: https://www.persee.fr/doc/psy_0003-5033_2004_num_104_4_29689
- Chinese novice→expert review: https://fsxb.cbpt.cnki.net/portal/journal/portal/client/paper/64ba5633be5d10b27442af829acbdb76

## Pass-1 language yield decision

- EN: high yield for empirical/ML/data.
- RU: high yield for explicit error taxonomies and trainer knowledge; lower evidential ceiling for prevalence unless studies are found.
- FR: useful expertise synthesis; substantial shared lineage.
- ZH: current pass yielded generic expertise material but no strong chess-specific error-by-rating dataset; lane remains conditional.
- ES: useful coaching hypotheses; weak current evidence for hard rating-conditioned rules.

No language quota is used. Future search is triggered by an unresolved question, not by missing languages.
