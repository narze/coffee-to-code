extern crate regex;

use std::io::{self, BufRead};
use regex::{Regex, Captures};

pub fn convert_coffee_to_code(string: &str) -> String {
    let coffee_checker = Regex::new(r"(?i)coffee").unwrap();
    coffee_checker.replace_all(string, |caps: &Captures| {
        let found = caps.get(0).unwrap().as_str();
        let mut result: Vec<char> = vec![];
        for c in found.chars() {
            let tmp = match (c, result.len()) {
                (x, 2) if x == 'f' => 'd',
                (x, 2) if x == 'F' => 'D',
                (x, 3) if x == 'f' || x == 'F' => '\0',
                (x, 4) if x == 'e' || x == 'E' => '\0',
                (x, _) => x,
            };
            if tmp != '\0' { result.push(tmp) }
        }
        result.into_iter().collect::<String>()
    }).to_string()
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    for line in stdin.lock().lines() {
        let l = line.unwrap().to_string();
        println!("{} {}", l, convert_coffee_to_code(&l));
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    #[test]
    fn check_coffee_to_code() {
        let test_set = vec![
            ("Coffee", "Code"),
            ("CoffEe", "CodE"),
            ("coffEe", "codE"),
            ("coffeE", "code"),
            ("COfFeE", "COde"),
            ("CoFfeE", "CoDe"),
            ("I have to drink COFFEE everyday", "I have to drink CODE everyday"),
            ("IhavetodrinkCOFFEEeveryday", "IhavetodrinkCODEeveryday"),
        ];
        for (input, expected) in test_set {
            assert_eq!(crate::convert_coffee_to_code(input), expected);
        }
    }
}