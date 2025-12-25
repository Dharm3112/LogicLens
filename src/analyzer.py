# src/analyzer.py
from radon.complexity import cc_visit


def analyze_complexity(code_snippet):
    try:
        # Calculate Cyclomatic Complexity
        results = cc_visit(code_snippet)
        if not results:
            return "Low", "Simple execution flow."

        # Get the average complexity
        avg_complexity = sum([x.complexity for x in results]) / len(results)

        if avg_complexity <= 5:
            return "Low", "Good! This code is simple and readable."
        elif avg_complexity <= 10:
            return "Medium", "Moderate complexity. Watch out for edge cases."
        else:
            return "High", "Warning: High complexity! High chance of bugs. Consider refactoring."

    except Exception as e:
        return "Unknown", "Could not parse code syntax (ensure it is valid Python)."