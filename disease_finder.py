import csv

file = "dataset.csv"

diseases = {}

with open(file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        disease = row["Disease"].strip()

        if disease:
            diseases[disease] = diseases.get(disease, 0) + 1

print("Unique Diseases:")
print("-" * 40)

for i, (disease, count) in enumerate(diseases.items(), 1):
    print(f"{i}. {disease} -> {count} records")

print("\nTotal Unique Diseases:", len(diseases))