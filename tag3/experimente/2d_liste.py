ws = [ # A B C ...
       ["2026/01/01", 3.15, 1500 ],
       ["2026/02/01", 3.25, 2000 ],
       ["2026/03/01", 3.1, 3500 ],
     ]

print("Report")
for row in ws:
    print(f"{row[0]} - Kurs: {row[1]:>5} Volumen: {row[2]:>10}")
    