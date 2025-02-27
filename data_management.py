import sys
   
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])
e = int(sys.argv[5])

# def isNumeric(number):
#     if number.isnumeric():
#         return int(number)
#     else:
#         return print("<html><body><h2>Error: All inputs must be numeric.</h2></body></html>")

numeric_values = [a, b, c, d, e]
# numeric_values = [isNumeric(number) for number in numeric_values]

negative_present = any(num < 0 for num in numeric_values)
negative_message = ""
if negative_present:
    negative_message = "<p>Note: One or more values are negative.</p>"


avg = sum(numeric_values) / len(numeric_values)
average_message = f"<p>Average of numbers: {avg:.2f}</p>"
if avg > 50:
    average_message += "<p>The average is greater than 50.</p>"
else:
    average_message += "<p>The average is not greater than 50.</p>"

positive_count = sum(1 for num in numeric_values if num > 0)

if positive_count & 1 == 0:
    positive_message = f"<p>The count of positive numbers ({positive_count}) is even.</p>"
else:
    positive_message = f"<p>The count of positive numbers ({positive_count}) is odd.</p>"


new_list = [num for num in numeric_values if num > 10]
sorted_new_list = sorted(new_list)

original_list_html = f"<p>Original list: {numeric_values}</p>"
sorted_list_html = f"<p>Sorted list (values > 10): {sorted_new_list}</p>"


print(f"""
<html>
<body>
    <main 
    style="
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
    padding: 1rem;
    border-radius: 0.45rem;
    margin: auto;
    max-width: fit-content;
    ">   
        <h1>Assignment 6 - Felipe Franco de Camargo</h1>
        <h2>Data Management Results</h2>
        {original_list_html}
        {sorted_list_html}
        {negative_message}
        {average_message}
        {positive_message}      
    </main>
</body>
</html>
""")
    
    

