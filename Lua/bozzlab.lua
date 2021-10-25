function coffee_to_code(text)
	return text:gsub("ffe", "d")
end

print(coffee_to_code("coffee"))