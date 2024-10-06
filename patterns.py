
date_formats = [
    (r'(\d{4})-(\d{2})-(\d{2})', '%Y-%m-%d'),  # YYYY-MM-DD
    (r'(\d{2})/(\d{2})/(\d{4})', '%d/%m/%Y'),  # DD/MM/YYYY
    (r'(\d{2})-(\d{2})-(\d{4})', '%d-%m-%Y'),  # DD-MM-YYYY
    (r'([A-Z][a-z]+) (\d{1,2}), (\d{4})', '%B %d, %Y'),  # Month DD, YYYY
    (r'(\d{1,2}) ([A-Z][a-z]+) (\d{4})', '%d %B %Y'),  # DD Month YYYY
]
