import json

def analyze_devops_log(log):
    return {
        "issue": "Server timeout",
        "severity": "High",
        "solution": "Check server load and restart service"
    }


def analyze_web3_issue(error):
    return {
        "problem": "Transaction failure",
        "cause": "Insufficient gas fee",
        "fix": "Increase gas limit and retry"
    }


if __name__ == "__main__":
    print("DevOps Analysis:")
    print(json.dumps(analyze_devops_log("Server timeout error"), indent=2))

    print("\nWeb3 Analysis:")
    print(json.dumps(analyze_web3_issue("Transaction failed"), indent=2))
