"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        # TODO: Get input from user
        # TODO: Check if user typed 'done'
        # TODO: Try to convert to float and add to list
        # TODO: Handle invalid input gracefully
        number=input()

        try:
            number=float(number)
            numbers.append(number)
        except ValueError:
            if number.lower()=="done":
                return numbers
            else:
                print("Invalid input. Enter numbers one at a time. Type 'done' when finished. ")


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    # TODO: Calculate count
    # TODO: Calculate sum
    # TODO: Calculate average
    # TODO: Find minimum
    # TODO: Find maximum
    # TODO: Count even numbers (hint: use modulo operator)
    # TODO: Count odd numbers
    cnt=len(numbers)
    i=0
    total=sum(numbers)
    even_count=0
    odd_count=0
    while i<cnt:
        if numbers[i]%2==0:
            even_count+=1
        else:
            odd_count+=1
        i+=1
    avg=total/cnt
    return {
        "count": cnt,
        "sum": total,
        "average": round(avg, 2),  # float arrondi, pas string
        "minimum": min(numbers),
        "maximum": max(numbers),
        "even_count": even_count,
        "odd_count": odd_count,
    }


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.
    for key, value in analysis.items():
        print(f"{key}:{value}")
    print("-" * 20)

def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()