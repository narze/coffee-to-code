use std::io;

fn main() {
    loop {
        println!("Enter only `Coffee`: ");
        let stdin = io::stdin();
        let mut coffee = String::new();
        stdin.read_line(&mut coffee).expect("Failed to read input.");

        if coffee.contains("Coffee") {
            println!("{}", coffee.replace("ffe", "d"));
            break
        }
    }
}