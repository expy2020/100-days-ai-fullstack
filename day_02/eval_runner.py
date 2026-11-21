import random

PASS_THRESHOLD = 75

eval_results = [
    ["summarization", 420, 88],
    ["sql_generation", 950, 74],
    ["code_review", 1200, 91],
    ["json_extraction", 310, 96],
    ["rag_qa", 780, 62],
    ["translation", 500, 85],
]


def analyze_evals(results: list[list]):
    if not results:
        raise ValueError("Results list cannot be empty.")

    total_score = 0
    total_latency = 0

    best_name = results[0][0]
    best_score = results[0][2]

    slowest_name = results[0][0]
    slowest_latency = results[0][1]

    failing_cases: list[tuple[str, int]] = []

    for name, latency, score in results:
        total_score += score
        total_latency += latency

        if score > best_score:
            best_score = score
            best_name = name

        if latency > slowest_latency:
            slowest_latency = latency
            slowest_name = name

        if score < PASS_THRESHOLD:
            failing_cases.append((name, score))

    avg_score = total_score / len(results)
    avg_latency = total_latency / len(results)

    return (
        avg_score,
        avg_latency,
        (best_name, best_score),
        (slowest_name, slowest_latency),
        failing_cases,
    )


def sample_spot_checks(results: list[list], count: int) -> list[list]:
    if count <= 0 or count > len(results):
        raise ValueError(f"Count must be between 1 and {len(results)}.")
    return random.sample(results, count)


if __name__ == "__main__":
    avg_score, avg_latency, best_case, slowest_case, failing_cases = analyze_evals(
        eval_results
    )

    print("=== AI Eval Summary ===")
    print(f"Average score: {avg_score:.2f}")
    print(f"Average latency: {avg_latency:.2f} ms")
    print(f"Best case: {best_case[0]} ({best_case[1]}/100)")
    print(f"Slowest case: {slowest_case[0]} ({slowest_case[1]} ms)")
    print(f"Failing cases (< {PASS_THRESHOLD}): {failing_cases}")

    spot_checks = sample_spot_checks(eval_results, count=2)
    print("\n=== Random Spot Checks ===")
    for name, latency, score in spot_checks:
        print(f"- {name}: score={score}, latency={latency}ms")