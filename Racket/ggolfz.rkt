(define welcome-text "Welcome to coffee2code")
(println welcome-text)
(define (coffee2code str)
    (if (string-ci=? str "coffee") "code" "Nah, it is not a coffee!")
)

(println (coffee2code "coffee"))
