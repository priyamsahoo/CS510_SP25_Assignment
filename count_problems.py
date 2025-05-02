import json

# Thresholds
HARD_BAR = 1501
NON_BAR = 2701

# Counters
easy_count = 0
difficult_count = 0

input_path = 'data/program_synthesis_data.jsonl'

with open(input_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        diff = data.get('difficulty')
        if diff is None:
            # no difficulty field, skip
            continue

        if diff < HARD_BAR:
            easy_count += 1
        elif diff < NON_BAR:
            difficult_count += 1
        # else:
        #     # diff >= NON_BAR — ignored by default,
        #     # or count separately if you like

print(f"Easy problems (difficulty < {HARD_BAR}): {easy_count}")
print(f"Difficult problems ({HARD_BAR} ≤ difficulty < {NON_BAR}): {difficult_count}")
