from pathlib import Path
import soundfile as sf
import numpy as np


def load_files(path, maxLength, fadeTime):
    out_dir = Path(path) / "processed"
    out_dir.mkdir(exist_ok=True)

    for file in sorted(Path(path).iterdir()):
        if file.is_file():
            data, sr = sf.read(file)

            peak = np.max(np.abs(data))
            if peak > 0:
                data = data / peak
                data = data / 4

            data = data[:int(maxLength * sr)]

            fadeSamples = min(int(fadeTime * sr), len(data))
            if fadeSamples > 0:
                release = np.linspace(1, 0, fadeSamples)
                if data.ndim > 1:
                    release = release[:, None]
                data[-fadeSamples:] *= release

            sf.write(out_dir / file.name, data, sr)


#load_files("sounds/harp/31EDO#11", 1.4, 0.2)

