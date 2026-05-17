#!/usr/bin/env python3
import wave

def info(path):
    with wave.open(path, "rb") as wf:
        return {
            "channels": wf.getnchannels(),
            "sample_width": wf.getsampwidth(),
            "sample_rate": wf.getframerate(),
            "frames": wf.getnframes()
        }

cover = info("cover.wav")
stego = info("stego.wav")

print("COVER_INFO", cover)
print("STEGO_INFO", stego)

if cover == stego and cover["channels"] == 1 and cover["sample_width"] == 2:
    print("INSPECT_OK")
else:
    print("INSPECT_FAIL")
