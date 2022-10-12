(def coffee "coffee")

(defn coffee-to-drink
  [coff]
  (when (= coff coffee)
    "drink"))

(defn drink-to-thought
  [drink]
  (when (= drink "drink")
    "thought"))

(defn thought-to-action
  [thought]
  (when (= thought "thought")
    "action"))

(defn action-to-code
  [action]
  (when (= action "action")
    "code"))

(println
  (-> coffee
      coffee-to-drink
      drink-to-thought
      thought-to-action
      action-to-code))
