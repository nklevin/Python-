from json import dumps

input_file = "Task_7.txt"
output_file = "task_7.json"
results = [{}, {}]

with open(input_file, encoding='utf-8') as working_file:
    lines = working_file.readlines()
    for line in lines:
        name, _, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)

        results[1]['average_profit'] = round(
            sum(
                profit for _, profit in results[0].items() if profit > 0
            ) / len(results[0])
        )

        with open(output_file, "w", encoding='utf-8') as end_file:
            end_file.write(dumps(results))
