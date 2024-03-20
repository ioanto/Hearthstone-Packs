This is an auxiliary file to assist in better understanding the nature of the data.

The raw data file "packs.xlsx" has the following features:
    1.  pack_number (integer): A counter for the amount of packs opened during an expansion.
    2.  commons (integer): A counter for the amount of common rarity cards opened through a single pack.
    3.  rares (integer): A counter for the amount of rare rarity cards opened through a single pack.
    4.  epics (integer): A counter for the amount of epic rarity cards opened through a single pack.
    5.  legendaries (integer): A counter for the amount of legendary rarity cards opened through a single pack.
    6.  g_commons (integer): A counter for the amount of golden common rarity cards opened through a single pack.
    7.  g_rares (integer): A counter for the amount of golden rare rarity cards opened through a single pack.
    8.  g_epics (integer): A counter for the amount of golden epic rarity cards opened through a single pack.
    9.  g_legendaries (integer): A counter for the amount of golden legendary rarity cards opened through a single pack.
    10. expansion (categorical): A tracker for highlighting the expansion to which a pack belongs to.

The raw data file "expansion.xlsx" has the following features:
    1.  expansion (categorical): Simple tracker for Hearthstone's expansions.
    2.  exp_commons (integer): A counter for the unique common rarity cards from a single expansion.
    3.  exp_rares (integer): A counter for the unique rare rarity cards from a single expansion.
    4.  exp_epics (integer): A counter for the unique epic rarity cards from a single expansion.
    5.  exp_legendaries (integer): A counter for the unique legendary rarity cards from a single expansion.