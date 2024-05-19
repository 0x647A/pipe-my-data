# How to split a file in half?

## Using `split`!

1. **Split the file into equal parts:**

```sh
split -l $(( $(wc -l < pizza_data.csv) / 2 + 1)) pizza_data.csv pizza_data_part_
``` 
This command splits the file into two parts with an equal number of lines, but the header (if present) will not be included.

2. **Move the header to the second file:**

Assume the first file is named `pizza_data_part_aa` and the second is `pizza_data_part_ab`.

```sh
head -n 1 pizza_data.csv > header.csv
cat header.csv pizza_data_part_ab > temp && mv temp pizza_data_part_ab
rm header.csv
```

### Explanation:

- `split -l $(( $(wc -l < pizza_data.csv) / 2 )) pizza_data.csv pizza_data_part_`: This splits the file into two parts with an equal number of lines.
- `head -n 1 pizza_data.csv > header.csv`: This extracts the header from the original file and saves it to a temporary file header.csv.
- `cat header.csv pizza_data_part_ab > temp && mv temp pizza_data_part_ab`: This concatenates the header with the second part of the split file and moves the result back to the original file name.
- `rm header.csv`: This removes the temporary header file.