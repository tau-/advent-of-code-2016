(ns adventofclojure.day-01
  (:require [clojure.string :as str]))

(def starting-state
  {:dir :n, :n 0, :s 0, :e 0, :w 0})

(def starting-state-with-crumbs
  (assoc starting-state :crumbs '({:x 0, :y 0})))

(defn get-position
  [state]
  {:x (- (:n state) (:s state)), :y (- (:e state) (:w state))})

(defn taxicab-distance
  [state]
  (let [position (get-position state)
        x (:x position) y (:y position)]
    (+ (Math/abs x) (Math/abs y))))

(defn turn
  [state command]
  (let [turn (first command)
        current-direction (:dir state)
        left-turn {:n :w, :s :e, :e :n, :w :s}
        right-turn {:n :e, :s :w, :e :s, :w :n}]
    (case turn
      \L (assoc state :dir (current-direction left-turn))
      \R (assoc state :dir (current-direction right-turn))
      state
      )))

(defn move
  [state command]
  (let [distance (Integer/parseInt (apply str (rest command)))
        current-direction (:dir state)]
    (assoc state current-direction (+ (current-direction state) distance))
    ))

(defn turn-then-move
  [state command]
  (move (turn state command) command))

(defn add-crumb
  [state]
  (let [current-crumbs (:crumbs state)]
    (assoc state :crumbs (cons (get-position state) current-crumbs))))

(defn revisited?
  [state]
  (let [history (:crumbs state)]
    (not= (count history) (count (set history)))))

(defn move-with-crumbs
  [state command]
  (let [distance (Integer/parseInt (apply str (rest command)))]
    (loop [n 0
           s state]
      (if (revisited? s)
        (reduced s)
        (if (< n distance)
          (recur (inc n) (add-crumb (move s "X1")))
          s)))))

(defn turn-then-move-with-crumbs
  [state command]
  (move-with-crumbs (turn state command) command))

(defn solve
  "Given the input for the day, returns the solution."
  [input]
  (let [commands (map str/trim-newline (str/split input #", "))]
    [(taxicab-distance (reduce turn-then-move starting-state commands))
     (taxicab-distance (reduce turn-then-move-with-crumbs starting-state-with-crumbs commands))]))
