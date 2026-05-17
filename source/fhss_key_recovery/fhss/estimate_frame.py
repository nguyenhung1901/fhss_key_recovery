#!/usr/bin/env python3
import argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("--input", default="changed_samples.txt")
args = parser.parse_args()

positions = []

with open(args.input, "r") as f:
    for line in f:
        parts = line.split()
        if len(parts) >= 1:
            positions.append(int(parts[0]))

total_changed = len(positions)

if total_changed == 0:
    print("TOTAL_CHANGED 0")
    print("ESTIMATE_FAIL")
    raise SystemExit(1)

msg_len_estimate = total_changed // 8
expected_last_frame = total_changed - 1

print(f"TOTAL_CHANGED {total_changed}")
print(f"MSG_LEN_ESTIMATE {msg_len_estimate}")

candidates = [256, 512, 1024, 2048, 4096]
ranked = []

for fs in candidates:
    frames = [p // fs for p in positions]
    counts = Counter(frames)

    duplicate_frames = sum(1 for v in counts.values() if v > 1)
    unique_frames = len(counts)
    last_frame = max(frames) if frames else -1

    # Frame size đúng trong bài này có đặc điểm:
    # - mỗi bit nằm ở một frame khác nhau
    # - có đúng total_changed frame được dùng
    # - frame cuối xấp xỉ total_changed - 1
    last_frame_distance = abs(last_frame - expected_last_frame)

    score = 0
    score -= duplicate_frames * 100
    score -= last_frame_distance * 5
    score += unique_frames

    ranked.append((score, fs, duplicate_frames, unique_frames, last_frame, last_frame_distance))

    print(
        f"candidate_frame_size={fs} "
        f"duplicate_frames={duplicate_frames} "
        f"unique_frames={unique_frames} "
        f"last_frame={last_frame} "
        f"distance_from_expected={last_frame_distance}"
    )

ranked.sort(reverse=True)
best_score, best_fs, best_dup, best_unique, best_last, best_distance = ranked[0]

print("ESTIMATE_OK")
print(f"SUGGESTED_FRAME_SIZE={best_fs}")
print(f"SUGGESTED_MSG_LEN={msg_len_estimate}")
