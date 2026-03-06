import requests
from config import TON_NODE_URL, TON_API_KEY

def fetch_new_deployment_data():
    """
    Fetch recent blocks and scan for new token deployments (SFT/NFT contracts).
    """
    headers = {}
    if TON_API_KEY:
        headers['Authorization'] = f'Bearer {TON_API_KEY}'

    try:
        # Query the TON node to fetch updates
        response = requests.post(
            f"{TON_NODE_URL}",
            json={"id": 1, "method": "getTransactions", "params": {"limit": 10}},
            headers=headers
        )
        data = response.json()
        
        # Example of parsing, logs recent transactions
        new_deployments = []
        transactions = data.get("result", {}).get("transactions", [])
        for txn in transactions:
            if txn.get("msg_type") == "deploy_contract":  # Filter for deployments
                contract_info = txn.get("in_msg", {})
                new_deployments.append(
                    {
                        "address": txn.get("account_addr"),
                        "deployer": contract_info.get("source"),
                        "value": contract_info.get("value"),
                    }
                )
        return new_deployments
    except Exception as e:
        print(f"Error fetching deployments: {e}")
        return []
