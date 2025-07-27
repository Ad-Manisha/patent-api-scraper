import json
import requests

BASE_URL = "https://production.api.ipaustralia.gov.au/public/ipright-search-api/v1/patents"
QUERY = "Robotic Surgery"
LIMIT = 10        # How many results to get in each API call

offset = 0        # Starting index for pagination
all_results = []  # Store all fetched results

# --- Fetch Data from API ---
while True:
    url = f"{BASE_URL}?query={QUERY}&limit={LIMIT}&offset={offset}&orderBy=filingDate&order=desc"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed at offset: {offset}.Status: {response.status_code}")
        break

    # Parse the JSON response
    data = response.json()
    results = data.get("results")

    print(results)

    if not results:
        print("No more results")
        break
    
    all_results.extend(results)  # Accumulate current batch of results
    print(f"page {(offset/LIMIT) +1}: {len(results)} records")

    offset += LIMIT  # Move to next set of results


# --- Save Results to a File ---
print(f"\n Total records fetched: {len(all_results)}")

filename = f"results_{QUERY}.json"

with open(filename, "w") as f:
    json.dump(all_results, f, indent=4, sort_keys=True, ensure_ascii=False)