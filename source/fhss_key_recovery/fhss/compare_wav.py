#!/usr/bin/env python3
import wave

def read_samples(path):
    with wave.open(path, "rb") as wf:
        params = wf.getparams()
        frames = wf.readframes(wf.getnframes())

    if params.nchannels != 1 or params.sampwidth != 2:
        raise ValueError("Only mono 16-bit PCM WAV is supported")

    data = bytearray(frames)
    samples = []
    for i in range(0, len(data), 2):
        samples.append(int.from_bytes(bytes([data[i], data[i+1]]), byteorder="little", signed=True))
    return params, samples

cover_params, cover = read_samples("cover.wav")
stego_params, stego = read_samples("stego.wav")

print("COVER_INFO", cover_params)
print("STEGO_INFO", stego_params)

if cover_params != stego_params:
    print("COMPARE_FAIL")
    raise SystemExit(1)

changed = []
for i, (c, s) in enumerate(zip(cover, stego)):
    if c != s:
        changed.append((i, s - c))

with open("changed_samples.txt", "w") as f:
    for index, diff in changed:
        f.write(f"{index} {diff}\n")

print(f"changed_samples={len(changed)}")
print("output=changed_samples.txt")

if len(changed) > 0:
    print("COMPARE_OK")
else:
    print("COMPARE_FAIL")
