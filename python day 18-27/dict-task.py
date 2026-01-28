# ant to print below output using slicing and indexing only
# ['id', 102]
# ['name', 'Bob']

data = {
    "employees": [
        [
            "id", 101,
            "name", "Alice",
            "skills", ["Python", "SQL", "GCP"],
            "projects", [
                {"project_id": "P1", "status": "Completed"},
                {"project_id": "P2", "status": "Ongoing"}
            ],
            ["id", 102,
            "name", "Bob",
            "skills", ["Python", "SQL", "GCP"],
            "projects", [
                {"project_id": "P1", "status": "Completed"},
                {"project_id": "P2", "status": "Ongoing"}]
            ]
        ]
    ]
}

# print(data["employees"][0])

# print(data["employees"][0][8])

print(data["employees"][0][8][0:2])


print(data["employees"][0][8][2:4])

