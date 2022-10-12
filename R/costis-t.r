coffee_to_code <- function(caffeinated_string) {
decaf_message <- paste("The string does not contain",
                       "the right amount of caffeine,",
                       "change it to 'coffee'.", sep = ' ')
decaffeinated_string <- ifelse(caffeinated_string == 'coffee', 
                               'code',
                               decaf_message)
return(decaffeinated_string)
}

# coffee_to_code('random_string')
# coffee_to_code('coffee')

