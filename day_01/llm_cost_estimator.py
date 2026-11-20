

VALID_MODEL = ("fast", "balanced", "reasoning")

def llm_cost_estimator(
    model: str,
    input_tokens: int,
    output_tokens: int,
    use_cache: bool,
    use_batch: bool,
    use_priority: bool,
) -> float:
     

    if model == "fast":
        input_rate = 0.15
        output_rate = 0.60
    elif model == "balanced":
        input_rate = 2.50
        output_rate = 10.00
    elif model == "reasoning":
        input_rate = 10.00
        output_rate = 40.00
    else:
        print("Error: invalid model")
        return 0.0

    if input_tokens < 0 or output_tokens < 0:
        print("Error: input and output tokens must be non-negative")
        return 0.0

    input_cost = (input_tokens / 1_000_000) * input_rate
    output_cost = (output_tokens / 1_000_000) * output_rate

    if use_cache and input_tokens >= 1000:
        input_cost *= 0.5
    total_cost = input_cost + output_cost

    if use_batch:
        total_cost *= 0.5
    elif use_priority:
        total_cost *= 1.25

       

    print("\n=== LLM Cost Estimator ===")
    print(f"Model: {model}")
    print(f"Input:  {input_tokens:,} tokens (${input_cost:.4f})")
    print(f"Output: {output_tokens:,} tokens (${output_cost:.4f})")
    print(f"Total cost: ${total_cost:.4f}")

    return total_cost 

while True:
    model = input("Please enter a model (fast, balanced,reasoning): ").strip().lower()
    if model in VALID_MODEL:
        break
    print("Error: please choose fast, balanced, or reasoning")  
    
use_cache = input("Prompt caching enabled? (y/n): ").strip().lower() == "y"
use_batch = input("Batch API mode? (y/n): ").strip().lower() == "y"
use_priority = input("Priority SLA tier? (y/n): ").strip().lower() == "y"
input_tokens = int(input("Please enter your input token: ").strip())
output_tokens = int(input("Please enter your output token: ").strip())

llm_cost_estimator(
    model=model,
    input_tokens=input_tokens,
    output_tokens=output_tokens,
    use_cache=use_cache,
    use_batch=use_batch,
    use_priority=use_priority
)
