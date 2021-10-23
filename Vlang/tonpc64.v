import regex

fn coffee_to_code(s string) string {
	mut re := regex.regex_opt('[Cc][Oo][Ff][Ff][Ee][Ee]') or { panic(err) }
	return re.replace(s, 'code')
}

fn main() {
	println(coffee_to_code('Hello Coffee'))
}