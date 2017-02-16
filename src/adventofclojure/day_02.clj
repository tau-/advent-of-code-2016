(ns adventofclojure.day-02
  (:require [clojure.string :as str]))

(def keypad-square)

(defn take-step
  [position step])

(defn find-next-key
  [position command keypad]
  (let [new-position (reduce take-step position command)
        next-key (new-position keypad)]
    [new-position next-key]))

(defn solve
  "Given the input for the day, returns the solution."
  [input]
  (println input)
  (let [commands (map str/trim-newline (str/split input #"\n"))]
    [commands
     "part2"]))
