
MIN_MARKS = 70
MIN_GPA = 2.5
MIN_ATTENDANCE = 75
def check_student(student):
    reasons = []
    if student["marks"] < MIN_MARKS:
        reasons.append("Marks are below 70")
    if student["documents_complete"] == False:
        reasons.append("Documents are incomplete")
    if student["gpa"] < MIN_GPA:
        reasons.append("Semester GPA is below 2.5")
    if student["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance is below 75 percent")
    if len(reasons) == 0:
        return "Review", "All conditions are satisfied"
    return "Hold", "; ".join(reasons)
test_cases = [
    {
        "name": "All Conditions Passed",
        "input": {
            "marks": 85,
            "documents_complete": True,
            "gpa": 3.2,
            "attendance": 90
        },
        "expected": "Review"
    },
    {
        "name": "GPA Condition Failed",
        "input": {
            "marks": 85,
            "documents_complete": True,
            "gpa": 2.0,
            "attendance": 90
        },
        "expected": "Hold"
    },
    {
        "name": "Attendance Condition Failed",
        "input": {
            "marks": 85,
            "documents_complete": True,
            "gpa": 3.0,
            "attendance": 60
        },
        "expected": "Hold"
    },
    {
        "name": "Marks Threshold Boundary",
        "input": {
            "marks": 70,
            "documents_complete": True,
            "gpa": 2.5,
            "attendance": 75
        },
        "expected": "Review"
    }
]
for case in test_cases:
    actual, reason = check_student(case["input"])
    print("\n" + "=" * 45)
    print("Test Case:", case["name"])
    print("Input:", case["input"])
    print("Expected Result:", case["expected"])
    print("Actual Result:", actual)
    print("Reason:", reason)
    print("Test Passed:", actual == case["expected"])
print("\nAll four test cases have been executed.")

