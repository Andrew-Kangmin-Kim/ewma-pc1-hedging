"""Execute every code cell of a notebook in order."""
import json
import re
import sys
import time
import traceback

# The notebooks print non-ASCII (the Marcenko-Pastur edge, degree signs), and
# the default stdout encoding follows the console codepage, which on this
# machine cannot represent them. Isolated mode ignores PYTHONIOENCODING, so set
# it here instead of relying on the environment.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

import matplotlib
matplotlib.use("Agg")            # headless; plt.show() becomes a no-op

import sys as _s
nb = json.load(open(_s.argv[1] if len(_s.argv)>1 else "latent_market_drift_v2.ipynb", encoding="utf-8"))
cells = [c for c in nb["cells"] if c["cell_type"] == "code"]

g = {"__name__": "__main__"}
for i, c in enumerate(cells, 1):
    src = "".join(c["source"])
    m = re.search(r"CELL (\d+)", src)
    tag = m.group(1) if m else str(i)
    print(f"\n{'='*70}\n>>> CELL {tag}\n{'='*70}", flush=True)
    t0 = time.time()
    try:
        exec(compile(src, f"<cell {tag}>", "exec"), g)
    except Exception:
        traceback.print_exc()
        print(f"\n*** CELL {tag} FAILED after {time.time()-t0:.1f}s", flush=True)
        sys.exit(1)
    print(f"\n--- cell {tag} ok ({time.time()-t0:.1f}s)", flush=True)

print("\nALL CELLS EXECUTED")
