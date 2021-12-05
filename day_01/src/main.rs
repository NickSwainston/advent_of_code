use std::path::Path;
use std::fs::File;
use std::io::{BufReader,BufRead};

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn count_increases(str_array: &Vec<String>) -> u32 {
    let mut count = 0;
    for (i, item) in str_array.iter().enumerate() {
        //println!("The {}th item is {}", i+1, item);
        if i == 0 {
           continue;
        }
        if item.parse::<i32>().unwrap() > str_array[i-1].parse::<i32>().unwrap() {
            count += 1;
        }
    }
    return count;
}

fn sum_three_array(str_array: &Vec<String>) -> Vec<String> {
    let mut summed_array: Vec<String> = Vec::new();
    for (i, _item) in str_array.iter().enumerate() {
        if i < 2{
            continue;
        }
        summed_array.push((&str_array[i].parse::<i32>().unwrap() + 
                           &str_array[i-1].parse::<i32>().unwrap() + 
                           &str_array[i-2].parse::<i32>().unwrap()).to_string());
        }
    return summed_array;
}

fn main() {
    //let input_file = Path::new("example");
    let input_file = Path::new("input");
    let str_array: Vec<String> = lines_from_file(input_file);

    let count1 = count_increases(&str_array);
    println!("Part 1 count {}", count1);

    let sum_array: Vec<String> = sum_three_array(&str_array);
    let count2 = count_increases(&sum_array);
    println!("Part 2 count {}", count2);

}

#[cfg(test)]
mod tests {
    use crate::count_increases;
    #[test]
    fn test_count_increases() {
       let  test_1: Vec<String> = vec!["1".to_string(),
                                       "2".to_string(),
                                       "1".to_string(),
                                       "4".to_string(),
                                       "5".to_string()];
        assert_eq!(count_increases(test_1), 3);
    }
}