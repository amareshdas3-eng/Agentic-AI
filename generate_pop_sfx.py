import os
import wave
import math
import struct
import numpy as np

AUDIO_DIR = "d:/instagram/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_pop_sound(sample_rate=44100, duration=0.08):
    """
    Synthesizes a crisp, punchy UI 'bubble pop' sound effect.
    Exponential sine frequency sweep: 250Hz -> 850Hz with fast decay.
    """
    total_samples = int(sample_rate * duration)
    samples = []
    for i in range(total_samples):
        t = i / sample_rate
        # Frequency sweep from 250 Hz to 850 Hz
        freq = 250 + (600 * (t / duration) ** 2)
        # Fast envelope attack and exponential decay
        envelope = math.exp(-35 * (t / duration))
        val = math.sin(2 * math.pi * freq * t) * envelope
        samples.append(val)
    return np.array(samples)

def generate_ding_sound(sample_rate=44100, duration=0.3):
    """
    Synthesizes a clean metallic 'ding / chime' sound effect (e.g. for $400K stamp).
    Harmonic frequencies: 1200Hz + 2400Hz with exponential decay.
    """
    total_samples = int(sample_rate * duration)
    samples = []
    for i in range(total_samples):
        t = i / sample_rate
        envelope = math.exp(-12 * (t / duration))
        val = (0.7 * math.sin(2 * math.pi * 1200 * t) + 0.3 * math.sin(2 * math.pi * 2400 * t)) * envelope
        samples.append(val)
    return np.array(samples)

def generate_whoosh_sound(sample_rate=44100, duration=0.15):
    """
    Synthesizes a smooth whoosh / slide transition sound.
    Filtered white noise with pitch ramp down.
    """
    total_samples = int(sample_rate * duration)
    noise = np.random.uniform(-1.0, 1.0, total_samples)
    envelope = np.sin(np.linspace(0, np.pi, total_samples))
    return noise * envelope * 0.4

def build_synchronized_soundtrack(total_duration=8.0, timestamps=[0.8, 1.6, 2.4, 3.2, 4.0, 4.8, 5.6, 6.4]):
    """
    Creates a master WAV track with pop, ding, and whoosh effects
    precisely aligned with each visual element popup.
    """
    sample_rate = 44100
    total_samples = int(sample_rate * total_duration)
    track = np.zeros(total_samples, dtype=np.float32)
    
    # Low-volume ambient industrial pulse rhythm (40Hz bass + subtle high-hat tick)
    for i in range(total_samples):
        t = i / sample_rate
        # Sub-bass rhythm pulse every 0.5s
        beat_t = t % 0.5
        bass_env = math.exp(-20 * beat_t)
        bass = 0.15 * math.sin(2 * math.pi * 65 * beat_t) * bass_env
        track[i] += bass

    # Insert sound effects at exact timestamps
    pop = generate_pop_sound(sample_rate)
    ding = generate_ding_sound(sample_rate)
    whoosh = generate_whoosh_sound(sample_rate)
    
    sfx_sequence = [
        (0.8, pop),
        (1.6, whoosh),
        (2.4, pop),
        (3.2, pop),
        (4.0, ding),     # Big $400K alert ding!
        (4.8, pop),
        (5.6, ding),     # Zero change orders chime!
        (6.4, pop)      # CTA pop
    ]
    
    for ts, sfx in sfx_sequence:
        start_idx = int(ts * sample_rate)
        end_idx = min(start_idx + len(sfx), total_samples)
        track[start_idx:end_idx] += sfx[:end_idx - start_idx] * 0.85
        
    # Normalize track
    max_val = np.max(np.abs(track))
    if max_val > 0:
        track = track / max_val * 0.95
        
    out_wav = os.path.join(AUDIO_DIR, "synced_pop_soundtrack.wav")
    with wave.open(out_wav, "w") as wav_file:
        wav_file.setnchannels(1)      # Mono
        wav_file.setsampwidth(2)      # 16-bit
        wav_file.setframerate(sample_rate)
        int_samples = (track * 32767).astype(np.int16)
        wav_file.writeframes(int_samples.tobytes())
        
    print(f"Generated Synced Sound FX Track: {out_wav} (Duration: {total_duration}s)")
    return out_wav

if __name__ == "__main__":
    build_synchronized_soundtrack()

