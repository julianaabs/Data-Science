rows = [
	["Bassett", "Richard", "1745-04-02", "M", "sen", "DE", "Anti-Administration"],
	["Bland", "Theodorick", "1742-03-21", " ", "rep", "VA", " "]
]

for row in rows:
	if row[6] == " ":
		row[6] = "No Party"

print(rows)
