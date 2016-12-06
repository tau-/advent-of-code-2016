(ns adventofclojure.day-01
  (:require [clojure.string :as str]))

(def starting-state
  {:dir :n, :n 0, :s 0, :e 0, :w 0})

(defn turn
  [state command]
  (let [turn (first command) current-direction (:dir state)
        left-turn
        {:n :w, :s :e, :e :n, :w :s}
        right-turn
        {:n :e, :s :w, :e :s, :w :n}]
    (case turn
      \L (assoc state :dir (current-direction left-turn))
      \R (assoc state :dir (current-direction right-turn))
      )))

(defn move
  [state command]
  (let [distance
        (Integer/parseInt (apply str (rest command)))
        current-direction
        (:dir state)]
    (assoc state current-direction (+ (current-direction state) distance))
    ))

(defn turn-then-move
  [state command]
  (move (turn state command) command))

(defn taxicab-distance
  [state]
  (let [n (:n state) s (:s state) e (:e state) w (:w state)]
    (+ (Math/abs (- n s)) (Math/abs (- e w)))
    ))

(defn solve
  "Given the input for the day, returns the solution."
  [input]
  (let [commands
        (map str/trim-newline (str/split input #", "))]
    [(taxicab-distance (reduce turn-then-move starting-state commands))
    ]))
