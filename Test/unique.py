# EpsilonPL/Test/unique.py
"""
Stress-tests EpsilonPL with long programs (typically 200+ lines). Runs
every Test_code/Unique case and scores program longevity/stability by a
tiered penalty: a raw Python exception is the most severe failure (the
interpreter itself broke on a long program), an unexpected epsilon-level
error is a lesser penalty, and output mismatch scales whatever's left.

NOTE: the spec names three deduction sources (errors, unexpected output,
python errors) without specifying relative weights between them. This
tiering is a best-guess default - flagged clearly so the weights can be
adjusted once real long-form test cases exist to calibrate against.
"""
import difflib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_harness import (
    load_epsilon_module, run_eps_program, load_test_cases, TEST_CODE_ROOT,
)

# Tiered penalty weights - see module docstring
EPSILON_ERROR_PENALTY_FACTOR = 0.5  # unexpected epsilon error halves the remaining score


def _output_similarity(actual, expected):
    a = actual.strip()
    e = str(expected).strip()
    if a == e:
        return 1.0
    return difflib.SequenceMatcher(None, a, e).ratio()


def run_unique_tests(epsilon_module=None):
    """
    Runs every Unique (longevity/stress) test case. Returns:
        {"score": float, "results": [ {...} ]}
    """
    if epsilon_module is None:
        epsilon_module = load_epsilon_module()

    cases = load_test_cases(TEST_CODE_ROOT / "Unique")
    results = []

    for case in cases:
        meta = case["meta"]
        expected = meta.get("expected")
        run = run_eps_program(epsilon_module, case["code"])

        had_epsilon_error = bool(run["errors"]) and any(run["errors"].values())
        had_python_error = run["python_exception"] is not None

        entry = {
            "name": case["name"],
            "line_count": len(case["code"].splitlines()),
            "expected": expected,
            "actual_stdout": run["stdout"],
            "python_exception": run["python_exception"],
            "epsilon_errors": {k: v for k, v in (run["errors"] or {}).items() if v},
        }

        if had_python_error:
            entry["score"] = 0.0
            entry["note"] = "python exception - most severe failure on a longevity test"
        else:
            score = 1.0
            notes = []
            if had_epsilon_error:
                score *= EPSILON_ERROR_PENALTY_FACTOR
                notes.append("unexpected epsilon error raised")
            if expected is not None:
                similarity = _output_similarity(run["stdout"], expected)
                score *= similarity
                if similarity < 1.0:
                    notes.append(f"output similarity {similarity:.2f}")
            entry["score"] = score
            entry["note"] = "; ".join(notes) if notes else "clean run, output matched"

        results.append(entry)

    scored = [r["score"] for r in results]
    overall = sum(scored) / len(scored) if scored else None
    return {"score": overall, "results": results}


def _print_report(report):
    print("=== Unique (Longevity) Results ===")
    for r in report["results"]:
        print(f"  {r['name']:<20} lines={r['line_count']:<5} score={r['score'] * 100:.1f}%  {r['note']}")
        if r["python_exception"]:
            print(f"    !! Python exception: {r['python_exception'].splitlines()[-1]}")
    overall = report["score"]
    print(f"\nOverall longevity score: {overall * 100:.1f}%" if overall is not None else "\nOverall longevity score: N/A (no test cases found)")


if __name__ == "__main__":
    report = run_unique_tests()
    _print_report(report)